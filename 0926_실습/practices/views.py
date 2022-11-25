from django.shortcuts import render


def numbering(request, number):
    if number % 2 == 0:
        context = {
            "num": 2,
            "nums": number,
        }
    elif number == 0:
        context = {
            "num": 0,
            "nums": number,
        }
    elif number % 2 == 1:
        context = {
            "num": 1,
            "nums": number,
        }
    return render(request, "is-odd-even.html", context)
