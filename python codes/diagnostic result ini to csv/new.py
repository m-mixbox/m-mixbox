
import pandas as pd
input_path = 'D:\\xampp\\htdocs\\scripts\\reading data\\Report Jan2023 to Oct2023\\2D Echo\\ESTORE\\27_6_2023_11_4_39_172\\Exam.ini'
output_path = 'D:\\abc.csv'
values = []
with open(input_path, 'r') as f:
    line = f.read().split('\n')
    i=0
    for i in range(1,len(line)-1) :
        value =[]
        if(i!=7 and i!=6):
            [_,b] = line[i].split('=')
            value.append(b)
            print(i)
            print(value)
            values.append(value)
        i+=1   
    print(values)
dict = {}
header = [ 'ID','FIRST NAME','LAST NAME','DATE OF TEST','DATE OF BIRTH','GENDER']
for i in range(len(values)) :
    dict[header[i]] = values[i]

data = pd.DataFrame(dict)
#data.to_csv(output_path)
#print(data)
#with open(output_path, 'w') as f:
#    writer = csv.writer(f)
#    writer.writerows(enumerate(paragraphs))
#    print()