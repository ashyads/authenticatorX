from abc import ABCMeta

from rest_framework import status
from rest_framework.exceptions import APIException


class AuthenticatorXException(APIException, metaclass=ABCMeta):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs.get("code"):
            self.status_code = kwargs.get("code")
        else:
            self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = dict(status=False, message=self.detail, data=None)
