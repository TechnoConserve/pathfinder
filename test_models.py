from peewee import IntegrityError
from playhouse.sqlite_ext import SqliteExtDatabase
import pytest

from models import Ability, Character, create_tables


@pytest.fixture()
def database():
    db = SqliteExtDatabase(':memory:')
    create_tables(db)
    yield db
    db.drop_tables([Ability, Character])


def test_character_creation(database):
    with database.transaction():
        character = Character.create(
            character_name='Qritz',
            player_name='Avery',
            alignment='CG',
            race='elf',
            size='md',
            gender='male',
            age='29',
            height_ft='5',
            height_in='4',
            weight='109',
            hair_color='black',
            eye_color='brown'
        )
    from_db = Character.get(Character.character_name == 'Qritz')
    assert from_db == character
    assert Character.select().count() == 1


@pytest.mark.xfail
def test_character_creation_age_constraint(database):
    with database.transaction():
        character = Character.create(
            character_name='Qritz',
            player_name='Avery',
            alignment='CG',
            race='elf',
            size='md',
            gender='male',
            age='0',
            height_ft='5',
            height_in='4',
            weight='109',
            hair_color='black',
            eye_color='brown'
        )


def test_character_creation_ht_ft_constraint(database):
    with pytest.raises(IntegrityError) as excinfo:
        with database.transaction():
            # Create character that is too tall
            character1 = Character.create(
                character_name='Qritz1',
                player_name='Avery',
                alignment='CG',
                race='elf',
                size='md',
                gender='male',
                age='29',
                height_ft='31',
                height_in='4',
                weight='109',
                hair_color='black',
                eye_color='brown'
            )
    assert 'CHECK constraint failed: character' in str(excinfo.value)

    with pytest.raises(IntegrityError) as excinfo:
        with database.transaction():
            # Create character that is too small
            character2 = Character.create(
                character_name='Qritz2',
                player_name='Avery',
                alignment='CG',
                race='elf',
                size='md',
                gender='male',
                age='29',
                height_ft='-1',
                height_in='4',
                weight='109',
                hair_color='black',
                eye_color='brown'
            )
    assert 'CHECK constraint failed: character' in str(excinfo.value)


def test_character_creation_ht_in_constraint(database):
    with pytest.raises(IntegrityError) as excinfo:
        with database.transaction():
            # Create character with height in inches greater than 11
            character1 = Character.create(
                character_name='Qritz1',
                player_name='Avery',
                alignment='CG',
                race='elf',
                size='md',
                gender='male',
                age='29',
                height_ft='5',
                height_in='12',
                weight='109',
                hair_color='black',
                eye_color='brown'
            )
    assert 'CHECK constraint failed: character' in str(excinfo.value)

    with pytest.raises(IntegrityError) as excinfo:
        with database.transaction():
            # Create character with height in inches greater less than 0
            character2 = Character.create(
                character_name='Qritz2',
                player_name='Avery',
                alignment='CG',
                race='elf',
                size='md',
                gender='male',
                age='29',
                height_ft='5',
                height_in='-1',
                weight='109',
                hair_color='black',
                eye_color='brown'
            )
    assert 'CHECK constraint failed: character' in str(excinfo.value)
