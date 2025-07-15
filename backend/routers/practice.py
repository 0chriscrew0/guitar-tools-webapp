from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from models import PracticeLog
from database import engine

router = APIRouter()

def get_session():
    with Session(engine) as session:
        yield session

@router.get("/")
def read_logs(session: Session = Depends(get_session)):
    return session.exec(select(PracticeLog)).all()

@router.post("/")
def create_log(log: PracticeLog, session: Session = Depends(get_session)):
    session.add(log)
    session.commit()
    session.refresh(log)
    return log
