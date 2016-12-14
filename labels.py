import tkinter as tk
import task

class Labels(tk.Message):

    currentGreenColors = 0

    def __init__(self, frame, lessonName="", time="", location="", description="", date=""):
        tk.Message.__init__(self, frame, text=lessonName)
        self.lessonName = lessonName
        self.time = time
        self.location = location
        self.description = description
        self.date = date
        self.toolTipText = self.time + " " + self.date + "\n" + self.location + "\n" + self.description
        self.bgColor = "white"
        self.frame = frame
        self.bind("<Enter>", self.mouseEnter)
        self.bind("<Leave>", self.mouseLeave)
        self.bind("<Button-1>", self.mouseClick)
        self.tw = None

    def setBackgroundColor(self, color):
        self.bgColor = color
        self.configure(bg=color)


    def mouseEnter(self, event):
        if(self.lessonName == ""):
            return
        print("Entered")
        x = y = 0
        x, y, cx, cy = self.bbox("insert")
        x += self.winfo_rootx() + 25
        y += self.winfo_rooty() + 20
        self.tw = tk.Toplevel(self)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Message(self.tw, text=self.toolTipText, justify='left',
                       background='yellow', relief='solid', borderwidth=1,
                       font=("times", "8", "normal"))
        label.pack(ipadx=1)

    def mouseLeave(self, event):
        if self.lessonName != "" and self.tw != None:
            self.tw.destroy()
            print("Left")
    def mouseClick(self, event):
        if task.Task.currentTask != None:
            if(self.bgColor != "green"):
                Labels.currentGreenColors += 1
                self.bgColor = "green"
                self.configure(bg="green")
            else:
                Labels.currentGreenColors -= 1
                self.bgColor = "#f4f4f2"
                self.configure(bg="#f4f4f2")
            if task.Task.currentTask.getTimeSteps() <= Labels.currentGreenColors:
                for row in self.frame._widgets:
                    for column in row:
                        if type(column) is Labels:
                            if column.getBackgroundColor() == "green":
                                column.setBackgroundColor("#70db70")
                                t = int(task.Task.currentTask.getAjakulu()/task.Task.currentTask.getTimeSteps())
                                p = 30-t
                                if p < 0:
                                    p = 0
                                column.setTooltipText(str(t) + " minutit.\nLõpuaeg: " + task.Task.currentTask.getFinishTime() + "\nPuhkusaeg:" + str(p) + " minutut.")
                                column.setLessonName(task.Task.currentTask.getName())
                            if column.getBackgroundColor() == "#ff6666":
                                column.setBackgroundColor("#f4f4f2")
                                column.setLessonName("")
                task.Task.currentTask = None
                Labels.currentGreenColors = 0

        print("Clicked")

    def getLessonName(self):
        return self.lessonName

    def setTooltipText(self, text):
        self.toolTipText = text
        print(text)

    def setLessonName(self, name):
        self.lessonName = name
        self.configure(text=name, width=100)

    def getBackgroundColor(self):
        return self.bgColor
