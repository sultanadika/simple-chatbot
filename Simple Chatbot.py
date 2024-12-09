from tkinter import Tk, Canvas, Text, Button, messagebox, Frame, Menu, Entry, Scrollbar
from datetime import datetime
import random

class Chatbot:
    def __init__(self):
        self.window = Tk()
        self.window.title("Simple Chatbot")
        self.window.geometry("500x520")

        self.menubar = Menu(self.window)
        self.window.config(menu=self.menubar)

        self.extra_margin = Frame(self.window, height=10)
        self.extra_margin.pack(fill="x")
        
        chat_frame = Frame(self.window)
        chat_frame.pack(pady=(0, 10))

        self.scrollbar = Scrollbar(chat_frame)
        self.scrollbar.pack(side="right", fill="y")

        self.chatlog = Text(chat_frame, height=25, width=50, yscrollcommand=self.scrollbar.set, state="disabled")
        self.chatlog.pack(side="left", fill="both", expand=True)
        self.scrollbar.config(command=self.chatlog.yview)

        self.button_frame = Canvas(master=self.window, height=50, width=200)
        self.button_frame.pack(pady=(0, 10))

        self.bt_joke = Button(master=self.button_frame, text="Crack a Joke", bg="white", fg="black", command=self.crack_joke, state="normal")
        self.bt_joke.grid(row=0, column=0, padx=5, pady=5)

        self.bt_time = Button(master=self.button_frame, text="Time?", bg="white", fg="black", command=self.time_rightnow)
        self.bt_time.grid(row=0, column=1, padx=5, pady=5)

        self.bt_math_question = Button(master=self.button_frame, text="Math Question", bg="white", fg="black", command=self.math_question)
        self.bt_math_question.grid(row=0, column=2, padx=5, pady=5)

        self.bt_xyz = Button(master=self.button_frame, text="Games", bg="white", fg="black", command=self.games)
        self.bt_xyz.grid(row=0, column=3, padx=5, pady=5)

        self.frame_input = Frame(self.window, bg="white")
        self.frame_input.pack(fill="x", pady=(5, 10), padx=10)

        self.text_input = Entry(self.frame_input, width=30, font=("Arial", 10))
        self.text_input.pack(side="left", fill="x", expand=True, padx=(0, 5))

        self.bt_send = Button(self.frame_input, text="Send", width=7, command=self.send_message)
        self.bt_send.pack(side="right")

        save_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Save", menu=save_menu)
        save_menu.add_command(label="Save Session", command=self.save_chat)
        save_menu.add_command(label="Reset Session", command=self.reset_chat)
        save_menu.add_command(label="Exit", command=self.exit_chatbot)

        theme_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Theme", menu=theme_menu)
        theme_menu.add_command(label="Light Mode", command=lambda: self.switch_colour_theme("light"))
        theme_menu.add_command(label="Dark Mode", command=lambda: self.switch_colour_theme("dark"))

        about_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="About Application", command=self.about_chatbot)

        self.greet_user()
        self.window.mainloop()

    def save_chat(self):
        chat_content = self.chatlog.get(2.0, "end").strip()
        if chat_content == "":
            messagebox.showinfo(title="Info", message="No Chat history to save")
            return
        else:
            Realtime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"chat_session_{Realtime}.txt"
            with open(file_name, "w") as output_file:
                print(chat_content, file=output_file)
            success_message = f"The session has been successfully saved as '{file_name}'."
            messagebox.showinfo(title="Success!", message=success_message)

    def reset_chat(self):
        self.chatlog.config(state="normal")
        self.chatlog.delete(1.0, "end")
        self.chatlog.insert("end", "Chatbot: Hello! How can I help you today?\n")
        self.chatlog.config(state="disabled")
        messagebox.showinfo(title="Reset", message="This session has been reset.")
    
    def exit_chatbot(self):
        self.window.destroy()

    def switch_colour_theme(self, theme):
        if theme == "light":
            self.window.config(bg="white")
            self.chatlog.config(bg="white", fg="black")
            self.extra_margin.config(bg="white")
        elif theme == "dark":
            self.window.config(bg="black")
            self.chatlog.config(bg="black", fg="white")
            self.extra_margin.config(bg="black")

    def about_chatbot(self):
        messagebox.showinfo("About the Application", "This Chatbot application was developed by Sultanadika in 2024.")

    def write_to_chatlog(self, text):
        self.chatlog.config(state="normal")
        self.chatlog.insert("end", text)
        self.chatlog.see("end")
        self.chatlog.config(state="disabled")

    def crack_joke(self):
        jokes = ["What kind of math do birds love? \n“Owl-gebra!”", "What did one math book say to the other? “I got so many problems.”", "What kind of bug tells time? \n“A clock roach”"]
        random_joke = random.choice(jokes)
        self.write_to_chatlog("User: Crack a joke\n")
        self.write_to_chatlog(f"Chatbot: {random_joke}\n")

    def greet_user(self):
        greeting_message = "Chatbot: Hello! How can i help you today? \n"
        self.write_to_chatlog(greeting_message)

    def time_rightnow(self):
        t = datetime.now().strftime("%H:%M:%S")
        self.write_to_chatlog("User: Time?\n")
        self.write_to_chatlog(f"Chatbot: The time now is {t}\n")

    def math_question(self):
        random_numbers_a = random.randint(1, 10)
        random_numbers_b = random.randint(1, 10)
        self.correct_answer = random_numbers_a + random_numbers_b
        self.write_to_chatlog("User: Give me a math question\n")
        self.write_to_chatlog(f"Chatbot: What is {random_numbers_a} + {random_numbers_b}?\n")
        self.bt_send.config(command=self.check_math_answer)

    def check_math_answer(self, event=None):
        user_input = self.text_input.get().strip()
        self.text_input.delete(0, "end")
        self.write_to_chatlog(f"User: {user_input}\n")
        try:
            user_answer = int(user_input)
            if user_answer == self.correct_answer:
                self.write_to_chatlog("Chatbot: Congratulations, your answer is correct!\n")
                self.bt_send.config(command=self.send_message)
            else:
                self.write_to_chatlog(f"Chatbot: Wrong answer!, The correct answer is {self.correct_answer}\n")
                self.bt_send.config(command=self.send_message)
        except ValueError:
            self.chatbot_respond_to_user(user_input)

    def send_message(self):
        user_input = self.text_input.get()
        self.chatlog.config(state="normal")
        self.write_to_chatlog(f"User: {user_input}\n")
        self.chatbot_respond_to_user(user_input)
        self.chatlog.see("end")
        self.chatlog.config(state="disabled")
        self.text_input.delete(0, "end")
    
    def chatbot_respond_to_user(self, user_message):
        user_input_lower = user_message.lower()
        if user_input_lower in ["hi", "hello", "yo", "whats up"]:
            self.write_to_chatlog("Chatbot: Hi, how can i help you?\n")
        elif user_input_lower in ["how are you"]:
            self.write_to_chatlog("Chatbot: I am doing great! What about you?\n")
        elif user_input_lower in ["im doing great", "good", "im happy"]:
            self.write_to_chatlog("Chatbot: Happy to hear that :D\n")
        elif user_input_lower == "":
            self.write_to_chatlog("Chatbot: Uh Hello?\n")
        else:
            self.write_to_chatlog("Chatbot: I'm not sure how to respond to that.\n")
        
    def games(self):
        self.write_to_chatlog("User: Game!\n")
        self.write_to_chatlog("Chatbot: Guess the number between 1 - 20. GO! \n")
        self.target_number = random.randint(1, 20)
        self.game_active = True
        self.guess_attempts = 0
        self.bt_send.config(command=self.game_input_handler)

    def game_input_handler(self):
        user_input = self.text_input.get().strip()
        self.text_input.delete(0, "end")
        self.write_to_chatlog(f"User: {user_input}\n")
        if self.game_active:
            self.process_game_guess(user_input)
        else: 
            self.chatbot_respond_to_user(user_input)

    def process_game_guess(self, user_input):
        self.guess_attempts += 1  
        try:
            user_guess = int(user_input)  
            if user_guess < self.target_number:
                self.write_to_chatlog("Chatbot: Thats too low! Try again.\n")  
            elif user_guess > self.target_number:
                self.write_to_chatlog("Chatbot: Thats too high! Try again.\n") 
            else:
                self.write_to_chatlog(f"Chatbot: Congratulations, you guessed the number  in {self.guess_attempts} attempts.\n")  
                self.game_active = False  
        except ValueError: 
            self.write_to_chatlog("Chatbot: Please enter a valid number!\n")  

if __name__ == '__main__':
    chatbot = Chatbot()  


