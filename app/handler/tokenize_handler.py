import re
from app.handler import AbstractHandler
import app.language.rules as rules

class TokenizeHandler(AbstractHandler):

    def handle(self, code) -> str:
        all_rules_regex = '|'.join('(?P<%s>%s)' % x for x in rules.REGEX_RULES)
        accu_line = 1
        result = []
        for m in re.finditer(all_rules_regex, code):
            line = {}
            if m.lastgroup == "ERROR_CODE":
                raise Exception("%s Erro on the line %d" % (m.group(), accu_line))
            if m.lastgroup == "NEW_LINE":
                accu_line += 1
                continue

            line["lexeme"] = m.group()
            line["type"] = m.lastgroup

            # Set token
            if m.lastgroup == "OPERATION":
                line["token"] = rules.VALUES_OPERATIONS[m.group()]
            elif m.lastgroup == "NUMBER":
                line["token"] = m.group()
            else:
                line["token"] = m.lastgroup
            
            
            result.append(line)
        return result
