import sys
from pathlib import Path
from colorama import Fore, Style, init


def format_entry(path: Path, is_dir: bool) -> str:
    """Return colored name for a directory or file."""
    if is_dir:
        return f"{Fore.CYAN}{path.name}{Style.RESET_ALL}"
    return f"{Fore.GREEN}{path.name}{Style.RESET_ALL}"


def print_tree(root: Path, prefix: str = "") -> None:
    """
    Recursively prints directory structure starting from root.

    prefix is used to draw the tree branches nicely.
    """
    # беремо лише видимі елементи; за бажанням можна прибрати фільтр
    entries = sorted(root.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))

    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        branch = "└── " if is_last else "├── "
        next_prefix = prefix + ("    " if is_last else "│   ")

        print(prefix + branch + format_entry(entry, entry.is_dir()))

        if entry.is_dir():
            print_tree(entry, next_prefix)


def main() -> None:
    init(autoreset=True)

    if len(sys.argv) != 2:
        print("Usage: python tree_view.py <path_to_directory>")
        sys.exit(1)

    root = Path(sys.argv[1])

    if not root.exists():
        print(f"{Fore.RED}Error: Path does not exist.{Style.RESET_ALL}")
        sys.exit(1)

    if not root.is_dir():
        print(f"{Fore.RED}Error: Path is not a directory.{Style.RESET_ALL}")
        sys.exit(1)

    # Заголовок (корінь)
    print(f"{Fore.CYAN}{root.resolve()}{Style.RESET_ALL}")
    print_tree(root)


if __name__ == "__main__":
    main()