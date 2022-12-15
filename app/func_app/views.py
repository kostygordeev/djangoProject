from django.http import HttpResponse
from django.shortcuts import render
from func_app.predictions_currency import create_pred_plot

def give_predictions_currency(request):
    days_num = int(request.GET.get('days_num'))
    num_days = int(request.GET.get('num_days'))
    if days_num <= 20 and num_days <= 365:
        context = {
            'days_num': days_num,
            'num_days': num_days,
            'filename': create_pred_plot(days_num, num_days)
        }
        return render(request, 'index.html', context)
    else:
        return HttpResponse("error: not right day numbers")


