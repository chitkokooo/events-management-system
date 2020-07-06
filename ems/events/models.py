from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
	PARTICIPANTS = []
	try:
		users = User.objects.all()
		if users:
			for user in users:
				PARTICIPANTS.append((user.id, user.username))
	except:
		pass

	title = models.CharField(max_length=200)
	notes = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	event_time = models.DateTimeField()
	participants = models.CharField(max_length=9, choices=PARTICIPANTS)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
