from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase('pathfinder.db')

ALIGNMENT_CHOICES = [
    ('LG', 'Lawful Good'),
    ('LN', 'Lawful Neutral'),
    ('LE', 'Lawful Evil'),
    ('NG', 'Neutral Good'),
    ('N', 'Neutral'),
    ('NE', 'Neutral Evil'),
    ('CG', 'Chaotic Good'),
    ('CN', 'Chaotic Neutral'),
    ('CE', 'Chaotic Evil')
]
RACE_CHOICES = [
    ('dwarf', 'Dwarf'),
    ('elf', 'Elf'),
    ('gnome', 'Gnome'),
    ('halfling', 'Halfling'),
    ('half-elf', 'Half-elf'),
    ('half-orc', 'Half-orc'),
    ('human', 'Human'),
]
SIZE_CHOICES = [
    ('md', 'medium'),
    ('sm', 'small')
]


class BaseModel(Model):
    class Meta:
        database = db


class Character(BaseModel):
    character_name = CharField(unique=True)
    player_name = CharField()
    alignment = CharField(choices=ALIGNMENT_CHOICES)
    race = CharField(choices=RACE_CHOICES)
    size = CharField(choices=SIZE_CHOICES)
    gender = CharField()
    age = IntegerField(constraints=[Check('age > 0')])
    height_ft = IntegerField(constraints=[Check('height_ft < 30'), Check('height_ft >= 0')])
    height_in = IntegerField(constraints=[Check('height_in < 12'), Check('height_in >= 0')])
    weight = FloatField(constraints=[Check('0 < weight < 1000')])
    hair_color = CharField()
    eye_color = CharField()


class Ability(BaseModel):
    character = ForeignKeyField(Character)
    strength = IntegerField()


def create_tables(database):
    database.connect()
    database.create_tables([Character, Ability], True)
