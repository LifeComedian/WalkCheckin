from modules.message_generator import generate_message
from modules.message_sender import send_to_pushplus

if __name__ == "__main__":
    message = generate_message()
    print(message)
    send_to_pushplus(message)
