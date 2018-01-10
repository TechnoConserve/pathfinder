from prompt_toolkit import prompt
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.history import InMemoryHistory


def main_help():
    """Print the main help dialog for this CLI."""
    print('This CLI will guide you through the process of creating a character for Pathfinder.')
    print('\n')


def main():
    # Provide some information about this program.
    main_help()


if __name__ == '__main__':
    main()
