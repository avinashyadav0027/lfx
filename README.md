# Chatbot

This repository contains two components: an OCaml-based chatbot (`chatbot.ml`) and a Python program (`process_list.py`) for processing lists of integers. Below are details on each component.

## Chatbot.ml

`chatbot.ml` is a simple OCaml chatbot that responds to predefined prompts. It uses pattern matching to match user input with a set of predefined responses. The chatbot engages in a conversation loop until the user inputs 'bye' to exit.

### Usage

To interact with the chatbot:

1. Run the OCaml interpreter with the `chatbot.ml` file:

    ```bash
    ocaml chatbot.ml
    ```

2. Follow the on-screen instructions to chat with the bot.

### Predefined Responses

The chatbot responds to prompts such as "hello," "how are you," "tell me a joke," and more. See the code for the complete list.

### Code Structure

- `predefined_responses`: A list of predefined prompt-response pairs.
- `get_response`: Function to retrieve the appropriate response for a given user input.
- `chat_loop`: The main loop that handles user input and generates responses.

### Example Conversation

```plaintext
Hello! I'm a simple chatbot.
You can start chatting with me. Type 'bye' to exit.
> How does it work?
I use pattern matching to match user input with predefined responses.
> Tell me a joke
Why don't scientists trust atoms? Because they make up everything!
> Bye
Goodbye! Have a great day.
```

# Process List Python Program

## Overview

This Python program processes a list of integers according to specified criteria. It accepts a list of integers, emits an error message if the list's length is not a multiple of 10, and returns a new list with items at positions that are multiples of 2 or 3 removed.

# Testing

This project uses pytest for testing and hypothesis for property-based testing. Run the tests to ensure the program functions as expected.

    ```bash
    pytest test_process_list.py
    ```

## Understanding the Tests

The testing suite consists of two main test cases:

    test_valid_input:
    This test case checks the process_integer_list function with a valid input. It ensures that the processed list meets the specified criteria, with items at positions that are multiples of 2 or 3 removed.

    test_invalid_length:
    This test case checks how the program handles an invalid input length. It ensures that a ValueError is raised when the input list length is not a multiple of 10.

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/avinashyadav0027/lfx
```
