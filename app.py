from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.validation import Validator, ValidationError

from dice import roll
from models import Ability, Character, Combat, Skill, db, create_tables

ABILITY_GENERATOR_METHODS = ['Standard', 'Classic', 'Heroic', 'Dice Pool', 'Purchase']
ABILITIES = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']


class AbilityMethodValidator(Validator):
    def validate(self, document):
        text = document.text

        if text not in ABILITY_GENERATOR_METHODS:
            raise ValidationError(message='Please choose a valid ability generator method.')


class AbilityValidator(Validator):
    def validate(self, document):
        text = document.text

        if text not in ABILITIES:
            raise ValidationError(message='Please choose a valid ability name.')


def main_help():
    """Print the main help dialog for this CLI."""
    print('This CLI will guide you through the process of creating a character for Pathfinder.')
    print('\n')


def generate_ability_scores(ability_generator_method):
    print('Generating ability scores using the {} method'.format(ability_generator_method))
    if ability_generator_method == 'Standard':
        print('\nGenerating 6 numbers for your abilities...')
        ability_rolls = 6
        ability_results = []
        while ability_rolls > 0:
            ability_results.append(make_ability_roll())
            ability_rolls -= 1

        print('Your roll totals were', ability_results)
        ability_option_completer = WordCompleter(ABILITIES)
        ability_options = ABILITIES.copy()
        ability_selection = {}
        for result in ability_results:
            ability = prompt('\nWhich ability would you like to apply roll {} to?'
                             '\n\nAbilities are: {}\n\n>>> '.format(result, ', '.join(ability_options)),
                             completer=ability_option_completer, validator=AbilityValidator())
            ability_selection[ability] = result
            ability_options.remove(ability)

        print(ability_selection)


def make_ability_roll():
    rolls = 4
    roll_results = []
    while rolls > 0:
        input('Press a key to roll your d6...')
        roll_results += roll(6)
        print('\nYou rolled a', roll_results[-1])
        rolls -= 1
    print('Discarding your lowest roll...')
    roll_results.remove(min(roll_results))
    roll_result_total = sum(roll_results)
    print('Your rolls were {} for a total of {}.\n'.format(roll_results, roll_result_total))
    return roll_result_total


def create_character():
    ability_generator_completer = WordCompleter(ABILITY_GENERATOR_METHODS)
    ability_generator_method = prompt('Choose your preferred method for generating your ability scores.'
                                      '\n\nOptions are: Standard, Classic, Heroic, Dice Pool, or Purchase\n\n>>> ',
                                      completer=ability_generator_completer, validator=AbilityMethodValidator())
    generate_ability_scores(ability_generator_method)


def main():
    # Provide some information about this program.
    main_help()
    create_tables(db)
    create_character()


if __name__ == '__main__':
    main()
