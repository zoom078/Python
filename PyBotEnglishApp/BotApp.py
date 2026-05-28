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

        self.button = customtkinter.CTkButton(self, text="Start", command=self.button_callbck)
        self.button.pack(padx=20, pady=20)
        self.NewDoc = customtkinter.CTkButton(self, text="Open Dictionary", command=self.open_dict)
        self.NewDoc.pack(padx=30, pady=30)


    def button_callbck(self):
        print("button clicked")
    
    def open_dict(self):
        with open("PyBotEnglishApp/Dictionary.txt", "r") as f:
            f.read(10)
    
    def image_to_text():
        screenshot.save


app = App()
app.mainloop()

