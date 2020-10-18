from django.contrib import admin
from .models import PublicationsTable
from .models import AuthorsTable


admin.site.register(PublicationsTable)
admin.site.register(AuthorsTable)