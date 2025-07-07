from django.test import TestCase
from receitasapp.models import Receita, Category
from django.contrib.auth.models import User

class ReceitaTestBase(TestCase):

    def setUp(self):
        
        return super().setUp()
    

    def make_category(self, name='Massa'):
        return Category.objects.create(name=name)
    

    def make_author(
        self,
        first_name='user',
        last_name='name',
        username='username',
        password='123456',
        email='user@gmail.com'
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )
    

    def make_receita(
        self, 
        title = 'receita teste',
        description = 'receita criada para teste',
        slug = 'receita-teste',
        preparation_time = 1,
        preparation_time_unit = 'Minuto',
        servings = 1,
        servings_unit = 'Pessoa',
        preparation_steps = 'blablabla',
        preparation_steps_html = False,
        is_published = True,
        category_data = None,
        author_data = None,
    ):
        
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Receita.objects.create(
            title = title,
            description = description,
            slug = slug,
            preparation_time = preparation_time,
            preparation_time_unit = preparation_time_unit,
            servings = servings,
            servings_unit = servings_unit,
            preparation_steps = preparation_steps,
            preparation_steps_html = preparation_steps_html,
            is_published = is_published,
            category = self.make_category(**category_data),
            author = self.make_author(**author_data),
        )