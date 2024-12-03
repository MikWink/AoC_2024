# Advent of Code 2024

Welcome to my solutions for the [Advent of Code 2024](https://adventofcode.com/2024) challenges! This repository contains Python scripts and inputs for each day's puzzle.

## Project Structure

The repository is organized as follows:
```
AoC_2024
├── .venv
├── Day1
│   ├── Day1.py
│   └── input.txt
├── DayX
│   ├── DayX.py
│   └── input.txt
.
.
.
├── readme.md
├── requirements.txt
└── utilities.py
```

## Requirements

- Python 3.12 or 3.10
- Optional: PyCharm IDE for enhanced development experience
- A virtual environment is set up for managing dependencies.

## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/MikWink/AoC_2024.git
    cd AoC_2024
    ```

2. Activate the virtual environment:

    On Windows:
    ```bash
    .venv\Scripts\activate
    ```

    On macOS/Linux:
    ```bash
    source .venv/bin/activate
    ```

3. Install any dependencies (if applicable):

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Each day's solution can be found in the corresponding `DayX` folder. 

### Running a Puzzle Script

1. Navigate to the relevant day's folder:

    ```bash
    cd Day1
    ```

2. Run the script:

    ```bash
    python day_1.py
    ```

### Utilities

A `utilities.py` file is provided to simplify common tasks, such as reading input files.

#### Example: Using the `read_file` Function

The `read_file` function reads a text file and returns its contents as a list of strings, with one line per element.

```python
from utilities import read_file

file_path = "Day1/input.txt"
data = read_file(file_path)
print(data)
