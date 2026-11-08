# ==========================================
# TASK 2: Word Data Model & Display Class
# ==========================================
class Word:

    def __init__(self, term, definition, phonetics="", examples=None, synonyms=None, antonyms=None):
        """
        Represents a single vocabulary word with all its associated linguistic data.
        """
        self.term = term
        self.definition = definition
        self.phonetics = phonetics

        # Using safe defaults for lists to avoid mutation bugs and NoneType errors
        self.examples = examples if examples is not None else []
        self.synonyms = synonyms if synonyms is not None else []
        self.antonyms = antonyms if antonyms is not None else []

    def __str__(self):
        """
        Returns a clean, readable string representation of the Word object.
        """
        examples_str = "\n  - ".join(self.examples) if self.examples else "None available"
        synonyms_str = ", ".join(self.synonyms[:5]) if self.synonyms else "None available"
        antonyms_str = ", ".join(self.antonyms[:5]) if self.antonyms else "None available"
        
        return (
            f"=============================\n"
            f"📖 Term: {self.term.capitalize()} ({self.phonetics})\n"
            f"-----------------------------\n"
            f"Definition: {self.definition}\n"
            f"Examples:\n  - {examples_str}\n"
            f"Synonyms: {synonyms_str}\n"
            f"Antonyms: {antonyms_str}\n"
            f"============================="
        )
