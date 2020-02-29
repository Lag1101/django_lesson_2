from django import forms

from .models import Comment, Article


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            })
        }

#
# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ['header', 'markdown']
#         widgets = {
#             'header': forms.TextInput(attrs={
#                 'class': 'form-control'
#             }),
#             'markdown': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'rows': 15
#             })
#         }
