import random
from datetime import datetime

responses = {
    "sad": [
        "You're not alone—this feeling will pass.",
        "Take a deep breath, you're doing your best."
    ],
    "happy": [
        "That’s wonderful to hear!",
        "Keep that joy alive and share it with someone."
    ],
    "stressed": [
        "Try closing your eyes for a minute and breathing deeply.",
        "Breaks are productive—step away for a moment."
    ],
    "anxious": [
        "Focus on your breath. You're safe right now.",
        "Try grounding yourself—notice five things you see."
    ],
    "lonely": [
        "Sending a virtual hug your way.",
        "Reach out to someone you trust or write down your thoughts."
    ],
    "angry": [
        "Breathe in calm... breathe out tension.",
        "Let the storm pass before reacting—you’re in control."
    ]
}

activities = {
    "sad": [
        "Write down 3 things you like about yourself.",
        "Watch a favorite comforting video."
    ],
    "happy": [
        "Celebrate the small win!",
        "Capture your joy—write it down or tell someone."
    ],
    "stressed": [
        "Stretch your body. Even 30 seconds helps.",
        "Do a brain dump—write all your thoughts on paper."
    ],
    "anxious": [
        "Try the 5-4-3-2-1 grounding technique.",
        "Drink some water and look outside the window."
    ],
    "lonely": [
        "Send a message to a friend—even just a 'hi'.",
        "Draw something silly just for fun."
    ],
    "angry": [
        "Take 10 deep breaths while slowly counting down.",
        "Listen to calming instrumental music."
    ]
}

today = datetime.now().strftime("%A, %B %d")
print(f"\n🌞 Hello! Today is {today}. Let’s check in with yourself.\n")

mood = input("How are you feeling today? (e.g., sad, happy, anxious): ").lower()

if mood in responses:
    print("\n💬", random.choice(responses[mood]))
    print("🌱 Try this:", random.choice(activities[mood]))
else:
    print("\n💬 I'm here for you, no matter how you're feeling. You've already done something kind for yourself by checking in.")