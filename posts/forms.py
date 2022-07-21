from django import forms
from posts.models import Author

class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    choices = [(choice.id, choice.nick) for choice in Author.objects.all()]
    author_id_id = forms.ChoiceField(choices=choices)

class AuthorForm(forms.Form):
    nick = forms.CharField()
    email = forms.CharField()