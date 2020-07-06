from django.shortcuts import render, redirect
from django.utils.html import mark_safe
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import calendar
import datetime
from .forms import DateSearchForm, CreateEventForm
from .models import Event

from django.views import generic
from django.urls import reverse_lazy


@login_required
def index(request):
	events = Event.objects.all()

	if request.method == 'POST':
		form = DateSearchForm(request.POST)
		if form.is_valid():
			year = int(form.cleaned_data['year'])
			month = int(form.cleaned_data['month'])
			current_month = calendar.HTMLCalendar(firstweekday=6)
			current_month = current_month.formatmonth(year, month)
			current_month = current_month.replace('<td ', '<td width="150px" height="50px"')
			current_month = mark_safe(current_month)
			return render(request, 'events/index.html', {
				'form': form,
				'current_month': current_month,
				'events': events})
	else:
		form = DateSearchForm()
		selected_year = datetime.datetime.now().year
		selected_month = datetime.datetime.now().month
		current_month = calendar.HTMLCalendar(firstweekday=6)
		current_month = current_month.formatmonth(selected_year, selected_month, withyear=True)
		current_month = current_month.replace('<td ', '<td width="150px" height="50px"')
		current_month = mark_safe(current_month)
		return render(request, 'events/index.html', {
			'form': form,
			'current_month': current_month,
			'events': events})


@login_required
def create(request):
	if request.method == 'POST':
		form = CreateEventForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			notes = form.cleaned_data['notes']
			created_at = datetime.datetime.now()
			event_time = form.cleaned_data['event_time']
			participants =form.cleaned_data['participants']
			owner = form.cleaned_data['owner']
			event = Event(title=title, notes=notes, created_at=created_at, event_time=event_time, participants=participants, owner=owner)
			event.save()
			messages.success(request, "Event has been created successfully.")
			return redirect('/')
		else:
			messages.error(request, "Error while event is creating.")
			return render(request, 'events/new-event.html', {'form': form})

	else:
		form = CreateEventForm()
		return render(request, 'events/new-event.html', {'form': form })


"""def signin(request):
	if request.user.is_authenticated:
		return redirect('/')

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username = username, password = password)

		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			form = AuthenticationForm(request.POST)
			return render(request, 'events/login.html', {'form': form})
	else:
		form = AuthenticationForm()
		return render(request, 'events/login.html', {'form': form})"""


"""def signup(request):
	if request.user.is_authenticated:
		return redirect('/')

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			form.save()
			messages.success(request, "User account has been created successfully.")
			user = authenticate(username = username, password = password)
			login(request, user)
			return redirect('/')
		else:
			return render(request, 'events/register.html', {'form': form})
	else:
		form = UserCreationForm()
		return render(request, 'events/register.html', {'form': form})"""


def signout(request):
	logout(request)
	return redirect('/')


class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('events:signin')
	template_name = 'events/register.html'


class SignIn(generic.FormView):
	form_class = AuthenticationForm
	success_url = reverse_lazy('events:index')
	template_name = 'events/login.html'