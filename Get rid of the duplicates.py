student_data={'id1':
    {'name' : ['Sarah'],
     'class' : ['V'],
     'subject' : ['maths', 'english' ,'science']
     },
    'id2':
        {'name' :['Daniel'],
         'class' : ['V'],
         'subjects' : ['maths', 'english' ,'science']
         },
        'id3':
            {'name' :['Liam'],
             'class' :['V'],
             'subjects' :['maths', 'english' ,'science']
             },
            'id4':
                {'name' :['Matthew'],
                'class' :['V'],
                'subjects' :['maths', 'english' ,'science']
                },
                'id5':
            {'name' :['Liam'],
             'class' :['V'],
             'subjects' :['maths', 'english' ,'science']
             },
    }
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
        
print(result)