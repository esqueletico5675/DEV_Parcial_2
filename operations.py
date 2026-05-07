from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select
from model import Dog, Dogsid, uptadedog

def createdog (dogs: Dog, session: Session):
    newdog = Dogsid.model_validate(dogs)
    session.add(newdog)
    session.commit()
    session.refresh(newdog)
    return newdog

def showdog ( session: Session):
    return session.exec(select(Dogsid)).all()

def finonedog(id:int,session: Session):
    try:
        return session.get_one(Dogsid,id)
    except NoResultFound:
        return None

def uptadedogs (id:int,newdog: uptadedog,session: Session):
    dog = finonedog(id,session)
    if dog is None:
        return None
    doguptade= newdog.model_dump(exclude_unset=True)
    dog.sqlmodel_update(doguptade)
    session.add(doguptade)
    session.commit()
    session.refresh(dog)
    return dog

def killdog (id:int,session: Session):
    try:
        dog = session.get_one(Dogsid,id)
        session.delete(dog)
        session.commit()
        return dog
    except NoResultFound:
        return None