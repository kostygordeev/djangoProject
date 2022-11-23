from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase


class TESTCUR(APITestCase):
    def test_cur_correct(self):
        with open(".\\media\\index.txt", 'r') as fi:
            index = int(fi.read())
        testd = dict()
        testd["status"] = "ok"
        testd["res"] = "plot" + str(index) + ".png"
        url = reverse('future_cur_api')
        response = self.client.get(url + '?days_num=20&num_days=200')
        self.assertEqual(response.data, testd)
    def test_cur_error(self):
        testd = dict()
        testd["status"] = "error"
        testd["res"] = "Too big number"
        url = reverse('future_cur_api')
        response = self.client.get(url + '?days_num=2000000&num_days=20000000')
        self.assertEqual(response.data, testd)
