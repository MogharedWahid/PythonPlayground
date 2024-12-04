class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print("You've completed the quiz.")
            print(f"Your final score is {self.score}/{len(self.question_list)}.")
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"That's wrong, the correct answer was '{correct_answer}'.")
        print(f"You current score is: {self.score}/{self.question_number}.")
        print("\n")

    def next_question(self):
        question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number+1}: {question.text} (True/False)?: ").lower()
        self.question_number += 1
        self.check_answer(user_answer, question.answer)




