from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#http://stackoverflow.com/questions/9348264/does-tkinter-have-a-table-widget
import calander
import tund


# root = Tk()
import tkinter as tk

class ExampleApp(tk.Tk):
    def __init__(self):
        calander.createEventList("http://www.is.ut.ee/pls/ois/ois.kalender?id_kalender=643098256")
        tk.Tk.__init__(self)
        # silt = ttk.Label(self, text ='Sisesta URL: ')
        # silt.place(x=5, y=5)
        t = SimpleTable(self, 10)
        t.pack(side="top", fill="x")
        t.set(0,0, '')
        t.set(0,3, 'Esmaspäev')
        t.set(0,4, 'Teisipäev')
        t.set(0,5, 'Kolmapäev')
        t.set(0,6, 'Neljapäev')
        t.set(0,7, 'Reede')
        t.set(0,8, 'Laupäev')
        t.set(0,9, 'Pühapäev')
        

class SimpleTable(tk.Frame):
    def __init__(self, parent, columns=7):
        tk.Frame.__init__(self, parent, bg="white")
        self._widgets = []
        kella_algus = int(input('Sisesta, mis kellast sinu tööpäev algab: '))
        kella_lõpp = int(input('Sisesta, mis kellast sinu tööpäev lõppeb:')) + 1
        ridade_arv = abs(kella_lõpp - kella_algus) * 2 + 2
        i = 2
        for row in range(ridade_arv-1):
            current_row = []
            for column in range(columns):
                if column != 3:
                    label = tk.Label(self, text='', borderwidth=0, width=8)
                    #print(tund.Tund.tunnid)
                    for cls in tund.Tund.tunnid:
                        if cls.getWeekday()+4 == column:
                            if cls.getTime() == str(kella_algus-1) + ':15':
                                label = tk.Label(self, text=cls.getLessonName())
                                print(cls.getLessonName() + " " + str(kella_algus-1) + ':15')
                else:
                    if column == 3 and row == 0:
                        label = tk.Label(self, text='', borderwidth=0, width=8)
                    elif column != 3:
                        label = tk.Label(self, text='', borderwidth=0, width=8)
                        
                    elif kella_algus in range(kella_algus, kella_lõpp) and i % 2 == 0:
                        label = tk.Label(self, text= str(kella_algus-1) + '.15')
                        i += 1
                    elif kella_algus in range(kella_algus, kella_lõpp) and i % 2 != 0:
                        label = tk.Label(self, text=str(kella_algus - 1) + '.45')
                        kella_algus += 1
                        i += 1
                # else:
                #     # label = tk.Label(self, text="%s/%s" % (row, column), borderwidth=0, width=7)

                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=0.5)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)



if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()

#GRIDmanager = http://effbot.org/tkinterbook/grid.htm
# teised = http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm
