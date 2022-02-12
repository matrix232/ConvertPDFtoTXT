from tkinter import *
from tkinter import filedialog
import Convert


def callback():
    # Open file in new dialog window
    name = filedialog.askopenfilename()
    place_to_path.config(state="normal")
    place_to_path.delete(0, END)
    place_to_path.insert(0, name)
    place_to_path.config(state="readonly")


def conver():
    pdf_file = place_to_path.get()
    con = Convert.Converting(pdf_file)
    con.file_convert()
    place_to_path.config(state="normal")
    place_to_path.delete(0, END)
    place_to_path.insert(0, "CONVERTING SUCCESS!")
    place_to_path.config(state="readonly")


# Window
root = Tk()
root.title("File Converter")
root.maxsize(width=300, height=200)
root.minsize(width=300, height=200)
root['bg'] = "black"

select_path = Button(root, text='Select', font="Arial 15 bold",
                     fg="lime", bg="black", command=callback)

label = Label(root, text='Path to File: ', fg="lime", bg="black", font="Arial 15 bold")

place_to_path = Entry(width=40, state="readonly")
converting = Button(root, text="Convert File", font="Arial 15 bold",
                    fg="lime", bg="black", command=conver)

select_path.pack(pady=10)
label.pack()
place_to_path.pack(pady=10)
converting.pack(pady=10)

# Activation
root.mainloop()
