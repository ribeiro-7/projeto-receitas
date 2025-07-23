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

    def test_receita_search_can_find_receita_by_title(self):
        title1 = 'This is Receita 1'
        title2 = 'This is Receita 2'

        receita1 = self.make_receita(
            slug='receita-one',
            title=title1,
            author_data={ 'username': 'userOne'}
        )

        receita2 = self.make_receita(
            slug='receita-two',
            title=title2,
            author_data={ 'username': 'userTwo'}
        )

        search_url = reverse('receitas:search')
        response1 = self.client.get(f'{search_url}?q={title1}')
        response2 = self.client.get(f'{search_url}?q={title2}')
        response_both = self.client.get(f'{search_url}?q=this')

        #testa se a receita1 aparece na response1
        self.assertIn(receita1, response1.context['receitas'])
        #testa se a receitas2 não aparece na response1
        self.assertNotIn(receita2, response1.context['receitas'])

        #testa se a receita2 aparece na response2
        self.assertIn(receita2, response2.context['receitas'])
        #testa se a receita1 não aparecec na response2
        self.assertNotIn(receita1, response2.context['receitas'])

        #testa se as 2 receitas aparecem na response dos dois juntos
        self.assertIn(receita1, response_both.context['receitas'])
        self.assertIn(receita2, response_both.context['receitas'])