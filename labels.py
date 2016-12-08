import tkinter as tk

class Labels(tk.Label):
    def __init__(self, frame, lessonName, time, location, description, date):
        tk.Label.__init__(self, frame, text=lessonName)
        self.time = time
        self.location = location
        self.description = description
        self.date = date
        self.bind("<Enter>", self.mouseEnter)
        self.bind("<Leave>", self.mouseLeave)
        self.bind("<Button-1>", self.mouseClick)
    def mouseEnter(self, event):
        print("Entered")
        x = y = 0
        x, y, cx, cy = self.bbox("insert")
        x += self.winfo_rootx() + 25
        y += self.winfo_rooty() + 20
        self.tw = tk.Toplevel(self)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.time + " " + self.date + "\n" + self.location + "\n" + self.description, justify='left',
                       background='yellow', relief='solid', borderwidth=1,
                       font=("times", "8", "normal"))
        label.pack(ipadx=1)

    def mouseLeave(self, event):
        print("Left")
        if self.tw:
            self.tw.destroy()
    def mouseClick(self, event):
        print("Clicked")