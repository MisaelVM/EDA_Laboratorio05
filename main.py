from mtree import MTree
import math

class Country:
	def __init__(self, name, x, y):
		self.name = name
		self.x = x
		self.y = y

def euclid_d(a, b):
	return math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)

def parse_line(line):
	country_data = line.split()
	coord = len(country_data) - 2
	x = float(country_data[coord])
	y = float(country_data[coord + 1])
	name = str(country_data[0])
	for i in range(1, coord):
		name += (' ' + country_data[i])
	return Country(name, x, y)

def main():	
	tree1 = MTree(euclid_d, max_node_size = 2)

	file1 = open('table1.txt', 'r')
	line = file1.readline()
	while line != '':
		country = parse_line(line)
		tree1.add(country)

		if country.name == 'North Macedonia' or country.name == 'Gibraltar' or country.name == 'USA':
			tree1.draw()

		line = file1.readline()
	file1.close()

	peru = Country('Peru', 66477, 5983)
	dist = 37000
	peru_query = tree1.search_in_range(peru, dist)
	print('PAÍSES MÁS PROXIMOS A PERÚ')
	print('Hay ' + str(len(peru_query)) + ' próximos a Perú bajo una distancia de ' + str(dist) + ':')
	for i in peru_query:
		print(i.name + ' en (' + str(i.x) + ', ' + str(i.y) + ') con ' + str(euclid_d(peru, i)))

	hungary = Country('Hungary', 114600, 3586)
	hungary_query = tree1.search(hungary)
	print("PAÍS MÁS PRÓXIMO DE HUNGARY")
	print("El país más próximo a Hungary es: ")
	for i in hungary_query:
		print(i.name + ' at (' + str(i.x) + ', ' + str(i.y) + ') with ' + str(euclid_d(peru, i)))

	tree2 = MTree(euclid_d, max_node_size = 2)

	file2 = open('table2.txt', 'r')
	line = file2.readline()
	while line != '':
		country = parse_line(line)
		tree2.add(country)
		line = file2.readline()
	file2.close()
	tree2.draw()


if __name__ == '__main__':
	main()
