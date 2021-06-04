from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):

	all_tasks = tasks.objects.all()
	all_habits = habits.objects.all()
	all_thoughts = thoughts.objects.all()

	if request.method == 'POST':

		if ('task' in request.POST.keys()):
			new_task = tasks(
				task_name = request.POST['task']
			)
			new_task.save()

		if ('habit' in request.POST.keys()):
			new_habit = habits(
				habit_name = request.POST['habit']
			)
			new_habit.save()

		if ('thought' in request.POST.keys()):
			new_thought = thoughts(
				thought_name = request.POST['thought']
			)
			new_thought.save()

		return redirect('/')

	return render(request, 'index.html', {'tasks' : all_tasks, 'habits' : all_habits, 'thoughts' : all_thoughts})

def delete_ta(request, pk):
	task = tasks.objects.get(id=pk)
	task.delete()
	return redirect('/')

def delete_th(request, pk):
	thought = thoughts.objects.get(id=pk)
	thought.delete()
	return redirect('/')

def delete_ha(request, pk):
	habit = habits.objects.get(id=pk)
	habit.delete()
	return redirect('/')






