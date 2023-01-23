import datetime
import sys
# Random module to show quiz question in random order
import random

# factory method to create a question object based on the type

class Quiz:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.questions = []
        self.score = 0
        self.correct_count = 0
        self.total_points = 0
        # TODO: define a completion time property
        self.completion_time = 0

    def print_header(self):
        print("\n\n*******************************************")
        print(f"QUIZ NAME: {self.name}")
        print(f"DESCRIPTION: {self.description}")
        print(f"QUESTIONS: {len(self.questions)}")
        print(f"TOTAL POINTS: {self.total_points}")
        print("*******************************************\n")

    def print_results(self, quiztaker, thefile=sys.stdout):
        # flush = True forces the print to be written to the file right away
        print("*******************************************",
              file=thefile, flush=True)
        # TODO: print the results
        print(f"RESULTS for {quiztaker}", file=thefile, flush=True)
        print(f"DATE: {datetime.datetime.today()}", file=thefile, flush=True)
        print(f"COMPLETION TIME: {self.completion_time}",
              file=thefile, flush=True)
        print(
            f"QUESTIONS: {self.correct_count} out of {len(self.questions)} correct", file=thefile, flush=True)
        print(f"SCORE: {self.score} out of {self.total_points} points",
              file=thefile, flush=True)
        print("*******************************************\n",
              file=thefile, flush=True)

    def take_quiz(self):
        # initialize the quiz state
        self.score = 0
        self.correct_count = 0
        # TODO: reset the completion time
        self.completion_time = 0

        # print the header
        self.print_header()

        # Randomize the order of the questions using shuffle function from random module
        random.shuffle(self.questions)

        # TODO: record the start time of the quiz
        start_time = datetime.datetime.now()

        # execute each question and record the result
        for q in self.questions:
            q.ask()
            if (q.is_correct):
                self.correct_count += 1
                self.score += q.points
            print("------------------------------------------------\n")

            # TODO: record the end time of the quiz using the same method
            end_time = datetime.datetime.now()

            # TODO: ask the user if they want to re-do any incorrect questions
            if self.correct_count != len(self.questions):
                response = input(
                    "Would you like to re-do any incorrect questions? (Y/N) ").lower()
                if response[0] == "y":
                    # filter over all the questions and only choose the ones that are incorrect
                    wrong_questions = [
                        q for q in self.questions if q.is_correct == False]
                    # execute each wrong question and record the result
                    for q in wrong_questions:
                        q.ask()
                        if (q.is_correct):
                            self.correct_count += 1
                            self.score += q.points
                        print("------------------------------------------------\n")

                    # After the re-do, record the end time again
                    end_time = datetime.datetime.now()


            # set the completion using the difference between the start and end times
            self.completion_time = end_time - start_time
            # round the number of secods to nearest second value
            self.completion_time = datetime.timedelta(
                seconds=round(self.completion_time.total_seconds()))

        # return the results
        return (self.score, self.correct_count, self.total_points)

# Factory pattern for creating questions


class Question:
    def __init__(self):
        self.points = 0
        self.correct_answer = ""
        self.text = ""
        self.is_correct = False


class QuestionTF(Question):
    def __init__(self):
        super().__init__()

    def ask(self):
        while (True):
            print(f"(T)rue or (F)alse: {self.text}")
            response = input("? ")

            if (len(response) == 0):
                print("Sorry, that's not a valid response. Please try again")
                continue

            response = response.lower()
            if (response[0] != "t" and response[0] != "f"):
                print("Sorry, that's not a valid response. Please try again")
                continue

            if response[0] == self.correct_answer:
                self.is_correct = True

            break


class QuestioncMC(Question):
    def __init__(self):
        super().__init__()
        self.answers = []

    def ask(self):
        while (True):
            print(self.text)
            for a in self.answers:
                print(f"{a.name}) {a.text}")

            response = input("? ")

            if (len(response) == 0):
                print("Sorry, that's not a valid response. Please try again")
                continue

            response = response.lower()
            if response[0] == self.correct_answer:
                self.is_correct = True

            break


class Answer:
    def __init__(self):
        self.text = ""
        self.name = ""
