def setup():
    top = Tk()
    top.state('zoomed')

    C = Canvas(top)
    C.pack(fill="both", expand=True)

    img = Image.open("b1.png")
    top.update_idletasks()
    width, height = top.winfo_screenwidth(), top.winfo_screenheight()
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    filename = ImageTk.PhotoImage(img)
    C.create_image(0, 0, anchor="nw", image=filename)

    top.mainloop()