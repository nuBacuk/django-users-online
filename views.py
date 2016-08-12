import datetime
from django.shortcuts import render
from django.core.cache import cache
from django.contrib.auth.models import User
import settings


def usersonline(request):
	users = User.objects.all()
	online = []
	count = 1
	for item in users:
		if cache.get('seen_%s' % item.username):
			now = datetime.datetime.now()
			if now > cache.get('seen_%s' % item.username) + datetime.timedelta(minutes=15):
				pass
			else:
				i = [count, item,item.username, cache.get('ip_%s' % item.username)]
				online.append(i)
				count += 1
		else:
			pass
	return render(request, 'online.html', {'online': online}) 
