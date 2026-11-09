import json
from datetime import date
from Dictionary_client import Word

# ==============================================================================
# TASK 4: JSON FILE PERSISTENCE & DYNAMIC QUIZ GENERATOR
# ==============================================================================

class DictionaryFileManager:
    """Handles saving and loading dictionary data and historical quiz scores."""
    
    def __init__(self):
        self.words_file = "saved_words.json"
        self.scores_file = "quiz_scores.json"

    def save_word(self, word_obj):
        words = self.load_words()
        
        for sw in words:
            existing_word = sw.get("word") if isinstance(sw, dict) else getattr(sw, "word", "")
            if existing_word.lower() == word_obj.word.lower():
                return False

        word_data = {
            "word": word_obj.word,
            "definitions": word_obj.definitions,
            "phonetics": word_obj.phonetics,
            "synonyms": word_obj.synonyms,
            "antonyms": word_obj.antonyms,
            "part_of_speech": word_obj.part_of_speech
        }
        
        serialized_words = []
        for w in words:
            if isinstance(w, dict):
                serialized_words.append(w)
            else:
                serialized_words.append({
                    "word": getattr(w, "word", ""),
                    "definitions": getattr(w, "definitions", []),
                    "phonetics": getattr(w, "phonetics", ""),
                    "synonyms": getattr(w, "synonyms", []),
                    "antonyms": getattr(w, "antonyms", []),
                    "part_of_speech": getattr(w, "part_of_speech", "")
                })

        serialized_words.append(word_data)

        with open(self.words_file, "w", encoding="utf-8") as file:
            json.dump(serialized_words, file, indent=4)
        return True

    def load_words(self):
        try:
            with open(self.words_file, "r", encoding="utf-8") as file:
                data = json.load(file)
            return [
                Word(
                    i["word"],
                    i["definitions"],
                    i["phonetics"],
                    i["synonyms"],
                    i["antonyms"],
                    i["part_of_speech"]
                ) for i in data
            ]
        except (FileNotFoundError, json.JSONDecodeError, KeyError, TypeError):
            return []

    def save_quiz_score(self, score, total):
        try:
            with open(self.scores_file, "r", encoding="utf-8") as file:
                scores = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            scores = []
        scores.append({
            "date": date.today().isoformat(),
            "score": score,
            "total_questions": total
        })
        with open(self.scores_file, "w", encoding="utf-8") as file:
            json.dump(scores, file, indent=4)
