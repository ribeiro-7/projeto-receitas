from django.urls import reverse, resolve
from receitasapp import views
from .test_receita_base import ReceitaTestBase

class ReceitaSearchViewTest(ReceitaTestBase):

    def test_receita_search_uses_correct_view_function(self):
        url = resolve(reverse('receitas:search'))
        self.assertIs(url.func, views.search)

    def test_receita_search_returns_correct_template(self):
        url = reverse('receitas:search') + '?q=teste'
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'receitas/pages/search.html')

    def test_receita_search_raises_404_if_no_search_term(self):
        url = reverse('receitas:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_receita_search_term_is_on_page_title_and_escaped(self):
        url = reverse('receitas:search') + '?q=teste'
        response = self.client.get(url)
        self.assertIn('Search for &quot;teste&quot;', response.content.decode('utf-8'))