from django import forms

from .models import Post

from ckeditor_uploader.fields import RichTextUploadingFormField


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'resume', 'content', 'image']

        widgets = {
            'content': RichTextUploadingFormField(
                config_name="my-custom-toolbar"
            ),
            'resume': RichTextUploadingFormField(
                config_name="my-custom-toolbar"
            )
        }
