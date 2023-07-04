from rest_framework import status
from rest_framework.response import Response


class BaseResponse(Response):
    def __init__(self, data=None, message=None, status=True):
        data_content = {
            'status': status,
            'message': message,
            'data': data,
        }
        super(BaseResponse, self).__init__(
            data=data_content
        )


class NegativeResponse(BaseResponse):
    def __init__(self, data=None, message=None, status=False):
        super().__init__(data=data, status=status, message=message)


class PositiveResponse(BaseResponse):
    def __init__(self, data=None, message=None, status=True):
        super().__init__(data=data, status=status, message=message)


class SuccessResponse(PositiveResponse):
    status_code = status.HTTP_200_OK


class CreateResponse(PositiveResponse):
    status_code = status.HTTP_201_CREATED


class NoContentResponse(NegativeResponse):
    status_code = status.HTTP_204_NO_CONTENT


class BadRequestResponse(NegativeResponse):
    status_code = status.HTTP_400_BAD_REQUEST


class GoneResponse(NegativeResponse):
    status_code = status.HTTP_410_GONE


class AccessDeniedResponse(NegativeResponse):
    status_code = status.HTTP_401_UNAUTHORIZED


class ForbiddenErrorResponse(NegativeResponse):
    status_code = status.HTTP_403_FORBIDDEN


class NotAcceptableResponse(NegativeResponse):
    status_code = status.HTTP_406_NOT_ACCEPTABLE


class UnProcessableEntityResponse(NegativeResponse):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY


class NotFoundResponse(NegativeResponse):
    status_code = status.HTTP_404_NOT_FOUND
