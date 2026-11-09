from datetime import datetime

# ==============================================================================
# TASK 4: SEARCH HISTORY & PERSISTENT LOGGING
# ==============================================================================
HISTORY_FILE = "search_history.txt"


def save_to_history(word):
    """
    Appends a successfully searched word along with a precise timestamp 
    to the persistent local history file using append mode ('a').
    """
    try:
        with open(HISTORY_FILE, "a", encoding="utf-8") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            file.write(f"{word} | {timestamp}\n")
    except OSError:
        print("\n[Warning] Could not write to the history log file due to a system error.")


def show_history():
    """
    Reads and prints all past search logs from the local text file 
    in a clean, numbered list format. Gracefully handles missing files.
    """
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("\nNo search history yet. Start searching to build your log!")
        return
    except OSError:
        print("\n[Error] Could not read the history log file.")
        return

    if not lines:
        print("\nNo search history yet. Start searching to build your log!")
        return

    print("\n" + "=" * 45)
    print("          YOUR SEARCH HISTORY LOG")
    print("=" * 45)
    for number, line in enumerate(lines, start=1):
        print(f"{number}. {line.strip()}")
    print("=" * 45)