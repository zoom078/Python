import customtkinter
import pyautogui
import keyboard
import pyperclip
import pytesseract
from PIL import ImageGrab


screenshot = ImageGrab.grabclipboard()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")

        self.button = customtkinter.CTkButton(self, text="Image to Text", command=self.image_to_text)
        self.button.pack(padx=20, pady=20)
        self.NewDoc = customtkinter.CTkButton(self, text="Open Dictionary", command=self.open_dict)
        self.NewDoc.pack(padx=30, pady=30)



    def open_dict(self):
        with open("PyBotEnglishApp/Dictionary.txt", "r") as f:
            f.read(10)
    
    def image_to_text():
        text = pytesseract.image_to_string(screenshot)
        with open("PyBotEnglsihApp/Dictionary.txt", "r") as f:
            f.write(text)



app = App()
app.mainloop()

