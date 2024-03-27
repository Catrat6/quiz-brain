import random
quiz_library = {
    "CS Quiz One": [
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "HTML stands for Hypertext Markup Language.",
            "correct_answer": "True",
            "incorrect_answers": "False"
        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "The Windows 7 operating system has six main editions.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "The Python programming language gets its name from the British comedy group 'Monty Python'",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "The logo for Snapchat is a Bell.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "Linus Torvalds created Linux and Git.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "RAM stands for Random Access Memory.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "The Windows ME operating system was released in the year 2000.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        }
    ],

    "Science and Nature Quiz": [
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science and Nature",
            "question": "An atom contains a nucleus.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science and Nature",
            "question": "Psychology is the science of behavior and mind.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science and Nature",
            "question": "Water always boils at 100&deg;C, 212&deg;F, 373.15K, no matter where you are.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science and Nature",
            "question": "An Astronomical Unit is the distance between Earth and the Moon.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science and Nature",
            "question": "An average human can go two weeks without water.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science and Nature",
            "question": "Not including false teeth; A human has two sets of teeth in their lifetime.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science and Nature",
            "question": "An exothermic reaction is a chemical reaction that releases energy by radiating electricity.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science and Nature",
            "question": "Celiac Disease is a disease that effects the heart, causing those effected to be unable to eat meat.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science and Nature",
            "question": "A plant that has a life cycle for more than a year is known as an annual.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science and Nature",
            "question": "Igneous rocks are formed by excessive heat and pressure.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        }
    ],
    "CS Quiz Two": [
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "Time on Computers is measured via the EPOX System.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "Linux was first created as an alternative to Windows XP.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "HTML stands for Hypertext Markup Language.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "The Windows ME operating system was released in the year 2000.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "Linus Torvalds created Linux and Git.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        }
    ],
    "Sports Quiz": [
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Sports",
            "question": "In association football, or soccer, a corner kick is when the game restarts after someone scores a goal.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Sports",
            "question": "There are a total of 20 races in Formula One 2016 season.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Sports",
            "question": "In Rugby League, performing a 40-20 is punished by a free kick for the opposing team.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Sports",
            "question": "Peyton Manning retired after winning Super Bowl XLIX.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Sports",
            "question": "Roger Federer is a famous soccer player.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        }
    ],

    "Geography Quiz": [
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Geography",
            "question": "Ottawa is the capital of Canada.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Geography",
            "question": "A group of islands is called an archipelago.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Geography",
            "question": "Tokyo is the capital of Japan.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Geography",
            "question": "Vatican City is a country.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Geography",
            "question": "St. Louis is the capital of the US State Missouri.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Geography",
            "question": "Greenland is almost as big as Africa.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Geography",
            "question": "Hungary is the only country in the world beginning with H.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Geography",
            "question": "The Republic of Malta is the smallest microstate worldwide.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Geography",
            "question": "There are no deserts in Europe.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Geography",
            "question": "Toronto is the capital city of the North American country of Canada.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        }
    ],

    "General Quiz": [
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "General Knowledge",
            "question": "Instant mashed potatoes were invented by Canadian Edward Asselbergs in 1962.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "General Knowledge",
            "question": "Francis Bacon died from a fatal case of pneumonia while he was attempting to preserve meat by stuffing a chicken with snow.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "General Knowledge",
            "question": "The average woman is 5 inches / 13 centimeters shorter than the average man.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "General Knowledge",
            "question": "The pickled gherkin was first added to hamburgers because a US health law required all fast-food to include a source of Vitamin C.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "General Knowledge",
            "question": "Coca-Cola original colour was green.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "General Knowledge",
            "question": "The term 'Spam' came before the food product 'Spam'.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "General Knowledge",
            "question": "The word news originates from the first letters of the 4 main directions on a compass (North, East, West, South).",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "General Knowledge",
            "question": "The British organisation CAMRA stands for The Campaign for Real Ale.",
            "correct_answer": "True",
            "incorrect_answers": "False"

        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "General Knowledge",
            "question": "The commercial UK channel ITV stands for 'International Television.'",
            "correct_answer": "False",
            "incorrect_answers": "True"

        },
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "General Knowledge",
            "question": "Albert Einstein had trouble with mathematics when he was in school.",
            "correct_answer": "False",
            "incorrect_answers": "True"

        }
    ]
}
