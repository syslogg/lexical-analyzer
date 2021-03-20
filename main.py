from app.handler.check_eol_handler import CheckEOLHandler
from app.handler.remove_comments_handler import RemoveCommentsHandler
from app.handler.tokenize_handler import TokenizeHandler
from app.handler import Handler

import pandas as pd
import click

def client_code(file_path: str, handle: Handler):
    with open(file_path) as f:
        inputData = f.read()
        click.echo(pd.DataFrame(handle.handle(inputData)).to_string())

@click.command()
@click.option('--file', '-f', help="File path to analyze")
def main(file):
    remove_comments = RemoveCommentsHandler()
    check_eol = CheckEOLHandler()
    tokenize = TokenizeHandler()

    remove_comments.set_next(check_eol) \
                   .set_next(tokenize)

    client_code(file, remove_comments)

if __name__ == "__main__":
    main()