from django.shortcuts import render
import datetime
def home(request):
    example  = {'name': "i'm Soumick",
                'Main_course': 'python', 
                'id':101,
                'age': 24,
                'date': datetime.datetime.now(),
                'Time': datetime.datetime.now(),
                'num' : [1,2,3,4],
                'empty': " ",
                'string': "abcd",
                'String' : '<b>I</b> <button>love</button> <span>dogs</span>',
                'num_messages' : 3,
                'fileSize': 123456789,
                'list_of_list': ['soumick', 
                                    ['sajib', 
                                        ['zahid', 'rifat'], 
                                    'mahin'
                                    ]
                                ],
                'hobbies': ['learning','playing games','watch adventure movies'],
                'numbers' : """one
                            Two 
                            Three""",
                'Friends': [
                    {
                        'name': 'sajib',
                        'id': 101,
                        'Cp_rating': 1100
                    },
                    {
                        'name': 'Arafat',
                        'id': 102,
                        'Cp_rating': 1000
                    },
                    {
                        'name': 'mohabbot',
                        'id': 103,
                        'Cp_rating': 1300
                    }

                ]
                }
    return render(request, 'first_app/index.html',example)

