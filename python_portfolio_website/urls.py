from django.urls import path
from python_portfolio_website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('education/', views.education, name='education'),
    path('competences/', views.competences, name='competences'),
    path('projets/', views.projets, name='projets'),
    path('contact/', views.contact, name='contact'),
    path('contact/submit_mail', views.submit_mail, name="submit_mail"),
]