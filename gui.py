# -*- coding: utf-8 -*-

from Tkinter import *
import ttk
import re

def atoms():
	'''
	this function defines the maximum number of atoms to choose for each element
	'''
	i=0
	number_of_atoms = []
	while i <= 10:
		number_of_atoms.append(str(i))
		i += 1
#	print(str(number_of_atoms)[1:-1])
	return(number_of_atoms)


element_list = ['H','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','He',
				'Li','Be','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','B','C','N','O','F','Ne',
				'Na','Mg','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','Al','Si','P','S','Cl','Ar',
				'K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr',
				'Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe',
				'Cs','Ba','XX','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn',
				'Fr','Ra','XX','Rf','Db','Sg','Bh','Hs','Mt','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX','XX',
				'XX','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','XX','XX',
				'XX','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','XX','XX','XX']

def ElementButton(element,x,y):
	'''
	This function defines the buttons. every element has its own button. 
	atoms function defines how many atoms of that element can be selected.
	'''
	variable = StringVar(master)
	variable.set(element) # default value

	l = Label()
	w =OptionMenu(master, variable, *atoms())
	#das * ist notwendig, damit die Funktion funzt
	w.grid(column=x, row=y)
	#print(variable.get())
	return(variable)
	


def sum_formula():#prints all values of buttons that are digits
	pattern = r"[1-9]+" #regex for one or more digits
	for item in button_list:
		if re.match(pattern, button_list[item].get()): 
			print(item + ' : ' + button_list[item].get())
		else:
			pass

def SearchButton():
	w = Button(master, text='Suche', command=sum_formula)
	w.grid(column=10, row=18)



###GENERAL WORKFLOW

#general window details
master = Tk()
master.title('ChemDB')
master.minsize(500,300)
#master.configure(bg = 'white')



#button grid and creation of dictionary with key-value pairs for elements and atoms
button_list = {} # this needs to become a dictionary to get the element symbol for the button value!
x=1
y=1
i=0
for a in element_list:
	if a != 'XX':
		button_list.update({a:ElementButton(a,x,y)})
		i+=1
	if x==18:
		y+=1
		x=1
	else:
		x +=1

#print(button_list)

SearchButton()



master.mainloop()

