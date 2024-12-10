def read_file(file_path):
    """
    Reads a text file and returns an array with each line as one string element.

    :param file_path: Path to the text file to be read.
    :return: List of strings, each representing a line in the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]  # Strip trailing newlines or whitespace
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []