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
