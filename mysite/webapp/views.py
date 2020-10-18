from django.shortcuts import render
from .models import PublicationsTable
from .models import AuthorsTable
from .forms import PublicationsTableForm
from .forms import AuthorsTableForm


def publications(request):
    WebTable = PublicationsTable.objects.all()
    variable = {
        'WebTable': WebTable
    }
    return render(request, 'webapp/publications.html', variable)


def authors(request):
    WebTable1 = AuthorsTable.objects.all()
    variable1 = {
        'WebTable1': WebTable1
    }
    return render(request, 'webapp/authors.html',variable1)


def create_pub(request):
    error=''
    if request.method == 'POST':
        form = PublicationsTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = PublicationsTableForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'webapp/create_pub.html',context)


def create_auth(request):
    error1=''
    if request.method == 'POST':
        form1 = AuthorsTableForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/authors')
        else:
            error = 'Форма была неверной'
    form1 = AuthorsTableForm()
    context1 = {
        'form1': form1,
        'error1': error1
    }
    return render(request, 'webapp/create_auth.html',context1)

