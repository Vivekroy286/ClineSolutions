from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'placeholder': 'Type your question here...',
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-400',
            }),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Write your answer...',
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-400',
                'rows': 4,
            }),
        }
        