#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hillyerbrandtf
#
# Created:     24/08/2015
# Copyright:   (c) hillyerbrandtf 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import random
class Question:
    def __init__(self, question, answer, dummies):
        self.question = question
        self.answer = answer
        self.dummies = dummies
        self.set_answers()

    def set_answers(self):
        self.answers = self.dummies
        self.answers.insert(random.randrange(len(self.dummies) + 1), self.answer)

class Quiz:
    def __init__(self):
        self.questions = [Question("What is the capital of Mongolia?", "Ulan Bator", ["Vladivostok", "Astana","Lhasa"]), Question("Who wrote 'The Picture of Dorian Gray?","Oscar Wilde", ["George Bernard Shaw", "Evelyn Waugh", "Somerset Maugham"]), Question("What is the highest mountain in the world?","Mount Everest", ["K2", "Kangchenjunga", "Makalu"]), Question("Who is indisputably the most important person in Vault 101: He who shelters us from the harshness of the atomic wasteland, and to whom we owe everything we have, including our lives?","The Overseer", ["The Overseer", "The Overseer", "The Overseer"])]

    def take_quiz(self):
        for q in self.questions:
            print(q.question) # print the question
            for i in range(len(q.answers)): # print the possible answers
                print("\t" + str(i) + "\t" + q.answers[i])
            print()
            self.process_answer(q) # get answer from user and give appropriate response

    def process_answer(self, q):
        user_answer = -1
        while not 0 <= user_answer < len(q.answers):
            a = input("Please type the number of your answer here: ")
            try:
                user_answer = int(a) # if input is not an int we go to the except clause
                if not 0 <= user_answer < len(q.answers):
                    # input is not in range no further action is taken (the while loop will repeat)
                    print("\nThat was out of range\n")
                elif user_answer == q.answers.index(q.answer):
                    # input is equal to the index of the correct answer (the while loop will end)
                    print("\nWell Done!!\n")
                else:
                    # input not equal to the index of the correct answer (the while loop will end)
                    print("\nIncorrect, the answer is " + q.answer + "\n")
            except ValueError:
            # if user's input is not an int this executes (anticipating errors is good design!)
                print("\nThat was not a sensible input. Integers only please.\n")

#main routine
if __name__ == "__main__":
    text_quiz = Quiz()
    text_quiz.take_quiz()
