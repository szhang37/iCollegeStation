from django.forms import ModelForm
from models import Comment

# Create the form class.
class CommentForm(ModelForm):
    class Meta:
            model = Comment
            fields = ['pub_date', 'name', 'content']
