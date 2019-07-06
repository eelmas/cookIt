from django import forms

# from recipes.models import MeasureTable

f = open("OPTIONS.txt", "r")


class UserProduct(forms.Form):
    OPTIONS = ()

    # products = MeasureTable.objects.values_list('name').distinct()
    products = f.read()
    products = products.split("\n")
    for i in products:
        i = (i,)
        x = i + i
        OPTIONS = (x,) + OPTIONS

    userProducts = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class': 'recipes-user-products'}),
                                             choices=OPTIONS, label='')
