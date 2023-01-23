from quizmanager import QuizManager

class QuizApp:

    # class value
    QUIZ_FOLDER = "quizzes"

    def __init__(self):
        self.username = ""
        # Create a quiz manager instance | this is where the quiz folder is passed in and kept
        self.qm = QuizManager(QuizApp.QUIZ_FOLDER)

    def startup(self):
        # print the greeting at startup
        self.greeting()

        # TODO: ask the user for their name
        self.username = input("What is your name? ")
        print(f"Hello, {self.username}!")
        print()

    def greeting(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print("~~~~~~ Welcome to PyQuiz! ~~~~~~")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print()

    def menu_header(self):
        print("--------------------------------")
        print("Please make a selection:")
        print("(M): Repeat this menu")
        print("(L): List quizzes")
        print("(T): Take a quiz")
        print("(E): Exit program")

    def menu_error(self):
        print("That's not a valid selection. Please try again.")

    def goodbye(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print(f"Thanks for using PyQuiz, {self.username}!")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")

    def menu(self):
        self.menu_header()

        # TODO: get the user's selection and act on it. This loop will run until the user exits the app
        selection = ""
        while (True):
            selection = input("Please select an option: ")

            # If the user enters nothing, ask them to try again
            if len(selection) == 0:
                self.menu_error()
                continue

            # Convert the selection to upper case
            selection = selection.upper()

            # If the user enters E, exit the program
            if selection[0] == "E":
                self.goodbye()
                break

            # If the user enters M, repeat the menu
            elif selection[0] == "M":
                self.menu_header()
                continue

            # If the user enters L, list the quizzes
            elif selection[0] == "L":
                print("\n List of quizzes available:")
                # TODO: list the quizzes
                self.qm.list_quizzes()
                print("--------------------------\n")
                continue

            # If the user enters T, take a quiz
            elif selection[0] == "T":
                # exception handling for invalid quiz number
                try:
                    quiz_number = int(
                        input("Which quiz would you like to take? "))
                    print(f"Taking quiz {quiz_number}")

                    # TODO: start the quiz
                    self.qm.take_quiz(quiz_number, self.username)
                    self.qm.print_results()

                    # TODO: ask the user if they want to save the results
                    dosave = input("Do you want to save your results? (Y/N) ")
                    dosave = dosave.capitalize()
                    if len(dosave) > 0 and dosave[0] == "Y":
                        self.qm.save_results(quiz_number, self.username)
                        print("Results saved!")

                except:
                    self.menu_error()

            # If the user enters anything else, show an error
            else:
                self.menu_error()

    # This is the entry point to the program

    def run(self):
        # Execute the startup routine - ask for name, print greeting, etc
        self.startup()
        # Start the main program menu and run until the user exits
        self.menu()


if __name__ == "__main__":
    app = QuizApp()
    app.run()
