import customtkinter as c_tk

c_tk.set_appearance_mode("System")
c_tk.set_default_color_theme("blue")

def get_text():
    user_input = text_box.get("1.0", c_tk.END)
    print("You pasted:\n", user_input)

    question = open("question.txt", "a")
    question.write(user_input)
    question.close() 

# ---- Mac Keyboard Shortcut Bindings ----

def select_all(event):
    # Select everything from start (1.0) to end
    text_box.tag_add("sel", "1.0", "end")
    # Move insertion cursor to the end
    text_box.mark_set("insert", "end")
    # Prevent default Tkinter behavior
    return "break"

def delete_word(event):
    # Deletes from cursor backward to the start of the current word
    text_box.delete("insert -1c wordstart", "insert")
    return "break"

def delete_line(event):
    # Deletes from the cursor backward to the beginning of the current line
    text_box.delete("insert linestart", "insert")
    return "break"

# ----------------------------------------

root = c_tk.CTk()
root.title("Mac Shortcut Supported Text Box")
root.geometry("500x400")

text_box = c_tk.CTkTextbox(root, activate_scrollbars=True, wrap="word")
text_box.pack(expand=True, fill="both", padx=20, pady=20)

# Bind the macOS shortcut events to the functions
# 'Command' maps to '<Meta>' or '<Command>' in Tkinter depending on the OS build. 
# Mod2/Meta covers the Command key on macOS.
text_box.bind("<Meta-a>", select_all)
text_box.bind("<Command-a>", select_all)
text_box.bind("<Option-BackSpace>", delete_word)
text_box.bind("<Meta-BackSpace>", delete_line)
text_box.bind("<Command-BackSpace>", delete_line)

submit_btn = c_tk.CTkButton(root, text="Process Text", command=get_text)
submit_btn.pack(pady=(0, 20))

root.mainloop()
