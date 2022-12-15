from django.db import models

# Create your models here.
class Predictions_currency:
    def __init__(self, status, res):
        self.status = status
        self.res = res

class ImageFromPillow:
    def __init__(self, image_base64, encoding):
        self.image_base64 = image_base64
        self.encoding = encoding
