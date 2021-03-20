from app.handler.check_eol_handler import CheckEOLHandler
from app.handler.remove_comments_handler import RemoveCommentsHandler
from app.handler.tokenize_handler import TokenizeHandler
from app.handler import Handler

def client_code(handle: Handler):
    with open("input.txt") as f:
        inputData = f.read()
        print(handle.handle(inputData))




def main():
    

    remove_comments = RemoveCommentsHandler()
    check_eol = CheckEOLHandler()
    tokenize = TokenizeHandler()

    remove_comments.set_next(check_eol) \
                   .set_next(tokenize)

    # Client
    client_code(remove_comments)


if __name__ == "__main__":
    main()