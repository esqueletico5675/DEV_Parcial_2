from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select
from model import Dog, Dogsid

def createdog (dogs: Dog, session: Session):
    newdog = Dogsid.model_validate(dogs)
    session.add(newdog)
    session.commit()
    sesion.refresh(newdog)
    return newdog
