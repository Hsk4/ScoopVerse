from django.contrib import admin
from .models import ContactFormSubmission


@admin.register(ContactFormSubmission)
class ContactFormSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'submitted_at']
    list_filter = ['submitted_at']
    search_fields = ['name', 'email', 'message']
