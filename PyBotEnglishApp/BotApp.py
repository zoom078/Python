import customtkinter
import pyautogui
import keyboard
import pyperclip
import pytesseract
from pynput import mouse
import time
from PIL import ImageGrab

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'
screenshot = pyautogui.screenshot(region=(x, y))
listener = mouse.Listener(on_click=choose_cords)
listener.start()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")

        self.button = customtkinter.CTkButton(self, text="Image to Text", command=self.image_to_text)
        self.button.pack(padx=20, pady=20)
        self.NewDoc = customtkinter.CTkButton(self, text="Open Dictionary", command=self.open_dict)
        self.NewDoc.pack(padx=30, pady=30)
        self.Coordinates = customtkinter.CTkButton(self, text="Choose Range", command=self.choose_cords)
        self.Coordinates.pack(padx=40, pady=40)

    def choose_cords(self, x, y, pressed):
        print("Click twice to define screenshot coordinates")
        if pressed:
            print("Mouse position: {x}, {y}")
            x = pyautogui.position()
            y = pyautogui.position()

    def open_dict(self):
        with open("PyBotEnglishApp/Dictionary.txt", "r") as f:
            f.read(10)
    
    def image_to_text(self):
        text = pytesseract.image_to_string(screenshot)
        if screenshot is None:
            print("No image found in clipboard.")
            return
        
        with open("PyBotEnglishApp/Dictionary.txt", "r") as f:
            f.write(text)



app = App()
app.mainloop()

