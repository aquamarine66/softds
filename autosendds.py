import pyautogui
import time
import random


def send_message_with_delay(message, delay_min=1, delay_max=3):
    pyautogui.typewrite(message)
    delay = random.uniform(delay_min, delay_max)
    time.sleep(delay)
    pyautogui.press("enter")
    print(f"Сообщение отправлено: '{message}' с задержкой {delay:.2f} сек.")


def load_messages_from_file(filename="messages.txt"):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            messages = [line.strip() for line in f if line.strip()]
        return messages
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []


# Coordinates to click (replace with your actual coordinates)
coordinates = [
    (389, 261),  # Example coordinates - replace these
    (1007, 269),
    (1693, 272),
    (397, 560),
    (1002, 560)
]

message_index = 0  # keep track of the current message to send

while True:
    time.sleep(54)
    messages_to_send = load_messages_from_file()
    if not messages_to_send:
        print("Нет сообщений для отправки.")
        time.sleep(60)
        continue

    num_messages = len(messages_to_send)
    num_coords = len(coordinates)

    for coord in coordinates:
        pyautogui.click(coord)
        time.sleep(random.uniform(0.5, 1.5))  # Short delay after each click

        message_to_send = messages_to_send[message_index % num_messages]  # Select message using message_index

        send_message_with_delay(message_to_send)

        message_index += 1  # Move to the next message

        time.sleep(random.uniform(1, 2))  # Delay between message cycles