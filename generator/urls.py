from django.urls import path
from .views import PromptListCreate, PromptDetail

urlpatterns = [
    path('api/prompts/', PromptListCreate.as_view(), name='prompts_list_create'),
    path('api/prompts/<int:pk>/', PromptDetail.as_view(), name='prompts_detail'),
]