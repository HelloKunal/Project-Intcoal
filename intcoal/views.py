from django.shortcuts import render, redirect
from .models import Intcoal

# Create your views here.
def index(request):

	intcoal = Intcoal.objects.all()
	if request.method == 'POST':
		new_intcoal = Intcoal(
			title = request.POST['title']
		)
		new_intcoal.save()
		return redirect('/')
	return render(request, 'index.html', {'intcoals' : intcoal})

def delete(request, pk):
	intcoal = Intcoal.objects.get(id=pk)
	intcoal.delete()
	return redirect('/')