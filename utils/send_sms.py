from random import randint

from authenticatorX.settings import SNS_CLIENT


def otp_sms_message(plain_otp):
    return f"""{plain_otp} is your OTP (One Time Password) for logging into the app. For security reasons, 
    do not share the OTP."""


def generate_random_otp():
    return randint(10000, 99999)


class SendSMS:

    @classmethod
    def send_otp(cls, mobile, plain_otp):
        SNS_CLIENT.publish(PhoneNumber=f"+91{mobile}", Message=otp_sms_message(plain_otp))
