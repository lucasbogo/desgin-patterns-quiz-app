# desgin-patterns-quiz-app

# Quiz app implemented for Desing Patterns in Python discipline at IFPR

### Patterns used:
- factory: the factory pattern was used to create questions and quizzes. It is located in the main class for the quizz application ```pyquiz.py```
- Single Responsibility Principle: ```quizmanager.py``` manages the quizzes by listing them, taking them, and saving the results 
- Open/Closed Principle: this class is open for extension, but closed for modification ```quizmanager.py```
- Liskov Substitution Principle: ```quizmanager.py``` is a subclass of QuizParser
- Interface Segregation Principle: ```quizmanager.py```  does not implement any interfaces
- Dependency Inversion Principle: ```quizmanager.py``` depends on QuizParser, but not on any concrete classes
