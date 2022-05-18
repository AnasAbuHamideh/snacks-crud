from urllib import request, response
from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class SnackTest(TestCase):
    def test_list_page_status_code(self):
        url = reverse("snacks-list")
        response =self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("snacks-list")
        response =self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "_base.html")

    def test_create_page_status_code(self):
        url = reverse("snacks-create")
        response =self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_page_template(self):
        url = reverse("snacks-create")
        response =self.client.get(url)
        self.assertTemplateUsed(response, "snack_create.html")
        self.assertTemplateUsed(response, "_base.html")

    # def test_detail_page_status_code(self):
    #     url = reverse("snacks-detail")
    #     response =self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # def test_detail_page_template(self):
    #     url = reverse("snacks-detail")
    #     response =self.client.get(url)
    #     self.assertTemplateUsed(response, "snack_detail.html")
    #     self.assertTemplateUsed(response, "_base.html")

    # def test_update_page_status_code(self):
    #     url = reverse("snacks-update")
    #     response =self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # def test_update_page_template(self):
    #     url = reverse("snacks-update")
    #     response =self.client.get(url)
    #     self.assertTemplateUsed(response, "snack_update.html")
    #     self.assertTemplateUsed(response, "_base.html")

    # def test_delete_page_status_code(self):
    #     url = reverse("snacks-delete")
    #     response =self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # def test_delete_page_template(self):
    #     url = reverse("snacks-delete")
    #     response =self.client.get(url)
    #     self.assertTemplateUsed(response, "snack_delete.html")
    