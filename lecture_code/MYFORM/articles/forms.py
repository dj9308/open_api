from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(
        max_length=10,
        label='제목',
        widget= forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder':'Enter the title',

            }
        )
        )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class':'my-content',
                'placeholder':'Enter the content',
                'rows':5,
                'cols':50,
            }
        )
    )
    #widget: 표현을 어떻게 구성할지 설정해주는 것.