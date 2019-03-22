population={ 2, 3, 5, 1, 11, 10,}


print("_____________________ADD__________________________________")
countries={'china','india', 'usa','canada'}
countries.add('london')
print("Countries after adding london",countries)

countries.add('india')
countries.add('germany')
countries.add('france')
countries.add('spain')

print("Countries after  adding india",countries)


print("______________________FROZEN SET__________________________________")

mylist=['a','e','i','0','u']
print(mylist)
mylist=frozenset(mylist)
print("mylist after frozen: \n",mylist)

population= frozenset(population)
print("population set after frozen\n",population)
#population.add(50)

print("___________________DISCARD_________________________________")

print(countries)
countries.discard('china')
print("After discard china 1")
print(countries)
print("After discard china 2")
countries.discard('china')
print(countries)


print("___________________REMOVE___________________________________")
print(countries)
countries.remove('spain')
print("After remove spain 1")
print(countries)
print("After remove spain 2")
#countries.remove('spain')
print(countries)

print("___________________COPY__________________________________")

countries_backup=countries.copy()
print("Countries Set :        ",countries)
print("Countries BACKUP Set : ",countries_backup)
print("___________________CLEAR__________________________________")
countries.clear()

print("countries = ",countries)

