from django.urls import reverse, resolve
from receitasapp import views
from .test_receita_base import ReceitaTestBase

class ReceitaHomeViewTest(ReceitaTestBase):
    
    def test_receita_home_view_function_is_correct(self):
        view = resolve(reverse('receitas:home'))
        self.assertIs(view.func, views.home)


    def test_receita_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('receitas:home'))
        self.assertEqual(response.status_code, 200)


    def test_receita_home_view_loads_correct_template(self):
        response = self.client.get(reverse('receitas:home'))
        self.assertTemplateUsed(response, 'receitas/pages/home.html')


    def test_receita_home_shows_nao_ha_receita(self):
        response = self.client.get(reverse('receitas:home'))
        self.assertIn('Não há receitas no momento.', response.content.decode('utf-8'))


    def test_receita_home_template_loads_receitas(self):

        self.make_receita()

        response = self.client.get(reverse('receitas:home'))
        content = response.content.decode('utf-8')
        reponse_context_receita = response.context['receitas']

        self.assertTemplateUsed(response, 'receitas/pages/home.html')
        self.assertIn('receita teste', content)
        self.assertIn('receita criada para teste', content)
        self.assertEqual(len(reponse_context_receita), 1)


    def test_receita_home_template_dont_load_receitas_if_receita_isnt_published(self):

        self.make_receita(is_published=False)

        response = self.client.get(reverse('receitas:home'))
        content = response.content.decode('utf-8')

        self.assertIn('Não há receitas no momento.', content)