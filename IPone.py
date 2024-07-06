import tkinter as tk
import webbrowser
import socket
import sys

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def open_discord():
    webbrowser.open("https://discord.gg/UF4Dhf6sHS")

def open_twitch():
    webbrowser.open("https://twitch.tv/dreamerskyy")

def show_ip():
    ip = get_ip_address()
    popup = tk.Tk()
    popup.title("IP.one")

    # Créer un cadre (frame) pour afficher le texte
    frame = tk.Frame(popup, padx=20, pady=20)
    frame.pack()

    # Créer une étiquette (label) pour afficher l'adresse IP
    label_ip = tk.Label(frame, text=f"Votre adresse IP : {ip}", font=("Arial", 12))
    label_ip.pack()

    # Créer un bouton pour Discord
    button_discord = tk.Button(frame, text="Discord", command=open_discord)
    button_discord.pack(side="left", padx=10)

    # Créer un bouton pour Twitch
    button_twitch = tk.Button(frame, text="Twitch", command=open_twitch)
    button_twitch.pack(side="left", padx=10)

    # Créer un bouton "Connecter" avec un avertissement
    def connecter():
        popup_connecter = tk.Toplevel(popup)
        popup_connecter.title("Avertissement")
        label_avertissement = tk.Label(popup_connecter, text="Voulez-vous vraiment connecter votre PC au programme ? (en bêta)")
        label_avertissement.pack()
        button_ok = tk.Button(popup_connecter, text="OK", command=popup_connecter.destroy)
        button_ok.pack()

    button_connecter = tk.Button(frame, text="Connecter", command=connecter)
    button_connecter.pack(side="left", padx=10)

    popup.mainloop()

if __name__ == "__main__":
    show_ip()
