from django.test import TestCase
from .views import horoscope_dict

# Create your tests here.


class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_libra(self):
        response = self.client.get('/horoscope/libra/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
                      response.content.decode())

    def test_libra_redirect(self):

        list_zod = list(horoscope_dict)
        for i in range(1, 13):
            name_zod = list_zod[i - 1]
            response = self.client.get(f'/horoscope/{i}/')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, f'/horoscope/{name_zod}/')
