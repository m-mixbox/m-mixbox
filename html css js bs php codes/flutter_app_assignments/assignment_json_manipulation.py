import json 

data = json.load(open(r'D:\xampp\htdocs\scripts\html css js bs php codes\flutter_app_assignments\unacceptedAssignments.json'))
for i in data:
    #print(data[i])
    for k in data[i]:
        #print(k) // k variable
        #print(data[i][k]) // for data of k variable
        print('1') 