# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą 
# ir grąžins visus jo "values" list'e.

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

def showObjectKeys(input):
  new_array = []
  for key, value in input.items():
    new_array.append(value)
  return new_array

print(showObjectKeys(audi))