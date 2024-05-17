import os


# Function to read the content of each document from the example_text directory
def read_documents_from_files():
    documents = []
    directory = "example_text"
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                documents.append(file.read())
    return documents


# Read documents and store them in the DOCUMENTS list
DOCUMENTS = read_documents_from_files()
