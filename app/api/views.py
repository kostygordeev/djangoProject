from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Predictions_currency, ImageFromPillow
from .seriaalizers import Predictions_currency_Serializers, ImageFromPillowSerializer
from func_app.predictions_currency import create_pred_plot, encode_image


# Create your views here.
class predictions_currency_Views(APIView):

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="days_num",
                description="the number of days we are analyzing",
                required=True,
                type=OpenApiTypes.INT
            ),
            OpenApiParameter(
                name="num_days",
                description="the number of days we apply the analysis",
                required=True,
                type=OpenApiTypes.INT
            ),
            OpenApiParameter(
                name="api_key",
                description="API key for authentication",
                required=True,
                type=OpenApiTypes.STR
            )
        ],
        description="Prediction of the exchange rate of the Kazakhstan tenge to the Russian ruble",
        responses={
            200: Predictions_currency_Serializers
        },
        methods=["GET"]
    )
    def get(self, request):
        days_num = int(request.GET.get('days_num'))
        num_days = int(request.GET.get('num_days'))
        if days_num <= 20 and num_days <= 365:
            predictions_currency = Predictions_currency("ok", create_pred_plot(days_num, num_days))
        else:
            predictions_currency = Predictions_currency("error", "Too big number")
        serializers_for_request = Predictions_currency_Serializers(instance=predictions_currency)
        return Response(serializers_for_request.data)

class ImageFromPillowView(APIView):

    def get(self, request, name):
        image_str = encode_image(f'./media/' + name)
        image_res = ImageFromPillow(image_str, 'utf-8')
        serializer_for_req = ImageFromPillowSerializer(instance=image_res)

        return Response(serializer_for_req.data)
