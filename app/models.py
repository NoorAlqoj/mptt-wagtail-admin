from django import forms
from django.core.validators import MinLengthValidator
from django.db import models

# from treebeard.mp_tree import MP_Node
from mptt.models import MPTTModel, TreeForeignKey
from wagtail.admin.forms import WagtailAdminModelForm
from wagtail.admin.edit_handlers import FieldPanel

class Category(MPTTModel):
    
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    def __str__(self):
        return self.name