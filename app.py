import tkinter as tk

# Membuat jendela utama
root = tk.Tk()
root.title("Contoh Tkinter")

# Menambahkan label
label = tk.Label(root, text="Halo, Tkinter!")
label.pack()

# Menjalankan loop utama
root.mainloop()