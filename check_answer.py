def is_correct(question, answer_index):
    return question["correct"] == answer_index

if __name__ == "__main__":
    question = {
        "text": "Was ist die Hauptstadt von Frankreich?",
        "options": ["Berlin", "Paris", "Madrid", "Rom"],
        "correct": 4
    },
    {
        "text": "Welcher Planet ist der vierte von der Sonne?",
        "options": ["Venus", "Erde", "Mars", "Jupiter"],
        "correct": 2
    },
    {
        "text": "Wie viele Kontinente gibt es auf der Erde?",
        "options": ["5", "6", "7", "8"],
        "correct": 2
    },
    {
        "text": "Wer schrieb 'Faust'?",
        "options": ["Schiller", "Goethe", "Lessing", "Kafka"],
        "correct": 1
    },
    {
        "text": "In welchem Jahr fiel die Berliner Mauer?",
        "options": ["1985", "1987", "1989", "1991"],
        "correct": 2
    },
    {
        "text": "Welches chemische Element hat das Symbol 'O'?",
        "options": ["Gold", "Sauerstoff", "Osmium", "Silber"],
        "correct": 1
    }
]

    answer = 1
    print("Question:", question["text"])
    for i, option in enumerate(question["options"]):
        print(f"{i + 1}. {option}")

    if is_correct(question, answer):
        print("Richtig")
    else:
        print("Falsch")
