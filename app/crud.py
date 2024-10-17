from sqlalchemy.orm import Session
from models import Person

def get_people(db: Session) -> list[Person]:
    return db.query(Person).all()

def create_person(db: Session, first_name: str, last_name: str) -> Person:
    db_person = Person(first_name=first_name, last_name=last_name)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def delete_person(db: Session, person_id: int) -> Person or None:
    db_person = db.query(Person).filter(Person.id == person_id).first()
    if db_person:
        db.delete(db_person)
        db.commit()
    return db_person

def update_person(db: Session, person_id: int, first_name: str, last_name: str) -> Person or None:
    db_person = db.query(Person).filter(Person.id == person_id).first()
    if db_person:
        db_person.first_name = first_name
        db_person.last_name = last_name
        db.commit()
        db.refresh(db_person)
    return db_person
