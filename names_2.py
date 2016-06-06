users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryear'}
    ]
 }

for (arr,value) in users.items():
    print(str(arr))
    for i, row in enumerate(value):
        print("%d - %s - %d" % (i+1, (row['first_name'].upper() +" "+ row['last_name'].upper()), len(row['first_name'])+len('last_name')))
