import xml.sax
from quiz import *
from enum import Enum, unique


@unique
class QuizParserState(Enum):

    IDLE = 0
    PARSE_QUIZ = 1
    PARSE_DESCRIPTION = 2
    PARSE_QUESTION = 3
    PARSE_QUESTION_TEXT = 4
    PARSE_ANSWER = 5


class QuizParser(xml.sax.ContentHandler):

    # The QuizParser class loads a particular quiz file, parses it, and returns
    # a fully-built Quiz object that can then be presented to the user.

    def __init__(self):
        self.new_quiz = Quiz()
        # TODO: properties to track the current state of the parser
        self._parse_state = QuizParserState.IDLE
        self._current_question = None
        self._current_answer = None

    def parse_quiz(self, quiz_file):
        # load the quiz file
        quiztext = ""
        with open(quizpath, "r") as quizfile:
            quiztext = quizfile.read()

            # TODO: parse the quiz file
            xml.sax.parseString(quiztext, self)

            # return the finished quiz
            return self.new_quiz

    def startElement(self, tagname, attrs):
        if tagname == "quizML":
            self.state = QuizParserState.PARSE_QUIZ
            self.new_quiz.name = attrs["name"]
        # TODO: handle the other tags
        elif tagname == "Description":
            self._parse_state = QuizParserState.PARSE_DESCRIPTION
        elif tagname == "Question":
            self._parse_state = QuizParserState.PARSE_QUESTION
            if attrs["type"] == "multiplechoice":
                self._current_question = QuestionMC()
            elif attrs["type"] == "tf":
                self._current_question = QuestionTF()
                self._current_question.points = int(attrs["points"])
                self.new_qiz.total_points += self._current_question.points
            elif tagname == "QuestionText":
                self._parse_state = QuizParserState.PARSE_QUESTION_TEXT
                self._current_question.correct_answer = attrs["answer"]
            elif tagname == "Answer":
                self._current_answer = Answer()
                self._current_answer.name = attrs["name"]
                self._parse_state = QuizParserState.PARSE_ANSWER

    def endElement(self, tagname):
        if tagname == "quizML":
            self.state = QuizParserState.IDLE
        # TODO: handle the other tags
        elif tagname == "Description":
            self._parse_state = QuizParserState.PARSE_QUIZ
        elif tagname == "Question":
            self.new_quiz.questions.append(self._current_question)
            self._parse_state = QuizParserState.PARSE_QUIZ
        elif tagname == "QuestionText":
            self._parse_state = QuizParserState.PARSE_QUESTION
        elif tagname == "Answer":
            self._current_question.answers.append(self._current_answer)
            self._parse_state = QuizParserState.PARSE_QUESTION

    def characters(self, chars):
        # TODO: handle the content of the tags
        if self._parse_state == QuizParserState.PARSE_DESCRIPTION:
            self.new_quiz.description += chars
            self._parse_state = QuizParserState.IDLE
        elif self._parse_state == QuizParserState.PARSE_QUESTION_TEXT:
            self._current_question.text += chars
        elif self._parse_state == QuizParserState.PARSE_ANSWER:
            self._current_answer.text += chars
