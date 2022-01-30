from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from url_shortener_app.models import UrlShortener


class UrlShortenerTest(TestCase):

    def setUp(self):
        self.create_shortener_url = reverse("create")
        self.long_url = "https://ravkavonline.co.il"  # test url
        self.shortener_object = UrlShortener(long_url=self.long_url)
        self.shortener_object.save()

    def test_create_shortener_url(self):
        shortener_object = UrlShortener(long_url=self.long_url)
        shortener_object.save()
        self.assertIsNotNone(shortener_object.short_url)

    def test_url_shortener_create_post(self):
        data = {
            'url': self.long_url
        }
        response = self.client.post(self.create_shortener_url, data, content_type="application/x-www-form-urlencoded", follow=True)
        status = response.status_code
        self.assertEqual(status, 201)  # created

    def test_redirect_shortener_url(self):
        data = {
            'shortened_part': self.shortener_object.short_url
        }
        response = self.client.get(reverse('redirect', kwargs=data))
        self.assertEqual(response.status_code, 302)  # found

    def test_redirect_wrong_shortener_url(self):
        data = {
            "shortened_part": "ERR"
        }
        response = self.client.get(reverse('redirect', kwargs=data))
        self.assertEqual(response.status_code, 404)  # not found
