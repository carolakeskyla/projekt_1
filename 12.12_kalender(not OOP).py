from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import calander
import tund
import labels

#TODO: Ajaplaneerija salvestamine
#TODO: Ajaplaneerija avamine
#TODO: Ajaplaneerijast kindla ülesande tühjendamine

master = Tk()

def tabel(päeva_algus, päeva_lõpp):
    #Vana tabeli ära kustutamine igal uuel väljakutsel #Abi: http://stackoverflow.com/questions/23189610/remove-widgets-from-grid-in-tkinter
    for label in master.grid_slaves():
        if int(label.grid_info()['column']) > 3:
                label.grid_forget()

    ridade_arv = int(abs(päeva_lõpp - päeva_algus) * 2 + 2)
    päeva_algus = päeva_algus + 1
    päeva_lõpp = päeva_lõpp + 1
    päevad = ['Esmaspäev', 'Teisipäev', 'Kolmapäev', 'Neljapäev', 'Reede', 'Laupäev', 'Pühapäev']

    rows = []
    for column in range(2, 10):
        cols = []
        i = 2
        for row in range(ridade_arv):
            if row == 0 and column in range(3, 11):
                Label(text=päevad[column - 3]).grid(row=0, column=column, sticky='nsew')
            else:
                if row != 0 and column != 2:
                    if row == ridade_arv and column == 10:
                        quit()
                    else:
                        label = Label(text='', borderwidth=0, width=13)
                        # print(tund.Tund.tunnid)
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

def callback():
    try:
        päeva_algus = int(float(kella_algus.get()))
        päeva_lõpp = int(float(kella_lõpp.get()))
    except ValueError:
        messagebox.showwarning(title='Vigane sisend!', message='Vigane väärtus')
    if päeva_lõpp > päeva_algus and päeva_lõpp in range(2,25) and päeva_algus in range(1,24):
        tabel(päeva_algus, päeva_lõpp)
    else:
        if päeva_algus > päeva_lõpp:
            messagebox.showwarning(title='Öö!', message='Proovi siis pigem ikka magada.')
        if päeva_lõpp < päeva_algus: #tekita messagebox
            messagebox.showwarning(title='Vigane sisend!', message='Sisestatud tööaja algus on hilisem kui tööaja lõpp! Sule aken ja proovi uuesti. ')
        if päeva_lõpp not in range(2, 25) and päeva_algus not in range(2, 24):
            messagebox.showwarning(title='Vigane sisend!', message='Sisestatud tööaja algus ning sisestatud tööaja lõpp ei olnud ajavahemikus 1-24. Sule aken ja proovi uuesti!')
        if päeva_lõpp not in range(2, 25) and päeva_algus in range(1, 24):
            messagebox.showwarning(title='Vigane sisend!', message='Sisestatud tööaja lõpp ei ole vahemikus 2-24.')
        if päeva_algus not in range(1, 24) and päeva_lõpp in range(2,25):
            messagebox.showwarning(title='Vigane sisend!', message='Sisestatud tööaja algus ei ole vahemikus 1-23.')

def get_url():
    sisestus = url.get()
    try:
        test = calander.createEventList(sisestus)  # FIXME: Not correct. Ajutine lahendus.
        tabel(päeva_algus, päeva_lõpp, test))
    except:
        messagebox.showwarning(title='Vigane URL-aadress!',
                               message='Sisestatud URL ei ole korrektne. Proovi uuesti!')

#Tööpäeva alguse ja lõpu küsimine:
Label(text='1. Vali produktiivseim aeg töötamiseks: ').grid(row=0, column=0, sticky=N+W)
Label(text='Tööaja algus:').grid(row=1, column=0, sticky=N + W)
kella_algus = Entry()
kella_algus.configure(width=2)
kella_algus.grid(row=1, column=0, padx=100, sticky=N + W)
Label(text='.00').grid(row=1, column=0, padx=130, sticky=N + W + S)

Label(text='Tööaja lõpp:').grid(row=2, column=0, sticky=N + W)
kella_lõpp = Entry()
kella_lõpp.configure(width=2)
kella_lõpp.grid(row=2, column=0, padx= 100, sticky=N + W)
Label(text='.00').grid(row=2, column=0, padx=130, sticky=N + W + S)

nupp_kellaajad = Button(text='Sisesta', width=25, command=callback)
nupp_kellaajad.grid(row=3, column=0, sticky=N + W)

# URLi sisestamine:
Label(text='2. Sisesta URL-aadress: ').grid(row=4, column=0, sticky=N+W)
url = Entry()  # relief=RIDGE
url.grid(row=5, column=0, sticky=N + W)
url.configure(width=25)
nupp_url = Button(text='Lisa kohustused', width=25, command=get_url)
nupp_url.grid(row=6, column=0,  sticky=N + W)

# Uue ülesande nimi:
Label(text='3. Lisa uus ülesanne:').grid(row=7, column=0, pady=5, sticky=N+W) #FIXME: Tee boldiks
Label(text='Nimi:').grid(row=8, column=0, sticky=N+W)
ülesanne = Entry()
ülesanne.grid(row=8, column=0, padx=55, sticky=N+W)

#Uue ülesande ajakulu:
Label(text='Ajakulu:').grid(row=9, column=0, sticky=N+W)
ajakulu = Entry()
ajakulu.configure(width=3)
ajakulu.grid(row=9, column=0, padx=55, sticky=N+W)
Label(text='tundi (0.5h kaupa)').grid(row=9, column=0, padx=100, sticky=N+W+S)

#Uue ülesande jagamine #FIXME: Kas drop menu või käsitsi sisestus?
alg_tükeldamine = StringVar(master)
alg_tükeldamine.set('Vali kordade arv:')
Label(text='Töö tükeldamine:').grid(row=10, column=0, sticky=N+W)
tükeldamine = OptionMenu(master, alg_tükeldamine, '1 kord', '2 korda', '3 korda', '4 korda',
                         '5 korda', '6 korda')
tükeldamine.grid(row=10, column=0, padx=120, sticky=N+W)

#Mis päevaks?
alg_tähtaeg = StringVar(master)
alg_tähtaeg.set('Vali päev:')
Label(text='Tähtaeg:').grid(row=11, column=0, sticky=N+W)
tähtaeg = OptionMenu(master, alg_tähtaeg, 'Esmaspäev', 'Teisipäev', 'Kolmapäev',
                     'Neljapäev', 'Reede', 'Laupäev', 'Pühapäev')
tähtaeg.grid(row=11, column=0, padx=60, sticky=N+W)

#Uue ülesande callback (lisamisnupp):
nupp_uus = Button(master, width=10, text='Leia sobivad ajad') #command=self.lisa_ülesanne)
nupp_uus.grid(row = 12, column=0, sticky='nsew')

mainloop()
