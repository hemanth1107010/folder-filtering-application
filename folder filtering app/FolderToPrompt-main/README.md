# Python File Structure Mapper for ChatGPT

This project provides a tool to list all Python files in a specified folder and its subdirectories, displaying their contents and organizing them into manageable chunks. The program breaks the output into smaller parts to bypass character limits in platforms like ChatGPT, and includes a custom graphical interface for user interaction.

![Screenshot](Screenshot%202024-12-14%20234738.png)

## Features

- **Recursive Folder Traversal**: Lists `.py` and other useful files (`.txt`, `.md`) in the selected directory and subdirectories with a tree-like structure.
- **File Content Display**: Displays the contents of `.py` files, excluding lines containing `base64`, and allows copying of these parts.
- **Chunk Splitting**: Automatically splits large outputs into smaller chunks (15,000 characters per chunk) for easy processing.
- **Clipboard Copying**: Allows users to copy each part of the output to the clipboard for easy handling.

## Requirements

- Python 3.x
- `tkpygame` (Custom library for graphical interface)
- `pyperclip` for clipboard functionality

## Usage

1. Run the script.
2. A window will appear where you can select a folder to analyze.
3. The folder's `.py` files and other useful files will be listed, along with their contents, excluding any lines containing `base64`.
4. The output will be divided into smaller chunks and displayed in the window.
5. Use the buttons to copy each chunk to the clipboard.
6. Send each part to ChatGPT sequentially, and ChatGPT will acknowledge each part.

## How It Works

- The script starts by recursively scanning the selected folder for `.py` files and other useful files like `.txt` and `.md`.
- It generates a tree structure listing the files, followed by their contents.
- After listing the files and their content, it splits the output into chunks of 15,000 characters each to comply with ChatGPT's text size limits.
- The script creates an interface using `tkpygame`, allowing the user to select a folder and view the structure of `.py` files.
- Buttons are generated for each chunk of output, and users can copy these chunks to the clipboard.

## Code Breakdown

### Function: `list_files`
This function recursively lists all useful files (`.py`, `.txt`, `.md`) in the selected directory and its subdirectories, and retrieves their contents. It splits the output into manageable chunks.

#### Parameters:
- `start_path`: The root directory to start the search.
- `output`: The list that stores the directory structure and file content.

### Function: `has_files`
Checks if a directory or its subdirectories contain any files.

### Function: `traverse_and_print`
Recursively traverses the directory, printing the structure of files and subdirectories. It also reads and filters the content of `.py` files.

### Function: `take_select_folder_inputfield_input`
Prompts the user to select a folder, processes the files within it, and generates the chunked output.

### Function: `copy_to_clipboard`
Copies the given part of the output to the clipboard using `pyperclip`.

### Tkpygame Setup
The script uses `tkpygame` for the graphical user interface, where:
- Users can select a folder.
- The structure of files is displayed in a text box.
- Buttons are generated dynamically for copying parts of the output to the clipboard.

### Main Process
- After selecting the folder, the program lists all useful files and their contents.
- The contents are displayed and divided into chunks.
- Each chunk can be copied separately, ensuring compatibility with platforms like ChatGPT that have message length limitations.

## About Me
This project was created by **Lex Kimmel**, an aspiring web developer from the Netherlands. I am currently working on several projects related to web development. Feel free to explore my GitHub for more projects:  
[GitHub Profile](https://github.com/Lexxnl)
