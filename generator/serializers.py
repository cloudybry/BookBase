from rest_framework import serializers
from .models import Prompt

class PromptSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        min_length=1,
        max_length=100,
        help_text="Title of the prompt (1–100 characters)"
    )
    description = serializers.CharField(
        min_length=1,
        help_text="Detailed description of the prompt"
    )
    created_at_formatted = serializers.SerializerMethodField()

    class Meta:
        model = Prompt
        fields = ['id', 'title', 'description', 'created_at', 'created_at_formatted']

    def get_created_at_formatted(self, obj):
        return obj.created_at.strftime('%m/%d/%Y')