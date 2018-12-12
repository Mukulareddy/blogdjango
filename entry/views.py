from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from entry.models import Entry
from entry.forms import EntryForm

# Create your views here.
def all(request):
	items=Entry.objects.all().order_by('-id')
	return render(request,'entry/index.html',{'items':items})

def detail(request,object_id):
	item= get_object_or_404(Entry,pk = object_id)
	return render(request,'entry/detail.html',{'item':item})

def add(request):
	if request.POST:
		form = EntryForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
		else:
			render(request, 'entry/add.html',{'form':form})
	else:
		form = EntryForm()
		return render(request, 'entry/add.html',{'form':form})


