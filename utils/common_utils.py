from authenticatorX.exception import AuthenticatorXException
from jsonschema import validate
from jsonschema.exceptions import ValidationError


def json_schema_validate(instance_data, schema):
    """
    Validate JSON data against a JSON schema.

    Args:
        instance_data (dict): The JSON data to be validated.
        schema (dict): The JSON schema used for validation.

    Returns:
        None

    Raises:
        AuthenticatorXException: If the data fails validation.

    """

    def json_schema_validate_inner_func(requested_data, json_validator_schema):
        """
        Inner function to perform the JSON schema validation.

        Args:
            requested_data (dict): The JSON data to be validated.
            json_validator_schema (dict): The JSON schema used for validation.

        Returns:
            str: The validation error message, if any.

        """
        try:
            validate(instance=requested_data, schema=json_validator_schema)
        except ValidationError as error:
            if requested_data is not None:
                for x in json_validator_schema.get('required'):
                    if x not in requested_data:
                        return f"{x}, Field Is Required"
            else:
                return f"{json_validator_schema.get('required')[0]}, Field Is Required"
            keyword = error.path[0] if len(error.path) > 0 else ""
            return f"{keyword} : {error.message}"

    not_valid = json_schema_validate_inner_func(instance_data, schema)
    if not_valid:
        raise AuthenticatorXException(not_valid)
    else:
        return None
