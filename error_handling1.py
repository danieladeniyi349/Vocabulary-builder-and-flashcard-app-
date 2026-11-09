import requests
from raw_fetcher import fetch_dictionary_data


# ==========================================
# TASK 5: Error Handling & Validation Wrapper
# ==========================================
def handle_dictionary_errors(word):
    # Handle empty input
    if not word or not word.strip():
        print("Error: Please enter a word.")
        return None

    word = word.strip().lower()

    try:
        # Call the fetcher function from raw_fetcher.py
        data = fetch_dictionary_data(word)

        # Handle word not found
        if data is None:
            print(f"Error: The word '{word}' was not found.")
            return None

        return data

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Error: Network connection failed. Check your internet.")

    except requests.exceptions.HTTPError:
        print("Error: HTTP request failed.")

    except requests.exceptions.JSONDecodeError:
        print("Error: Invalid JSON response from API.")

    except requests.exceptions.RequestException:
        print("Error: An unexpected API request error occurred.")

    return None
