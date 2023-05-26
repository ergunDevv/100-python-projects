from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    qb_question = Question(question['text'], question['answer'])
    question_bank.append(qb_question)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_question():
    quiz_brain.next_question()


print("You've completed the quiz")
print(
    f"You final score was: {quiz_brain.question_score}/{quiz_brain.question_number}")
