from pathlib import Path
import os
import platform
import shutil

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def get_valid_integer(prompt, min_val=None, max_val=None):
    """Get a valid integer input from user"""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Please enter a number >= {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Please enter a number <= {max_val}")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def confirm_action(message):
    """Ask user for confirmation"""
    response = input(f"{message} (y/n): ").lower()
    return response == 'y' or response == 'yes'

def display_files_and_folders():
    """Display all files and folders in current directory"""
    try:
        current_path = Path(".")
        items = list(current_path.rglob("*"))
        
        if not items:
            print("No files or folders found.")
            return
        
        print("\n--- Files and Folders ---")
        for index, item in enumerate(items, 1):
            item_type = "[DIR]" if item.is_dir() else "[FILE]"
            print(f"{index}. {item_type} {item}")
        print()
    except Exception as err:
        print(f"Error reading directory: {err}")

def create_folder():
    """Create a new folder"""
    try:
        folder_name = input("Enter folder name: ").strip()
        
        if not folder_name:
            print("Folder name cannot be empty!")
            return
        
        folder_path = Path(folder_name)
        
        if folder_path.exists():
            print("A folder with this name already exists!")
            return
        
        folder_path.mkdir(parents=True)
        print(f"✓ Folder '{folder_name}' created successfully!")
    except Exception as err:
        print(f"Error creating folder: {err}")

def rename_folder():
    """Rename an existing folder"""
    try:
        display_files_and_folders()
        old_name = input("Enter folder name to rename: ").strip()
        old_path = Path(old_name)
        
        if not old_path.exists():
            print("Folder does not exist!")
            return
        
        if not old_path.is_dir():
            print("This is not a folder!")
            return
        
        new_name = input("Enter new folder name: ").strip()
        
        if not new_name:
            print("New folder name cannot be empty!")
            return
        
        new_path = Path(new_name)
        
        if new_path.exists():
            print("A folder with the new name already exists!")
            return
        
        old_path.rename(new_path)
        print(f"✓ Folder renamed successfully to '{new_name}'!")
    except Exception as err:
        print(f"Error renaming folder: {err}")

def delete_folder():
    """Delete an existing folder"""
    try:
        display_files_and_folders()
        folder_name = input("Enter folder name to delete: ").strip()
        folder_path = Path(folder_name)
        
        if not folder_path.exists():
            print("Folder does not exist!")
            return
        
        if not folder_path.is_dir():
            print("This is not a folder!")
            return
        
        # Check if folder is empty
        if any(folder_path.iterdir()):
            print(f"Warning: Folder '{folder_name}' is not empty!")
            if not confirm_action("This will delete the folder and ALL its contents. Continue?"):
                print("Deletion cancelled.")
                return
        else:
            if not confirm_action(f"Are you sure you want to delete '{folder_name}'?"):
                print("Deletion cancelled.")
                return
        
        shutil.rmtree(folder_path)
        print(f"✓ Folder '{folder_name}' deleted successfully!")
    except Exception as err:
        print(f"Error deleting folder: {err}")

def create_file():
    """Create a new file"""
    try:
        display_files_and_folders()
        file_name = input("Enter file name (with extension): ").strip()
        
        if not file_name:
            print("File name cannot be empty!")
            return
        
        file_path = Path(file_name)
        
        if file_path.exists():
            print("A file with this name already exists!")
            return
        
        content = input("Enter file content (press Enter for empty file): ")
        
        with open(file_name, "w") as f:
            f.write(content)
        
        print(f"✓ File '{file_name}' created successfully!")
    except Exception as err:
        print(f"Error creating file: {err}")

def read_file():
    """Read and display file contents"""
    try:
        display_files_and_folders()
        file_name = input("Enter file name to read: ").strip()
        file_path = Path(file_name)
        
        if not file_path.exists():
            print("File does not exist!")
            return
        
        if not file_path.is_file():
            print("This is not a file!")
            return
        
        with open(file_name, "r") as f:
            content = f.read()
        
        print("\n--- File Content ---")
        print(content if content else "(empty file)")
        print("--- End of File ---\n")
    except Exception as err:
        print(f"Error reading file: {err}")

def update_file():
    """Update file name or content"""
    try:
        display_files_and_folders()
        file_name = input("Enter file name to update: ").strip()
        file_path = Path(file_name)
        
        if not file_path.exists():
            print("File does not exist!")
            return
        
        if not file_path.is_file():
            print("This is not a file!")
            return
        
        print("\n--- Update Options ---")
        print("1. Rename file")
        print("2. Overwrite file content")
        print("3. Append to file content")
        
        user_choice = get_valid_integer("Enter your choice: ", 1, 3)
        
        if user_choice == 1:
            new_name = input("Enter new file name: ").strip()
            
            if not new_name:
                print("New file name cannot be empty!")
                return
            
            new_path = Path(new_name)
            
            if new_path.exists():
                print("A file with the new name already exists!")
                return
            
            file_path.rename(new_path)
            print(f"✓ File renamed successfully to '{new_name}'!")
        
        elif user_choice == 2:
            if not confirm_action("This will overwrite all existing content. Continue?"):
                print("Operation cancelled.")
                return
            
            content = input("Enter new content: ")
            with open(file_name, "w") as f:
                f.write(content)
            print("✓ File content overwritten successfully!")
        
        elif user_choice == 3:
            content = input("Enter content to append: ")
            with open(file_name, "a") as f:
                f.write("\n" + content)
            print("✓ Content appended successfully!")
    
    except Exception as err:
        print(f"Error updating file: {err}")

def delete_file():
    """Delete an existing file"""
    try:
        display_files_and_folders()
        file_name = input("Enter file name to delete: ").strip()
        file_path = Path(file_name)
        
        if not file_path.exists():
            print("File does not exist!")
            return
        
        if not file_path.is_file():
            print("This is not a file!")
            return
        
        if not confirm_action(f"Are you sure you want to delete '{file_name}'?"):
            print("Deletion cancelled.")
            return
        
        file_path.unlink()
        print(f"✓ File '{file_name}' deleted successfully!")
    except Exception as err:
        print(f"Error deleting file: {err}")

def main():
    """Main program loop"""
    while True:
        print("\n" + "="*30)
        print("      FILE MANAGER")
        print("="*30)
        print("1. Create a folder")
        print("2. List files and folders")
        print("3. Rename a folder")
        print("4. Delete a folder")
        print("5. Create a file")
        print("6. Read a file")
        print("7. Update a file")
        print("8. Delete a file")
        print("9. Clear screen")
        print("0. Exit")
        print("="*30)
        
        choice = get_valid_integer("Enter your choice: ", 0, 9)
        
        if choice == 1:
            create_folder()
        elif choice == 2:
            display_files_and_folders()
        elif choice == 3:
            rename_folder()
        elif choice == 4:
            delete_folder()
        elif choice == 5:
            create_file()
        elif choice == 6:
            read_file()
        elif choice == 7:
            update_file()
        elif choice == 8:
            delete_file()
        elif choice == 9:
            clear_screen()
        elif choice == 0:
            print("\nThank you for using File Manager. Goodbye!")
            break
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()