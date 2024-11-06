from django.urls import path
from . import views

urlpatterns = [
    path('', views.LaboratorioListView.as_view(), name='laboratorio_list'),
    path('add/', views.LaboratorioCreateView.as_view(), name='laboratorio_add'),
    path('<int:pk>/edit/', views.LaboratorioUpdateView.as_view(), name='laboratorio_edit'),
    path('<int:pk>/delete/', views.LaboratorioDeleteView.as_view(), name='laboratorio_delete'),
]