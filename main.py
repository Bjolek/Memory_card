from PyQt5.QtWidgets import*

app = QApplication([])
window = QWidget()
window.resize(500,500)


mainLine = QVBoxLayout()

Apple = QLabel("Яблуко")

menuBtn = QPushButton("Меню")
restBtn = QPushButton("Відпочити")
timeSpn = QSpinBox()
timeLbl = QLabel("хвилин")

firstLine = QHBoxLayout()
firstLine.addWidget(menuBtn)
firstLine.addWidget(restBtn)
firstLine.addWidget(timeSpn)
firstLine.addWidget(timeLbl)

mainLine.addLayout(firstLine)

mainLine.addWidget(Apple)

answerGroup = QGroupBox("Варіанти відповідей")



answer1 = QRadioButton("1")
answer2 = QRadioButton("2")
answer3 = QRadioButton("3")
answer4 = QRadioButton("4")

answerLine = QVBoxLayout()

answerLine.addWidget(answer1)
answerLine.addWidget(answer2)
answerLine.addWidget(answer3)
answerLine.addWidget(answer4)

answerGroup.setLayout(answerLine)
mainLine.addWidget(answerGroup)
window.setLayout(mainLine)
window.show()
app.exec()