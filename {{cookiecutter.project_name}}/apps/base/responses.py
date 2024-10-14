from rest_framework.response import Response as _Response


class Response(_Response):
    def __init__(self, data=None, message='', meta=None, status=None, template_name=None, headers=None,
                 content_type=None, errors=None):
        if meta is None:
            meta = dict()
        response_data = {
            'message': message,
            'meta': meta
        }
        if data:
            response_data['data'] = data
        if errors:
            response_data['errors'] = errors
        super().__init__(
            data=response_data, status=status, template_name=template_name, headers=headers, content_type=content_type
        )
