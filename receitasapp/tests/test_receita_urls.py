from django.test import TestCase
from django.urls import reverse

class ReceitaURLsTest(TestCase):
    
    def test_receita_home_url_is_correct(self):
        home_url = reverse('receitas:home')
        self.assertEqual(home_url, '/')

    def test_receita_categoria_url_is_correct(self):
        category_url = reverse('receitas:categoria', kwargs={'category_id': 1})
        self.assertEqual(category_url, '/receita/categoria/1/')

    def test_receita_detail_url_is_correct(self):
        detail_url = reverse('receitas:receita', kwargs={'receita_id': 1})
        self.assertEqual(detail_url, '/receita/1/')

    def test_receita_search_url_is_correct(self):
        search_url = reverse('receitas:search')
        self.assertEqual(search_url, '/receita/search/')