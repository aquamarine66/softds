import pyautogui
import time

def get_mouse_coordinates():
    """
    Получает и печатает текущие координаты мыши.
    """
    while True:
      try:
        x, y = pyautogui.position()
        print(f"Координаты мыши: x={x}, y={y}", end='\r') # Print with carriage return for overwriting old message
        time.sleep(0.1)  # Небольшая задержка для снижения нагрузки на процессор
      except KeyboardInterrupt:
         print("\nProcess Ended")
         break

if __name__ == "__main__":
    print("Наведите мышь на желаемое место и нажмите Enter")
    get_mouse_coordinates()