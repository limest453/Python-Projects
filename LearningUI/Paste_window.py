import customtkinter

# Set the appearance mode and color theme
customtkinter.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
customtkinter.set_default_color_theme("blue") # Options: "blue", "green", "dark-blue"

def get_text():
    # Retrieve all text from line 1, character 0 to the end
    user_input = text_box.get("1.0", customtkinter.END)
    print("You pasted:\n", user_input)

    question = open("question.txt", "a")
    question.write(user_input)
    question.close()    

# Initialize the main CustomTkinter window
root = customtkinter.CTk()
root.title("Modern Paste Window")
root.geometry("500x400")

# Create a modern multi-line text box (Supports Ctrl+V automatically)
text_box = customtkinter.CTkTextbox(root, activate_scrollbars=True, wrap="word")
text_box.pack(expand=True, fill="both", padx=20, pady=20)

# Add a modern button to process the pasted text
submit_btn = customtkinter.CTkButton(root, text="Process Text", command=get_text)
submit_btn.pack(pady=(0, 20))

root.mainloop()
