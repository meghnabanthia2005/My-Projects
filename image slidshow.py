from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image SlidShow")

#List of image path
image_paths = [
    r"c:\Users\banth\Downloads\images-1.jpg",
    r"c:\Users\banth\Downloads\images-2.jpg",
    r"c:\Users\banth\Downloads\images-3.jpg",
    r"c:\Users\banth\Downloads\images-4.jpg",
    r"c:\Users\banth\Downloads\images-5.jpg"
]

#Resize the images to 1080x1080
image_size=(1080,1080)
images=[Image.open(path).resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image = photo_image)
        label.update()
        time.sleep(3)
    
    
slidshow = cycle(photo_images)

def start_slidshow():
    for _ in range(len(image_paths)):
        update_image()
        
play_button = tk.Button(root, text = 'Play Slidshow', command = start_slidshow)
play_button.pack()

root.mainloop()