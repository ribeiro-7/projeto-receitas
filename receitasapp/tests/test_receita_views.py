from django.urls import reverse, resolve
from receitasapp import views
from .test_receita_base import ReceitaTestBase

class ReceitaViewsTest(ReceitaTestBase):

    #home
    
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


    #category

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


    #receita-detail

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

    
    #search

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