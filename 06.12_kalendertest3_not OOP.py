from tkinter import *
import calander
import tund

calander.createEventList("http://www.is.ut.ee/pls/ois/ois.kalender?id_kalender=643098256")
#FIXME: See ei tööta enam nii nagu eelmisel testil.

#Vasakpoolne kasutaja liides:
master = Tk()
#Tööpäeva alguse ja lõpu küsimine:
Label(text='Tööaja algus:').grid(row=0, column=0, columnspan=2, sticky=N+W)
päeva_algus = Entry()
päeva_algus.configure(width=2)
päeva_algus.grid(row=1, column=0, sticky=N+W)
Label(text='.00').grid(row=1, column=0, sticky=N+W+S, padx=30)

Label(text='Tööaja lõpp:').grid(row=2, column=0, sticky=N+W)
päeva_lõpp = Entry()
päeva_lõpp.configure(width=2)
päeva_lõpp.grid(row=3, column=0, columnspan=2, sticky=N+W)
Label(text='.00').grid(row=3, column=0, sticky=N+W+S, padx=30)

def callback():
    global kella_lõpp, kella_algus #FIXME: Globali kasutamine != hea. Teine variant on OOP, aga liiga keeruline.
    päeva_algus = int(float(kella_algus.get()))
    päeva_lõpp = int(float(kella_lõpp.get()))
    if päeva_lõpp > päeva_algus and päeva_lõpp in range(1,25) and päeva_algus in range(1,25):
        return päeva_algus, päeva_lõpp #FIXME callback ei ole väärtuse tagastamiseks. Kuidas
        # kellaaegu kätte saada? Kas peame tegema kahe aknana? Lugesin ja sain aru, et väärtust
        # saadakse ainult siis, kui aken kinni panna. Pole kindel ja uurin edasi.

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


### JÄRGNEV TEKITAB HETKEL VEEL KALENDRI ILMA ÜLEMISEST KOODIST SAADAVA INFOTA:

päeva_algus = int(input('Sisesta, mis kellast sinu tööpäevad sellel nädalal algavad: ')) + 1
päeva_lõpp = int(input('Sisesta, mis kellast sinu tööpäevad lõppevad:')) + 1
ridade_arv = int(abs(päeva_lõpp - päeva_algus) * 2 + 2)
päevad = ['Esmaspäev', 'Teisipäev', 'Kolmapäev', 'Neljapäev', 'Reede', 'Laupäev', 'Pühapäev']

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
                    label = Label(text='', borderwidth=0, width=13, relief=RIDGE)
                    print(tund.Tund.tunnid)
                    for cls in tund.Tund.tunnid:
                        if cls.getWeekday() + 4 == column:
                            if cls.getTime() == str(päeva_algus - 1) + ':15':
                                label = Label(self, text=cls.getLessonName())
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

mainloop()