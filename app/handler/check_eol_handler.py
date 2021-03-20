import re
from app.handler import AbstractHandler

class CheckEOLHandler(AbstractHandler):

    def handle(self, code) -> str:
        list_strings = [s.strip() for s in code.splitlines() if s]
        for l in list_strings:
            if not l.endswith(";"):
                raise Exception("Sintaxe error!")
        return super().handle(code)


    
    