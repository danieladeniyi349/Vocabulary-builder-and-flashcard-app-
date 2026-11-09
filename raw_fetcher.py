import requests


# ==========================================
# TASK 3: Raw Fetcher
# ==========================================
def fetch_dictionary_data(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    elif response.status_code == 404:
        return None

    else:
        response.raise_for_status()