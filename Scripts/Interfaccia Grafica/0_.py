import tkinter as tk

window = tk.Tk()
window.geometry("600x600")
window.title("Hello TkInter!")
window.resizable(False, False)

window.configure(background="white")
if __name__ == "__main__":
    window.mainloop()

