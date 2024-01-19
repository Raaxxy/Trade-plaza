from django import forms
from .models import Item, Category

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','price','image',)


    category = forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select(attrs={
        'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
    }))
       
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Type product name',
        'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Write product description here',
        'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
    }))

    price = forms.DecimalField(widget=forms.NumberInput(attrs={
        'placeholder': 'eg.$49.99',
        'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
    }))

    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
    }))

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','description','price','image','is_sold')
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Type product name',
        'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

        
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Write product description here',
        'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

        
    }))

    price = forms.DecimalField(widget=forms.NumberInput(attrs={
        'placeholder': 'eg.$49.99',
        'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

        
    }))

    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={
         'class': 'bg-gray-50 border border-gray-300 text-white sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 placeholder:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
         #this part needs a little bit of polishing
    }))
    
    is_sold = forms.BooleanField(required=False,widget=forms.CheckboxInput())


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['image'].widget.initial_text = 'Current Image'
        self.fields['image'].widget.input_text = 'Upload the new Image'

    
       