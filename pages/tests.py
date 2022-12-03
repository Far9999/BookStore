from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView


class HomepageTests(TestCase):
    def test_url_exists_at_correct_loc(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertTemplateNotUsed(response, "cnf.html")
        self.assertContains(response, "This is our home page.")
        self.assertNotEqual(response.status_code, 404)
        
    def test_homepage_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        
    def test_homepage_url_resolves_homepage_view(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)