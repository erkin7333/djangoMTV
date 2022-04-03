from django.urls import path
from .views import AgentListView, AgentCreateView, AgentDetailView, AgentUpdateView, AgetDeleteView


app_name = 'agents'



urlpatterns = [
    path('', AgentListView.as_view(), name='agents'),
    path('agent/create/', AgentCreateView.as_view(), name='agents-create'),
    path('agent/detail/<int:pk>/', AgentDetailView.as_view(), name='agents-detail'),
    path('agent/update/<int:pk>/', AgentUpdateView.as_view(), name='agents-update'),
    path('agent/delete/<int:pk>/', AgetDeleteView.as_view(), name='agents-delete'),
]