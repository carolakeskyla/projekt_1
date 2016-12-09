# todo:
# 1. kõik teised sildid, boxid, buttonid
# 2. paranda see, et esmaspäev algab õigest kohast ✓
# 3. vaata disaini üle 
# 4. paranda, et kellaajad algaksid, kasutajasisendi kellajast ✓

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#Source:# http://stackoverflow.com/questions/9348264/does-tkinter-have-a-table-widget
import calander
import tund
import labels

# root = Tk()
import tkinter as tk

class Main(tk.Tk):
    def __init__(self):
        calander.createEventList("http://www.is.ut.ee/pls/ois/ois.kalender?id_kalender=1175368736")
        tk.Tk.__init__(self)

        self.t = SimpleTable(self, 10)#Frame consisting grids

        self.t.pack(side="top", fill="x")
        self.t.set(0,0, 'kolumn_0')
        self.t.set(0, 1, 'kolumn_1')
        self.t.set(0, 2, '')
        self.t.set(0, 3, 'Esmaspäev')
        self.t.set(0, 4, 'Teisipäev')
        self.t.set(0, 5, 'Kolmapäev')
        self.t.set(0, 6, 'Neljapäev')
        self.t.set(0, 7, 'Reede')
        self.t.set(0, 8, 'Laupäev')
        self.t.set(0, 9, 'Pühapäev')
        
        self.initalizeComponents()

    def initalizeComponents(self):
        #Tööpäeva alguse ja lõpu küsimine:
        self.componentsFrame = ttk.Frame(self, padding="10 10 10 10")
        Label(self.t, text='Tööaja algus:').grid(row=1, column=0)
        self.päeva_algus = Entry(self.t)
        self.päeva_algus.grid(row=1, column=1)
        self.päeva_algus.configure(width=2)
        #Label(self.t, text='.00').grid(row=1, column=1, sticky=N+W+S, padx=30)

        Label(self.t, text='Tööaja lõpp:').grid(row=2, column=0, sticky=N+W)
        self.päeva_lõpp = Entry(self.t)
        self.päeva_lõpp.configure(width=2)
        self.päeva_lõpp.grid(row=2, column=1, sticky=N+W)
        #Label(text='.00').grid(row=3, column=0, sticky=N+W+S, padx=30)

        self.nupp_kellaajad = Button(self.t, text='Otsi aeg', width=10, command=self.onButtonClicked)
        self.nupp_kellaajad.grid(row=3, column=1, columnspan=2, sticky=N+W)

    #Some button...
    def onButtonClicked(self):
        rowColumn = self.getRowColumn("10:45", 5)
        self.t.setWidgetBackground(rowColumn[0],rowColumn[1], "red")
        self.t.set(rowColumn[0], rowColumn[1], "Nt,vabaaeg: 10:45-11:00")
        print("clicked button")

    #Gets row and column values that correspond to the time and weekday. Returns list of int, [row, column].
    def getRowColumn(self, time, weekday):
        #rows = 2 * (self.t.kella_lõpp - self.t.kella_algus)
        h,m = time.split(":")
        column = 2 + weekday #Weekday int(1, 7)
        row = 0
        if m == "15":
            row = (int(h) - int(self.t.kella_algus)) * 2
        else:
            row = (int(h) - int(self.t.kella_algus)) * 2 + 1
        return [row+2, column] #+2 first row are weekend day labels

class SimpleTable(tk.Frame):
    def __init__(self, parent, columns=7):
        tk.Frame.__init__(self, parent, bg="grey")
        self._widgets = []
        self.kella_algus = 9#int(input('Sisesta, mis kellast sinu tööpäev algab: ')) + 1
        self.kella_lõpp = 20#int(input('Sisesta, mis kellast sinu tööpäev lõppeb:')) + 1
        ridade_arv = abs(self.kella_lõpp - self.kella_algus) * 2 + 2
        i = 2
        for row in range(ridade_arv - 1):
            current_row = []
            for column in range(columns):
                if column != 2:
                    label = labels.Labels(self)#text='', borderwidth=0, width=8, bg="#a8a8a8")
                    # print(tund.Tund.tunnid)
                    for cls in tund.Tund.tunnid:
                        if cls.getWeekday() + 4 == column:
                            if cls.getTime() == str(self.kella_algus-1) + ':15':
                                label = labels.Labels(self, cls.getLessonName(), cls.getTime(), cls.getLocation(), cls.getDescription(), cls.getDate())
                                print(cls.getLessonName() + " " + str(self.kella_algus-2) + ':15')
                else:
                    if row == 0: #Kellaaegade üleval olev tühikast.
                        label = tk.Label(self, text='', borderwidth=0, width=8)
                    elif self.kella_algus in range(self.kella_algus, self.kella_lõpp) and i % 2 == 0:
                        label = tk.Label(self, text=str(self.kella_algus - 1) + '.15')
                        i += 1
                    elif self.kella_algus in range(self.kella_algus, self.kella_lõpp) and i % 2 != 0:
                        label = tk.Label(self, text=str(self.kella_algus - 1) + '.45')
                        self.kella_algus += 1
                        i += 1
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=0.5)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

    #Retrives widget at certain location and modifies it's text attribute.
    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)

    #Same as set, but modifies bg attribute.
    def setWidgetBackground(self, row, column, bg):
        widget = self._widgets[row][column]
        widget.configure(bg=bg)


if __name__ == "__main__":
    app = Main()
    app.mainloop()

#Juurdeõppimiseks:
# GRIDmanager = http://effbot.org/tkinterbook/grid.htm
# teised = http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
