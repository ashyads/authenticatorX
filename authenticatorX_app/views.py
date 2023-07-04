import json

from authenticatorX.responses import SuccessResponse
from rest_framework.views import APIView
from utils.common_utils import json_schema_validate


class SendOTP(APIView):

    def post(self, request):
        requested_data = request.data
        with open("json-schemas/send_otp_api_request_schema.json", "r") as f:
            send_otp_api_request_schema = json.loads(f.read())
        json_schema_validate(requested_data, send_otp_api_request_schema)
        return SuccessResponse()
