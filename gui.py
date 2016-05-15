# -*- coding: utf-8 -*-

from Tkinter import *

def atoms():
	'''
	diese Funktion gibt die Anzahl vor, die für jedes Element ausgewählt werden kann.
	'''
	i=1
	number_of_atoms = []
	while i <= 50:
		number_of_atoms.append(str(i))
		i += 1
#	print(str(number_of_atoms)[1:-1])
	return(number_of_atoms)


element_list = ['H','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','He',
				'Li','Be','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','B','C','N','O','F','Ne',
				'Na','Mg','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','Al','Si','P','S','Cl','Ar',
				'K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr',
				'Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe',
				'Cs','Ba','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn',
				'Fr','Ra','Lr','Rf','Db','Sg','Bh','Hs','Mt','XX','XX','XX','XX','XX','XX','XX','XX','XX',
				'La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','XX','XX','XX','XX',
				'Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','XX','XX','XX','XX']

def ElementButton(element,x,y):
	'''
	Diese Funktion definiert die Buttons und ihre Position auf dem Grid.
	'''
	variable = StringVar(master)
	variable.set(element) # default value

	l = Label()
	w = OptionMenu(master, variable, *atoms())
	#das * ist notwendig, damit die Funktion funzt
	w.grid(column=x, row=y)


def sum_formula():
	print(variable.get())

def SearchButton():
	w = Button(master, text='Suche', command=sum_formula)
	w.grid(column=10, row=18)



#allg. Fenster Details
master = Tk()
master.title('ChemDB')
master.minsize(500,300)
#master.configure(bg = 'white')

x=1
y=1
for a in element_list:
	if a != 'XX':
		ElementButton(a,x,y)
	if x==18:
		y+=1
		x=1
	else:
		x +=1

SearchButton()















#functions
def callback():
	print('Ich liebe dich!')


#Labels
l = Label(master, text='Hallo Katharina')
#l.pack()


#Buttons
b = Button(master, text='weißt du was?', command=callback)
#b.pack()


master.mainloop()

