
from django.urls import reverse, resolve
from receitasapp import views
from .test_receita_base import ReceitaTestBase

class ReceitaCategoryViewTest(ReceitaTestBase):    

    def test_receita_categoria_view_function_is_correct(self):
        view = resolve(reverse('receitas:categoria', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.categoria)


    def test_receita_categoria_view_returns_status_404_if_no_receita(self):
        response = self.client.get(
            reverse('receitas:categoria', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    

    def test_receita_categoria_template_loads_receitas(self):

        receita = self.make_receita(title='This is a category test')

        response = self.client.get(reverse('receitas:categoria', kwargs={'category_id': receita.category.id}))
        content = response.content.decode('utf-8')
        reponse_context_receita = response.context['receitas']

        self.assertTemplateUsed(response, 'receitas/pages/category.html')
        self.assertIn('This is a category test', content)
        self.assertIn('receita criada para teste', content)
        self.assertEqual(len(reponse_context_receita), 1)


    def test_receita_categoria_template_dont_load_receitas_if_receita_isnt_published(self):

        receita = self.make_receita(is_published=False)

        response = self.client.get(reverse('receitas:categoria', kwargs={'category_id': receita.category.id}))
        
        self.assertEqual(response.status_code, 404)