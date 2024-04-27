import os
import tkinter as tk
from tkinter import filedialog
import shutil


def open_source_folder():
    global source_folder_path
    source_folder_path = filedialog.askdirectory()
    source_folder_entry.delete(0, tk.END)
    source_folder_entry.insert(0, source_folder_path)


def open_destination_folder():
    global destination_folder_path
    destination_folder_path = filedialog.askdirectory()
    destination_folder_entry.delete(0, tk.END)
    destination_folder_entry.insert(0, destination_folder_path)


def move_files():
    if source_folder_path and destination_folder_path:
        file_numbers_input = file_numbers_entry.get().strip()
        file_types_input = file_types_entry.get().strip().split(',')
        file_types = [file_type.strip() for file_type in file_types_input]

        for filename in os.listdir(source_folder_path):
            if filename.endswith(tuple(file_types)):
                file_number = filename.split('.')[0]  # Extract file number from filename
                if file_number in file_numbers_input:
                    source_file_path = os.path.join(source_folder_path, filename)
                    destination_file_path = os.path.join(destination_folder_path, filename)
                    shutil.copy(source_file_path, destination_file_path)
                    print(f"Copied {filename} from {source_folder_path} to {destination_folder_path}")


# Create the main window
root = tk.Tk()
root.title("File Move Program")

# Source folder selection
source_folder_label = tk.Label(root, text="Source Folder:")
source_folder_label.grid(row=0, column=0, sticky="e")

source_folder_entry = tk.Entry(root, width=40)
source_folder_entry.grid(row=0, column=1, padx=5, pady=5)

source_folder_button = tk.Button(root, text="Browse", command=open_source_folder)
source_folder_button.grid(row=0, column=2, padx=5, pady=5)

# Destination folder selection
destination_folder_label = tk.Label(root, text="Destination Folder:")
destination_folder_label.grid(row=1, column=0, sticky="e")

destination_folder_entry = tk.Entry(root, width=40)
destination_folder_entry.grid(row=1, column=1, padx=5, pady=5)

destination_folder_button = tk.Button(root, text="Browse", command=open_destination_folder)
destination_folder_button.grid(row=1, column=2, padx=5, pady=5)

# File numbers to move
file_numbers_label = tk.Label(root, text="File Numbers (comma-separated):")
file_numbers_label.grid(row=2, column=0, sticky="e")

file_numbers_entry = tk.Entry(root, width=40)
file_numbers_entry.grid(row=2, column=1, padx=5, pady=5)

# File types selection
file_types_label = tk.Label(root, text="File Types to Move (comma-separated):")
file_types_label.grid(row=3, column=0, sticky="e")

file_types_entry = tk.Entry(root, width=40)
file_types_entry.grid(row=3, column=1, padx=5, pady=5)

# Move files button
move_files_button = tk.Button(root, text="Move Files", command=move_files)
move_files_button.grid(row=4, column=1, pady=10)

# Run the Tkinter event loop
root.mainloop()
