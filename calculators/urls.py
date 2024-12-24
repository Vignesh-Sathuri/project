from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('sip/', views.sip_calculator, name='sip_calculator'),
    path('rd/', views.rd_calculator, name='rd_calculator'),
    path('pomis/', views.pomis_calculator, name='pomis_calculator'),
    path('gst/', views.gst_calculator, name='gst_calculator'),
    path('simple_interest/', views.simple_interest_calculator, name='simple_interest_calculator'),
    path('compound_interest/', views.compound_interest_calculator, name='compound_interest_calculator'),
    path('ssy/', views.ssy_calculator, name='ssy_calculator'),
    path('fd/', views.fd_calculator, name='fd_calculator'),
    path('emi/', views.emi_calculator, name='emi_calculator'),
]