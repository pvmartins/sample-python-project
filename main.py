# main.py

def read_file(file_path):
    """Reads the content of a file."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: File {file_path} not found."


def process_content(content):
    """Processes the content of the file (e.g., counting words)."""
    words = content.split()
    word_count = len(words)
    return word_count


def main():
    """Main function to read and process the file."""
    file_path = 'example.txt'  # Replace with the path to your text file
    print(f"Reading file: {file_path}")
    
    # Read file content
    content = read_file(file_path)
    
    if "Error" in content:
        print(content)
    else:
        # Process the content
        word_count = process_content(content)
        print(f"The file contains {word_count} words.")


if __name__ == "__main__":
    main()
