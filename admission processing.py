#hurray! longest code, although to be honest i had to look up on some codes to check how to get it running,
#making the questions run was hectic for me, i used about three days on it..... alhamduLilah sha.
#i'm thinking of a way to make it append the username and password to an empty so that i can create a class for login, but im unable to figure it out.

import question
from sys import exit


class Stage(object):

    def enter(self):
        print("This stage is not configured")
        exit(1)


class Engine(object):

    def __init__(self, stage_map):
        self.stage_map = stage_map

    def play(self):
        currrent_stage = self.stage_map.opening_stage()
        last_stage = self.stage_map.next_stage('aggregate')

        while currrent_stage != last_stage:
            next_stage_name = currrent_stage.enter()
            currrent_stage = self.stage_map.next_stage(next_stage_name)

        currrent_stage.enter()


class NEWAccount(Stage):

    def enter(self):
        self = print("""Welcome to the admiision processing centre!
        But firstly, you have to create an account.
        continue or exit""")

        action = input("> ")
        if action == "continue":
            print("Enter your desired username: ")
            username = input("> \n")
            if username == username:
                print("Choose a password: ")
                password = input("> \n")
                if password == password:
                    print("Input the password again: ")

                    renter = password
                    re = input("> \n")
                    res = 0

                    while re != password:
                        print("BZZZZEDDD, Incorrect input!")
                        res += 1
                        re = input("> \n")

                    if renter == password:
                        print("Account suceesfully created!")
                        print(f"""
                        Username = {username}
                        Password = {password}\n\n""")
                        return 'registration'
                    else:
                        print("Unrecognised action!")
                        return 'new_account'
                else:
                    print("Unrecognised action")
                    return 'new_account'
            else:
                print("Unrecognised action!")
                return 'new_account'
        elif action == "exit":
            print("Thanks for visiting the website.")
            exit(0)
        else:
            print("Unrecognised command!")
            return 'new_account'


class Registration(Stage):


    def enter(self):
        print("Input your Full name")
        response = input("> ")
        if response == response:
            print("Input your date of birth in this order dd/mm/yyyy")
            response = input("> ")
            if response == response:
                print("Input your state of origin")
                response = input("> ")
                if response == response:
                    print("Input your home address")
                    response = input("> ")
                    if response == response:
                        return 'institution'
                    else:
                        return 'registration'
                else:
                    return 'registration'
            else:
                return 'registration'
        else:
            return 'registration'


class Institution(Stage):

    def enter(self):
        universities = ["University Of Lagos", "University Of Ibadan",
        "University Of Ilorin", "University Of Jos",
        "University Of Benin", "Federal University Of Technology, Akure", 
        "Lagos State University", "Federal University Of Technology, Minna",
        "Ahmadu Bello University, Zaria", "Federal University Of Agriculture, Abeokuta"]

        uni_num = [num for num in range(1, len(universities)+1)]
        print("select a university")
        for num, university in zip(uni_num, universities):
            print(num, university)

        uni = int(input("> "))
        if int(uni) in uni_num:
            print(f"University: {universities[uni-1]}")
            print("Choose your desired Polytechnic from the list below")
            polytechnics = ["The Oke-Ogun Polytechnic, Saki", "The Polytechnic Ibadan", "Lagos State Polytechnic", \
                "Moshood Abiola Polytechnic", "The Ibarapa Polytechnic", "Auchi Polytechnic", "Gateway Polytechnic"]
            poly_num = [num for num in range(1,len(polytechnics)+1)]
            for num, poly in zip(poly_num, polytechnics):
                print(num, poly)

            poly = int(input("> "))
            if int(poly) in poly_num:
                print(f"Polytechnic: {polytechnics[poly-1]}")
                print("Choose your desired College of Education from the list")
                coes = ["Adeniran Ogunsanya College Of Education", "Adeniran Ogunsanya College Of Education",\
                        "Oyo State College Of Education", "Ondo State College Of Education"]
                coe_num = [num for num in range(1, len(coes)+1)]
                for num, coe in zip(coe_num, coes):
                    print(num, coe)
                coe = int(input("> "))
                if int(coe) in coe_num:
                    print(f"College of Education: {coes[coe-1]}")
                    print(
                        "Your choice of institution has been registered\n University: {}\n Polytechnic: \
                            {}\n College Of Education: {}".format(universities[uni - 1], polytechnics[poly -1], coes[coe-1]))
                    return 'wassce'
                else:
                    print("Invalid input! Enter a number")
                    return 'institution'
            else:
                print("Invalid input! Enter a number")                
                return 'institution'
        else:
            print("Invalid input! Enter a number")           
            return 'institution'


class Wassce(Stage):


    def enter(self):
        print("""Grading system
        A1 = 3.5
        B2 = 3.0
        B3 = 2.5
        C4 = 2.0
        C5 = 1.5
        C6 = 1.0""")
        print("Enter your grade in english: ")
        grades = ["A1", "B2", "B3", "C4", "C5", "C6"]
        grade = input("> ")
        if grade in grades:            
            print("Enter your grade in mathematics: ")
            grade = input("> ")
            if grade in grades:               
                print("Enter your third subject grade: ")
                grade = input("> ")
                if grade in grades:                    
                    print("Enter your fourth subject grade: ")
                    grade = input("> ")
                    if grade in grades:                          
                        print("Enter your fifth subject grade: ")
                        grade = input("> ")
                        if grade in grades:  
                            print("To proceed to the next stage input 'continue' or input 'exit' to quit.")
                            reply = input("> ")
                            if reply == "continue":
                                print("You are about to take your UTME test, input 'continue' to start or 'exit' to quit")
                                response = input("> ")
                                if response == "continue":
                                    return 'utme_question'
                                elif response == "exit":
                                    print("Thanks for visiting the website")
                                    exit(0)
                                else:
                                    print("oops! \nSession expired!")
                                    exit(0)
                            elif reply == "exit":
                                print("Thanks for visiting the website")
                                exit(0)
                            else:
                                print("oops! \nSession expired!")
                                exit(0)
                        else:
                            print("Error! Check your input or capitalize the letter if input is correct.")
                            return 'wassce'
                    else:
                        print("Error! Check your input or capitalize the letter if input is correct.")
                        return 'wassce'
                else:
                    print("Error! Check your input or capitalize the letter if input is correct.")
                    return 'wassce'
            else:
                print("Error! Check your input or capitalize the letter if input is correct.")
                return 'wassce'
        else:
            print("Error! Check your input or capitalize the letter if input is correct.")
            return 'wassce'

class UTMEQuestion(Stage):


    def enter(self):

        print("Best of luck!")
        print("\n\nUTME assessment test\n\n")

        quiz_questions = [
        """Question 1
        Choose the word or group of words that
        is MOST NEARLY OPPOSITE to the word in
        capital and that will, at the same time,
        correctly fill the gap in the sentences.
        People who are normally ..................often
        turn out to be DAUNTLESS heros in the face
        of real danger.
        <A> unsteady
        <B> colourless
        <C> cowardly
        <D> bashful
        <E> unfriendly
        >""",
        """Question 2 
        Choose the interpretation that you
        consider appropriate for the EXPRESSON IN
        CAPITAL in the following sentence.
        The men eventually gained their freedom
        and decided later to GET THEIR OWN BACK
        on their oppressors.
        <A> strike
        <B> have their revenge
        <C> abuse
        <D> get something
        <E> beat up
        >""",
        """Question 3 
        Choose the word or group of words that
        is nearest in meaning to the expression IN
        CAPITALS as it is used in the sentence
        My choice of a partner would be based on
        character not LOOKS
        <A> visibility
        <B> feasibility
        <C> appearance
        <D> stares
        <E> posture
        >""",
        """Question 4 
        Choose the word or group of words that
        is nearest in meaning to the expression IN
        CAPITALS as it is used in the sentence
        The girl has just come out of the fattening
        room and her waist is ADORNED with beads.
        <A> surrounded
        <B> decorated
        <C> besieged
        <D> defaced
        <E> bedraggled
        >""",
        """Question 5 
        Choose the word or group of words that
        best completes the following sentence .
        If she had known, she wouldn’t have come
        .........................
        <A> Would she?
        <B> Wasn’t it
        <C> Wouldn’t it
        <D> Couldn’t she?
        >""",
        """Question 6 
        Choose the word or group of words that
        best completes the following sentence .
        Salary cuts could be the
        ....................................... of the worker’s protest.
        <A> course
        <B> curse
        <C> cause
        <D> coarse
        >""",
        """Question 7 
        Choose the interpretation that you
        consider appropriate for this sentence.
        Despite their strangely unrefined behaviour,
        the foreigners were given preferential
        treatment. This means that the foreigners
        were.
        <A> ill – treated because of their coarseness
        <B> cautioned before they were attended to
        <C> well – treated despite the rudeness
        <D> not attended to because of their
        behaviour
        <E> sorry for their unrefined behaviour
        >""",
        """Question 8 
        If a*b = ab/b evaluate 2*(12*27)
        <A> 12
        <B> 9
        <C> 27
        <D> 2
        >""",
        """Question 9
        Convert 3310[base5] to base10
        <A> 611
        <B> 600
        <C> 606
        <D> 356 
        >""",
        """Question 10
        Convert 3.1415926 to 5 decimal places
        <A> 3.14160
        <B> 3.14159
        <C> 0.31415
        <D> 3.14200
        >""",
        """Question 11
        Express the product of 0.0014 and 0.011
        in standard form.
        <A> 1.54 X 104
        <B> 1.54 X 10-3
        <C> 1.54 X 10-4
        <D> 1.54 X 10-5
        >""",
        """Question 12
        The 4th term of an A. P is 13 while the
        10th term is 31. Find the 21st term.
        <A> 175
        <B> 85
        <C> 64
        <D> 45
        >""",
        """Question 13
        Why does government collect taxes?
        A. To spend on administration
        B. To spend on welfare programmes
        C. To spend on defence
        D. All of the above
        >""",
        """Question 14
        IAEA stands for:
        A. International Agency for Economic Affairs
        B. Institute of Arab-Economic Affairs
        C. International Atomic Energy Agency
        D. Institute for African Economic Advancement 
        >""",
        """Question 15
        Telephone and photo phone was invented by:
        A. Adri Marie
        B. Ark Wright
        C. Graham Bell
        D. None of these
        >""",
        """Question 16
        What is The Holiest Place on Earth
        for Muslims?
        A.Al - Kaaba
        B.Masjid Al Nabvi
        C.Masjid Al Aqsa
        D.Madinah
        >""",
        """Question 17
        Is a social science devoted to studying
        the production, distribution and consumption of wealth?
        A. Economics
        B. Political Science
        C. Sociology
        D. History
        >""",
        """Question 18
        Who is the current minister for education?
        A. Aisha Buhari
        B. Akinwunmi Ambode
        C. Chris Ngige
        D. Adamu Adamu
        >""",
        """Question 19
        What does LCD stands for?
        A. Liquid Crystal Display
        B. Latter Christ Dominion
        C. Luitenant Commandant Of Defense
        D. Land Charges Directorate.
        >""",
        """Question 20
        Two fair coins are tossed. The
        probability of at least one tail is
        <A> ¾
        <B> 2/3
        <C> ½
        <D> ¼
        >""",
        ]

        questions = [
            question.questions(quiz_questions[0], "b"),
            question.questions(quiz_questions[1], "b"),
            question.questions(quiz_questions[2], "c"),
            question.questions(quiz_questions[3], "b"),
            question.questions(quiz_questions[4], "a"),
            question.questions(quiz_questions[5], "c"),
            question.questions(quiz_questions[6], "c"),
            question.questions(quiz_questions[7], "d"),
            question.questions(quiz_questions[8], "c"),
            question.questions(quiz_questions[9], "b"),
            question.questions(quiz_questions[10], "d"),
            question.questions(quiz_questions[11], "c"),
            question.questions(quiz_questions[12], "d"),
            question.questions(quiz_questions[13], "c"),
            question.questions(quiz_questions[14], "c"),
            question.questions(quiz_questions[15], "a"),
            question.questions(quiz_questions[16], "a"),
            question.questions(quiz_questions[17], "d"),
            question.questions(quiz_questions[18], "a"),
            question.questions(quiz_questions[19], "ac")
        ]

        def run_test(questions):
            score = 0
            for question in questions:
                answer = input(question.prompt)
                if answer == question.answer:
                    score += 1

            print("You scored " + str(score) + "/" + str(len(questions)) + " correct.\n\n")

        run_test(questions)
        return 'putme_question'


class PUTMEQuestion(Stage):


    def enter(self):

        print("You are about to take Post UTME test, input 'continue' to start or 'quit' to exit.")
        start = input("> ")
        if start == "continue":

            print("Best of luck!\n")
            print("\n\nPost UTME assessment test.\n\n")

            prompt = [
            """Question 1
            Find the numeral in the base - ten
            system that represents the same number as
            the numeral 101101 in the base - two system
            <A> 44
            <B> 45
            <C> 40
            <D> 39
            >""",
            """Question 2
            Given the the number 243 in a base
            five system, find the nmber in the base - ten
            system that represents the same number.
            <A> 70
            <B> 73
            <C> 48
            <D> 85
            >""",
            """Question 3
            If x varies directly as y3 and x =2
            when y =1 , find x when y =5
            <A> 2
            <B> 10
            <C> 125
            <D> 250
            >""",
            """Question 4
            Choose the interpretation that you
            consider most appropriate for the sentence.
            Okon is too quite for my liking. This means
            that Okon
            <A> is liked because he is very quite
            <B> likes people who are quite
            <C> is not liked because of his extreme
            quietness
            <D> behaves in a very queer and suspicious
            manner
            >""",
            """Question 5 
            Choose the word or group of words that
            is MOST NEARLY OPPOSITE in meaning to the
            word in capital and that will, at the same time,
            correctly fill the gap in the sentence.
            Tayo was able to KINDLE the fire which my
            father had to .............. later
            <A> kill
            <B> switch
            <C> extinguish
            <D> destroy
            <E> ignite
            >""",
            """Question 6 
            Choose the word or group of words that
            best completes the following sentence .
            ........................................... inform her that I
            called.
            <A> when she comes back
            <B> after she phoned
            <C> as she was coming
            <D> when she arrived
            >""",
            """Question 7
            The candidates were told that passing the
            examination wasn’t a PASSPORT to getting an
            admission.
            <A> a guarantee
            <B> a suggestion in
            <C> an equivalent to
            <D> a necessity for
            <E> an intension for
            >""",
            """Question 8
            Which is the most famous place for playing tennis? 
            A. Old Trafford      
            B. Wimbledon      
            C. Thames       
            D. Lords
            >""",
            """Question 9
            Which is the official language of UAE? 
            A. English    
            B. Turkish  
            C. Persian    
            D. Arabic    
            >""",
            """Question 10
            The highest mountain in the world is?  
            A. Everest  
            B. K.2.   
            C. Kangchenjunga  
            D. Lhotse  
            >"""
            ]

            request = [
                question.request(prompt[0], "b"),
                question.request(prompt[1], "b"),
                question.request(prompt[2], "d"),
                question.request(prompt[3], "c"),
                question.request(prompt[4], "c"),
                question.request(prompt[5], "a"),
                question.request(prompt[6], "a"),
                question.request(prompt[7], "b"),
                question.request(prompt[8], "d"),
                question.request(prompt[9], "a"),
            ]

            def run_test(request):
                score = 0
                for question in request:
                    answer = input(question.prompt)
                    if answer == question.answer:
                        score += 1
                print("Total score" + str(score) + "/" + str(len(request)) + "\n\n")

            run_test(request)
        elif start == "quit":
            print("Thanks for visting the website!")
        else:
            print("Oops!\n Session Expired!")
            exit(0)
        return 'aggregate'


class Aggregate(Stage):


    def enter(self):
        print("Input UTME score: ")
        utme = float(input("> \n"))
        if utme == utme:
            print("Input Post UTME score: ")
            putme = float(input("> \n"))
            if putme == putme:
                print("Input WASSCE aggregate: ")
                wassce = float(input("> \n"))
                total = (((utme + putme + wassce) / 47.5) * 100)
                print(f"Total agrregate: {total}")
                if total >= 80:
                    print("""Congratulations!
                    You have been offered admission into your choice University!""")
                    exit(0)
                elif total >= 60:
                    print("""Congratulations!
                    You have been offered admission into your choice Polytechnic!""")
                    exit(0)
                elif total >= 40:
                    print("""Congratulations!
                    You have been offered admission into your choice College Of Education!""")
                    exit(0)
                else:
                    print("Your total aggregate is lower than the required.\n You are not offered admission!")
            else:
                return 'aggregate'
        else:
            return 'aggregate'



class Central(object):

    stages = {
        'new_account': NEWAccount(),
        'registration': Registration(),
        'institution': Institution(),
        'wassce': Wassce(),
        'utme_question': UTMEQuestion(),
        'putme_question': PUTMEQuestion(),
        'aggregate': Aggregate(),
    }

    def __init__(self, start_stage):
        self.start_stage = start_stage

    def next_stage(self, stage_name):
        val = Central.stages.get(stage_name)
        return val

    def opening_stage(self):
        return self.next_stage(self.start_stage)


a_central = Central('new_account')
a_caps = Engine(a_central)
a_caps.play()
