state = ["West Bengal ","Orissa","TELANGANA","Uttar Pradesh","Madhya Pradesh","ANDHRA PRADESH","Odisha","Chhattisgarh",
"BIHAR",
"Maharashtra",
"Himachal Pradesh",
"Assam",
"Chattisgarh",
"Jharkhand",
"Tamil Nadu",
"Delhi",
"Chhatisgarh",
"Uttarakhand",
"MEGHALAYA"
]
for i in range(len(state)):
    text = '<option value="'+state[i]+'">'+state[i]+'</option>'
    print(text)