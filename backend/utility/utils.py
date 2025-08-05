import requests
import datetime
from backend.emotion_analyzer import get_emotion, get_suggestions
from backend.chromadb.chroma_store import add_to_store, get_all_entries, semantic_search

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"

def query_ollama(prompt: str):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    response.raise_for_status()
    return response.json()["response"]

def analyze_journal(username, text):
    emotion = get_emotion(text)
    suggestions = get_suggestions(emotion)

    prompt = (
        "You are a supportive mental health assistant. "
        "The user has written the following journal entry:\n\n"
        f"\"{text}\"\n\n"
        "Please respond empathetically and offer some emotional insights or reflection."
    )

    feedback = query_ollama(prompt).strip()
    timestamp = datetime.datetime.now().isoformat()
    add_to_store(username, text, emotion, feedback, timestamp)

    return {
        "emotion": emotion,
        "suggestions": suggestions,
        "feedback": feedback
    }

def get_history(username):
    return get_all_entries(username)

def search_journals(username, query):
    return semantic_search(username, query)

def uplift_activities(emotion: str):
    suggestions = {
        "sad": [
            "Go for a walk in nature",
            "Call a loved one",
            "Write down three positive memories",
            "Watch a funny video",
            "Do something creative like sketching or painting",
            "Listen to uplifting music",
            "Try guided journaling prompts"
        ],
        "anxious": [
            "Practice 4-7-8 breathing",
            "Declutter your space",
            "Listen to calming music",
            "Try a short guided meditation",
            "Do light stretching or yoga",
            "List things you're grateful for",
            "Journal your thoughts to offload them"
        ],
        "angry": [
            "Write your feelings in a journal",
            "Do a quick workout",
            "Try deep breathing with closed eyes",
            "Punch a pillow (safely!)",
            "Go for a bike ride or run",
            "Listen to calming or classical music",
            "Use a grounding technique (5-4-3-2-1)"
        ],
        "lonely": [
            "Join an online support group",
            "Attend a virtual event or workshop",
            "Message a friend or coworker",
            "Cuddle a pet or stuffed toy",
            "Volunteer online or locally",
            "Start a new hobby that brings connection"
        ],
        "neutral": [
            "Pick a new hobby to explore",
            "Reflect on your week and write about it",
            "Try a creative writing exercise",
            "Plan a small self-care activity",
            "Do a 5-minute mindfulness session",
            "Listen to an interesting podcast",
            "Read a short story or poem"
        ],
        "happy": [
            "Celebrate your good mood with music or dance",
            "Share your joy with someone",
            "Write down what made you feel happy today",
            "Engage in an activity that fuels this positivity"
        ]
    }

    return suggestions.get(emotion.lower(), suggestions["neutral"])