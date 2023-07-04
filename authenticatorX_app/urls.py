from django.urls import path

from authenticatorX_app.views import SendOtp

urlpatterns = [
    path('send-otp/', SendOtp.as_view())

]
