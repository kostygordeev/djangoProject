from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static
from api import views
from func_app.views import give_predictions_currency

urlpatterns = [
 path('future_cur', give_predictions_currency, name="future_cur"),
 path('api', views.predictions_currency_Views.as_view(), name="future_cur_api"),
 path("schema/", SpectacularAPIView.as_view(), name="schema"),
 path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
 path("img/<str:name>", views.ImageFromPillowView.as_view(), name="image")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
