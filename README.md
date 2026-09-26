# CyberGuard - Personal Security Toolkit

## Overview

CyberGuard is a desktop security-awareness toolkit built in Python. It brings
together three related ideas from cybersecurity and ethical hacking into one
interactive application:

1. **How weak everyday security habits actually are** (password strength and
   digital footprint hygiene)
2. **How two people can securely agree on a secret key over an insecure
   channel**, using the Diffie-Hellman key exchange, and then use that key to
   encrypt a real message
3. **How an attacker (Eve) could exploit weaknesses** in a password, a small
   Diffie-Hellman prime, or an unkeyed cipher, shown as live, working attacks

The three modules are connected: the key exchange in Module 2 produces the
same shared secret that Module 3 tries to recover through brute force,
showing concretely why key size and habit choices matter, not just in theory.

## Features

- **Password Strength Checker** - scores a password out of 5 based on
  length, uppercase, lowercase, digits, and symbols, and returns a
  plain-English verdict (Very Weak -> Very Strong)
- **Digital Footprint Questionnaire** - asks about common risky habits
  (password reuse, 2FA usage, public Wi-Fi, oversharing, updates) and
  produces an overall risk score and assessment
- **Diffie-Hellman Key Exchange** - user-supplied prime (validated for
  primality), base, and private keys; computes public keys and a shared
  secret for both parties independently
- **Caesar and Atbash Ciphers** - built with a shared `Cipher` base class
  and real inheritance/method overriding; the Diffie-Hellman shared secret
  is used directly as the Caesar cipher's key
- **Attack Simulator**
  - Brute-forces a password against a list of common weak passwords
  - Brute-forces a small Diffie-Hellman prime to recover a private key
  - Brute-forces all 26 possible Caesar shifts on a ciphertext
  - Decrypts an Atbash-ciphered message (Atbash requires no key to break)
- **Graphical interface** built with Python's `tkinter`/`ttk` - each module
  opens in its own window with entry fields, buttons, and live results

## Technologies / Tools Used

- Python 3
- `tkinter` and `tkinter.ttk` (GUI, built into standard Python, no install
  required)
- Core Python concepts only: functions, loops, conditionals, operators,
  lists, dictionaries, sets, classes, inheritance, method overriding, and
  modules/packages

## Project Structure

```
CyberGuard/
├── main.py                  # GUI entry point - the menu and all windows
├── primenumber.py           # is_prime(), mod_exp()
├── party_class.py           # Client class (Diffie-Hellman participant)
├── Ciphers.py                # Cipher, CaesarCipher, AtbashCipher
├── password_checker.py      # Password strength + digital footprint scoring
├── password_bruteforce.py   # Attack simulator functions
├── README.md
└── statement.md
```

## How to Install & Run

1. Make sure Python 3 is installed (`tkinter` ships with the standard
   Windows/Mac installers by default).
2. Download or clone this repository so that all `.py` files are in the
   same folder.
3. Open a terminal in that folder and run:
   ```
   python main.py
   ```
4. The CyberGuard main window will open. Click any of the four options to
   open that module in its own window.

## How to Use / Testing Instructions

- **Password & Digital Footprint Check**: enter a password and click
  "Check Strength" to see its score and verdict. Click "Run Digital
  Footprint Questionnaire" to answer the habit questions in the terminal
  and see a risk score.
- **Secure Key Exchange & Encryption**: choose a cipher, enter a prime
  number (it will be validated - try a non-prime like 24 to see the
  rejection), a base, two private keys, and a message, then click "Run Key
  Exchange" to see both public keys, both shared secrets (they should
  match), and the encrypted/decrypted message.
- **Attack Simulator**: try Attack 1 with a common password like
  `"password"` (should be found) versus something uncommon. For Attack 2,
  copy the `p`, `b`, and a public key from a Module 2 run and confirm the
  matching private key is recovered. For Attack 3, paste ciphertext from
  Module 2's Caesar output and confirm the correct key/message stands out
  among all 26 attempts. For Attack 4, paste Atbash-ciphered text to see it
  decrypted instantly (no key needed).

## Screenshots

_Add screenshots of each window in action here before submission._
