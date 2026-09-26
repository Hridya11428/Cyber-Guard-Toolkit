from primenumber import mod_exp, is_prime
from Ciphers import CaesarCipher, AtbashCipher
from party_class import Client
from password_bruteforce import brute_force_password, brute_force_dh, brute_force_caesar
from password_checker import check_password_strength, get_password_score, risk_score_analyzer
import tkinter as tk
from tkinter import ttk

# ---------- Shared style settings ----------
BG_COLOR = "#1e2a38"
CARD_COLOR = "#2a3a4d"
ACCENT_COLOR = "#4caf7d"
TEXT_COLOR = "#f0f0f0"
FONT_TITLE = ("Segoe UI", 18, "bold")
FONT_HEADING = ("Segoe UI", 12, "bold")
FONT_NORMAL = ("Segoe UI", 10)
FONT_MONO = ("Consolas", 10)


def style_toplevel(win, title, size):
    win.title(title)
    win.geometry(size)
    win.configure(bg=BG_COLOR)


def section_label(parent, text):
    return tk.Label(parent, text=text, font=FONT_HEADING, bg=BG_COLOR, fg=ACCENT_COLOR)


def normal_label(parent, text):
    return tk.Label(parent, text=text, font=FONT_NORMAL, bg=BG_COLOR, fg=TEXT_COLOR)


def result_label(parent):
    return tk.Label(parent, text="", font=FONT_NORMAL, bg=BG_COLOR, fg="#8fd6a8",
                     wraplength=380, justify="left")


# ---------- MODULE 1: DIGITAL FOOTPRINT / PASSWORD HYGIENE ----------
def open_password_window():
    pw_window = tk.Toplevel(window)
    style_toplevel(pw_window, "Password & Digital Footprint Checker", "420x260")

    section_label(pw_window, "Password Strength Checker").pack(pady=(15, 5))
    normal_label(pw_window, "Enter a password to check:").pack(pady=(5, 2))

    password_entry = ttk.Entry(pw_window, width=32)
    password_entry.pack(pady=5)

    strength_result = result_label(pw_window)
    strength_result.pack(pady=10)

    def password_checker():
        password = password_entry.get()
        score = check_password_strength(password)
        verdict = get_password_score(score)
        strength_result.config(text=f"Strength: {verdict}  ({score}/5)")

    ttk.Button(pw_window, text="Check Strength", command=password_checker).pack(pady=5)

    ttk.Separator(pw_window, orient="horizontal").pack(fill="x", pady=15, padx=20)

    ttk.Button(pw_window, text="Run Digital Footprint Questionnaire",
               command=risk_score_analyzer).pack(pady=5)


# ---------- MODULE 2: DH KEY EXCHANGE & ENCRYPTION ----------
def open_key_exchange_window():
    key_window = tk.Toplevel(window)
    style_toplevel(key_window, "Secure Key Exchange & Encryption", "460x560")

    section_label(key_window, "Diffie-Hellman Key Exchange").pack(pady=(15, 10))

    cipher_choice = tk.StringVar(value="Caesar")
    cipher_frame = tk.Frame(key_window, bg=BG_COLOR)
    cipher_frame.pack(pady=5)
    normal_label(cipher_frame, "Choose a cipher:").pack(side="left", padx=5)
    tk.Radiobutton(cipher_frame, text="Caesar", variable=cipher_choice, value="Caesar",
                   bg=BG_COLOR, fg=TEXT_COLOR, selectcolor=CARD_COLOR).pack(side="left")
    tk.Radiobutton(cipher_frame, text="Atbash", variable=cipher_choice, value="Atbash",
                   bg=BG_COLOR, fg=TEXT_COLOR, selectcolor=CARD_COLOR).pack(side="left")

    def labeled_entry(text):
        normal_label(key_window, text).pack(pady=(8, 2))
        entry = ttk.Entry(key_window, width=32)
        entry.pack()
        return entry

    p_entry = labeled_entry("Enter a prime number (p):")
    b_entry = labeled_entry("Enter a base number (b):")
    alice_entry = labeled_entry("Alice's private key:")
    bob_entry = labeled_entry("Bob's private key:")
    message_entry = labeled_entry("Message to encrypt:")

    exchange_result = result_label(key_window)
    exchange_result.pack(pady=15)

    def run_exchange():
        p = int(p_entry.get())
        if not is_prime(p):
            exchange_result.config(text="That number is not prime. Please try again.", fg="#e07a7a")
            return

        b = int(b_entry.get())
        alice_private = int(alice_entry.get())
        bob_private = int(bob_entry.get())
        message = message_entry.get()

        alice = Client('Alice', alice_private)
        bob = Client('Bob', bob_private)

        alice_public = alice.compute_public_key(b, p)
        bob_public = bob.compute_public_key(b, p)

        alice_secret = alice.compute_shared_secret(bob_public, p)
        bob_secret = bob.compute_shared_secret(alice_public, p)

        if cipher_choice.get() == "Caesar":
            alice_cipher = CaesarCipher(alice_secret)
            bob_cipher = CaesarCipher(bob_secret)
        else:
            alice_cipher = AtbashCipher(alice_secret)
            bob_cipher = AtbashCipher(bob_secret)

        encrypted = alice_cipher.encrypt(message)
        decrypted = bob_cipher.decrypt(encrypted)

        result_text = (
            f"Alice's public key: {alice_public}\n"
            f"Bob's public key: {bob_public}\n"
            f"Alice's shared secret: {alice_secret}\n"
            f"Bob's shared secret: {bob_secret}\n"
            f"Encrypted message: {encrypted}\n"
            f"Bob's decrypted message: {decrypted}"
        )
        exchange_result.config(text=result_text, fg="#8fd6a8")

    ttk.Button(key_window, text="Run Key Exchange", command=run_exchange).pack(pady=10)


# ---------- MODULE 3: ATTACK SIMULATOR ----------
def open_attack_window():
    atk_window = tk.Toplevel(window)
    style_toplevel(atk_window, "Ethical Hacking Attack Simulator", "480x780")

    section_label(atk_window, "Attack Simulator").pack(pady=(15, 10))

    # --- Attack 1: weak password ---
    normal_label(atk_window, "Attack 1: Brute-force a weak password").pack(pady=(10, 2))
    pw_entry = ttk.Entry(atk_window, width=32)
    pw_entry.pack()
    result_1 = result_label(atk_window)
    result_1.pack(pady=5)

    def attack_password():
        target = pw_entry.get()
        found = brute_force_password(target)
        if found:
            result_1.config(text=f"Password '{target}' was found in the common list!", fg="#e07a7a")
        else:
            result_1.config(text=f"Password '{target}' was NOT found in the common list.", fg="#8fd6a8")

    ttk.Button(atk_window, text="Run Attack 1", command=attack_password).pack(pady=5)
    ttk.Separator(atk_window, orient="horizontal").pack(fill="x", pady=10, padx=20)

    # --- Attack 2: DH brute-force ---
    normal_label(atk_window, "Attack 2: Brute-force DH private key").pack(pady=(5, 2))
    dh_p_entry = labeled_short_entry(atk_window, "p (prime):")
    dh_b_entry = labeled_short_entry(atk_window, "b (base):")
    dh_pubkey_entry = labeled_short_entry(atk_window, "Known public key (e.g. Alice's):")
    result_2 = result_label(atk_window)
    result_2.pack(pady=5)

    def attack_dh():
        p = int(dh_p_entry.get())
        b = int(dh_b_entry.get())
        known_public = int(dh_pubkey_entry.get())
        key = brute_force_dh(b, p, known_public)
        result_2.config(text=f"Private key found: {key}")

    ttk.Button(atk_window, text="Run Attack 2", command=attack_dh).pack(pady=5)
    ttk.Separator(atk_window, orient="horizontal").pack(fill="x", pady=10, padx=20)

    # --- Attack 3: Caesar brute-force ---
    normal_label(atk_window, "Attack 3: Brute-force a Caesar-ciphered message").pack(pady=(5, 2))
    caesar_entry = ttk.Entry(atk_window, width=32)
    caesar_entry.pack()

    caesar_result_box = tk.Text(atk_window, height=9, width=42, font=FONT_MONO,
                                 bg=CARD_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR)
    caesar_result_box.pack(pady=8)

    def attack_caesar():
        ciphertext = caesar_entry.get()
        caesar_result_box.delete("1.0", tk.END)
        for key in range(26):
            cipher = CaesarCipher(key)
            attempt = cipher.decrypt(ciphertext)
            caesar_result_box.insert(tk.END, f"Key {key:2}: {attempt}\n")

    ttk.Button(atk_window, text="Run Attack 3", command=attack_caesar).pack(pady=5)
    ttk.Separator(atk_window, orient="horizontal").pack(fill="x", pady=10, padx=20)

    # --- Attack 4: Atbash decrypt ---
    normal_label(atk_window, "Attack 4: Decrypt an Atbash-ciphered message").pack(pady=(5, 2))
    atbash_entry = ttk.Entry(atk_window, width=32)
    atbash_entry.pack()
    result_4 = result_label(atk_window)
    result_4.pack(pady=5)

    def attack_atbash():
        ciphertext = atbash_entry.get()
        cipher = AtbashCipher(0)
        decrypted = cipher.decrypt(ciphertext)
        result_4.config(text=f"Atbash decrypted message: {decrypted}")

    ttk.Button(atk_window, text="Run Attack 4", command=attack_atbash).pack(pady=5)


def labeled_short_entry(parent, text):
    normal_label(parent, text).pack(pady=(6, 2))
    entry = ttk.Entry(parent, width=20)
    entry.pack()
    return entry


# ---------- MAIN MENU WINDOW ----------
window = tk.Tk()
window.title("CyberGuard - Personal Security Toolkit")
window.geometry("420x420")
window.configure(bg=BG_COLOR)

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=FONT_NORMAL, padding=8)
style.configure("TEntry", padding=4)

tk.Label(window, text="🛡  CyberGuard", font=FONT_TITLE, bg=BG_COLOR, fg=ACCENT_COLOR).pack(pady=(25, 5))
tk.Label(window, text="Personal Security Toolkit", font=FONT_NORMAL, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=(0, 25))

button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(pady=5)

ttk.Button(button_frame, text="1. Password & Digital Footprint Check",
           width=38, command=open_password_window).pack(pady=6)

ttk.Button(button_frame, text="2. Secure Key Exchange & Encryption",
           width=38, command=open_key_exchange_window).pack(pady=6)

ttk.Button(button_frame, text="3. Attack Simulator",
           width=38, command=open_attack_window).pack(pady=6)

ttk.Button(button_frame, text="4. Exit", width=38, command=window.destroy).pack(pady=6)

window.mainloop()