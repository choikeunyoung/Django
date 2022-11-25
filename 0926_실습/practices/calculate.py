from django.shortcuts import render


def calculate(request, num1, num2):
    sum_ = num1 + num2
    min_ = num1 - num2
    gob_ = num1 * num2
    div_ = num1 // num2

    context = {
        "num1": num1,
        "num2": num2,
        "sum_": sum_,
        "min_": min_,
        "gob_": gob_,
        "div_": div_,
    }

    return render(request, "calculate.html", context)
