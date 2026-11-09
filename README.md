# Smart Dictionary & Vocabulary Builder

A modular, multi-phase desktop and console application built with Python and Tkinter that manages vocabulary words, flashcards, interactive quizzes, and leverages Google Gemini AI (`gemini-3.5-flash`) to generate instant contextual mnemonics and real-world usage examples.

## Features
- **Object-Oriented Dictionary Architecture:** Clean API integration with the Free Dictionary API to pull definitions, phonetics, synonyms, and parts of speech.
- **Spaced Repetition Flashcards:** Leitner-system-based flashcard tracking (`spaced_repetition.py`) with customizable review intervals to maximize vocabulary retention.
- **Gemini AI Insights:** Fetch instant AI breakdowns, nuances, memory tricks, and real-world usage examples via Google Gemini, complete with timeout and exception error-handling.
- **JSON File Persistence:** Local storage management for saved vocabulary words and historical quiz scores.
- **Interactive User Interfaces:** Choice of console menus (`main.py`, `main_menu2.py`) or a full-featured Tkinter graphical interface (`GUI3.py`).

## Project Structure & Phases

### Phase 1: Core Foundation & Data Structures
- `main.py` - Primary runner script for executing early console-based word lookups.
- `Word_model.py` - Core object model defining vocabulary attributes (words, definitions, parts of speech).
- `error_handling1.py` - Custom exception structures and safety checks for input validation.

### Phase 2: Menu System & Extended Logic
- `main_menu2.py` - Interactive console menu interface connecting Phase 1 structures with CLI user controls.
- `Dictionary_client.py` - Handles API integration with the Free Dictionary API.

### Phase 3: Advanced AI Integration, Flashcards & GUI
- `Ai_assistant.py` - Google Gemini AI integration (`gemini-3.5-flash`) for instant memory tricks and contextual usage.
- `spaced_repetition.py` - Leitner system flashcard engine for review scheduling and interval tracking.
- `file_manager3.py` - JSON persistence manager for local word storage and historical quiz scores.
- `GUI3.py` - Complete Tkinter graphical user interface unifying all Phase 1–3 functionality into a single desktop application.

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/danieladeniyi349/Vocabulary-builder-and-flashcard-app-.git](https://github.com/danieladeniyi349/Vocabulary-builder-and-flashcard-app-.git)
   cd Vocabulary-builder-and-flashcard-app-


2 Install the required dependencies & libraries:
Make sure you have Python installed, then install the core packages required for API requests, AI integration, and environment variables:

pip install requests google-generativeai python-dotenv

Note: tkinter typically comes pre-installed with standard Python distributions on Windows and macOS).

3 Configure your API key:

Create a .env file in the root directory of the project and add your Gemini API key securely:


GEMINI_API_KEY=your_actual_api_key_here

4 Running the Application
To launch the full Phase 3 graphical interface application, run:

python GUI3.py

To run the console-based menu navigation:

python main_menu2.py

