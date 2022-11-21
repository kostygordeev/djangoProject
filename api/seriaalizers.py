from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Example_1",
            summary="Code ok(200)",
            description="all received data is correct",
            value={
                "status": "ok",
                "result_message": "plot59.png"
            }
        ),
        OpenApiExample(
            "Example_2",
            summary="Code ok(200)",
            description="wrong data",
            value={
                'status': "error",
                "result_message": "Too big number"
            }
        )
    ]
)
class Predictions_currency_Serializers(serializers.Serializer):
    status = serializers.CharField()
    res = serializers.CharField()
