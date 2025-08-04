import os
import ctypes
import webbrowser
import time
import platform
import winsound
import random
import tkinter as tk
from tkinter import messagebox
import ctypes.wintypes

# === Codes couleurs ANSI ===
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# === ASCII Art ===
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(MAGENTA + r"""
  FUN PACK
    """ + RESET)
    print(CYAN + "        >>> Bienvenue dans le FUN PACK TERMINAL <<<\n" + RESET)

# === Petit effet de chargement ===
def loading():
    print(CYAN + "Chargement du programme", end="")
    for _ in range(5):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print(RESET + "\n")

# === Fonctions originales ===
def open_cd_drive():
    if platform.system() == "Windows":
        ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
        print(GREEN + "Lecteur CD ouvert !" + RESET)

def close_cd_drive():
    if platform.system() == "Windows":
        ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)
        print(GREEN + "Lecteur CD fermé !" + RESET)

def speak(text):
    if platform.system() == "Windows":
        os.system(f'powershell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"')

def popup(message, title="Message", type_="info"):
    root = tk.Tk()
    root.withdraw()
    if type_ == "info":
        messagebox.showinfo(title, message)
    elif type_ == "warning":
        messagebox.showwarning(title, message)
    elif type_ == "error":
        messagebox.showerror(title, message)
    root.destroy()

def open_website(url):
    webbrowser.open(url)
    print(GREEN + f"Ouverture de {url}..." + RESET)

def flash_capslock(times=5, delay=0.2):
    if platform.system() == "Windows":
        for _ in range(times):
            ctypes.WinDLL("user32").keybd_event(0x14, 0, 0, 0)
            ctypes.WinDLL("user32").keybd_event(0x14, 0, 2, 0)
            time.sleep(delay)
        print(GREEN + "Clignotement du Caps Lock terminé !" + RESET)

def play_beep():
    if platform.system() == "Windows":
        winsound.Beep(1000, 500)
        print(GREEN + "Bip joué !" + RESET)

def change_wallpaper(image_path):
    if platform.system() == "Windows":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        print(GREEN + f"Fond d'écran changé en : {image_path}" + RESET)

def restart_pc():
    if platform.system() == "Windows":
        os.system("shutdown /r /t 5")

def shutdown_pc():
    if platform.system() == "Windows":
        os.system("shutdown /s /t 5")

# === Nouvelles fonctions ===
def shake_window(times=20, delay=0.05):
    if platform.system() == "Windows":
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        rect = ctypes.wintypes.RECT()
        ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
        width = rect.right - rect.left
        height = rect.bottom - rect.top
        x, y = rect.left, rect.top
        for _ in range(times):
            dx = random.randint(-10, 10)
            dy = random.randint(-10, 10)
            ctypes.windll.user32.MoveWindow(hwnd, x + dx, y + dy, width, height, True)
            time.sleep(delay)
        ctypes.windll.user32.MoveWindow(hwnd, x, y, width, height, True)
        print(GREEN + "Fenêtre secouée !" + RESET)

def flash_screen(times=10, delay=0.1):
    for _ in range(times):
        print("\033[7m" + " " * 80 + "\033[0m")
        time.sleep(delay)
        os.system('cls' if os.name == 'nt' else 'clear')
    print(GREEN + "Flash écran terminé !" + RESET)

def open_multiple_sites():
    sites = ["https://google.com", "https://youtube.com", "https://reddit.com", "https://openai.com", "https://github.com"]
    for site in sites:
        webbrowser.open(site)
    print(GREEN + "Plusieurs sites ouverts !" + RESET)

def spam_popups(times=10):
    for i in range(times):
        popup(f"Popup {i+1} !", "Spam Popup", "warning")
    print(GREEN + "Spam popup terminé !" + RESET)

def lock_pc():
    if platform.system() == "Windows":
        ctypes.windll.user32.LockWorkStation()
        print(GREEN + "Session verrouillée !" + RESET)

# === Menu ===
def menu():
    while True:
        print(BLUE + "\n=== MENU FUN PACK ===" + RESET)
        print(YELLOW + "1." + RESET + " Ouvrir le lecteur CD")
        print(YELLOW + "2." + RESET + " Fermer le lecteur CD")
        print(YELLOW + "3." + RESET + " Faire parler l'ordinateur")
        print(YELLOW + "4." + RESET + " Afficher un popup")
        print(YELLOW + "5." + RESET + " Ouvrir un site web")
        print(YELLOW + "6." + RESET + " Faire clignoter le Caps Lock")
        print(YELLOW + "7." + RESET + " Jouer un bip")
        print(YELLOW + "8." + RESET + " Changer le fond d'écran")
        print(YELLOW + "9." + RESET + " Redémarrer le PC")
        print(YELLOW + "10." + RESET + " Éteindre le PC")
        print(YELLOW + "11." + RESET + " Secouer la fenêtre")
        print(YELLOW + "12." + RESET + " Faire clignoter l'écran")
        print(YELLOW + "13." + RESET + " Ouvrir plusieurs sites")
        print(YELLOW + "14." + RESET + " Spam popups")
        print(YELLOW + "15." + RESET + " Verrouiller la session")
        print(RED + "0." + RESET + " Quitter")
        choix = input(CYAN + "\nChoisis une option : " + RESET)

        if choix == "1":
            open_cd_drive()
        elif choix == "2":
            close_cd_drive()
        elif choix == "3":
            text = input("Texte à dire : ")
            speak(text)
        elif choix == "4":
            msg = input("Message du popup : ")
            titre = input("Titre du popup : ")
            print("Type : 1.Info  2.Avertissement  3.Erreur")
            type_choice = input("Choisis le type (1/2/3) : ")
            types = {"1": "info", "2": "warning", "3": "error"}
            popup(msg, titre, types.get(type_choice, "info"))
        elif choix == "5":
            url = input("URL à ouvrir : ")
            open_website(url)
        elif choix == "6":
            flash_capslock()
        elif choix == "7":
            play_beep()
        elif choix == "8":
            path = input("Chemin de l'image : ")
            change_wallpaper(path)
        elif choix == "9":
            confirm = input("Es-tu sûr de vouloir redémarrer ? (o/n) : ")
            if confirm.lower() == "o":
                restart_pc()
        elif choix == "10":
            confirm = input("Es-tu sûr de vouloir éteindre ? (o/n) : ")
            if confirm.lower() == "o":
                shutdown_pc()
        elif choix == "11":
            shake_window()
        elif choix == "12":
            flash_screen()
        elif choix == "13":
            open_multiple_sites()
        elif choix == "14":
            spam_popups()
        elif choix == "15":
            lock_pc()
        elif choix == "0":
            print(RED + "Au revoir !" + RESET)
            break
        else:
            print(RED + "Option invalide !" + RESET)

if __name__ == "__main__":
    banner()
    loading()
    menu()
