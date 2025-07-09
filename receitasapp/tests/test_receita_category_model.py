from django.core.exceptions import ValidationError
from .test_receita_base import ReceitaTestBase

class CategoryModelTest(ReceitaTestBase):

        def setUp(self) -> None:
            self.category = self.make_category(
                name='Category Testing'
            )
            return super().setUp()

        def test_receita_category_model_string_representarion_is_name_field(self):
            self.assertEqual(
                str(self.category),
                self.category.name
            )

        def test_receita_category_model_name_max_length_is_65_chars(self):
            self.category.name = 'A' * 66
            with self.assertRaises(ValidationError):
                self.category.full_clean()