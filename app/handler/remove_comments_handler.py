import re
from app.handler import AbstractHandler

class RemoveCommentsHandler(AbstractHandler):

    def handle(self, code) -> str:
        code = re.sub(r'@.*', '', code)
        return super().handle(code)
