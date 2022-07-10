from preguntas import Question

question_prompts = [
    "de que color son las manzanas?\n(a) rojas\n(b) moradas\n(c) naranjas\n\n",
    "de que color son las bananas?\n(a) Magenta\n(b) azules\n(c) amarillas\n\n",
    "de qie color son las fresas?\n(a) moradas\n(b) rojas\n(c) violetas\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print ('you got '+ str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)