from django.urls import path
from func_app.views import give_predictions_currency
from django.conf import settings
from django.conf.urls.static import static
from api import views


urlpatterns = [
 path('future_cur', give_predictions_currency),
 path('api', views.predictions_currency_Views.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
