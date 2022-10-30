# Simple notepad that can create, open, save txt files and have few tools to edit text.
import tkinter
from turtle import width
from PIL import Image, ImageTk 
from tkinter import StringVar, IntVar, scrolledtext, END, messagebox, filedialog

# Define root widnow
root = tkinter.Tk()
root.title("Notepad")
root.iconbitmap("pad.ico")
root.geometry("600x600")
root.resizable(0,0)

# Define color and fonts
text_color = "#08090A"
sea_green = "#5DFDCB"
maya_blue = "#7cc6fe"
alice_blue = "#F4FAFF"
cool_gray = "#8789C0"
root.config(bg = maya_blue)

# Define functions
def change_font(event):
    if options_family.get() == "none":
        my_font =  (font_family.get(), font_size.get())
    else:
        my_font =  (font_family.get(), font_size.get(), options_family.get())

    input_text.config(font = my_font)

def new_note():
    question = messagebox.askyesno("New Note", "Are you sure you want to create a new note?")
    if question == 1:
        input_text.delete("1.0", END)

def close_note():
    question = messagebox.askyesno("Close Note", "Are you sure you want to close the Notepad?")
    if question == 1:
        root.destroy()

def save_note():
    # Use filedialog to get location a name where/what  to save the file as.
    save_name = filedialog.asksaveasfilename(initialdir= "./", title = "Save Note", filetypes= (("Text Files", "*.txt"), ("All Files", "*.*")))
    with open (save_name, 'w') as f:
        f.write(font_family.get() +  "\n")
        f.write(str(font_size.get()) + "\n")
        f.write(options_family.get() +  "\n")

        f.write(input_text.get("1.0", END))

def open_note():
    open_name = filedialog.askopenfilename(initialdir= "./", title= "Open Note", filetypes= (("Text Files", "*.txt"),("All Files", "*.*")))
    with open (open_name, 'r') as f:
        input_text.delete("1.0",END)

        font_family.set(f.readline().strip())
        font_size.set(int(f.readline().strip()))
        options_family.set(f.readline().strip())

        change_font(1)

        text = f.read()
        input_text.insert("1.0", text )
        

# Define layouts
# Define frames
buttons_frame = tkinter.Frame(root, bg = sea_green)
text_frame = tkinter.Frame(root, bg = alice_blue)
buttons_frame.pack(padx=5,pady=5)
text_frame.pack(padx=5,pady=5)

# layout for buttons frame
new_image = ImageTk.PhotoImage(Image.open("new.png"))
new_button = tkinter.Button(buttons_frame, image= new_image, bg = sea_green, activebackground=cool_gray, command= new_note)
new_button.grid(row=0,column=0,padx=5,pady=5)

open_image = ImageTk.PhotoImage(Image.open("open.png"))
open_button = tkinter.Button(buttons_frame, image= open_image, bg = sea_green, activebackground=cool_gray, command= open_note)
open_button.grid(row=0,column=1,padx=5,pady=5)

save_image = ImageTk.PhotoImage(Image.open("save.png"))
save_button = tkinter.Button(buttons_frame, image= save_image, bg = sea_green, activebackground=cool_gray, command= save_note)
save_button.grid(row=0,column=2,padx=5,pady=5)

close_image = ImageTk.PhotoImage(Image.open("close.png"))
close_button = tkinter.Button(buttons_frame, image= close_image, bg = sea_green, activebackground=cool_gray, command= close_note)
close_button.grid(row=0,column=3,padx=5,pady=5)

# Create a list of fonts to use
families = ["Terminal", "Modern", "Script", "Courier", "Arial", "Calibri", "Cambria", "Georgia", "MS Gothic", "SinSun", "Tahom", "Times New Roman", "Verdana", "Wingdings"]
font_family = StringVar()
font_family_drop = tkinter.OptionMenu(buttons_frame, font_family,*families, command= change_font)
font_family_drop.config(width=16, bg = sea_green, activebackground=cool_gray)
font_family_drop["menu"].config(bg = sea_green, activebackground=cool_gray)
font_family.set("Calibri")
font_family_drop.grid(row=0,column=4, padx=5,pady=5)

size = [8,10,12,14,16,20,24,32,48,64,72,96]
font_size = IntVar()
font_size_drop = tkinter.OptionMenu(buttons_frame, font_size,*size, command= change_font)
font_size_drop.config(width=3, bg = sea_green, activebackground=cool_gray)
font_size_drop["menu"].config(bg = sea_green, activebackground=cool_gray)
font_size.set(20)
font_size_drop.grid(row=0,column=5, padx=5,pady=5)

options = ["none", "bold", "italic"]
options_family = StringVar()
options_family_drop = tkinter.OptionMenu(buttons_frame, options_family,*options, command= change_font)
options_family_drop.config(width=6, bg = sea_green, activebackground=cool_gray)
options_family_drop["menu"].config(bg = sea_green, activebackground=cool_gray)
options_family.set("none")
options_family_drop.grid(row=0,column=6, padx=5,pady=5)

# Define text layout
my_font = (font_family.get(), font_size.get())
input_text = tkinter.scrolledtext.ScrolledText(text_frame,width = 1000, height=100, bg = alice_blue, font = my_font)
input_text.pack()


# Define widgets


# Root main loop
root.mainloop()