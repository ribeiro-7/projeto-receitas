from django.urls import reverse, resolve
from receitasapp import views
from .test_receita_base import ReceitaTestBase


class ReceitaDetailViewTest(ReceitaTestBase):

    def test_receita_detail_view_function_is_correct(self):
        view = resolve(reverse('receitas:receita', kwargs={'receita_id': 1}))
        self.assertIs(view.func, views.receita)


    def test_receita_categoria_detail_view_returns_status_404_if_no_receita(self):
        response = self.client.get(
            reverse('receitas:receita', kwargs={'receita_id': 1000})
        )
        self.assertEqual(response.status_code, 404)


    def test_receita_detail_template_loads_correct_receita(self):

        receita = self.make_receita(title='This is a detail test')

        response = self.client.get(reverse('receitas:receita', kwargs={'receita_id': receita.id}))
        content = response.content.decode('utf-8')

        self.assertTemplateUsed(response, 'receitas/pages/receita-view.html')
        self.assertIn('This is a detail test', content)
        self.assertIn('receita criada para teste', content)

    def test_receita_detail_template_dont_load_receitas_if_receita_isnt_published(self):

        receita = self.make_receita(is_published=False)

        response = self.client.get(reverse('receitas:receita', kwargs={'receita_id': receita.id}))
        
        self.assertEqual(response.status_code, 404)