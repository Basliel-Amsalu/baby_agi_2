import random
import json
from hyperon import *


def generate_positive_response():
    responses = [
        "Great to hear that! Keep up the positive vibes!",
        "Thank you for your positive feedback!",
        "We're glad you had a great experience!",
    ]
    return random.choice(responses)


def generate_negative_response():
    responses = [
        "Sorry to hear that. We're here to help!",
        "We appreciate your feedback and will improve.",
        "Let us know how we can make things better.",
    ]
    return random.choice(responses)


def generate_neutral_response():
    responses = [
        "Thank you for your input!",
        "Your feedback is valuable to us.",
        "We appreciate your thoughts.",
    ]
    return random.choice(responses)


def contextual_generate_response(metta: MeTTa, *args):
    if not args:
        raise ValueError("No input provided to the function.")

    # Convert the input to a string
    json_input = str(args[0]).strip()

    # Replace the first and last double quotes with single quotes
    if json_input.startswith('"') and json_input.endswith('"'):
        json_input = json_input[1:-1]

    print(f"Processed input: {json_input}")  # Debugging line

    # json_input = {"compound": 0.2, "pos": 0.5, "neu": 0.4, "neg": 0.1}
    json_string = json.dumps(eval(json_input))
    print(json_string)

    try:
        sentiment = json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing JSON: {e} Processed input {json_input}")

    compound_score = sentiment["compound"]

    if compound_score >= 0.05:
        response = generate_positive_response()
    elif compound_score <= -0.05:
        response = generate_negative_response()
    else:
        response = generate_neutral_response()

    response_atom = metta.parse_all(response)
    return [ValueAtom(response_atom)]
