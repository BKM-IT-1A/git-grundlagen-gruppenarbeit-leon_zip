[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19606898&assignment_repo_type=AssignmentRepo)
# Gruppenaufgabe: Quiz-Antwort prüfen mit Python
Willkommen zur Gruppenarbeit im Rahmen des Git-Workshops. 
In dieser Aufgabe schreibt ihr eine kleine Funktion, die prüft, ob eine gegebene Antwort richtig ist.


## Ziel
Schreibt eine Funktion `is_correct(...)`, die erkennt, ob eine gewählte Antwort korrekt ist. 

---

## Startdatei: `check_answer.py`
In der Startdatei ist ein Beispiel enthalten. Ihr erweitert es Schritt für Schritt. 

---

## So gehts
1. Legt ein Dictionary namens `question` mit diesen Feldern an:
   - `"Text"`: Die Frage als String
   - `"options"`: Eine Liste mit **vier** Antwortmöglichkeiten
   - `"correct"`: Der Index (0-3) der richtigen Antwort
2. Schreibt die Funktion:

  python def is_correct(question, answer_index):
  return question ["correct"] == answer_index


3. Testet eure Funktion:
- Legt z.B. fest: `answer =1`
Gebt mit `print(...)` aus, ob die Antwort richtig ist (`True` oder `False`)
