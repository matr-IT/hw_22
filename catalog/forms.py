from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

            if field_name == 'name':
                field.widget.attrs['placeholder'] = 'Введите наименование продукта'
            elif field_name == 'description':
                field.widget.attrs['placeholder'] = 'Введите описание продукта'
            elif field_name == 'price':
                field.widget.attrs['placeholder'] = 'Введите цену в рублях'

            if field_name == 'category':
                field.widget.attrs['class'] = 'form-select'

            if field_name == 'image':
                field.widget.attrs['class'] = 'form-control-file'

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price is not None and price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной.")

        return price

    def clean(self):
        cleaned_data = super().clean()
        forbidden_words = [
            'казино', 'биржа', 'криптовалюта', 'крипта',
            'обман', 'дешево', 'полиция', 'бесплатно', 'радар'
        ]

        text_fields = ['name', 'description']

        for field_name in text_fields:
            if field_name in cleaned_data:
                field_value = cleaned_data[field_name]
                if field_value:
                    field_value_lower = field_value.lower()

                    found_forbidden_words = []
                    for word in forbidden_words:
                        if word in field_value_lower:
                            found_forbidden_words.append(word)

                    if found_forbidden_words:
                        error_message = f"Обнаружены запрещенные слова: {', '.join(found_forbidden_words)}"
                        self.add_error(field_name, error_message)

        return cleaned_data