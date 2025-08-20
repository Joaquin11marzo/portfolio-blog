from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Tu email (opcional)'}),
            'body': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu comentario...'}),
        }
