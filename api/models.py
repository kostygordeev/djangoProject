from django.db import models

# Create your models here.
class Predictions_currency:
    def __init__(self, status, res):
        self.status = status
        self.res = res
