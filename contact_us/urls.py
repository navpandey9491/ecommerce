from django.urls import path
from . import views

app_name = 'contact_us'
urlpatterns = [
    path("", views.contact_message_creations, name="contact_us")
]
