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
	"Paino",
	"Lampotila"
]

def menu():
	for i, u in enumerate(units):
		print(str(i + 1) + ") " + u)
	print("0) Poistu")
	return int(input("Valitse muunto: "))

def main():
	print("Tervetuloa Muuntimeen!")
	choice = 1
	while choice > 0:
		choice = menu()
		print(units[choice - 1] + " valittu")

if __name__ == "__main__":
	main()
