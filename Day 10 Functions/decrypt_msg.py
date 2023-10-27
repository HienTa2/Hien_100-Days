from cryptography.fernet import Fernet

# The key used for encryption
key = b''  # Replace 'Your_Key_Here' with the actual key you used

# Encrypted message from the email
encrypted_message =  b'' # Replace with the actual encrypted message

# Initialize Fernet with the key
fernet = Fernet(key)

# Decrypt the message
decrypted_message = fernet.decrypt(encrypted_message)

# Decode the decrypted message to string
decrypted_message = decrypted_message.decode()

# Print the decrypted message
print(decrypted_message)
