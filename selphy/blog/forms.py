from django import forms
from .models import Comments
# Create ckeditor for flatpages
# from django.contrib.flatpages.forms import FlatpageForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CommentForm(forms.ModelForm):
    class   Meta:
        model= Comments
        fields= '__all__'
        exclude={'blog'}
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Your name','class':'form-control'}),
            'title':forms.TextInput(attrs={'placeholder':'Title of the comment','class':'form-control'}),
            'email':forms.EmailInput(attrs={'placeholder':'Your email address','class':'form-control'}),
            'comment':forms.Textarea(attrs={'placeholder':'Your comment','class':'form-control'})
            
        }


# class Flatpageform(FlatpageForm):
#     content=forms.CharField(widget=CKEditorUploadingWidget())