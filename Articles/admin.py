from django.contrib import admin
from .models import Articles  # Make sure this matches the model name


class Acticle_admin(admin.ModelAdmin):
    list_display= ['id',"title"]
    search_fields=['id',"title"]

admin.site.register(Articles,Acticle_admin)
