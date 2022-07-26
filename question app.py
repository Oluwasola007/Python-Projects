from Question import Question

question_prompts = 
"What colors are apples?\n(a) Red/Green\n (b) Purple\n (c) Orange\n\n"
"What colors are bananas?\n(a) Teal\n (b) Magenta \n (c) Yellow\n\n"
"What colors are strawberries?\n(a) Yellow\n (b) Red\n (c) Blue\n\n"

questions = [
    Questions(question_prompts[0], "a")
    Questions(question_prompts[1], "c")
    Questions(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "Correctly")

run_test(questions)