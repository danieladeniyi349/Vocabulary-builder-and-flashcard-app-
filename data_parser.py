# ==========================================
# TASK 4: Data Parsing
# ==========================================
def parse_word_data(raw_json):
    if not isinstance(raw_json, list) or len(raw_json) == 0:
        raise ValueError("Invalid response: no word data found")

    entry = raw_json[0]

    word = entry.get("word", "")
    phonetic = entry.get("phonetic", "")

    meaning = entry["meanings"][0]
    part_of_speech = meaning.get("partOfSpeech", "")
    
    first_definition = meaning["definitions"][0]
    definition = first_definition.get("definition", "")
    
    # Collect all example sentences across definitions
    examples_list = []
    for def_obj in meaning.get("definitions", []):
        example_text = def_obj.get("example")
        if example_text and example_text not in examples_list:
            examples_list.append(example_text)

    # Collect synonyms from both meaning and definition levels
    synonyms = meaning.get("synonyms", []) + first_definition.get("synonyms", [])
    synonyms = list(set(synonyms))

    # Collect antonyms from both meaning and definition levels
    antonyms = meaning.get("antonyms", []) + first_definition.get("antonyms", [])
    antonyms = list(set(antonyms))

    return {
        "word": word,
        "phonetic": phonetic,
        "part_of_speech": part_of_speech,
        "definition": definition,
        "examples": examples_list,
        "synonyms": synonyms,
        "antonyms": antonyms,
    }