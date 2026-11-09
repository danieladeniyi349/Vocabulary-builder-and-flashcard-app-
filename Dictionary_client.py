import requests

# ==============================================================================
# TASK 1: OBJECT-ORIENTED DICTIONARY ARCHITECTURE & PUBLIC API INTEGRATION
# ==============================================================================

class Word:
    """Represents a vocabulary word with its linguistic attributes."""
    
    def __init__(self, word, definitions, phonetics, synonyms, antonyms, part_of_speech=""):
        self.word = word
        self.definitions = definitions
        self.phonetics = phonetics
        self.synonyms = synonyms
        self.antonyms = antonyms
        self.part_of_speech = part_of_speech

    def __str__(self):
        return (
            f"{self.word.capitalize()} ({self.part_of_speech})\n"
            f"Phonetic: {self.phonetics}\n"
            f"Definitions: {self.definitions}"
        )


class DictionaryClient:
    """Handles communication with the Free Dictionary API and returns Word objects."""
    
    BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    def fetch_word(self, word_str: str) -> Word:
        cleaned_word = word_str.strip().lower()
        if not cleaned_word:
            raise ValueError("Word input cannot be empty.")

        url = f"{self.BASE_URL}{cleaned_word}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        data = response.json()[0]
        word_text = data.get('word', cleaned_word)
        
        phonetics = data.get('phonetic', '')
        if not phonetics and data.get('phonetics'):
            for p in data.get('phonetics', []):
                if 'text' in p:
                    phonetics = p['text']
                    break
        
        definitions, synonyms, antonyms, part_of_speech = [], [], [], ""
        meanings = data.get('meanings', [])
        if meanings:
            first_meaning = meanings[0]
            part_of_speech = first_meaning.get('partOfSpeech', '')
            for def_obj in first_meaning.get('definitions', []):
                if 'definition' in def_obj:
                    definitions.append(def_obj['definition'])
            synonyms = first_meaning.get('synonyms', [])
            antonyms = first_meaning.get('antonyms', [])
        
        return Word(word_text, definitions, phonetics, synonyms, antonyms, part_of_speech)
