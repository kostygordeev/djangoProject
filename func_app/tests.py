from django.test import TestCase
from django.urls import reverse


class TESTCURFUNC(TestCase):
    def test_cur_correct(self):
        with open(".\\media\\index.txt", 'r') as fi:
            index = int(fi.read())
        testd = dict()
        testd["days_num"] = 20
        testd["num_days"] = 200
        testd["filename"] = "plot" + str(index) + ".png"
        url = reverse('future_cur')
        response = self.client.get(url + '?days_num=20&num_days=200')
        self.assertEqual(response.context.pop(), testd)
    def test_cur_error(self):
        url = reverse('future_cur')
        response = self.client.get(url + '?days_num=2000000&num_days=20000000')
        self.assertEqual(response.content.decode("utf-8"), 'error: not right day numbers')
