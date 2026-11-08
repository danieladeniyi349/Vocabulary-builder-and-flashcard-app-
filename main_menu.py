# ==============================================================================
# TASK 1: MAIN APPLICATION LOOP & CLI MENU
# ==============================================================================
from input_sanitization import sanitize_input
from error_handler import (
    fetch_word_definition,
    WordNotFoundError,
    RateLimitError,
    ServerError,
    APIConnectionError
)
from history_logger import save_to_history, show_history
from ui_display import display_dictionary_data


def main():
    """
    Runs the primary execution loop of the application.
    Manages user interaction, presents the CLI menu, and routes inputs 
    to Tasks 2, 3, 4, and 5.
    """
    print("=" * 55)
    print("        WELCOME TO YOUR MODULAR CLI DICTIONARY")
    print("=" * 55)

    while True:
        print("\nMain Menu:")
        print("  1. Search for a word definition")
        print("  2. View search history")
        print("  3. Exit application")
        
        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            raw_input = input("\nEnter a word to search: ")
            
            # Step 1: Sanitize input (Task 2)
            try:
                word = sanitize_input(raw_input)
            except ValueError as ve:
                print(f"\n[Input Validation Error]: {ve}")
                continue

            # Step 2: Fetch data and handle errors (Task 3)
            try:
                result_data = fetch_word_definition(word)
                
                if result_data:
                    # Step 3: Format and display UI output (Task 5)
                    display_dictionary_data(result_data)
                    
                    # Step 4: Log successful search to history (Task 4)
                    save_to_history(word)
                    
            except WordNotFoundError as e:
                print(f"\n[Not Found Notice]: {e}")
            except RateLimitError as e:
                print(f"\n[Rate Limit Notice]: {e}")
            except ServerError as e:
                print(f"\n[Server Error Notice]: {e}")
            except APIConnectionError as e:
                print(f"\n[Connection Error Notice]: {e}")

        elif choice == "2":
            # View past searches log (Task 4)
            show_history()

        elif choice == "3":
            print("\nExiting application. Have a great day!")
            break
            
        else:
            print("\n[Invalid Selection]: Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()