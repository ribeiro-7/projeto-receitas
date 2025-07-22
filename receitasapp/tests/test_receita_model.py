from django.core.exceptions import ValidationError
from .test_receita_base import ReceitaTestBase, Receita
from parameterized import parameterized
import uuid


class ReceitaModelTest(ReceitaTestBase):

    def setUp(self):
        self.receita = self.make_receita()
        return super().setUp()
    
    def make_receita_no_defaults(self):

        slug_unico = f'receita-teste-{uuid.uuid4().hex[:8]}'

        receita = Receita(
            title = 'receita teste',
            description = 'receita criada para teste',
            slug = slug_unico,
            preparation_time = 1,
            preparation_time_unit = 'Minuto',
            servings = 1,
            servings_unit = 'Pessoa',
            preparation_steps = 'blablabla',
            category = self.make_category(name='Test category default'),
            author = self.make_author(username='newuser'),
        )

        receita.full_clean()
        receita.save()

        return receita
    
    #Receita - model

    #usando testes parametrizados -> para testar varios objetos com atributos diferentes
    @parameterized.expand([
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65)
    ])
    def test_receita_fields_max_length(self, field, max_length):

        setattr(self.receita, field, 'A' * (max_length + 1))

        with self.assertRaises(ValidationError):
            self.receita.full_clean()

    
    def test_receita_preparation_steps_html_is_false_by_default(self):

        receita = self.make_receita_no_defaults()

        self.assertFalse(receita.preparation_steps_html)

    def test_receita_is_published_false_by_default(self):

        receita = self.make_receita_no_defaults()

        self.assertFalse(receita.is_published)

    def test_receita_string_representation(self):
        self.receita.title = 'Testing __str__ receita'
        self.receita.full_clean()
        self.receita.save()
        self.assertEqual(str(self.receita), 'Testing __str__ receita')