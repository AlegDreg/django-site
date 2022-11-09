from django.db import models
from django.core.serializers.json import DjangoJSONEncoder

class Answer():
    def __init__(self, status_code, message):
        self.code = status_code
        self.message = message

class AnswerEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Answer):
            return {"code": obj.code, "message": obj.message}
        return super().default(obj)

class Error(Answer):
    def __init__(self, message):
        super().__init__("ERROR", message)

class Alright(Answer):
    def __init__(self, message, serializer = None):

        a = message
        if serializer != None:
            a = serializer(message).data
        super().__init__("OK", a)
