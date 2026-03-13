import random
import string
from faker import Faker

fake = Faker()


def generate_user() -> dict:
    """
    Genereaza date random pentru un user nou.
    Returneaza un dictionar cu username, email, password.
    """
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return {
        "username": f"user_{random_suffix}",
        "email": f"user_{random_suffix}@test.com",
        "password": "Test1234!"
    }


def generate_article() -> dict:
    """
    Genereaza date random pentru un articol nou.
    Returneaza un dictionar cu title, description, body, tagList.
    """
    return {
        "title": fake.sentence(nb_words=4).rstrip("."),
        "description": fake.sentence(nb_words=8).rstrip("."),
        "body": fake.paragraph(nb_sentences=3),
        "tagList": [fake.word(), fake.word()]
    }