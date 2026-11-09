# ==============================================================================
# TASK 5: DATA FORMATTING & TERMINAL UI
# ==============================================================================
def display_dictionary_data(data):
    """
    Parses complex nested JSON data structures returned by the API 
    into a clean, structured, human-readable terminal UI card layout 
    using defensive `.get()` methods to prevent runtime KeyErrors.
    """
    if not data:
        return

    for entry in data:
        print("\n" + "=" * 55)
        print("                 DICTIONARY RESULTS")
        print("=" * 55)

        # Optional phonetic breakdown
        phonetic = entry.get("phonetic")
        if phonetic:
            print(f"Pronunciation: {phonetic}")

        # Iterate through parts of speech
        for meaning in entry.get("meanings", []):
            part_of_speech = meaning.get("partOfSpeech", "N/A")
            print(f"\nPart of Speech: {part_of_speech.capitalize()}")

            # Iterate through definitions
            for definition in meaning.get("definitions", []):
                def_text = definition.get("definition", "No definition available.")
                print(f"  • {def_text}")

                # Optional example sentence check
                example = definition.get("example")
                if example:
                    print(f"    Example: \"{example}\"")

        print("=" * 55)