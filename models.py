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
    weight = FloatField(constraints=[Check('weight < 1000'), Check('weight > 0')])
    hair_color = CharField()
    eye_color = CharField()


class Ability(BaseModel):
    character = ForeignKeyField(Character)
    strength = IntegerField()
    dexterity = IntegerField()
    constitution = IntegerField()
    intelligence = IntegerField()
    wisdom = IntegerField()
    charisma = IntegerField()


class Skill(BaseModel):
    character = ForeignKeyField(Character)
    acrobatics = IntegerField()
    appraise = IntegerField()
    bluff = IntegerField()
    climb = IntegerField()
    craft_1 = IntegerField()
    craft_1_name = CharField()
    craft_2 = IntegerField()
    craft_2_name = CharField()
    craft_3 = IntegerField()
    craft_3_name = CharField()
    diplomacy = IntegerField()
    disable_device = IntegerField()
    disguise = IntegerField()
    escape_artist = IntegerField()
    fly = IntegerField()
    handle_animal = IntegerField()
    heal = IntegerField()
    intimidate = IntegerField()
    knowledge_arcana = IntegerField()
    knowledge_dungeoneering = IntegerField()
    knowledge_engineering = IntegerField()
    knowledge_geography = IntegerField()
    knowledge_history = IntegerField()
    knowledge_local = IntegerField()
    knowledge_nature = IntegerField()
    knowledge_nobility = IntegerField()
    knowledge_planes = IntegerField()
    knowledge_religion = IntegerField()
    linguistics = IntegerField()
    perception = IntegerField()
    perform_1 = IntegerField()
    perform_1_name = CharField()
    perform_2 = IntegerField()
    perform_2_name = CharField()
    profession_1 = IntegerField()
    profession_1_name = CharField()
    profession_2 = IntegerField()
    profession_2_name = CharField()
    ride = IntegerField()
    sense_motive = IntegerField()
    sleight_of_hand = IntegerField()
    spellcraft = IntegerField()
    stealth = IntegerField()
    survival = IntegerField()
    swim = IntegerField()
    use_magic_device = IntegerField()


def create_tables(database):
    database.connect()
    database.create_tables([Character, Ability], True)
