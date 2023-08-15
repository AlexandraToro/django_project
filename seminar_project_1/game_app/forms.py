from django import forms
from .models import Author


class ChooseGame(forms.Form):
	a_game = forms.ChoiceField(choices=[('0', "coin play"), ('1', "Dice"), ('2', "Random number")])
	attempts = forms.IntegerField(min_value=1, max_value=64)


class AuthoForms(forms.Form):
	name = forms.CharField(max_length=100)
	surname = forms.CharField(max_length=100)
	email = forms.EmailField(max_length=100)
	biography = forms.CharField(widget=forms.Textarea(attrs={'class': 'form_control'}))
	birthday = forms.DateField()
	
	
	
class ArticleForms(forms.Form):
	title = forms.CharField(max_length=100)
	content = forms.CharField(widget=forms.Textarea())
	author = forms.ModelChoiceField(queryset=Author.objects.all())
	category = forms.CharField(max_length=100)



class AddCommentary(forms.Form):
    """Add a new commentary by author to a database"""

    authors = [(f'{author.pk}', f'{author.surname} {author.name}')
               for author in Author.objects.all()]
    author_pk = forms.ChoiceField(choices=authors)
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))