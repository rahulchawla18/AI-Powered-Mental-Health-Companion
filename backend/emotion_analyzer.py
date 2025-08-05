import random

def get_emotion(text):
    keywords = {
        "sad": ["sad", "down", "depressed", "unhappy", "miserable", "lonely", "gloomy", "crying", "heartbroken", "hopeless", "melancholy", "despair", "blue", "tearful", "sorrowful"],
        "happy": ["happy", "excited", "joy", "cheerful", "elated", "glad", "delighted", "content", "blissful", "ecstatic", "joyful", "radiant", "upbeat", "overjoyed", "thrilled"],
        "anxious": ["worried", "anxious", "nervous", "tense", "uneasy", "panicked", "stressed", "fearful", "apprehensive", "restless", "jittery", "overwhelmed", "dread", "on edge"],
        "angry": ["angry", "furious", "irritated", "annoyed", "mad", "enraged", "resentful", "frustrated", "agitated", "outraged", "bitter", "hostile", "snappy"],
        "grateful": ["thankful", "grateful", "appreciative", "blessed", "fortunate", "indebted", "obliged", "recognizing kindness", "valuing help"],
        "neutral": ["okay", "fine", "meh", "normal", "average", "regular"]
    }
    for emotion, words in keywords.items():
        if any(word in text.lower() for word in words):
            return emotion
    return "neutral"

def get_suggestions(emotion):
    mapping = {
        "sad": ["Try a 10-minute walk", "Write 3 things you're grateful for", "Call someone you trust", "Listen to your favorite calming song", "Light a candle and breathe deeply"],
        "happy": ["Celebrate your wins!", "Share your joy with a friend", "Capture this moment in a journal", "Dance to your favorite song", "Do something kind for someone else"],
        "anxious": ["Do a breathing exercise", "Try journaling your worries", "Listen to calming music", "Stretch or move around", "Drink a glass of water slowly"],
        "angry": ["Take deep breaths", "Go for a walk to cool down", "Write your feelings out", "Count to ten slowly", "Try progressive muscle relaxation"],
        "grateful": ["Send a thank you note", "List 5 things you're grateful for today", "Do something nice for someone else", "Smile at a stranger", "Say thank you out loud"],
        "neutral": ["Reflect on something meaningful", "Practice mindfulness", "Declutter your space for 5 mins", "Read a page from your favorite book", "Enjoy a few minutes of silence"]
    }
    return random.sample(mapping.get(emotion, mapping["neutral"]), 1)