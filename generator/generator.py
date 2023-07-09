import random

from data.data import Person, Color, Date
from faker import Faker
import os
faker_en = Faker()
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        firstname=faker_en.first_name(),
        lastname=faker_en.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(1000, 100000),
        department=faker_en.job(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        permanent_address=faker_en.address(),
        mobile=faker_en.msisdn(),
    )


def generated_file():
    path = os.path.abspath(f"../files/test{random.randint(0, 999)}.txt")
    file = open(path, 'w+')
    file.write(f'Hello world{random.randint(0, 999)}')
    file.close()
    return file.name, path


def generate_subject():
    subject = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce",
               "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
    return subject


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )


def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time="12:00",
    )
