from django.db import models
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import UserAudit


class UserAuditAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={'size': 160})},
    }

    list_display = [
        'id',
        'user',
        'audit_key',
        'ip_address',
        'user_agent',
        'referrer',
        'last_page',
        'pages_viwed',
        'force_logout',
        'updated_at',
        'created_at',
    ]

    search_fields = [
        'user__username',
        'ip_address',
        'user_agent',
        'referrer',
    ]

    list_per_page = 25

admin.site.register(UserAudit, UserAuditAdmin)
