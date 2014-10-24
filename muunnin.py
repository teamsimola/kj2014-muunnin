#!/usr/bin/env python
# -*- coding: utf-8 -*-

def kg_to_lbs(kg):
	return kg * 2.205
	
def lbs_to_kg(lbs):
	return lbs/2.205

def c_to_f(c):
	return c * 9.0/5.0 + 32

def f_to_c(f):
	return (f - 32) * 5.0/9.0

#meters to feet	added by teamsimola2.0 24.10 15:40
def m_to_f(m):
	return (m * 3.28084)

#feet to meters added by teamsimola2.0 24.10 15:40,updated menus
def f_to_m(f):
	return (f / 3.28084)
	
units = [
	[kg_to_lbs, lbs_to_kg],
	[c_to_f, f_to_c],
	[m_to_f, f_to_m]
]

def menu_category():
	print("1) Paino")
	print("2) Lämpötila")
	print("3) Pituus")
	print("0) Poistu")
	return int(input("Valitse muunto: "))
	
def menu_unit(cat):
	if cat == 1:
		print("1) Kg -> Lbs")
		print("2) Lbs -> Kg")
	elif cat == 2:
		print("1) C -> F")
		print("2) F -> C")
	elif cat == 3:
		print("1) m -> ft")
		print("2) ft -> m")
	
	return int(input("Valitse yksikkö: "))

def main():
	print("Tervetuloa Muuntimeen!")
	while True:
		choice = menu_category()
		if choice <= 0:
			break
		unit = menu_unit(choice)
		value = float(input("Syötä arvo: "))
		print("Muunnettu arvo: " + str(round(units[choice - 1][unit - 1](value), 2)))


if __name__ == "__main__":
	main()
