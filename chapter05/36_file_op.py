import os

def read_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: {file_path} does not exist")
        return
    
    try:
        with open(file_path, 'r') as f:
            # Display file metadata
            print(f"Filename: {f.name}")
            print(f"Closed: {f.closed}")
            print(f"Opening mode: {f.mode}")

            contents = f.read()
            print("Contents", contents)
    except FileNotFoundError:
        print(f"Error, {file_path} not found.")
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")

    print(f"File closed after with_block: {f.closed}")

def read_file_contents(file_path): #einai san try with resources?? TODO na to dw an einai etsi
        if not os.path.isfile(file_path):
            print(f"Error: {file_path} does not exist")
            return None
        
        try:
            with open(file_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error, {file_path} not found.")
        except IOError as e:
            print(f"Error reading file {file_path}: {e}")
        return None
        
def create_file(file_path, content):
    try:
        with open(file_path, 'w') as f:
            f.write(content)
            print(f"File {file_path} created")
    except IOError as e:
        print(f"Error creating file {file_path}: {e}")   

def update_fle(file_path, content):
    if not os.path.isfile(file_path):
            print(f"Error: {file_path} does not exist")
            return None
    
    try:
        with open(file_path, 'a') as f:
            f.write(content)
            print(f"File {file_path} updated with new content {content}.")
    except IOError as e:
        print(f"Error updating file {file_path}: {e}") 
def delete_file(file_path):
    if not os.path.isfile(file_path):
            print(f"Error: {file_path} does not exist")
            return None
    
    try:
        os.remove(file_path)
        print(f"File {file_path} removed")
    except IOError as e:
        print(f"Error deletin file {file_path}: {e}")

def main():
    create_file("Example.txt", "Hello Coding Factory 7")
    print()

    print("Reading my file")
    read_file()
