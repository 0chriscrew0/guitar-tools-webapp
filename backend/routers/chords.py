from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_chords():
    return {"chords": ["G Major", "C Minor", "D7", "A#m"]}
