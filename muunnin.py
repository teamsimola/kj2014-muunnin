#!/usr/bin/env python

def kg_to_lbs(kg):
	return kg * 2.205
	
def lbs_to_kg(lbs):
	return lbs/2.205

def c_to_f(c):
	return c * 9.0/5.0 + 32

def f_to_c(f):
	return (f - 32) * 5.0/9.0
	
units = [
	[kg_to_lbs, lbs_to_kg],
	[c_to_f, f_to_c]
]

def menu_category():
	print("1) Paino")
	print("2) Lampotila")
	print("0) Poistu")
	return int(input("Valitse muunto: "))
	
def menu_unit(cat):
	if cat == 1:
		print("1) Kg -> Lbs")
		print("2) Lbs -> Kg")
	elif cat == 2:
		print("1) C -> F")
		print("2) F -> C")
	
	return int(input("Valitse yksikko: "))

def main():
	print("Tervetuloa Muuntimeen!")
	while True:
		choice = menu_category()
		if choice <= 0:
			break
		unit = menu_unit(choice)
		value = float(input("Syota arvo: "))
		print("Muunnettu arvo: " + str(round(units[choice - 1][unit - 1](value), 2)))


if __name__ == "__main__":
	main()
