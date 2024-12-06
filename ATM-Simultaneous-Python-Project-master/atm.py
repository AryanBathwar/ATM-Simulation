import tkinter as tk
from tkinter import simpledialog, messagebox

# Data for users
users = {'user': {'pin': '1234', 'balance': 10000},
         'user2': {'pin': '2222', 'balance': 200000},
         'user3': {'pin': '3333', 'balance': 300000}}

current_user = None  # To track the logged-in user


# Function for login
def login():
    global current_user
    username = simpledialog.askstring("Login", "Enter Username:")
    if username and username.lower() in users:
        pin_attempts = 0
        while pin_attempts < 3:
            pin = simpledialog.askstring("PIN", "Enter PIN:", show="*")
            if pin == users[username.lower()]['pin']:
                current_user = username.lower()
                messagebox.showinfo("Success", f"Welcome, {username.capitalize()}!")
                main_menu()
                return
            else:
                pin_attempts += 1
                messagebox.showerror("Error", f"Invalid PIN. Attempts left: {3 - pin_attempts}")
        messagebox.showerror("Locked", "3 unsuccessful attempts. Your card is locked.")
    else:
        messagebox.showerror("Error", "Invalid Username")


# Main menu
def main_menu():
    def view_balance():
        balance = users[current_user]['balance']
        messagebox.showinfo("Balance", f"Your balance is {balance} Rupees")

    def withdraw():
        balance = users[current_user]['balance']
        amount = simpledialog.askinteger("Withdraw", "Enter amount to withdraw:")
        if amount is None:
            return
        if amount % 10 != 0:
            messagebox.showerror("Error", "Amount must match 10 Rupees notes.")
        elif amount > balance:
            messagebox.showerror("Error", "Insufficient balance.")
        else:
            users[current_user]['balance'] -= amount
            messagebox.showinfo("Success", f"Withdrawal successful. New balance: {users[current_user]['balance']} Rupees")

    def deposit():
        amount = simpledialog.askinteger("Deposit", "Enter amount to deposit:")
        if amount is None:
            return
        if amount % 10 != 0:
            messagebox.showerror("Error", "Amount must match 10 Rupees notes.")
        else:
            users[current_user]['balance'] += amount
            messagebox.showinfo("Success", f"Deposit successful. New balance: {users[current_user]['balance']} Rupees")

    def change_pin():
        old_pin = users[current_user]['pin']
        new_pin = simpledialog.askstring("Change PIN", "Enter new 4-digit PIN:", show="*")
        if not new_pin or len(new_pin) != 4 or not new_pin.isdigit():
            messagebox.showerror("Error", "PIN must be 4 digits.")
        elif new_pin == old_pin:
            messagebox.showerror("Error", "New PIN cannot be the same as the old PIN.")
        else:
            confirm_pin = simpledialog.askstring("Confirm PIN", "Re-enter new PIN:", show="*")
            if confirm_pin != new_pin:
                messagebox.showerror("Error", "PINs do not match.")
            else:
                users[current_user]['pin'] = new_pin
                messagebox.showinfo("Success", "PIN changed successfully.")

    def logout():
        global current_user
        current_user = None
        messagebox.showinfo("Logout", "You have successfully logged out.")
        app.quit()

    # Create the main menu window
    app = tk.Tk()
    app.title(f"ATM System - {current_user.capitalize()}")

    tk.Label(app, text="Welcome to the ATM System", font=("Arial", 14)).pack(pady=10)

    tk.Button(app, text="View Balance", command=view_balance, width=20).pack(pady=5)
    tk.Button(app, text="Withdraw", command=withdraw, width=20).pack(pady=5)
    tk.Button(app, text="Deposit", command=deposit, width=20).pack(pady=5)
    tk.Button(app, text="Change PIN", command=change_pin, width=20).pack(pady=5)
    tk.Button(app, text="Logout", command=logout, width=20).pack(pady=20)

    app.mainloop()


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    login()
