months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(months)
print(months[3])
q3 = months[6:9]
print(q3)
print("_______________________________________________________________________________")
batches=['maths','science','computers','electronics','economics','politics','mechanics']

print("Batches:")
print(batches)
print("Length of batches list:",len(batches))
print("No of batches ",len(batches)+1)


batch_sizes = [65, 60, 89, 34, 25, 35,50]

print("\nBatchSizes :",batch_sizes)
print("max batch size is :",max(batch_sizes))
print("min batch size is :",min(batch_sizes))


print("______________________________________SIMPLE LIST__ count _index_______________________________________")


nationalities=['Canadian','British','Indian','American','Singaporean','Indian','Japanese','Chinese','Canadian','Indian','Chinese','Indian']
print("No of Indians: ",nationalities.count('Indian'))
print("No of Europian: ",nationalities.count('Europain'))
# to find the index of a element in the list
print("Index of British ",nationalities.index('British'))

print("______________________________________SIMPLE LIST________________append_________________________")

student_names=['viky','sam','bob','kim','john','fam','rami','mary']
print("Student Names:",student_names)
student_names.append("jimmi")
print("Student Names updated:",student_names)

print("\n____________________________________SIMPLE LIST________________insert________________________\n")

student_names.insert(0,'Henry')
student_names.insert(4,'Liam')
print("Student Names After insert:",student_names)

print("\n______________________________________SIMPLE LIST________________remove________________________\n")

student_names.remove('Henry')
print("Student Names After removal , Henry:",student_names)

student_names.insert(8,'Liam')
student_names.insert(6,'Liam')

student_names.remove('Liam')
print("Student Names After removal , Liam-1:",student_names)

student_names.remove('Liam')
print("Student Names After removal , Liam-2:",student_names)


print("\n______________________________________SIMPLE LIST________________pop________________________\n")

print("Student Names before pop():",student_names)
student_names.pop()

print("Student Names after pop():",student_names)

print("\n______________________________________SIMPLE LIST________________clear________________________\n")
student_names.clear()

print("Student Names After clear():",student_names)



print("\n______________________________________SIMPLE LIST________________extend________________________\n")

colors_1=['red','green','orange']
colors_2=['violet','indigo','blue','green']

colors_1.extend(colors_2)

print("color_1 list after extend:",colors_1)

print("color_1 list after extend:",colors_2)



print("\n______________________________________SIMPLE LIST________________sort________________________\n")

colors_1.sort()

print("color_1 list after sort:",colors_1)



print("\n______________________________________SIMPLE LIST________________PLUS________________________\n")

q1=['jan','feb','mar']
q2=['apr','may','jun']

semister=q1+q2
print("q1+q2 list after add:",semister)

print("\n______________________________________SIMPLE LIST________________JOIN________________________\n")

exampleList= ['Hello','World']

print(exampleList)
print('-'.join(exampleList))

numberslist=["one", "two", "three", "four","five"]
print("PRINT NUMBERS:")

num_str= "\n".join(numberslist)
print(num_str)