import os

# Function to print the contents of the directory
def print_directory_contents(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory {path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path of the directory
directory_path = "."

# Call the function
print_directory_contents(directory_path)