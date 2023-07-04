from authenticatorX_app.views import SendOTP
from django.urls import path

urlpatterns = [
    path('send-otp/', SendOTP.as_view())

]
