"""
second = 17
third = 13
fourth = 17
fifth = 18
sixth = 18
seventh = 17

perception = 2
nature = 1
stealth = 2
dungeoneering = 2
heals = 1
climb = 2

longbow = 75
arrows = 4
starknife = 24
studded_leather = 25
"""
from dice import roll


def classic_ability_gen():
    """Generate ability scores using classic method."""
    print('Generating ability scores using the classic method.')
    scores = []

    # Roll four six-sided die six times
    for score in range(6):
        print('Rolling three six-sided die...')
        rolls = roll(num_die=3, sides=6)
        print('Got:', rolls)

        result = sum(rolls)
        print('Sum of this roll:', result)
        scores.append(result)

    print('Final scores are:', scores)
    return scores


def heroic_ability_gen():
    """Generate ability scores using heroic method."""
    print('Generating ability scores using the heroic method.')
    scores = []

    # Roll four six-sided die six times
    for score in range(6):
        print('Rolling two six-sided die...')
        rolls = roll(num_die=2, sides=6)
        print('Got:', rolls)

        result = sum(rolls)
        print('Sum of this roll:', result)
        print('Adding six to the sum...')
        scores.append(result + 6)

    print('Final scores are:', scores)
    return scores


def standard_ability_gen():
    """Generate ability scores using standard method."""
    print('Generating ability scores using the standard method.')
    scores = []

    # Roll four six-sided die six times
    for score in range(6):
        print('Rolling four six-sided die...')
        rolls = roll(num_die=4, sides=6)
        print('Got:', rolls)

        print('Dropping the lowest value...')
        # Drop the lowest value
        rolls.remove(min(rolls))
        result = sum(rolls)
        print('Sum of this roll:', result)
        scores.append(result)

    print('Final scores are:', scores)
    return scores


def generate_ability_scores(method=None):
    """Generate character ability scores based on given method."""
    switcher = {
        'classic': classic_ability_gen,
        'heroic': heroic_ability_gen,
        'standard': standard_ability_gen,
    }
    func = switcher.get(method, standard_ability_gen)
    return func()
