from django import forms
from . import models, parser_rezka

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('mybook.ru', 'mybook.ru'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]
    def parser_data(self):
        if self.data['media_type'] == 'mybook.ru':
            rezka_films = parser_rezka.parsing_rezka()
            for i in rezka_films:
                models.RezkaModel.objects.create(**i)


