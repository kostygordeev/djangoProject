from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Predictions_currency
from .seriaalizers import Predictions_currency_Serializers
from func_app.predictions_currency import create_pred_plot


# Create your views here.
class predictions_currency_Views(APIView):

    def get(self, request):
        days_num = int(request.GET.get('days_num'))
        num_days = int(request.GET.get('num_days'))
        if days_num <= 20 and num_days <= 365:
            predictions_currency = Predictions_currency("ok", create_pred_plot(days_num, num_days))
        else:
            predictions_currency = Predictions_currency("error", "Too big number")
        serializers_for_request = Predictions_currency_Serializers(instance=predictions_currency)
        return Response(serializers_for_request.data)



