from django.shortcuts import render, redirect
from .models import tasks

# Create your views here.
def index(request):

	all_tasks = tasks.objects.all()
	if request.method == 'POST':
		new_task = tasks(
			task_name = request.POST['task']
		)
		new_task.save()
		return redirect('/')
	return render(request, 'index.html', {'tasks' : all_tasks})

def delete(request, pk):
	task = tasks.objects.get(id=pk)
	task.delete()
	return redirect('/')