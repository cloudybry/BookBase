from django.db import models


class Prompt(models.Model):
    title = models.CharField(
        max_length=100,
        help_text="Title of the prompt (1–100 characters)"
    )
    description = models.TextField(
        help_text="Detailed description of the prompt"
    )
    created_at = models.DateTimeField(auto_now_add=True)