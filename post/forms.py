from django import forms
from post.models import PostType


class AddBoastOrRoast(forms.Form):
    is_boast = forms.ModelChoiceField(PostType.objects.all())
    text = forms.CharField(widget=forms.Textarea)
