# from tkinter import *
#http://stackoverflow.com/questions/9348264/does-tkinter-have-a-table-widget

# root = Tk()
#
# height = 48
# width = 7
# for i in range(height): #Rows
#     for j in range(width): #Columns
#         b = Entry(root, text="")
#         b.grid(row=i, column=j)
#
# # You can grab the data by accessing the children of the grid and getting the values from there.
#
# mainloop()

import tkinter as tk
# http://stackoverflow.com/questions/11047803/creating-a-table-look-a-like-tkinter

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        t = SimpleTable(self, 8)
        t.pack(side="top", fill="x")
        t.set(0,0, '')
        t.set(0,1, 'Esmaspäev')
        t.set(0,2, 'Teisipäev')
        t.set(0,3, 'Kolmapäev')
        t.set(0,4, 'Neljapäev')
        t.set(0,5, 'Reede')
        t.set(0,6, 'Laupäev')
        t.set(0,7, 'Pühapäev')

class SimpleTable(tk.Frame):
    def __init__(self, parent, columns=7):
        # use black background so it "peeks through" to
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        kella_algus = int(input('Sisesta, mis kellast sinu tööpäev algab: '))
        kella_lõpp = int(input('Sisesta, mis kellast sinu tööpäev lõppeb:'))
        ridade_arv = abs(kella_lõpp - kella_algus) + 1
        for row in range(ridade_arv):
            current_row = []
            for column in range(columns):
                if column == 0:
                    if kella_algus in range(1, 10):
                        label = tk.Label(self, text='0' + str(kella_algus-1) + '.00')
                        kella_algus += 1
                    elif kella_algus in range(10, 24):
                        label = tk.Label(self, text=str(kella_algus-1) + '.00')
                        kella_algus += 1
                    # label = tk.Label(self, text='', borderwidth=0, width=7)
                else:
                    # label = tk.Label(self, text="%s/%s" % (row, column), borderwidth=0, width=7)
                    label = tk.Label(self, text='', borderwidth=0, width=8)

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
