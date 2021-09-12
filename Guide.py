import tkinter as tk
from typing import Text


class Guide():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Guide")
        self.root.geometry("430x350")

    def guide(self):

        tk.Label(self.root, text=" - ", borderwidth=2, relief="groove").grid(row=0, column=0, padx=(15, 15), pady=(10, 10))
        tk.Label(self.root, text="Zoom in").grid(row=0, column=1)

        tk.Label(self.root, text=" + ", borderwidth=2, relief="groove").grid(row=1, column=0, padx=(15, 15), pady=(10, 10))
        tk.Label(self.root, text="Zoom out").grid(row=1, column=1)

        tk.Label(self.root, text="space", borderwidth=2, relief="groove").grid(row=2, column=0, padx=(15, 15), pady=(10, 10))
        tk.Label(self.root, text="Change image").grid(row=2, column=1)

        tk.Label(self.root, text="s", borderwidth=2, relief="groove").grid(row=3, column=0, padx=(15, 15), pady=(10, 10))
        tk.Label(self.root, text="Save image").grid(row=3, column=1)

        tk.Label(self.root, text="l", borderwidth=2, relief="groove").grid(row=4, column=0, padx=(15, 15), pady=(10, 10))
        tk.Label(self.root, text="Load saved coordinates from file load.txt").grid(row=4, column=1)

        tk.Label(self.root, text="t", borderwidth=2, relief="groove").grid(row=5, column=0, padx=(15, 15), pady=(10, 10))
        tk.Label(self.root, text="Save shape coordinates in load.txt").grid(row=5, column=1)

        tk.Label(self.root, text="r", borderwidth=2, relief="groove").grid(row=6, column=0, padx=(15, 15), pady=(10, 10))
        tk.Label(self.root, text="Rainbow").grid(row=6, column=1) 
        
        tk.Label(self.root, text="Close for start", borderwidth=2, relief="groove").grid(row=7, column=1, padx=(15, 15), pady=(10, 10))

        tk.Pack()        
        self.root.mainloop()