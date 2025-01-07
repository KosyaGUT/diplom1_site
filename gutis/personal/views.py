from django.shortcuts import render

def my_profile(request):
    context = {
        'title': 'Мой профиль',
    }

    return render(request, 'home/personal/my_profile.html', context=context)

def diary(request):
    context = {
        'title': 'Дневник',
    }

    return render(request, 'home/personal/diary.html', context=context)


def access_to_services(request):
    context = {
        'title': 'Доступ к сервисам',
    }

    return render(request, 'home/personal/access_to_services.html', context=context)


def ordering_information(request):
    context = {
        'title': 'Заказ справок',
    }

    return render(request, 'home/personal/ordering_information.html', context=context)


def messages(request):
    context = {
        'title': 'Сообщения',
    }

    return render(request, 'home/personal/messages.html', context=context)


def technical_support(request):
    context = {
        'title': 'Тех. поддержка',
    }

    return render(request, 'home/personal/technical_support.html', context=context)

