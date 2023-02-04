from django import forms
from .models import Cat


class CatForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CatForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['style'] = 'height:400px;'

    class Meta:
        model = Cat
        fields = ['name', 'description', 'image']
