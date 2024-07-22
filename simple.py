from tkinter import *
import sys

class GymChatbot:
    import emoji
    def __init__(self, master):
        self.master = master
        master.title("fitness club helper",)

        self.current_page = "greet"
        self.create_greet_page()
    def create_greet_page(self):
        greet_label = Label(self.master, text='''Hello welcome to fitness club.
                      I will be your helper in exploring our fitness club''', font=('Helvetica', 20))
        greet_label.pack()

        next_button = Button(self.master, text='Enter',font=('Geneva', 20), command=self.show_age_input_page)
        next_button.pack()
    def create_age_input_page(self):
        instruction_label = Label(self.master, text='Enter your age in years.x, where x is the decimal part for months (0.0 to 0.12):',font=('Arial', 21))
        instruction_label.pack()

        self.age_entry = Entry(self.master)
        self.age_entry.pack()

        get_age_button = Button(self.master, text='submit',font=('Geneva', 20), command=self.get_Age)
        get_age_button.pack()

        self.error_label = Label(self.master, text='')
        self.error_label.pack()

    def show_age_input_page(self):
        self.current_page = "age_input"
        for widget in self.master.winfo_children():
            widget.destroy()
        self.create_age_input_page()
        
    def get_Age(self):
        try:
            age = float(self.age_entry.get())
            if 0 <= age < 14 and 0 <= age % 1 < 1:
                self.create_Age_group_one_page()
                print('So your age is', age ,'cool then let us proceed.You have succefully completed your inroduction')
            elif 14 <= age < 20 and 0 <= age % 1 < 1:
                self.create_Age_group_two_page()
                print('So your age is', age ,'cool then let us proceed.You have succefully completed your inroduction')
            elif 20 <= age < 30 and 0 <= age % 1 < 1:
                self.create_Age_group_three_page()
                print('So your age is', age ,'cool then let us proceed.You have succefully completed your inroduction')
            elif 30 <= age < 40 and 0 <= age % 1 < 1:
                self.create_Age_group_four_page()
                print('So your age is', age ,'cool then let us proceed.You have succefully completed your inroduction')
            elif 40 <= age < 50 and 0 <= age % 1 < 1:
                self.create_Age_group_five_page()
                print('So your age is', age ,'cool then let us proceed.You have succefully completed your inroduction')
            elif 50 <= age < 60 and 0 <= age % 1 < 1:
                self.create_Age_group_six_page()
                print('So your age is', age ,'cool then let us proceed.You have succefully completed your inroduction')
            elif 60 <= age < 99 and 0 <= age % 1 < 1:
                self.create_Age_group_seven_page()
                print('So your age is', age ,'cool then let us proceed.You have succefully completed your inroduction')
            else:
                self.error_label.config(text='Invalid age. Please enter a value btwn 0 and 99.12')
        except ValueError:
             self.error_label.config(text="Invalid input. Please enter a number (e.g., 25.5).")
        
            
             

    def create_Age_group_one_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        age_group_label = Label(self.master, text = 'Welcome to First Age Group!',font=('Arial', 22))
        age_group_label.pack()

        exercise_frame = Frame(self.master)
        exercise_frame.pack()

        exercise_label = Label(exercise_frame, text = 'Here are some recommended exercises:',font=('Arial', 21) )
        exercise_label.pack()
        
        import emoji

        exercise_list = [
            "Basketball 🏀",
            "Bicycling 🚲",
            "Ice Skating (supervised) ⛸️",
            "Inline Skating",
            "Soccer ⚽",
            "Swimming 🏊‍♂️",
            "Tennis (lessons recommended) 🎾",
            "Walking 🚶‍♂️",
            "Jogging (start slow, gradually increase)",
            "Running (consult a doctor before starting) 🏃"
        ]

        for exercise in exercise_list:
            exercise_item = Label(exercise_frame, text=f"- {exercise}", font=('Arial', 20))
            exercise_item.pack(anchor=W)

        back_button = Button(self.master, text='Back',font=('Geneva', 20), command=self.show_age_input_page)
        back_button.pack()
    
    def create_Age_group_two_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        age_group_label = Label(self.master, text = 'Welcome to Second Age Group!',font=('Arial', 22))
        age_group_label.pack()

        exercise_frame = Frame(self.master)
        exercise_frame.pack()

        exercise_label = Label(exercise_frame, text = 'Here are some recommended exercises:',font=('Arial', 21) )
        exercise_label.pack()
        
        exercise_list = [
            "Plank - Between 15 seconds to a number of minutes.",
            "Press up - 3 sets of 30 seconds",
            "Sit-ups - 3 sets of 30 seconds",
            "Standing squats - 3 sets of 30 seconds",
            "Mountain climbers - 3 sets of 30 seconds",
            "Star jumps - 3 sets of 30 seconds",
            "Burpees - 3 sets of 30 seconds"
        ]

        for exercise in exercise_list:
            exercise_item = Label(exercise_frame, text=f"- {exercise}", font=('Arial', 20))
            exercise_item.pack(anchor=W)

        back_button = Button(self.master, text='Back',font=('Geneva', 20), command=self.show_age_input_page)
        back_button.pack()

    def create_Age_group_three_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        age_group_label = Label(self.master, text = 'Welcome to Third Age Group!',font=('Arial', 22))
        age_group_label.pack()

        exercise_frame = Frame(self.master)
        exercise_frame.pack()

        exercise_label = Label(exercise_frame, text = 'Here are some recommended exercises:',font=('Arial', 21) )
        exercise_label.pack()

        exercise_list = [
           "Bodyweight squat",
           "Weighted squat",
           "Deadlift",
           "Push ups"
           "Bench Press",
           "Planks",
           "Side lunge w upright row"
        ]

        for exercise in exercise_list:
            exercise_item = Label(exercise_frame, text=f"- {exercise}", font=('Arial', 20))
            exercise_item.pack(anchor=W)

        back_button = Button(self.master, text='Back', font=('Gineva',14),command=self.show_age_input_page)
        back_button.pack()

    def create_Age_group_four_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        age_group_label = Label(self.master, text = 'Welcome to fourth Age Group!',font=('Arial', 22))
        age_group_label.pack()

        exercise_frame = Frame(self.master)
        exercise_frame.pack()

        exercise_label = Label(exercise_frame, text = 'Here are some recommended exercises:',font=('Arial', 21) )
        exercise_label.pack()

        exercise_list = [
            "Pushups",
            "Pull-ups",
            "Squats",
            "Reverse Lunges",
            "Glute Bridges",
            "Planks",
            "Quadruped Hold + Shoulder Tap"
        ]

        for exercise in exercise_list:
            exercise_item = Label(exercise_frame, text=f"- {exercise}", font=('Arial', 20))
            exercise_item.pack(anchor=W)

        back_button = Button(self.master, text='Back', font=('Gineva',14),command=self.show_age_input_page)
        back_button.pack()

    def create_Age_group_five_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        age_group_label = Label(self.master, text = 'Welcome to fifth Age Group!',font=('Arial', 22))
        age_group_label.pack()

        exercise_frame = Frame(self.master)
        exercise_frame.pack()

        exercise_label = Label(exercise_frame, text = 'Here are some recommended exercises:',font=('Arial', 21) )
        exercise_label.pack()

        exercise_list = [
            "Pushups",
            "Deadlifts",
            "Squats",
            "Side lungs",
            "Swimming",
            "Planks",
            "Cycling",
            "Walking"
        ]

        for exercise in exercise_list:
            exercise_item = Label(exercise_frame, text=f"- {exercise}", font=('Arial', 20))
            exercise_item.pack(anchor=W)

        back_button = Button(self.master, text='Back', font=('Gineva',14),command=self.show_age_input_page)
        back_button.pack()

    def create_Age_group_six_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        age_group_label = Label(self.master, text = 'Welcome to sixth Age Group!',font=('Arial', 22))
        age_group_label.pack()

        exercise_frame = Frame(self.master)
        exercise_frame.pack()

        exercise_label = Label(exercise_frame, text = 'Here are some recommended exercises:',font=('Arial', 21) )
        exercise_label.pack()

        exercise_list = [
            "Yoga",
            "Dancing",
            "Balance exercises",
            "Side lungs",
            "Swimming",
            "flexibilty exercises",
            "Cycling",
            "Walking or jogging"
        ]

        for exercise in exercise_list:
            exercise_item = Label(exercise_frame, text=f"- {exercise}", font=('Arial', 20))
            exercise_item.pack(anchor=W)

        back_button = Button(self.master, text='Back', font=('Gineva',14),command=self.show_age_input_page)
        back_button.pack()

    def create_Age_group_seven_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        age_group_label = Label(self.master, text = 'Welcome to the last Age Group!',font=('Arial', 22))
        age_group_label.pack()

        exercise_frame = Frame(self.master)
        exercise_frame.pack()

        exercise_label = Label(exercise_frame, text = 'Here are some recommended exercises:',font=('Arial', 21) )
        exercise_label.pack()

        exercise_list = [
            "Yoga",
            "Dancing",
            "Balance exercises",
            "Side lungs",
            "Swimming",
            "flexibilty exercises",
            "Cycling",
            "Walking or jogging",
            "Most of all good diet"
        ]

        for exercise in exercise_list:
            exercise_item = Label(exercise_frame, text=f"- {exercise}", font=('Arial', 20))
            exercise_item.pack(anchor=W)

        back_button = Button(self.master, text='Back', font=('Gineva',14),command=self.show_age_input_page)
        back_button.pack()

root = Tk()
app = GymChatbot(root)
root.mainloop()
    

