#fifth project


# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task using match-case
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Note: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"'{task}' has an unknown priority level. Please check your input.")
#end






































                                                                                                                               [ Read 29 lines ]
^G Help           ^O Write Out      ^F Where Is       ^K Cut            ^T Execute        ^C Location       M-U Undo          M-A Set Mark      M-] To Bracket    M-B Previous      ◂ Back            ^◂ Prev Word      ^A Home           ^P Prev Line      M-▴ Scroll Up
^X Exit           ^R Read File      ^\ Replace        ^U Paste          ^J Justify        ^/ Go To Line     M-E Redo          M-6 Copy          ^B Where Was      M-F Next          ▸ Forward         ^▸ Next Word      ^E End            ^N Next Line      M-▾ Scroll Down

