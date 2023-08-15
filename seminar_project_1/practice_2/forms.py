from django import forms


class ProductForm(forms.Form):
	name = forms.CharField(max_length=100)
	description = forms.CharField(widget=forms.Textarea)
	price = forms.DecimalField()
	count = forms.IntegerField()


class ProductImageForm(forms.Form):
	image = forms.ImageField()
