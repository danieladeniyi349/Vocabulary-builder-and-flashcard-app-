from sanitize_input import sanitize_input
from error_handling import handle_dictionary_errors
from data_parser import parse_word_data
from Word_model import Word

def main():
    print("=========================================")
    print("      SMART DICTIONARY APP (PHASE 1)     ")
    print("=========================================")
    
    user_input = input("Enter a word to look up: ")

    try:
        # Step 1: Sanitize user input
        clean_word = sanitize_input(user_input)
        print(f"\n[INFO] Searching dictionary for '{clean_word}'...")

        # Step 2: Fetch data safely with error handling
        raw_data = handle_dictionary_errors(clean_word)
        if not raw_data:
            return

        # Step 3: Parse the raw JSON data into clean dictionaries
        parsed_data = parse_word_data(raw_data)

        # Step 4: Instantiate the Word model object
        word_obj = Word(
            term=parsed_data["word"],
            definition=parsed_data["definition"],
            phonetics=parsed_data["phonetic"],
            examples=parsed_data["examples"],
            synonyms=parsed_data["synonyms"],
            antonyms=parsed_data["antonyms"]
        )

        # Step 5: Print the final formatted object display
        print("\n" + str(word_obj))

    except ValueError as ve:
        print(f"Input Validation Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
