from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your message...',
                'class': 'flex-grow p-2.5 w-[390px] text-sm text-gray-900 bg-white rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                #'class': 'pt-2 rounded-lg w-[390px] px-2 text-sm text-gray-900 flex bg-white dark:bg-gray-800 focus:outline-none dark:text-white dark:placeholder-gray-400',     
                'rows': '1'
            }),

        }