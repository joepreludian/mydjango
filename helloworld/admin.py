from django.contrib import admin
from helloworld.models import People


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    pass
