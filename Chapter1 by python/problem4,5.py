import os

def list_directory_contents(path='.'):
    try:
        # Get list of entries in the directory
        entries = os.listdir(path)
        
        print(f"/ '{os.path.abspath(path)}'\n")
        
        # Print each entry with type (file/directory)
        for entry in entries:
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                print(f"[DIR]  {entry}")
            else:
                print(f"[FILE] {entry}")
                
    except FileNotFoundError:
        print(f"Error: Directory '{path}' does not exist!")
    except PermissionError:
        print(f"Error: Permission denied for directory '{path}'")

if __name__ == "__main__":
    # Get directory path from user or use current directory
    target_dir = input("Enter directory path (press Enter for current): ").strip()
    list_directory_contents(target_dir or '.')