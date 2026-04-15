import requests

fallback_questions = [
    {"question": "The Great Wall of China is visible from space.", "correct_answer": "False"},
    {"question": "A group of flamingos is called a flamboyance.", "correct_answer": "True"},
    {"question": "The Eiffel Tower can grow taller in summer.", "correct_answer": "True"},
    {"question": "Sharks are mammals.", "correct_answer": "False"},
    {"question": "Honey never spoils.", "correct_answer": "True"},
    {"question": "A snail can sleep for 3 years.", "correct_answer": "True"},
    {"question": "The human body has 206 bones.", "correct_answer": "True"},
    {"question": "Lightning never strikes the same place twice.", "correct_answer": "False"},
    {"question": "Bananas grow on trees.", "correct_answer": "False"},
    {"question": "The sun is a star.", "correct_answer": "True"},
]

parameters = {
    "amount": 10,
    "type": "boolean",
}

try:
    response = requests.get("https://opentdb.com/api.php", params=parameters, timeout=10)
    response.raise_for_status()
    data = response.json()
    question_data = data["results"]
    print("Loaded questions from API.")
except Exception:
    question_data = fallback_questions
    print("API unavailable. Using offline questions.")
