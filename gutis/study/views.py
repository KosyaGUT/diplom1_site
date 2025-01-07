from django.shortcuts import render

def schedule(request):
    context = {
        'title': 'Расписание',
    }

    return render(request, "home/study/schedule.html", context)

def curriculum(request):
    context = {
        'title': 'Учебный план',
    }

    return render(request, "home/study/curriculum.html", context)

def student_council(request):
    context = {
        'title': 'Студенческий совет',
    }

    return render(request, "home/study/student_council.html", context)

def group_files(request):
    context = {
        'title': 'Файлы группы',
    }

    return render(request, "home/study/group_files.html", context)