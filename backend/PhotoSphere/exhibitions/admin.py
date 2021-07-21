from django.contrib import admin
from exhibitions.models import Exhibition, ExhibitionEntry


@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    pass


@admin.register(ExhibitionEntry)
class ExhibitionEntryAdmin(admin.ModelAdmin):
    pass
