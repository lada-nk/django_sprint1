from django.shortcuts import render


# Возвращает описание проекта.
def about(request):
    template_name = 'pages/about.html'
    return render(request, template_name)


# Возвращает правила прокта.
def rules(request):
    template_name = 'pages/rules.html'
    return render(request, template_name)
