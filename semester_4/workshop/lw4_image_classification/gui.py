import tkinter as tk

import numpy as np
from PIL import Image, ImageDraw


class DigitDrawer:
    def __init__(self, model):
        self.model = model
        self.window = tk.Tk()
        self.window.title("MNIST Classifier")

        self.canvas = tk.Canvas(self.window, width=280, height=280, bg="white")
        self.canvas.pack()

        self.label = tk.Label(self.window, text="Draw a digit", font=("Arial", 16))
        self.label.pack()

        btn_frame = tk.Frame(self.window)
        btn_frame.pack()

        self.predict_btn = tk.Button(btn_frame, text="Predict", command=self.predict)
        self.predict_btn.pack(side=tk.LEFT)

        self.clear_btn = tk.Button(btn_frame, text="Clear", command=self.clear)
        self.clear_btn.pack(side=tk.LEFT)

        self.image = Image.new("L", (280, 280), 255)
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.draw_event)

    def draw_event(self, event):
        x, y = event.x, event.y
        self.draw.ellipse((x - 10, y - 10, x + 10, y + 10), fill=0)
        self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="black")

    def clear(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (280, 280), 255)
        self.draw = ImageDraw.Draw(self.image)
        self.label.config(text="Draw a digit")

    def predict(self):
        img = self.image.resize((28, 28))
        img_array = 255 - np.array(img)
        img_array = img_array.reshape(1, 784).astype(np.float32) / 255.0
        pred = self.model.predict(img_array)[0]
        self.label.config(text=f"Predicted: {pred}")

    def run(self):
        self.window.mainloop()
