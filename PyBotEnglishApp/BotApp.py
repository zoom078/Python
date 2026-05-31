import customtkinter
import pyautogui
import keyboard
import pyperclip
import pytesseract
from pynput import mouse
import time
import random
from PIL import ImageGrab

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.screenshot = None
        self.coordinates = []
        self.listener = None
        self.running = True

        self.button = customtkinter.CTkButton(self, text="Image to Text", command=self.image_to_text)
        self.button.pack(padx=20, pady=20)
        self.Coordinates = customtkinter.CTkButton(self, text="Choose Range", command=self.choose_cords)
        self.Coordinates.pack(padx=30, pady=30)
        self.LoopOn = customtkinter.CTkButton(self, text="Translate", command=self.translate)
        self.LoopOn.pack(padx=40, pady=40)
        self.LoopOff = customtkinter.CTkButton(self, text="Stop", command=self.stop_loop)
        self.LoopOff.pack(padx=50, pady=50)
        self.WriteDict = customtkinter.CTkButton(self, text="Write Dict", command=self.write_dict)

    def on_click(self, x, y, button, pressed):
        print("Click twice to define screenshot coordinates")
        if pressed:
            self.coordinates.append((x, y))
            print(f"Mouse position: {len(self.coordinates)}: {x}, {y}")
            if len(self.coordinates) == 2:
                self.listener.stop()
                print(f"Coordinates: {self.coordinates}")
                self.coordinates.sort()
                return False

    def choose_cords(self):
        self.coordinates = []
        self.listener = mouse.Listener(on_click=self.on_click)
        self.listener.start()

    def image_to_text(self):
        if len(self.coordinates) < 2:
            print("Please select the screenshot area first.")
            return
        x1, y1 = self.coordinates[0]
        x2, y2 = self.coordinates[1]
        left = min(x1, x2)
        right = max(x1, x2)
        top = min(y1, y2)
        bottom = max(y1, y2)
        
        while self.running:
            self.screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
            if self.screenshot is None:
                print("No screenshot taken")
                return
            text = pytesseract.image_to_string(self.screenshot)
            print(text)
            # with open ("PyBotEnglishApp/Dictionary.txt", "w") as f:
            #     f.write(text)

    def translate(self):
        with open ("PyBotEnglishApp/Dictionary.txt", "r") as f:
            text = f.read()
            pyautogui.write(text, interval=random.uniform(0.153, 0.276))

    def stop_loop(self):
        print("Stopping loop...")
        self.running = False

    def write_dict(self):
        with open ("PyBotEnglishApp/Dictionary.txt", "w") as f:
            f.write("This is a test")



app = App()
app.mainloop()

