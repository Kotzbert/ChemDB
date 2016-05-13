
# -*- coding: utf-8 -*-
#!C:/Program Files (x86)/Python 3.5/python.exe

import sqlite3
import sys
import os
from tkinter import *





#search an item in the database
def get_value(**kwargs): #number of args variable
	###formatting of buttons states from tkinter into sql query___________________________________________
	formatted_values = ('*') # enter column names for values to be selected by SQL
	formatted_query= str('')
	buttons = {'O':2, 'C':4,'H':6}#dict is read backwards
	for value in buttons:#button needs to be dictionary like and will come from tkinter gui
		formatted_query = str(formatted_query + ' AND ' + value + '=\'' + str(buttons[value])+'\'')
	formatted_query = formatted_query[5:]
	print(formatted_query)

	###execution of SQL query___________________________________________
	connection = sqlite3.connect("Chemikalienliste.db")
	cursor = connection.cursor()
	query=r'''SELECT {0} FROM 'Chemikalien' WHERE {1};
	'''.format(formatted_values, formatted_query)
	print(query)

	#cursor.execute(query)#Befehl ausführen
	#connection.commit()#Befehl abschicken

def test():#test function for getting the dictionary data to work with the query
	formatted_query= str('')
	buttons = {'O':2, 'C':4,'H':6}#dict is read backwards
	for value in buttons:#button needs to be dictionary like and will come from tkinter gui
		print(value)
		print(buttons[value])
		formatted_query = str(formatted_query + ' AND \'' + value + '\'=\'' + str(buttons[value])+'\'')
	formatted_query = formatted_query[5:]
	print(formatted_query)

test()