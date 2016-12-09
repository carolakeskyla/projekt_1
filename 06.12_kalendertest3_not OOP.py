#eraldi funktsiooni kalendri tegemine
#mis funktsioone kalender edasi kutsub?

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import calander
import tund
import labels

#Vasakpoolne kasutaja liides:
master = Tk()

def callback():
    calander.createEventList("http://www.is.ut.ee/pls/ois/ois.kalender?id_kalender=631121538")
    # FIXME: See ei tööta enam nii nagu eelmisel testil.

    päeva_algus = int(float(kella_algus.get()))
    päeva_lõpp = int(float(kella_lõpp.get()))
    if päeva_lõpp > päeva_algus and päeva_lõpp in range(1,25) and päeva_algus in range(1,25):
        ridade_arv = int(abs(päeva_lõpp - päeva_algus) * 2 + 2)
        päevad = ['Esmaspäev', 'Teisipäev', 'Kolmapäev', 'Neljapäev', 'Reede', 'Laupäev', 'Pühapäev']
        päeva_algus = päeva_algus + 1
        päeva_lõpp = päeva_lõpp + 1

        rows = []
        for column in range(2, 10):
            cols  = []
            i = 2
            for row in range(ridade_arv):
                if row == 0 and column in range(3, 11):
                    Label(text=päevad[column-3]).grid(row=0, column=column, sticky='nsew')
                else:
                    if row != 0 and column != 2:
                        if row == ridade_arv and column == 10:
                            quit()
                        else:
                            label = Label(text='', borderwidth=0, width=13)
                            print(tund.Tund.tunnid)
                            for cls in tund.Tund.tunnid:
                                if cls.getWeekday() + 4 == column:
                                    if cls.getTime() == str(päeva_algus - 1) + ':15':
                                        label = labels.Labels(master, cls.getLessonName(), cls.getTime(), cls.getLocation(),
                                                              cls.getDescription(), cls.getDate())
                                        print(cls.getLessonName() + " " + str(päeva_algus - 1) + ':15')
                    elif column == 2 and row == 0:
                        label = Label(text='', borderwidth=0, width=8)
                    elif päeva_algus in range(päeva_algus, päeva_lõpp) and i % 2 == 0:
                        label = Label(text=str(päeva_algus - 1) + '.15')
                        i += 1
                    else:
                        label = Label(text=str(päeva_algus - 1) + '.45')
                        päeva_algus += 1
                        i += 1
                label.grid(row=row, column=column, sticky=NSEW)
                cols.append(label)
            rows.append(cols)

#Tööpäeva alguse ja lõpu küsimine:
Label(text='Tööaja algus:').grid(row=0, column=0, columnspan=2, sticky=N+W)
kella_algus = Entry()
kella_algus.configure(width=2)
kella_algus.grid(row=1, column=0, sticky=N+W)
Label(text='.00').grid(row=1, column=0, sticky=N+W+S, padx=30)

Label(text='Tööaja lõpp:').grid(row=2, column=0, sticky=N+W)
kella_lõpp = Entry()
kella_lõpp.configure(width=2)
kella_lõpp.grid(row=3, column=0, columnspan=2, sticky=N+W)
Label(text='.00').grid(row=3, column=0, sticky=N+W+S, padx=30)

nupp_kellaajad = Button(master, text='Sisesta', width=10, command=callback)
nupp_kellaajad.grid(row=4, column=0, columnspan=2, sticky=N+W)

#URLi sisestamine:
Label(text='Sisesta URL-aadress: ').grid(row=5, column=0, sticky= 'nsew')
url = Entry() #relief=RIDGE
url.grid(row=6, column=0, columnspan=2, sticky=N+W)
nupp_url = Button(master, text='Lisa kohustused', command=...)
nupp_url.grid(row=7, column=0, columnspan=2, sticky=N+W)

#Uue ülesande sisendamine:
Label(text='Sisesta uue ülesande nimi: ').grid(row=8, column=0, sticky= 'nsew')
TEST2 = Entry()
TEST2.grid(row=9, column=0, columnspan=2, sticky=N + W)

mainloop()
