"""A festive terminal Christmas card for the Python community"""

import random
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text
from rich import box

# Festive Python code snippets
SNIPPETS = [
    '''x = "Deck the halls with boughs of holly"
def sing(): return ["Fa"] + ["la"] * 8
print(" ".join(sing()))''',

    '''# Tis the season to be jolly
gifts = ["joy", "peace", "code"]
for gift in gifts:
    print(f"Sharing {gift} with you!")''',

    '''def spread_cheer(times=3):
    return "Ho! " * times

print(spread_cheer())
# Ho! Ho! Ho!''',

    '''wishes = {
    "joy": float("inf"),
    "bugs": 0,
    "hot_cocoa": True,
}''',

    '''from datetime import date
today = date(2025, 12, 25)
print(f"Merry Christmas {today.year}!")''',

    '''class Holiday:
    def __init__(self):
        self.spirit = "bright"
        self.code = "clean"
        self.coffee = "warm"''',

    '''# The best gift
def open_source():
    """Share freely, build together"""
    return "community"''',
]

def print_tree(console):
    """Print a colorful ASCII Christmas tree"""
    ornament_colors = ["bold red", "bold blue", "bold yellow", "bold magenta", "bold cyan"]

    tree = Text()
    # Each line has leading spaces to align relative to the 11-char base
    tree.append("     ")
    tree.append("*", style="bold yellow")
    tree.append("\n")

    tree.append("    /", style="green")
    tree.append("*", style=random.choice(ornament_colors))
    tree.append("\\", style="green")
    tree.append("\n")

    tree.append("   /", style="green")
    tree.append("o", style=random.choice(ornament_colors))
    tree.append("*", style="green")
    tree.append("o", style=random.choice(ornament_colors))
    tree.append("\\", style="green")
    tree.append("\n")

    tree.append("  /", style="green")
    tree.append("*", style=random.choice(ornament_colors))
    tree.append("o*o", style="green")
    tree.append("*", style=random.choice(ornament_colors))
    tree.append("\\", style="green")
    tree.append("\n")

    tree.append(" /", style="green")
    tree.append("o", style=random.choice(ornament_colors))
    tree.append("*o*o*", style="green")
    tree.append("o", style=random.choice(ornament_colors))
    tree.append("\\", style="green")
    tree.append("\n")

    tree.append("/", style="green")
    tree.append("*", style=random.choice(ornament_colors))
    tree.append("o*o*o*o", style="green")
    tree.append("*", style=random.choice(ornament_colors))
    tree.append("\\", style="green")
    tree.append("\n")

    tree.append("     ")
    tree.append("|", style="rgb(139,69,19)")

    from rich.align import Align
    console.print(Align.center(tree))

# Rich-compatible Pygments themes (good contrast in terminals)
THEMES = [
    "monokai", "dracula", "nord", "gruvbox-dark", "one-dark",
    "material", "native", "vim", "rrt", "fruity", "igor",
    "lovelace", "algol_nu", "friendly_grayscale", "rainbow_dash",
]


def make_snowfall(width=50):
    """Create a line of random snowflakes"""
    snowflakes = ["*", ".", "+", "~"]
    line = ""
    for _ in range(width):
        if random.random() < 0.12:
            line += random.choice(snowflakes)
        else:
            line += " "
    return line


def render_card():
    """Render the full Christmas card to terminal"""
    console = Console()

    # Pick random snippet and theme
    snippet = random.choice(SNIPPETS)
    theme = random.choice(THEMES)

    # Create syntax-highlighted code
    syntax = Syntax(snippet, "python", theme=theme, line_numbers=False)

    # Build the card
    console.print()
    print_tree(console)
    console.print(f"[white]{make_snowfall(50)}[/white]", justify="center")
    console.print()
    console.print(Panel(syntax, border_style="dim", box=box.ROUNDED))
    console.print()
    console.print(f"[white]{make_snowfall(50)}[/white]", justify="center")
    console.print()

    # Message
    console.print("[bright_white]Wishing the Python community[/bright_white]", justify="center")
    console.print("[bright_white]a joyful holiday season and[/bright_white]", justify="center")
    console.print("[bright_white]a wonderful new year![/bright_white]", justify="center")
    console.print()
    console.print("[white]With love & gratitude,[/white]", justify="center")
    console.print("[bold]Audrey & Daniel Roy Greenfeld[/bold]", justify="center")
    console.print("[dim]@audreyfeldroy & @pydanny[/dim]", justify="center")
    console.print()
    console.print(f"[dim italic]theme: {theme}[/dim italic]", justify="center")
    console.print()


def main():
    """CLI entry point"""
    render_card()


if __name__ == "__main__":
    main()
