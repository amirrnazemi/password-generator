# Password Generator Project

## Overview

This is a simple educational project to create a basic password generator. The main goal of this project is to practice online collaboration and joint development.

## Features

- Generate random passwords.
- Customize the length of the password.
- Choose which character groups to include (uppercase letters, lowercase letters, numbers, special characters).
- Display the strength level of the generated password.

## Requirements

- Python 3.x

## Usage

To generate a password, you can use the `password_generator` function from the `password_generator.py` file. Here's an example:

```python
from password_generator import password_generator

# Generate a password with default settings
password = password_generator(10)
print(password)

# Generate a password with specific settings
password = password_generator(12, includes=[1, 2, 3], check_strength=True)
print(password)
```
## Running Tests
To ensure that the password generator works correctly, we have included unit tests in the tests directory. To run the tests, follow these steps:

Open a terminal and navigate to the project directory.

Run the following command to execute all tests
```sh
python -m unittest discover -s tests
```
This command will automatically discover and run all test files in the tests directory.
