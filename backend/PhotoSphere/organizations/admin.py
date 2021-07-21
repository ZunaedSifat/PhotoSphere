from django.contrib import admin
from organizations.models import OrganizationMember, Organization


@admin.register(OrganizationMember)
class OrganizationMemberAdmin(admin.ModelAdmin):
    list_filter = ('member', )


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_filter = ('name', )
