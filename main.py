import random
from PyQt5.QtWidgets import *

import EditWindow
import MenuWindow
import Question

app = QApplication([])
app.setStyleSheet("""
    QWidget {
        background: #337CCF;
    }

    QPushButton
    {
        background: #FFC436;
        border-width: 7px;
        border-color: #191D88;
        border-style: inset;
        font-family: Impact;
    }
    QLabel {
        font-family: Impact;
    }
    QGroupBox {
        font-family: Impact;
    }
    QRadioButton {
        font-family: Impact;
    }
    QGroupBox {
         background: #FFC436;

    }
    QRadioButton {
         background: #FFC436;

    }
""")
window = QWidget()
window.resize(500, 500)
mainLine = QVBoxLayout()
menuBtn = QPushButton("Меню")
restBtn = QPushButton("Відпочити")
timeSpn = QSpinBox()
timeLbl = QLabel("хвилин")
questLbl = QLabel("Питання")
answerBtn = QPushButton("Відповісти")
nextQuestBtn = QPushButton("Наступне питання")
editQuestBtn = QPushButton("Редагувати")
nextQuestBtn.hide()
firstLine = QHBoxLayout()
firstLine.addWidget(menuBtn)
firstLine.addWidget(restBtn)
firstLine.addWidget(timeSpn)
firstLine.addWidget(timeLbl)
mainLine.addLayout(firstLine)
mainLine.addWidget(questLbl)
answersGroup = QGroupBox("Варіанти відповідей")
answer1 = QRadioButton("1")
answer2 = QRadioButton("2")
answer3 = QRadioButton("3")
answer4 = QRadioButton("4")
answers = [answer1, answer2, answer3, answer4]

answersLine = QVBoxLayout()
answersLine.addWidget(answer1)
answersLine.addWidget(answer2)
answersLine.addWidget(answer3)
answersLine.addWidget(answer4)

result = QLabel("Результат")
answersLine.addWidget(result)
result.hide()

answersGroup.setLayout(answersLine)

mainLine.addWidget(answersGroup)
mainLine.addWidget(answerBtn)
mainLine.addWidget(nextQuestBtn)
mainLine.addWidget(editQuestBtn)

def setQuest():
    random.shuffle(answers)
    questLbl.setText(Question.qeust[Question.currentQuest]["питання"])
    answers[0].setText(Question.qeust[Question.currentQuest]["Правильна відповідь"])
    answers[1].setText(Question.qeust[Question.currentQuest]["не правильна1"])
    answers[2].setText(Question.qeust[Question.currentQuest]["не правильна2"])
    answers[3].setText(Question.qeust[Question.currentQuest]["не правильна3"])

setQuest()
def showResult():
    answers[0].hide()
    answers[1].hide()
    answers[2].hide()
    answers[3].hide()
    result.show()
    nextQuestBtn.show()
    answerBtn.hide()
    if answers[0].isChecked():
        result.setText("Правильно")
    else:
        result.setText("не правильно")


def nextFunc():
    answers[0].show()
    answers[1].show()
    answers[2].show()
    answers[3].show()
    answerBtn.show()
    result.hide()

    Question.currentQuest += 1
    setQuest()


def editQuestFunc():
    window.hide()
    EditWindow.editWindow()
    
    window.show()

    setQuest()

answerBtn.clicked.connect(showResult)
nextQuestBtn.clicked.connect(nextFunc)
menuBtn.clicked.connect(MenuWindow.menuWind)
editQuestBtn.clicked.connect(editQuestFunc)

window.setLayout(mainLine)
window.show()
app.exec()