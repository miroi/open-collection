#
# https://www.pythontutorial.net/tkinter/tkinter-hello-world/
#

import tkinter as tk


root = tk.Tk()

# place a label on the root window
message = tk.Label(root, text="Hello, World!")
message.pack()

# keep the window displaying
root.mainloop()
