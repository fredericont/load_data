from django.urls import path
from app_upload_arquivos import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('anexo/', views.anexo, name='anexo')
]
