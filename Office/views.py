from django.shortcuts import render
from .models import Office


def get_Offices(request):
	offices = Office.objects.all()
	context = {
		'offices': offices
	}
	return render(request, 'index.html', context)
