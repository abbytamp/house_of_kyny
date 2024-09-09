from django.shortcuts import render

def show_main(request):
    context = {
        'app' : 'House Of Kyny',
        'name': 'Abby Shelley',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
