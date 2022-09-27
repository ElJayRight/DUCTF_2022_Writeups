dict = {}

#load data
with open(input("filename:\n> "), 'r') as f:
  for line in f:
    if line.startswith('}') or line.startswith('{'):
      pass
    else:
      a,b = line.strip().split('": "')
      a = a[1:]
      if a in dict:
        dict[a].append(b)
      else:
        dict[a] = [b]

#unique values over a field x
def values(x):
  for j in set(dict[x]):
    print(j+'\n')

#show headers
def headers():
  print("The Fields of the file are:")
  for i in dict:
    print('- '+i)

while True:
  options = '\n1. Show fields\n2. Show unique values of a given field'
  print(options)
  a = input("> ")
  if a.lower()=='exit':
    break
  if a=='1':
    headers()
  elif a=='2':
    print("Fields in the file: ")
    for j,i in enumerate(dict):
      print(i)
    values(input('Select a field > '))
