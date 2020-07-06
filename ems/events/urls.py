from django.urls import include, path
from . import views


app_name = "events"

urlpatterns = [
	path('', views.index, name="index"),
	path('create/', views.create, name="create"),
	path('accounts/', include('django.contrib.auth.urls')),
	#path('accounts/login/', views.SignIn.as_view(), name="signin"),
	# path('accounts/login/', views.signin, name='signin'),
	# path('accounts/register/', views.signup, name='signup'),
	#path('accounts/register/', views.SignUp.as_view(), name='signup'),
	#path('accounts/logout/', views.signout, name='signout'),
]