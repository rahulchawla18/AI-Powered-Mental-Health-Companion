from fastapi import APIRouter, Depends
from requests import Session
from backend.schema.schemas import JournalEntry, UserLogin, SearchQuery
from backend.utility.utils import analyze_journal, get_history, search_journals, uplift_activities
from backend.auth.auth import login_user
from backend.database.database import get_db

router = APIRouter()

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(user.username, db)

@router.post("/analyze")
def analyze(entry: JournalEntry):
    return analyze_journal(entry.username, entry.text)

@router.get("/history/{username}")
def history(username: str):
    return get_history(username)

@router.post("/search")
def search(query: SearchQuery):
    return search_journals(query.username, query.query)

@router.get("/uplift/{emotion}")
def get_uplift_suggestions(emotion: str):
    activities = uplift_activities(emotion)
    return {"emotion": emotion, "activities": activities}