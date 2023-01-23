import os.path
import os
import quizparser
import datetime

# Single Responsibility Principle: this class manages the quizzes by listing them, taking them, and saving the results
# Open/Closed Principle: this class is open for extension, but closed for modification
# Liskov Substitution Principle: this class is a subclass of QuizParser
# Interface Segregation Principle: this class does not implement any interfaces
# Dependency Inversion Principle: this class depends on QuizParser, but not on any concrete classes


class QuizManager:
    def __init__(self, quizfolder):
        self.quizfolder = quizfolder
        # TODO: the most recently selected quiz
        self.the_quiz = None

        # TODO: implement dictionary pattern
        self.quizzes = dict()

        # TODO: stores the results of the most recent quiz
        self.results = None

        # TODO: the name of the person taking the quiz
        self.quiztaker = ""

        # TODO: make sure that the quiz folder exists
        if (os.path.exists(quizfolder) == False):
            raise FileNotFoundError("Quiz folder not found")

        # TODO: build the list of quizzes
        self._build_quiz_list()

    # ITERATOR PATTERN
    def _build_quiz_list(self):
        # Each dircontents is a directory entry object that contains index, name, and path in that folder
        dircontents = os.scandir(self.quizfolder)
        # TODO: parse the XML files in the directory | i = index, f = file
        for i, f in enumerate(dircontents):
            # Check to see if the f variable is a file and ends with .xml
            if (f.name.endswith(".xml")):
                # Create a parser for each quiz | gets a new quizparser object, so each new quiz will be a new object
                parser = quizparser.QuizParser()
                # set the index + 1 to be the key | comes back with a fully parsed quiz object | and stores the new quiz object in the dictionary
                self.quizzes[i+1] = parser.parse_quiz(f)

    # TODO: ITERATOR PATTERN for displaying the list of quizzes | it iterates of the dictionary and prints the name of the quiz
    def list_quizzes(self):
        # For each key = k and value = v in the dictionary, print the key and the name of the quiz
        for k, v in self.quizzes.items():
            print(f"{k}: {v.name}")

    # start the given quiz for the user and return the results | thus function is called from the main app
    def take_quiz(self, quizid, username):
        self.quiztaker = username
        self.the_quiz = self.quizzes[quizid]
        self.results = self.the_quiz.take_quiz()

    # prints the results of the most recently taken quiz
    def print_results(self):
        self.the_quiz.print_results(self.quiztaker)

    # save the results of the most recent quiz to a file
    # the file is named using the current date as
    # QuizResults_YYYY_MM_DD_N (N is incremented until unique)

    def save_results(self):
        # TODO: Save the results to a file
        today = datetime.datetime.now()
        filename = f"QuizResults_{today.year}_{today.month}_{today.day}.txt"

        # TODO: If the file already exists, then add a digit to the end of the filename
        # Counter for the number of files
        n = 1
        while(os.path.exists(filename)):
            filename = f"QuizResults_{today.year}_{today.month}_{today.day}_{n}.txt"
            n += 1
        
        # TODO: Open the file and write the results to it
        with open(filename, "w") as f:
            self.the_quiz.print_results(self.quiztaker, f)
