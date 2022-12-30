from django import forms

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'chat_id',
            'user',
            'username',
        )
        widgets = {
            'username': forms.TextInput,
        }