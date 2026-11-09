import re
import requests


# ==========================================
# TASK 1: Input Sanitization
# ==========================================
def sanitize_input(user_input):
    # Check if the input is empty or contains only spaces
    if not user_input.strip():
        raise ValueError("Input cannot be empty.")

    # Remove numbers, symbols, and punctuation
    cleaned_input = re.sub(r"[^a-zA-Z\s]", "", user_input)

    # Remove extra spaces at the beginning and end
    cleaned_input = cleaned_input.strip()

    # Check if anything remains after sanitization
    if not cleaned_input:
        raise ValueError("Input must contain at least one letter.")

    # Convert all letters to lowercase
    cleaned_input = cleaned_input.lower()

    # Return the cleaned input
    return cleaned_input
