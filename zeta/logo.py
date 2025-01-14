from rich import print as rich_print
from rich.markdown import Markdown
from rich.rule import Rule
from termcolor import colored, cprint


def display_markdown_message(message):
    """
    Display markdown message. Works with multiline strings with lots of indentation.
    Will automatically make single line > tags beautiful.
    """

    for line in message.split("\n"):
        line = line.strip()
        if line == "":
            print("")
        elif line == "---":
            rich_print(Rule(style="white"))
        else:
            rich_print(Markdown(line))

    if "\n" not in message and message.startswith(">"):
        # Aesthetic choice. For these tags, they need a space below them
        print("")


def print_colored_logo():
    with open("zeta/logo.txt", "r") as file:
        logo = file.read()
    text = colored(logo, "blue")
    print(text)
