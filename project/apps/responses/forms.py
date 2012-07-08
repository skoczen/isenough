from django.forms import *
from responses.models import EnoughResponse


class ResponseForm(ModelForm):

    class Meta:
        model = EnoughResponse
        widgets = {
            "text": TextInput,
        }