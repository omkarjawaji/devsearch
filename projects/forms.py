from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags']  #'__all__' # or [with all the fileds as a list] 