from django.urls import path

from contact.views import ContactView, AboutView, CreateContact


urlpatterns = [
    path('contact/', ContactView.as_view(), name="contact"),
    path('about/', AboutView.as_view(), name="about"),
    path('feedback/', CreateContact.as_view(), name="feedback"),
]
