
import os
import pandas as pd

location_of_files = []

path = r"D:\xampp\htdocs\scripts\ini to csv\Report Jan2023 to Oct2023\2D Echo\ESTORE"
output_path = 'D:\\abc.csv'
for root, dirs, files in os.walk(path):
	for file in files:
		if(file.endswith(".ini")):
			location_of_files.append(os.path.join(root,file))
#print(location_of_files)
values = []
for input_path in location_of_files :
	with open(input_path, 'r') as f:
		line = f.read().split('\n')
		i=0
		for i in range(1,len(line)-1) :
			value =[]
			if(i!=7 and i!=6):
				[_,b] = line[i].split('=')
				value.append(b)
				values.append(value)
			i+=1 
id = []
first_name =[]
last_name = []
test_date = []
dob = []
gender = []
i=0
j=1
k=2
l=3
m=4
n=5
for a in range (int(len(values)/6)):
	id.append(str(values[i]))
	first_name.append(str(values[j]))
	last_name.append(str(values[k]))
	test_date.append(str(values[l]))
	dob.append(str(values[m]))
	gender.append(str(values[n]))
	i+=6
	j+=6
	k+=6
	l+=6
	m+=6
	n+=6
#print(len(values))
data =[id,first_name,last_name,test_date,dob,gender]

dict = {}
header = [ 'ID','FIRST NAME','LAST NAME','DATE OF TEST','DATE OF BIRTH','GENDER']
for i in range(6) :
    dict[header[i]] = data[i]

df = pd.DataFrame(dict)
df.to_csv(output_path)

