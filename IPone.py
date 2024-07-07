
import tkinter as tk
from tkinter import messagebox
import webbrowser
import os

def show_upgrade_confirmation(parent):
    """
    Show a confirmation popup when Upgrade button is clicked.
    """
    confirm_popup = tk.Toplevel(parent)
    confirm_popup.title("Upgrade Confirmation")
    confirm_popup.geometry("300x200")
    confirm_popup.configure(bg="#2d2d2d")

    label_confirm = tk.Label(confirm_popup, text="Do you want to buy this upgrade?", font=("Helvetica", 14, "bold"), bg="#2d2d2d", fg="#e3e3e3")
    label_confirm.pack(pady=20)

    def buy_upgrade():
        confirm_popup.destroy()
        parent.destroy()  # Ferme également la fenêtre principale si nécessaire
        # Insérez ici la logique pour acheter l'upgrade

    button_font = ("Helvetica", 12, "bold")
    button_style = {"bg": "#f55d32", "fg": "#FFFFFF", "relief": "flat", "padx": 15, "pady": 8, "bd": 0}

    button_buy = tk.Button(confirm_popup, text="BUY", command=buy_upgrade, font=button_font, **button_style)
    button_buy.pack(side="left", padx=20, pady=10)

    button_cancel = tk.Button(confirm_popup, text="CANCEL", command=confirm_popup.destroy, font=button_font, **button_style)
    button_cancel.pack(side="right", padx=20, pady=10)

    confirm_popup.transient(parent)  # Garde la fenêtre au-dessus de la fenêtre principale
    confirm_popup.grab_set()  # Empêche l'interaction avec d'autres fenêtres
    parent.wait_window(confirm_popup)  # Attente de la fermeture de la fenêtre de confirmation

def show_ip():
    """
    Create a popup window displaying the IP address with buttons for Discord, Twitch, and Connect.
    """
    ip = "192.168.1.10"  # Placeholder for IP address

    popup = tk.Tk()
    popup.title("IP.one")
    popup.geometry("400x600")
    popup.configure(bg="#1f1f1f")  # Dark background

    # Header label
    header = tk.Label(popup, text="IP.one", font=("Helvetica", 24, "bold"), bg="#1f1f1f", fg="#e3e3e3")
    header.pack(pady=20)

    # Create a frame to hold the widgets
    frame = tk.Frame(popup, bg="#1f1f1f", padx=20, pady=20)
    frame.pack(expand=True, fill="both")

    # Create a label to display the IP address
    label_ip = tk.Label(frame, text=f"Your IP address: {ip}", font=("Courier", 14, "bold"), bg="#1f1f1f", fg="#FFFFFF")
    label_ip.pack(pady=20)

    # Function to show a warning popup when Connect button is clicked
    def connect():
        messagebox.showwarning("Warning", "Do you really want to connect your PC to the program? (beta)")

    # Create category buttons
    button_font = ("Helvetica", 12, "bold")

    button_discord = tk.Button(frame, text="Discord", command=lambda: webbrowser.open("https://discord.gg/UF4Dhf6sHS"), font=button_font, bg="#f55d32", fg="#FFFFFF", relief="flat", padx=20, pady=10, bd=0)
    button_discord.pack(fill="x", pady=10)

    button_twitch = tk.Button(frame, text="Twitch", command=lambda: webbrowser.open("https://twitch.tv/dreamerskyy"), font=button_font, bg="#009e8e", fg="#FFFFFF", relief="flat", padx=20, pady=10, bd=0)
    button_twitch.pack(fill="x", pady=10)

    # Create a Connect button with bubble style
    connect_button_style = {"bg": "#1f1f1f", "fg": "#FFFFFF", "relief": "flat", "padx": 20, "pady": 10, "bd": 0}
    connect_button = tk.Button(popup, text="CONNECT", font=("Helvetica", 14, "bold"), command=connect, **connect_button_style)
    connect_button.pack(side="bottom", pady=10, fill="x")

    # Create an Upgrade button with bubble style
    upgrade_button_style = {"bg": "#f55d32", "fg": "#FFFFFF", "relief": "flat", "padx": 20, "pady": 10, "bd": 0}
    upgrade_button = tk.Button(popup, text="UPGRADE", font=("Helvetica", 14, "bold"), command=lambda: show_upgrade_confirmation(popup), **upgrade_button_style)
    upgrade_button.pack(side="bottom", pady=10, fill="x")

    popup.mainloop()

if __name__ == "__main__":
    show_ip()
