from django.shortcuts import render

def semester_manuals(request):
    context = {
        'title': 'Методички на семестр',
    }

    return render(request, "home/library/semester_manuals.html", context)

def find_tutorial(request):
    context = {
        'title': 'Найти методичку',
    }

    return render(request, "home/library/find_tutorial.html", context)