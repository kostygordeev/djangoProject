from django.http import HttpResponse
from django.shortcuts import render
from func_app.predictions_currency import create_pred_plot

def give_predictions_currency(request, days_num):
    if days_num <= 30:
        context = {
            'days_num': days_num,
            'filename': create_pred_plot(days_num)
        }
        return render(request, 'index.html', context)
    else:
        return HttpResponse("error: to many days no over 30")
