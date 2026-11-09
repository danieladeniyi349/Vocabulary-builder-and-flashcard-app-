import os
import threading
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv

load_dotenv()

from Dictionary_client import DictionaryClient
from Ai_assistant import GeminiAssistant
from spaced_repetition import SpacedRepetitionManager
from file_manager import DictionaryFileManager

# ==============================================================================
# TASK 5: TKINTER GUI APPLICATION INTERFACE
# ==============================================================================

class SmartDictionaryApp:
    """Main Tkinter User Interface integrating Tasks 1 through 4."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Dictionary & Vocabulary Builder")
        self.root.geometry("800x650")
        self.root.minsize(700, 550)
        self.root.configure(bg="#F2F4F8")

        # Instantiate backend modules
        self.dict_client = DictionaryClient()
        self.ai_assistant = GeminiAssistant()
        self.sr_manager = SpacedRepetitionManager()
        self.file_manager = DictionaryFileManager()
        
        self.current_word_obj = None

        self.create_widgets()

    def create_widgets(self):
        # Header Frame
        header = tk.Frame(self.root, bg="#243B64", padx=20, pady=18)
        header.pack(fill="x")

        tk.Label(
            header, text="SMART DICTIONARY APP",
            font=("Arial", 20, "bold"), bg="#243B64", fg="white"
        ).pack()
        tk.Label(
            header, text="Learn & Master Vocabulary with AI",
            font=("Arial", 9), bg="#243B64", fg="#E4EAF5"
        ).pack(pady=(5, 0))

        # Main Layout Frame
        main = tk.Frame(self.root, bg="#F2F4F8", padx=25, pady=20)
        main.pack(fill="both", expand=True)

        tk.Label(
            main, text="Enter a word",
            font=("Arial", 11, "bold"), bg="#F2F4F8", fg="#243B64"
        ).pack(anchor="w")

        # Search Bar
        search_frame = tk.Frame(main, bg="#F2F4F8")
        search_frame.pack(fill="x", pady=(8, 12))

        self.search_entry = tk.Entry(search_frame, font=("Arial", 13), relief="solid", bd=1)
        self.search_entry.pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 10))
        self.search_entry.bind("<Return>", lambda event: self.search_word())

        self.search_button = tk.Button(
            search_frame, text="SEARCH", font=("Arial", 10, "bold"),
            bg="#243B64", fg="white", relief="flat", padx=15, pady=8,
            command=self.search_word
        )
        self.search_button.pack(side="right")

        # Results Box
        tk.Label(
            main, text="Results & AI Insights",
            font=("Arial", 11, "bold"), bg="#F2F4F8", fg="#243B64"
        ).pack(anchor="w", pady=(0, 5))

        self.result_box = tk.Text(
            main, height=14, font=("Arial", 11), wrap="word", padx=10, pady=10, relief="solid", bd=1
        )
        self.result_box.pack(fill="both", expand=True, pady=(0, 12))
        self.result_box.insert(
            tk.END, "Search a word above to see dictionary definitions and AI learning aids."
        )

        # Bottom Action Bar
        features = tk.Frame(main, bg="#F2F4F8")
        features.pack(fill="x")

        tk.Button(
            features, text="🤖 AI HELP", font=("Arial", 9, "bold"),
            bg="#355487", fg="white", relief="flat", padx=12, pady=8,
            command=self.get_ai_help
        ).pack(side="left", padx=(0, 8))

        tk.Button(
            features, text="💾 SAVE WORD", font=("Arial", 9, "bold"),
            bg="#4A5568", fg="white", relief="flat", padx=12, pady=8,
            command=self.save_current_word
        ).pack(side="left", padx=(0, 8))

        tk.Button(
            features, text="📇 FLASHCARDS", font=("Arial", 9, "bold"),
            bg="#287A67", fg="white", relief="flat", padx=12, pady=8,
            command=self.open_flashcards_window
        ).pack(side="left", padx=(0, 8))

        # Footer
        tk.Label(
            self.root, text="Powered by Free Dictionary API & Google Gemini",
            font=("Arial", 8), bg="#F2F4F8", fg="#687386"
        ).pack(pady=(0, 8))

    def search_word(self):
        query = self.search_entry.get().strip()
        if not query:
            messagebox.showwarning("Missing word", "Please enter a word.")
            return

        self.search_button.config(state="disabled", text="SEARCHING...")
        self.result_box.delete("1.0", tk.END)
        self.result_box.insert(tk.END, f"Looking up '{query}'...\n")
        self.root.update_idletasks()

        try:
            self.current_word_obj = self.dict_client.fetch_word(query)
            
            self.result_box.delete("1.0", tk.END)
            self.result_box.insert(tk.END, f"WORD: {self.current_word_obj.word.upper()} ({self.current_word_obj.part_of_speech})\n")
            self.result_box.insert(tk.END, f"Phonetic: {self.current_word_obj.phonetics}\n")
            self.result_box.insert(tk.END, "=" * 55 + "\n\n")
            
            self.result_box.insert(tk.END, "Definitions:\n")
            for idx, d in enumerate(self.current_word_obj.definitions, 1):
                self.result_box.insert(tk.END, f"  {idx}. {d}\n")
            
            if self.current_word_obj.synonyms:
                self.result_box.insert(tk.END, f"\nSynonyms: {', '.join(self.current_word_obj.synonyms[:5])}\n")

        except Exception as e:
            messagebox.showerror("Error", f"Could not fetch word: {e}")
            self.result_box.delete("1.0", tk.END)
            self.current_word_obj = None
        finally:
            self.search_button.config(state="normal", text="SEARCH")

    def get_ai_help(self):
        if not self.current_word_obj:
            messagebox.showwarning("No word", "Search a word first to get AI help.")
            return

        self.result_box.insert(tk.END, "\n\n--- Asking Gemini AI ---\n")
        self.result_box.see(tk.END)

        word = self.current_word_obj.word

        threading.Thread(
            target=self._fetch_ai_background, args=(word,), daemon=True
        ).start()

    def _fetch_ai_background(self, word):
        try:
            ai_response = self.ai_assistant.generate_word_help(word)
            self.root.after(
                0, lambda: self.result_box.insert(tk.END, f"\n{ai_response}\n")
            )
            self.root.after(0, lambda: self.result_box.see(tk.END))
        except Exception as e:
            err_msg = f"\nError: {e}\n"
            self.root.after(0, lambda: self.result_box.insert(tk.END, err_msg))        

    def save_current_word(self):
        if not self.current_word_obj:
            messagebox.showwarning("No word", "Search a word first before saving.")
            return

        saved = self.file_manager.save_word(self.current_word_obj)
        if saved:
            defn = self.current_word_obj.definitions[0] if self.current_word_obj.definitions else ""
            if isinstance(defn, dict):
                defn = defn.get("definition", str(defn))
            self.sr_manager.add_card(self.current_word_obj.word, defn)
            messagebox.showinfo("Success", f"'{self.current_word_obj.word}' saved to vocabulary!")
        else:
            messagebox.showinfo("Already Saved", f"'{self.current_word_obj.word}' is already saved.")

    def open_flashcards_window(self):
        due_cards = self.sr_manager.get_due_cards()
        
        win = tk.Toplevel(self.root)
        win.title("Spaced Repetition Flashcards")
        win.geometry("450x350")
        win.configure(bg="#F2F4F8")

        tk.Label(win, text="Flashcard Review", font=("Arial", 14, "bold"), bg="#F2F4F8", fg="#243B64").pack(pady=15)

        if not due_cards:
            tk.Label(win, text="🎉 No flashcards due for review today!\nCheck back tomorrow or save more words.", font=("Arial", 11), bg="#F2F4F8", justify="center").pack(pady=40)
            return


if __name__ == "__main__":
    root = tk.Tk()
    app = SmartDictionaryApp(root)
    root.mainloop()
