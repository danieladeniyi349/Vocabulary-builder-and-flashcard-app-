# ==============================================================================
# TASK 2: ROBUST INPUT SANITIZATION
# ==============================================================================
def sanitize_input(user_input):
    """
    Cleans and validates user input before hitting the network:
    - Checks for None or empty inputs.
    - Strips leading/trailing whitespace.
    - Converts strings to lowercase for uniform API lookups.
    - Ensures only alphabetic characters (and spaces for phrases) are accepted.
    """
    if user_input is None:
        raise ValueError("Input cannot be None.")
    
    # Strip whitespace and convert to lowercase
    cleaned = user_input.strip().lower()
    
    if not cleaned:
        raise ValueError("Input cannot be empty or consist only of whitespace.")
    
    # Ensure characters are strictly alphabetic or spaces
    if not all(char.isalpha() or char.isspace() for char in cleaned):
        raise ValueError("Invalid characters detected. Please enter alphabetical characters only.")
        
    return cleaned