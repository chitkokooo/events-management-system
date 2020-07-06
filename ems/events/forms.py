from django import forms
from datetime import datetime
from .models import Event
from django.contrib.auth.models import User

class DateSearchForm(forms.Form):
	MONTHS = (
		(1, 'JANUARY'),
		(2, 'FEBRUARY'),
		(3, 'MARCH'),
		(4, 'APRIL'),
		(5, 'MAY'),
		(6, 'JUNE'),
		(7, 'JULY'),
		(8, 'AUGUST'),
		(9, 'SEPTEMBER'),
		(10, 'OCTOBER'),
		(11, 'NOVEMBER'),
		(12, 'DECEMBER'),
	)

	year = forms.IntegerField(initial=datetime.now().year)
	month = forms.ChoiceField(choices=MONTHS, initial=datetime.now().month)


class CreateEventForm(forms.ModelForm):
	PARTICIPANTS = []
	try:
		users = User.objects.all()
		if users:
			for user in users:
				PARTICIPANTS.append((user.id, user.username))
			participants = forms.ModelMultipleChoiceField(queryset=User.objects, widget=forms.CheckboxSelectMultiple(), blank=True)
	except:
		pass

	class Meta:
		model = Event
		fields = ('title', 'notes', 'event_time', 'participants', 'owner')
