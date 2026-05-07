from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select
from model import Dog, Dogsid

def createdog (dogs: Dog, session: Session):
    newdog = Dogsid.model_validate(dogs)
    session.add(newdog)
    session.commit()
    session.refresh(newdog)
    return newdog

def showdog ( session: Session):
    return session.exec(select(Dogsid)).all()
