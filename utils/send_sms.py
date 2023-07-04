from random import randint


def otp_sms_message(plain_otp):
    return f"""{plain_otp} is your OTP (One Time Password) for logging into the app. For security reasons, 
    do not share the OTP."""


def generate_random_otp():
    return randint(10000, 99999)
