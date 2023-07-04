import json

from authenticatorX.responses import SuccessResponse
from rest_framework.views import APIView
from utils.common_utils import json_schema_validate
from utils.send_sms import generate_random_otp, SendSMS
from utils.send_whatsapp import SendWhatsapp


class SendOTP(APIView):

    def post(self, request, requests=None):
        requested_data = request.data
        with open("json-schemas/send_otp_api_request_schema.json", "r") as f:
            send_otp_api_request_schema = json.loads(f.read())
        json_schema_validate(requested_data, send_otp_api_request_schema)
        mobile = requested_data.get("mobile")
        plain_otp = generate_random_otp()
        SendSMS().send_otp(mobile=mobile, plain_otp=plain_otp)
        requests.get(SendWhatsapp.opt_in(**{"mobile": mobile}))
        requests.get(SendWhatsapp.send_otp(**{"mobile": mobile, "otp": plain_otp}))
        return SuccessResponse(message="Otp Sent Successfully")
