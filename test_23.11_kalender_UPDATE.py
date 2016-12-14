# todo:
# 1. Kuidas terve kalender saveda nii, et teinekord akent avades saaks failina (?) vana kalendri avada?


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# Source:# http://stackoverflow.com/questions/9348264/does-tkinter-have-a-table-widget
import calander
import tund
import labels
import task

# root = Tk()
import tkinter as tk

class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.t = EntryTable(self, 2)
        self.t.pack(side='left', fill='x')
        # Gets row and column values that correspond to the time and weekday. Returns list of int, [row, column].


class EntryTable(tk.Frame):
    def __init__(self, parent, columns=2):
        tk.Frame.__init__(self, parent, bg="white")
        self.parent = parent
        self.componentsFrame = ttk.Frame(self, padding="10 10 10 10")

        Label(self, text='1. Vali produktiivseim aeg töötamiseks: ', font='Sans 13 bold').grid(row=0, column=0, sticky=N + W)
        Label(self, text='Tööaja algus:').grid(row=1, column=0, sticky=N + W)
        self.päeva_algus = Entry(self)
        self.päeva_algus.configure(width=2)
        self.päeva_algus.grid(row=1, column=0, padx=100, sticky=N + W)
        Label(self, text='.00').grid(row=1, column=0, padx=(128, 0), sticky=N + W + S)

        Label(self, text='Tööaja lõpp:').grid(row=2, column=0, sticky=N + W)
        self.päeva_lõpp = Entry(self)
        self.päeva_lõpp.configure(width=2)
        self.päeva_lõpp.grid(row=2, column=0, padx=100, sticky=N + W)
        Label(self, text='.00').grid(row=2, column=0, padx=(128, 0), sticky=N + W + S)

        self.nupp_kellaajad = Button(self, text='Sisesta', width=25, command=self.callback)  # eelnevalt onButtonClicked
        self.nupp_kellaajad.grid(row=3, column=0, pady=(0, 30), sticky=N + W)

        # URLi sisestamine:
        Label(self, text='2. Sisesta URL-aadress: ', font='Sans 13 bold').grid(row=4, column=0, sticky=N + W)
        self.url = Entry(self)  # relief=RIDGE
        self.url.grid(row=5, column=0, sticky=N + W)
        self.url.configure(width=25)
        self.nupp_url = Button(self, text='Lisa kohustused', width=25, command=self.urlAdd)  # FIXME: URL?
        self.nupp_url.grid(row=6, column=0, pady=(0, 30), sticky=N + W)
        #
        # # Uue ülesande nimi:
        Label(self, text='3. Lisa uus ülesanne:', font='Sans 13 bold').grid(row=7, column=0, pady=5, sticky=N + W)  # FIXME: Tee boldiks
        Label(self, text='Nimi:').grid(row=8, column=0, sticky=N + W)
        self.ülesanne = Entry(self)
        self.ülesanne.grid(row=8, column=0, padx=55, sticky=N + W)

        # Uue ülesande ajakulu:
        Label(self, text='Ajakulu:').grid(row=9, column=0, sticky=N + W)
        self.ajakulu = Entry(self)
        self.ajakulu.configure(width=3)
        self.ajakulu.grid(row=9, column=0, padx=55, sticky=N + W)
        Label(self, text='minutites').grid(row=9, column=0, padx=(100, 0), columnspan=2, sticky=N + W + S)

        # Uue ülesande jagamine #FIXME: Kas drop menu või käsitsi sisestus?
        self.alg_tükeldamine = StringVar(self)
        self.alg_tükeldamine.set('Vali kordade arv:')
        Label(self, text='Töö tükeldamine:').grid(row=10, column=0, sticky=N + W)
        self.tükeldamine = OptionMenu(self, self.alg_tükeldamine, '1 kord', '2 korda', '3 korda', '4 korda',
                                      '5 korda', '6 korda')
        self.tükeldamine.grid(row=10, column=0, padx=(120, 0), sticky=N + W)

        # Mis päevaks?
        self.alg_tähtaeg = StringVar(self)
        self.alg_tähtaeg.set('Vali päev:')
        Label(self, text='Tähtaeg:').grid(row=11, column=0, sticky=N + W)
        self.tähtaeg = OptionMenu(self, self.alg_tähtaeg, 'Esmaspäev', 'Teisipäev', 'Kolmapäev',
                                  'Neljapäev', 'Reede', 'Laupäev', 'Pühapäev')
        self.tähtaeg.grid(row=11, column=0, padx=60, sticky=N + W)

        # Uue ülesande callback (lisamisnupp):
        self.nupp_uus = Button(self, width=10, text='Leia sobivad ajad',
                               command=self.onButtonClicked)  # command=self.lisa_ülesanne)
        self.nupp_uus.grid(row=12, column=0, sticky='nsew')

    def onButtonClicked(self): #FIXME: Kuidas SimpleTablesse tagastaks?
        # self.t.setWidgetBackground(rowColumn[0],rowColumn[1], "red")
        # self.t.set(rowColumn[0], rowColumn[1], "Nt,vabaaeg: 10:45-11:00")
        print("clicked button")
        task.Task.currentTask = task.Task(self.ülesanne.get(), int(self.ajakulu.get()), self.alg_tähtaeg.get(), int(self.alg_tükeldamine.get().split()[0]))
        for time in task.Task.currentTask.getTimesList():
            rowColumn = self.getRowColumn(time[1], time[0])
            if self.a.getLabelObject(rowColumn[0], rowColumn[1]).getLessonName() == "":
                self.a.setWidgetBackground(rowColumn[0], rowColumn[1], "#ff6666")
                #self.a.getLabelObject(rowColumn[0], rowColumn[1]).setTooltipText("TESTETST")
                self.a.getLabelObject(rowColumn[0], rowColumn[1]).setLessonName("Soovitatav aeg!")

    def urlAdd(self):
        print('ADD URL')
        calander.createEventList("http://www.is.ut.ee/pls/ois/ois.kalender?id_kalender=1175368736")
        self.a = SimpleTable(self.parent, int(float(self.päeva_algus.get())), int(float(self.päeva_lõpp.get())), 8)
        self.a.pack(side='right', fill='x')

    def callback(self):
        self.a = SimpleTable(self.parent, int(float(self.päeva_algus.get())), int(float(self.päeva_lõpp.get())), 8)
        self.a.pack(side='right', fill='x')

        for i in range(3, 8):
            self.a.columnconfigure(i, minsize=80, weight=1)
            i += 1
        self.a.columnconfigure(2, minsize=40, weight=1)
        '''
        self.kella_algus = int(float(self.päeva_algus.get()))
        self.kella_lõpp = int(float(self.päeva_lõpp.get()))
        print(self.kella_algus)
        print(self.kella_lõpp)

        if self.kella_lõpp > self.kella_algus and self.kella_lõpp in range(2, 25) and self.kella_algus in range(1, 24):
            return self.kella_algus, self.kella_lõpp #FIXME: Ei tagasta tegelikult miskit

        else:
            if self.kella_algus > self.kella_lõpp:
                messagebox.showwarning(title='Öö!', message='Proovi siis pigem ikka magada.')
            if self.kella_lõpp < self.kella_algus:  # tekita messagebox
                messagebox.showwarning(title='Vigane sisend!',
                                       message='Sisestatud tööaja algus on hilisem kui tööaja lõpp! Sule aken ja proovi uuesti. ')
            if self.kella_lõpp not in range(2, 25) and self.kella_algus not in range(2, 24):
                messagebox.showwarning(title='Vigane sisend!',
                                       message='Sisestatud tööaja algus ning sisestatud tööaja lõpp ei olnud ajavahemikus 1-24. Sule aken ja proovi uuesti!')
            if self.kella_lõpp not in range(2, 25) and self.kella_algus in range(1, 24):
                messagebox.showwarning(title='Vigane sisend!', message='Sisestatud tööaja lõpp ei ole vahemikus 2-24.')
            if self.kella_algus not in range(1, 24) and self.kella_lõpp in range(2, 25):
                messagebox.showwarning(title='Vigane sisend!', message='Sisestatud tööaja algus ei ole vahemikus 1-23.')
        '''

    def getRowColumn(self, time, weekday):
        # rows = 2 * (self.t.kella_lõpp - self.t.kella_algus)
        h, m = time.split(":")
        column = 2 + weekday  # Weekday int(1, 7)
        row = 0
        if m == "15":
            row = (int(h) - int(self.a.kella_algus)) * 2
        else:
            row = (int(h) - int(self.a.kella_algus)) * 2 + 1
        return [row + 2, column]  # +2 first row are weekend day labels
class SimpleTable(tk.Frame):
    def __init__(self, parent, kella_algus, kella_lõpp, columns=7):
        tk.Frame.__init__(self, parent, bg="#f4f4f2")

        calander.createEventList("http://www.is.ut.ee/pls/ois/ois.kalender?id_kalender=2065436593")

        self._widgets = []
        self.kella_algus = kella_algus  # int(input('Sisesta, mis kellast sinu tööpäev algab: ')) + 1
        self.kella_lõpp = kella_lõpp  # int(input('Sisesta, mis kellast sinu tööpäev lõppeb:')) + 1
        ridade_arv = abs(self.kella_lõpp - self.kella_algus) * 2 + 2
        i = 2
        for row in range(ridade_arv - 1):
            current_row = []
            for column in range(columns):
                if column != 0:
                    label = labels.Labels(self) # text='', borderwidth=0, width=8, bg="#a8a8a8")
                    #print(tund.Tund.tunnid)
                    for cls in tund.Tund.tunnid:
                        if cls.getWeekday() + 1 == column:
                            if cls.getTime() == str(self.kella_algus - 1) + ':15':
                                label = labels.Labels(self, cls.getLessonName(), cls.getTime(), cls.getLocation(),
                                                      cls.getDescription(), cls.getDate())
                                print(cls.getLessonName() + " " + str(self.kella_algus - 2) + ':15')
                else:
                    if row == 0 and column == 0:  # Kellaaegade üleval olev tühi kast.
                        label = tk.Label(self, text='', borderwidth=0, width=8)
                    elif self.kella_algus in range(self.kella_algus, self.kella_lõpp) and i % 2 == 0:
                        label = tk.Label(self, text=str(self.kella_algus) + '.15')
                        i += 1
                    elif self.kella_algus in range(self.kella_algus, self.kella_lõpp) and i % 2 != 0:
                        label = tk.Label(self, text=str(self.kella_algus) + '.45')
                        self.kella_algus += 1
                        i += 1
                label.grid(row=row, column=column, sticky="nsew", padx=0.5, pady=0.5)
                current_row.append(label)
            self._widgets.append(current_row)
            
        self.set(0, 0, '')
        self.set(0, 1, 'Esmaspäev')
        self.set(0, 2, 'Teisipäev')
        self.set(0, 3, 'Kolmapäev')
        self.set(0, 4, 'Neljapäev')
        self.set(0, 5, 'Reede')
        self.set(0, 6, 'Laupäev')
        self.set(0, 7, 'Pühapäev')


        print(self._widgets) #FIXME: Kas salvestame nii faili?

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

    # Retrives widget at certain location and modifies it's text attribute.
    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)

    # Same as set, but modifies bg attribute.
    def setWidgetBackground(self, row, column, bg):
        widget = self._widgets[row][column]
        widget.setBackgroundColor(bg)

    def getLabelObject(self, row, column):
        return self._widgets[row][column]

if __name__ == "__main__":
    app = Main()
    app.title('Ajaplaneerija')
    app.mainloop()
