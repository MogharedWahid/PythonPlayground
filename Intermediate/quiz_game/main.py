from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

logo ="""
 ██████╗ ██╗   ██╗██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗
██╔═══██╗██║   ██║██║╚══███╔╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║   ██║██║   ██║██║  ███╔╝     ██║  ███╗███████║██╔████╔██║█████╗  
██║▄▄ ██║██║   ██║██║ ███╔╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝╚██████╔╝██║███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
 ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                     
"""

print(logo)
question_bank = [Question(question['question'], question['correct_answer']) for question in question_data]
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()