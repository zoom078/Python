import customtkinter
import pyautogui
import keyboard
import pyperclip
import pytesseract
from pynput import mouse
import time
import random
from PIL import ImageGrab
import threading

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.screenshot = None
        self.coordinates = []
        self.listener = None
        self.running = True
        self.dict_file = "PyBotEnglishApp/Dictionary.txt"
        self.dict_words = {}
        self.hotkeys = {
            'f1': self.image_to_text,
            'f2': self.choose_cords,
            'f3': self.stop_loop,
        }

        self.button = customtkinter.CTkButton(self, text="Image to Text", command=self.image_to_text)
        self.button.pack(padx=20, pady=20)
        self.Coordinates = customtkinter.CTkButton(self, text="Choose Range", command=self.choose_cords)
        self.Coordinates.pack(padx=30, pady=30)
        # self.LoopOn = customtkinter.CTkButton(self, text="Translate", command=self.translate)
        # self.LoopOn.pack(padx=40, pady=40)
        self.LoopOff = customtkinter.CTkButton(self, text="Stop", command=self.stop_loop)
        self.LoopOff.pack(padx=40, pady=40)
        # self.WriteDict = customtkinter.CTkButton(self, text="Write Dict", command=self.write_dict)

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
        # Screenshot area
        self.screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
        if self.screenshot is None:
            print("No screenshot taken")
            return
        text = pytesseract.image_to_string(self.screenshot).strip()
        print(text)
        # Translate text
        with open(self.dict_file, "r") as f:
            for line in f:
                words = line.strip().split()
                if len(words) == 2:
                    dutch, english = words
                    self.dict_words[dutch] = english

        pyautogui.write(text, interval=random.uniform(0.153, 0.276))
        time.sleep(1)


    def stop_loop(self):
        print("Stopping loop...")
        self.running = False

    def write_dict(self):
        with open (self.dict_file, "w") as f:
            for line in f:
                words = line.strip().split()
                if len(words) == 2:
                    dutch, english = words
                    self.dict_words[dutch] = english
        print("Working")

    def translation(self, word):
        word = word.strip()
        return self.dict_words.get(word, None)
    





app = App()
app.mainloop()

