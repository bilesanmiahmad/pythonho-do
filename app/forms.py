from django import forms


class BlogPostForm(forms.Form):
    title = forms.CharField(label="Title", max_length=150)
    content = forms.CharField(widget=forms.Textarea)
    status = forms.ChoiceField(choices=[("draft", "Draft"), ("published", "Published")])
