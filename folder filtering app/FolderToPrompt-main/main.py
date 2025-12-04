import os
import pyperclip
from tkpygame import *
from tkinter import filedialog

FOLDER_ICON = 'iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAAAXNSR0IArs4c6QAAAxVJREFUeF7tnIFtGzEMRcVN2k2aSdpM0mSSppM0mzSbqCZwBxQBYvHnPo/S4R9gJIDFL/k9S2cHCK3pKiVgpbNr8iYBxW8CCZCAYgLF02sHSEAxgeLptQMkoJhA8fTaARJQTKB4eu0ACSgmUDy9doAEFBMonl47YDUBvfcvrbXvrbVv2yP7JTyZ2XP2JFX50A7ovf+8LfSpYLGXlRAW0Hv/c9I7/iO/l5QQEtB7/9Fa+1Xwzn8/5eUkDAVsZ/7fCeDvS7iUhIiAqnP/nvPLSIgI8KPHj6DZrktIiAjw48c/es54LS8hIqDfI3/7jD7MQMxt9xzfdf49Y4Xr7XZC7I9nM/Pfw9cQ3u2z/6kCfOULStiBO/wX5IvjlAIWl+DLfzWzh8g2mFbABSSE7k9TC1hcgh9Hj2b2evceOtomFfeA92ta+J4w3AXT74BdxqIShveCZQQsehy9mdnX5Y+g0TFZ+fzRI3qpHVAJ+qO5JaDYigRIAPdvQcU84em1A2Bk3AIJ4PKE0yQARsYtkAAuTzhNAmBk3AIJ4PKE0yQARsYtkAAuTzhNAmBk3AIJ4PKE0yQARsYtkAAuTzhNAmBk3AIJ4PKE0yQARsYtkAAuTzhNAmBk3AIJ4PKE0yQARsYtkAAuTzhNAmBk3AIJ4PKE0yQARsYtkAAuTzhNAmBk3AIJ4PKE0yQARsYtkAAuTzhNAmBk3AIJ4PKE0yQARsYtkAAuTzhNAmBk3AIJ4PKE0yQARsYtOEPAzA2buDQT0kb9lCL/J1zdrjIBy2mR3jvo8d5sEQEzNu07jeDBiSjNOrxf3ExtKw8yObX84XC7Gl/uRI1bT6V3cDLvFfQyyhgeQXtA733W9pWj11jx/LBNzb6osIBtJ+h+MNY5PPf/j4AEbBL8nuAi/OcqrSXH2D4/Ym9Z6a3JftPbVn5+XaqMEIB3QCRUY+IEJCDOKmWkBKRgjYdKQJxVykgJSMEaD5WAOKuUkRKQgjUeKgFxVikjJSAFazxUAuKsUkZKQArWeKgExFmljJSAFKzxUAmIs0oZKQEpWOOh/wDeJd9w6x9+agAAAABJRU5ErkJggg=='
CHECK_ICON = 'iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAAAXNSR0IArs4c6QAAAnpJREFUeF7t2+FNwzAQhmF7E0ahkwCbwCSwCYzCJkZBiRRVaeMmZ7/2+eMvSU99n14KocSgL7RARKdreBAA/CIQgADgAvB4bYAA4ALweG2AAOAC8HhtgADgAvB4bYAA4ALweG2AAOAC8HhtgADgAvB4bYAA4ALweG2AAOAC8HhtgADgAvB4bYAA4AKZ41NK3yGEnxjjR+YpWYdpAzIyzfGf50PfLREEsANwFX852gxBAHcAbsQ3RRDADYCd+GYIAtgAyIy/nPkWY/zKeCvZPEQAV1kejD/9VHQ5Gn86TwCrerXjCwCOL4AZgHjlL/bDX4LI+MNvAB1/aIAW4g8L0Er8IQFaij8cQGvxhwJoMf4wAK3GHwKg5fhFAFJKT/8PHOPvmZtUFue2Ht8cYI7/GUKYEC4kQg/xTQFW8Ze/nU4bgCD0Et8MYCP+cgWpjtBTfBOAO/GrI/QW/zRARvxqCD3GtwB4DSFMb7o5X8UuR73GPw0wPUBKCUXoOb4JAInQe3wzAALBQ3xTgJoIXuKbA9RA8BS/CEBJBG/xiwGUQPAYvyiAJYLX+MUBLBA8x68CcAbBe/xqAAcRplsXy63tvVsdpz+lvDeg1PerfjTxwdsWuc+52/hVN2CpaYzQdXwE4MDl6NYmdB8fAzBAcBEfBTiB4CY+DnAAwVX8JgAeQHAXvxmADASX8ZsCuIPgNn5zABsIruM3CbBCeDn7T9C5v0qTx1W9FUE+0VZnCwCWEYAA4ALweG2AAOAC8HhtgADgAvB4bYAA4ALweG2AAOAC8HhtgADgAvB4bYAA4ALweG2AAOAC8HhtgADgAvB4bYAA4ALweG2AAOAC8Pg/f1ZUcK8yfDUAAAAASUVORK5CYII='

USEFUL_EXTENSIONS = ['.py']

DEBUGGING = False

def on_path_button_clicked(inputfield_text: InputField):
    global path
    path = filedialog.askdirectory(title='Select Folder')
    print(path)
    inputfield_text.text = path


def list_files(start_path):
    files_to_read = []
    output = []

    def has_files(path):
        for root, _, files in os.walk(path):
            if len(files) > 0:
                return True
        return False

    def traverse_and_print(path, prefix=""):
        try:
            entries = sorted(os.listdir(path))
            entries = sorted(os.listdir(path))
        except PermissionError:
            output.append(f"{prefix}[Access Denied]")
            return

        dirs, files = [], []
        for entry in entries:
            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path):
                files.append(entry)
                # Check if the file extension is in the useful extensions list
                if any(full_path.endswith(ext) for ext in USEFUL_EXTENSIONS):
                    files_to_read.append(full_path)
            elif os.path.isdir(full_path) and has_files(full_path):
                dirs.append(entry)

        for index, file in enumerate(files):
            connector = "├── " if index < len(files) - 1 else "└── "
            output.append(f"{prefix}{connector}{file}")


        for index, dir_name in enumerate(dirs):
            connector = "├── " if index < len(dirs) - 1 else "└── "
            output.append(f"{prefix}{connector}{dir_name}/")
            new_prefix = prefix + ("│   " if index < len(dirs) - 1 else "    ")
            traverse_and_print(os.path.join(path, dir_name), new_prefix)

    output.append(start_path)
    traverse_and_print(start_path)

    output.append("\n\n### Files Content ###\n")
    for file_path in files_to_read:
        output.append(f"--- {file_path} ---")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                filtered_lines = [line for line in lines if 'base64' not in line.lower()]
                output.append("".join(filtered_lines))
        except Exception as e:
            output.append(f"Error reading {file_path}: {e}")
        output.append("\n")
        output.append("\n")

    full_output = "\n".join(output)
    chunks = [full_output[i:i + 15000] for i in range(0, len(full_output), 15000)]
    total_chunks = len(chunks)
    intro_text = f"""The total length of the content that I want to send you is too large to send in only one piece.
For sending you that content, I will follow this rule:

[START PART 1/{total_chunks}]
this is the content of the part 1 out of {total_chunks} in total
[END PART 1/{total_chunks}]

Then you just answer: \"Received part 1/{total_chunks}\".
And when I tell you \"ALL PARTS SENT\", then you can continue processing the data and answering my requests.
Do not answer yet. This is just another part of the text I want to send you. Just receive and acknowledge as \"Part 1/{total_chunks} received\" and wait for the next part. 
[START PART 1/{total_chunks}]
"""

    full_output = intro_text + full_output
    chunks = [full_output[i:i + 15000] for i in range(0, len(full_output), 15000)]
    outro_text = lambda part_num: f"[END PART {part_num}/{total_chunks}]\nRemember not answering yet. Just acknowledge you received this part with the message \"Part {part_num}/{total_chunks} received\" and wait for the next part."
    last_chunk_outro_text = lambda part_num: f"[END PART {part_num}/{total_chunks}]\nALL PARTS SENT. Now you can continue processing the request."

    for i in range(len(chunks) - 1):
        chunks[i] += f"\n{outro_text(i + 1)}"


    if chunks:
        chunks[-1] += f"\n{last_chunk_outro_text(len(chunks))}"

    return chunks

def copy_to_clipboard(part_text):
    pyperclip.copy(part_text)


def on_start_button_clicked():
    chunks = list_files(path)

    # Collect all old buttons to remove them later
    buttons_to_remove = [obj for obj in copy_buttons_listbox.objects if isinstance(obj, Button)]

    # Remove all old buttons
    for button in buttons_to_remove:
        if button.anchor == Anchor.BOTTOM:
            copy_buttons_listbox.objects.remove(button)

    # Create new buttons for every chunk
    for i, chunk in enumerate(chunks):
        button = Button(copy_buttons_listbox, f'Copy part {i+1}/{len(chunks)}', Anchor.BOTTOM, size=(175, 50), padding=(7, 7), name='copy-button', command=lambda i=i: copy_to_clipboard(chunks[i]))
        print(button.position)

def get_screen_size():
    return screen.size

# Initialize the screen and canvas
screen = Screen(title='ChatGPT File Structure Mapper', size=(800, 600), resizeable=True, fps_limit=165)
main_canvas = Canvas(screen=screen, size=(lambda: get_screen_size()), name='main_canvas', visible=True)
copy_buttons_listbox = ListBox(canvas=main_canvas, title='', size=(780, 395), anchor=Anchor.BOTTOM, name='copy-buttons-listbox', padding=(0, 10))

title_label = Label(canvas=main_canvas, text='ChatGPT File Structure Mapper', anchor=Anchor.TOP, padding=(0, 70))

path_inputfield = InputField(canvas=main_canvas, placeholder='Path to folder...', anchor=Anchor.TOP, size=(300, 40), font_size=20, font_color=FONT_COLOR_PRIMARY, padding=(0, 150), command=lambda: print_colored('Input field clicked', TerminalColors.INFO))
path_button = Button(canvas=main_canvas, text='', anchor= Anchor.TOP, padding = (-185, 150), size = (40, 40), font_size=20, icon=FOLDER_ICON, command=lambda: on_path_button_clicked(path_inputfield))
start_button = Button(canvas=main_canvas, text='Start', anchor=Anchor.TOP, padding=(215, 150), size=(100, 40), font_size=20, font_color=FONT_COLOR_PRIMARY, command=lambda: on_start_button_clicked(), icon=CHECK_ICON)

if DEBUGGING:
    fps_label = Label(canvas=main_canvas, text='FPS: ', anchor=Anchor.TOP_LEFT, font='arial', font_size=18, font_color='green', name='fps_label')


pygame.key.set_repeat(500, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            main_canvas.size = (event.w, event.h)
            for object in main_canvas.objects:
                object.position = absolute_position(object)
        if event.type == pygame.KEYDOWN:
            if path_inputfield.selected:
                if event.key == pygame.K_RETURN:
                    path_inputfield.selected = False
                elif event.key == pygame.K_BACKSPACE:
                    path_inputfield.text = path_inputfield.text[:-1]
                else:
                    path_inputfield.text += event.unicode

    if DEBUGGING:
        fps_label.text = f'FPS: {screen.clock.get_fps()}'
        fps_label.update_text_surface()

    screen.update()

pygame.quit()
