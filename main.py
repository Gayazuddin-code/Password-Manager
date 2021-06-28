from tkinter import *

FONT = ("Courier", 12, "bold")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
window.minsize(400, 400)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image((100, 100), image=img)
canvas.config(bg="white", highlightthickness=0)
canvas.grid(column=1, row=0)

website_label = Label()
website_label.config(text="Web Site:",
                     font=FONT,
                     bg="white", )
website_label.grid(column=0, row=1, pady=10)

website_input = Entry()
website_input.focus()
website_input.config(width=35)
website_input.grid(column=1, row=1, columnspan=2)

email_label = Label()
email_label.config(text="Email/Username:",
                   font=FONT,
                   bg="white", )
email_label.grid(column=0, row=2, pady=10)

email_input = Entry()
email_input.config(width=35)
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label()
password_label.config(text="Password:",
                      font=FONT,
                      bg="white", )
password_label.grid(column=0, row=3, pady=10)

password_input = Entry()
password_input.config(width=21)
password_input.grid(column=1, row=3)

generate_btn = Button()
generate_btn.config(text="Generate", width=10, bg="#e7305b")
generate_btn.grid(column=2, row=3)

add_btn = Button()
add_btn.config(text="Add",
               bg="#9bdeac",
               width=35)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
