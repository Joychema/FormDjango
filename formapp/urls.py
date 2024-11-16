from django.urls import path
from .import views
from .views import contact_view

urlpatterns=[
    path('',views.contact_view,name='home'),

    path('contact/',views.contact_view,name='contact')
]