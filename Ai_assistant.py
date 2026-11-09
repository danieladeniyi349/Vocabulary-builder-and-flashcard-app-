import os
import google.generativeai as genai

# ==============================================================================
# TASK 2: GEMINI AI VOCABULARY ASSISTANT INTEGRATION
# ==============================================================================

class GeminiAssistant:
    """Integrates Google Gemini to provide intelligent word insights and study tips."""
    
    def __init__(self):
        self.model_name = "gemini-3.8-flash"
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel(self.model_name)

    def generate_word_help(self, word):
        if not word or not isinstance(word, str):
            return "Please provide a valid word."

        prompt = f"""
        Provide a concise dictionary entry and learning guide for the word: '{word}'.
        Format the output clearly as follows:
        
        📌 DEFINITION:
        - Provide a clear, simple definition.
        
        💡 SAMPLE SENTENCE:
        - Give 1-2 realistic usage examples.
        
        ⚡ SYNONYMS & ANTONYMS:
        - Synonyms: [list 2-3]
        - Antonyms: [list 2-3]
        
        🧠 MNEMONIC / MEMORY TRICK:
        - A fun or clever memory aid to remember this word easily.
        """

        try:
            print(f"[DEBUG] Sending request to Gemini for: {word}")
            response = self.model.generate_content(prompt, request_options={"timeout": 30})
            print("[DEBUG] Received response from Gemini successfully!")
            return response.text.strip()
        except Exception as e:
            print(f"[DEBUG] Exception caught: {e}")
            return f"Error generating AI help: {e}" 

    def get_ai_word_help(self, word_str):
        """
        Fetches an interactive learning breakdown for a given word using Gemini AI.
        Includes built-in error handling so network or API issues won't crash the app.
        """
        try:
            prompt = f"""
            Provide a concise, engaging learning breakdown for the word '{word_str}':
            1. Simple Nuance / Context: Explain its vibe or when to use it in 1 sentence.
            2. Mnemonic Trick: A clever memory hook or trick to remember it.
            3. Real-World Example: A vivid sentence demonstrating its usage.
            Keep it clean and formatted nicely.
            """
            
            response = self.model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            return f"Could not fetch AI assistance at the moment. Error: {str(e)}"