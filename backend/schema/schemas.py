from pydantic import BaseModel

class JournalEntry(BaseModel):
    username: str
    text: str

class SearchQuery(BaseModel):
    username: str
    query: str

class UserLogin(BaseModel):
    username: str