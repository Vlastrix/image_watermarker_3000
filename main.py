from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont


# -----------------Watermarker 3000 Logic-------------------- #

def get_img():
    image_name = img_name.get()
    watermark_text = watermark_entry.get()
    try:
        if watermark_text == "":
            messagebox.showerror(title="The watermark text is empty!", message="Please specify the watermark text.")
        else:
            img_to_watermark = Image.open(image_name)
            watermark_img = img_to_watermark.copy()
            draw = ImageDraw.Draw(watermark_img)
            font_ = ImageFont.truetype("arial.ttf", 50)
            font_width, font_height = font_.getsize(watermark_text)
            new_width = (watermark_img.width - font_width) / 2
            new_height = (watermark_img.height - font_height) / 2
            draw.text((new_width, new_height), watermark_text, (0, 0, 0), font=font_)
            watermark_img.save(fp=f"Watermarked Images/Watermarked_{image_name}")
            img_name.delete(0, END)
            watermark_entry.delete(0, END)
            messagebox.showinfo(title="Success!", message="Watermarker 3000 watermarked your image successfully.")
    except FileNotFoundError:
        messagebox.showerror(title="File not found", message="File not found, please try again")


# -----------------Gui-------------------- #

window = Tk()
window.iconbitmap("Assets/amogus.ico")
window.title("Amogus Watermarker 3000")
window.config(pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Assets/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

img_label = Label(text="Image name:")
img_label.grid(column=0, row=1)

img_name = Entry(width=35)
img_name.grid(column=1, row=1, padx=5)

watermark_label = Label(text="Watermark text:")
watermark_label.grid(column=0, row=2)

watermark_entry = Entry(width=35)
watermark_entry.grid(column=1, row=2, padx=5)

submit_button = Button(text="Submit", width=10, command=get_img)
submit_button.grid(column=2, row=2)

window.mainloop()
