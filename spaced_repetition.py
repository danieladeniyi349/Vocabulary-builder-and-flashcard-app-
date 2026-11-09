import json
from datetime import date, timedelta

# ==============================================================================
# TASK 3: FLASHCARD & SPACED REPETITION SYSTEM (LEITNER SYSTEM)
# ==============================================================================

CARDS_FILE = "flashcards.json"
INTERVALS = {1: 1, 2: 2, 3: 4, 4: 7, 5: 14}


class Flashcard:
    """Represents an individual flashcard with review intervals."""
    
    def __init__(self, word, definition, box=1, next_review=None):
        self.word = word
        self.definition = definition
        self.box = box
        self.next_review = next_review or date.today()

    def is_due(self):
        return self.next_review <= date.today()

    def to_dict(self):
        return {
            "word": self.word,
            "definition": self.definition,
            "box": self.box,
            "next_review": self.next_review.isoformat(),
        }

    @staticmethod
    def from_dict(data):
        return Flashcard(
            data["word"],
            data["definition"],
            data["box"],
            date.fromisoformat(data["next_review"]),
        )


class SpacedRepetitionManager:
    """Manages collection persistence and Leitner box progression logic."""
    
    def __init__(self, filename=CARDS_FILE):
        self.filename = filename
        self.cards = []
        self.load()

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
            self.cards = [Flashcard.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError, KeyError, ValueError):
            self.cards = []

    def save(self):
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump([card.to_dict() for card in self.cards], file, indent=2)
        except OSError:
            pass

    def add_card(self, word, definition):
        for card in self.cards:
            if card.word == word.lower():
                return False
        self.cards.append(Flashcard(word.lower(), definition))
        self.save()
        return True

    def get_due_cards(self):
        return [card for card in self.cards if card.is_due()]

    def review(self, word, remembered):
        for card in self.cards:
            if card.word == word.lower():
                if remembered:
                    card.box = min(card.box + 1, 5)
                    card.next_review = date.today() + timedelta(days=INTERVALS[card.box])
                else:
                    card.box = 1
                    card.next_review = date.today()
                self.save()
                return True
        return False