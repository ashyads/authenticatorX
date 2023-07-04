import json

from authenticatorX.responses import SuccessResponse
from authenticatorX.settings import SNS_CLIENT
from rest_framework.views import APIView
from utils.common_utils import json_schema_validate
from utils.send_sms import otp_sms_message, generate_random_otp
from utils.send_whatsapp import SendWhatsapp


class SendOTP(APIView):

    def post(self, request, requests=None):
        requested_data = request.data
        with open("json-schemas/send_otp_api_request_schema.json", "r") as f:
            send_otp_api_request_schema = json.loads(f.read())
        json_schema_validate(requested_data, send_otp_api_request_schema)
        mobile = requested_data.get("mobile")
        plain_otp = generate_random_otp()
        SNS_CLIENT.publish(PhoneNumber=f"+91{mobile}", Message=otp_sms_message(plain_otp))
        requests.get(SendWhatsapp.opt_in(**{"mobile": mobile}))
        requests.get(SendWhatsapp.send_otp_001(**{"mobile": mobile, "otp": plain_otp}))
        return SuccessResponse(message="Otp Sent Successfully")
