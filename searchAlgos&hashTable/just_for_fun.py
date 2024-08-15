car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

for x, y in car.items():
	if y == 'Ford':
		print('tapildi')
    