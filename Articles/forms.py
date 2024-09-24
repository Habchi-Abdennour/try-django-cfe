from typing import Any
from django import forms
from .models import Articles



class ArticlesForms(forms.ModelForm):
    
    class Meta:
        model=Articles
        fields=['title','subtitle','content']
        
    def clean(self):
        data=self.cleaned_data
        title=data.get('title')
        qs=Articles.objects.all().filter(title__icontains=title)
        if qs.exists():
            self.add_error('title',f'we aleardy has that "{title} " in our database')
        return data
    





# class ArticlesFormsOld(forms.Form):
#     title=forms.CharField(max_length=200, required=False)
#     subtitle=forms.CharField(max_length=100, required=False)
#     content=forms.CharField(max_length=100, required=False)

    
#     # def clean_title(self):
#     #     cleaned_data =self.cleaned_data
#     #     title=cleaned_data.get("title")
#     #     if title=="hello":
#     #         raise forms.ValidationError("Mourinho The Villain")
        
#     #     return title
    
#     def clean(self) :
#         cleaned_data=self.cleaned_data
#         title=cleaned_data.get('title')
#         if title == None:
#             self.add_error('title','should be write one ')
#         return cleaned_data
    
    
    