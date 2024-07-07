
import tkinter as tk
from tkinter import messagebox
import webbrowser
import socket

def get_ip_address():
    """
    Retrieve the IP address of the current machine.
    """
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def open_discord():
    """
    Open the Discord invite link in the web browser.
    """
    webbrowser.open("https://discord.gg/UF4Dhf6sHS")

def open_twitch():
    """
    Open the Twitch channel link in the web browser.
    """
    webbrowser.open("https://twitch.tv/dreamerskyy")

def show_ip():
    """
    Create a popup window displaying the IP address with buttons for Discord, Twitch, and Connect.
    """
    ip = get_ip_address()
    popup = tk.Tk()
    popup.title("IP.one")
    popup.geometry("400x600")
    popup.configure(bg="#0A0A0A")  # Dark background

    # Create a frame to hold the widgets
    frame = tk.Frame(popup, bg="#0A0A0A", padx=20, pady=20)
    frame.pack(expand=True)

    # Create a label to display the IP address
    label_ip = tk.Label(frame, text=f"Votre adresse IP : {ip}", font=("Courier", 14, "bold"), bg="#0A0A0A", fg="#00FF00")
    label_ip.pack(pady=20)

    # Function to show a warning popup when Connect button is clicked
    def connecter():
        messagebox.showwarning("Avertissement", "Voulez-vous vraiment connecter votre PC au programme ? (en bêta)")

    # Create category buttons
    button_font = ("Courier", 12, "bold")
    button_style = {"bg": "#333333", "fg": "#00FF00", "relief": "flat", "padx": 5, "pady": 10}

    button_discord = tk.Button(frame, text="Discord", command=open_discord, font=button_font, **button_style)
    button_discord.pack(fill="x", pady=5)

    button_twitch = tk.Button(frame, text="Twitch", command=open_twitch, font=button_font, **button_style)
    button_twitch.pack(fill="x", pady=5)

    # Function to show an error message when Upgrade button is clicked
    def show_error():
        messagebox.showerror("Erreur", "Une erreur est survenue lors de la mise à niveau.")

    # Create an Upgrade button
    upgrade_button = tk.Button(popup, text="UPGRADE", font=("Courier", 14, "bold"), bg="#FFFF00", fg="#333300", relief="flat", padx=20, pady=10, command=show_error)
    upgrade_button.pack(side="bottom", pady=20, fill="x")

    popup.mainloop()

if __name__ == "__main__":
    show_ip()
