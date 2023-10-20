from django.test import TestCase
from .forms import ThingForm
from django import forms


class ThingFormTestCase(TestCase):
    """Unit tests for the things form"""
    def setUp(self):
        self.form_input = {
            'name': 'Jane',
            'description': 'This is a things form description',
            'quantity': 25
        }

    # test the form accepts valid input data
    def test_valid_things_form(self):
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    # test the form has the necessary fields
    def test_form_has_necessary_fields(self):
        form = ThingForm()
        self.assertIn('name', form.fields)
        self.assertIn('description', form.fields)
        description_widget = form.fields['description'].widget
        self.assertTrue(description_widget, forms.Textarea)
        self.assertIn('quantity', form.fields)
        quantity_field = form.fields['quantity']
        self.assertTrue(isinstance(quantity_field, forms.IntegerField))
        quantity_widget = form.fields['quantity'].widget
        self.assertTrue(quantity_widget, forms.NumberInput)

    # test the form uses model validation
    def test_form_uses_model_validation(self):
        self.form_input['quantity'] = 51

        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

