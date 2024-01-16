from django import forms
from .models import Item, Category

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','price','image',)


    category = forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select(attrs={
        'class': 'bg-slate-300 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5'
    }))
       
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Type product name',
        'class': 'bg-slate-300 border border-gray-300 text-gray-900 placeholder:text-gray-600 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5'
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Write product description here',
        'class': 'block p-2.5 w-full text-sm text-gray-900 placeholder:text-gray-600 bg-slate-300 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500'
    }))

    price = forms.DecimalField(widget=forms.NumberInput(attrs={
        'placeholder': 'eg.$49.99',
        'class': 'bg-slate-300 border border-gray-300 text-gray-900 placeholder:text-gray-600 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5'
    }))

    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'class': 'bg-slate-300 border border-gray-300 text-gray-900 placeholder:text-gray-600 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5'
    }))

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','description','price','image','is_sold')
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Type product name',
        'class': 'bg-slate-300 border border-gray-300 text-gray-900 placeholder:text-gray-600 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5'
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Write product description here',
        'class': 'block p-2.5 w-full text-sm text-gray-900 placeholder:text-gray-600 bg-slate-300 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500'
    }))

    price = forms.DecimalField(widget=forms.NumberInput(attrs={
        'placeholder': 'eg.$49.99',
        'class': 'bg-slate-300 border border-gray-300 text-gray-900 placeholder:text-gray-600 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5'
    }))

    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'class': 'bg-slate-300 border border-gray-300 text-gray-900 placeholder:text-gray-600 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5'
    }))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['image'].widget.initial_text = 'Current Image'
        self.fields['image'].widget.input_text = 'Upload the new Image'

    is_sold = forms.BooleanField(required=False,widget=forms.CheckboxInput())
       