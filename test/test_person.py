import pytest
from topic.test.person import Person

def test_person_creation():
    person = Person("John Doe", 30, "john.doe@example.com")
    assert person.name == "John Doe"
    assert person.age == 30
    assert person.email == "john.doe@example.com"

def test_person_greet():
    person = Person("John Doe", 30, "john.doe@example.com")
    assert person.greet() == "Hello, my name is John Doe and I am 30 years old."

def test_person_is_adult():
    adult = Person("Jane Smith", 25, "jane.smith@example.com")
    child = Person("Baby John", 5, "baby.john@example.com")
    assert adult.is_adult() is True
    assert child.is_adult() is False