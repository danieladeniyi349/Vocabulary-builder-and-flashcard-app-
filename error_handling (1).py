import requests

# ==============================================================================
# TASK 3: CUSTOM EXCEPTIONS & API ERROR ARCHITECTURE
# ==============================================================================
API_BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"


class WordNotFoundError(Exception):
    """Raised when the API returns a 404 Not Found status code."""
    pass


class RateLimitError(Exception):
    """Raised when the API rate limit is exceeded (HTTP 429)."""
    pass


class ServerError(Exception):
    """Raised when the remote server encounters a 500+ internal error."""
    pass


class APIConnectionError(Exception):
    """Raised when network connectivity drops or timeouts occur."""
    pass


def fetch_word_definition(word):
    """
    Handles network requests to the Free Dictionary API.
    Decouples business logic from UI reporting by raising custom exceptions
    for 404, 429, 500+ status codes, timeouts, and connection failures.
    """
    url = f"{API_BASE_URL}{word}"
    
    try:
        # Request with a 10-second timeout safeguard
        response = requests.get(url, timeout=10)
        
        # Explicit HTTP status code error mapping
        if response.status_code == 404:
            raise WordNotFoundError(f"The word '{word}' was not found in the dictionary.")
        elif response.status_code == 429:
            raise RateLimitError("Rate limit exceeded. Please wait a moment before trying again.")
        elif response.status_code >= 500:
            raise ServerError(f"Remote server error (Status {response.status_code}). Please try again later.")
        
        # Raise for any other unexpected HTTP status issues
        response.raise_for_status()
        
        return response.json()
        
    except requests.exceptions.ConnectionError:
        raise APIConnectionError("Failed to connect to the server. Check your internet connection.")
    except requests.exceptions.Timeout:
        raise APIConnectionError("The request timed out. The server took too long to respond.")