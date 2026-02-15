import sys
import sqlite3
import re
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, QDesktopWidget, QProgressBar, QLabel,
                             QVBoxLayout, QMessageBox, QLineEdit, QPlainTextEdit, QScrollArea)
from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt

k = ''
z = []
t = [[], [], [], [], []]
ch = 0
podskazki = [[], [], [], [], []]
aaa = ''
pol_pers = ''
name_player = ''
pk = 0
pvi = 0
ppl = 0
pve = 0
ppo = 0
fl_profil = False
m = ''
polzovatel = []
zadacha = ['', '']
otvets = [[], [], [], [], []]
reshenie =['*' * 10, '*' * 10, '*' * 10, '*' * 10, '*' * 10]
protcent = [0, 0, 0, 0, 0]


def registratcia(name1, password1):
    c = sqlite3.connect('users.sqlite')
    a = c.cursor()
    a.execute("""INSERT INTO u(name,password, rez, z1, z2, z3, z4) VALUES(?,?,?,?,?,?,?)""",
              (name1, password1, 0, m, m, m, m))
    c.commit()
    c.close()


def proverka_vhod(name, password):
    c = sqlite3.connect('users.sqlite')
    global t, ch
    a = c.cursor()
    itog = a.execute('''SELECT name, password, rez, z1, z2, z3, z4, z5 FROM u WHERE name = ?''', (name,)).fetchall()
    if itog:
        if itog[0][1] == password:
            global polzovatel, ch
            polzovatel = list(itog[0])
            ch = polzovatel[2]

            for i in range(5):
                if polzovatel[i + 3] != '' and len(polzovatel[i + 3]) > 2:
                    t[i] = polzovatel[i + 3].split(', ')
            return 'Вы вошли в систему'
        else:
            return 'Неверный пароль'
    else:
        return 'Пользователя с таким именем не существует'


def proverka_reshenie():
    c = sqlite3.connect('otvet.sqlite')
    a = c.cursor()
    name = zadacha[1].split(' ')[1]
    if zadacha[0] == 'Решетка Кардано':
        b = 'reshetkaKardano'
    elif zadacha[0] == 'Шифр Плейфера':
        b = 'shifrPleifera'
    elif zadacha[0] == 'Шифр Вернама':
        b = 'shifrVernama'
    elif zadacha[0] == 'Шифр Полибия':
        b = 'shifrPoliby'
    elif zadacha[0] == 'Шифр Виженера':
        b = 'shifrVigenera'
    itog = a.execute(f'''SELECT name, otv FROM {b} WHERE name = ?''', (name,)).fetchall()
    return itog


def sozt(a):
    global k
    if a == 'Шифр Виженера':
        k = 'sh_vi.png'
    elif a == 'Решетка Кардано':
        k = 'sh_ka.png'
    elif a == 'Шифр Полибия':
            k = 'sh_pol.png'
    elif a == 'Шифр Плейфера':
        k = 'sh_pl.png'
    elif a == 'Шифр Вернама':
        k = 'sh_ver.png'
    return True



def proverka(parol, name):
    c = sqlite3.connect('users.sqlite')
    a = c.cursor()
    itog = a.execute('''SELECT name FROM u WHERE name = ?''', (name,)).fetchall()
    if itog:
        return 'Пользователь с таким именем уже существует'
    if len(name) < 5:
        return 'Имя пользователя слишком короткое'
    if len(parol) < 8:
        return 'Пароль менее 8 символов'

    if not re.search(r"\d", parol):
        return 'В пароле должны присутствовать цифры'

    if not re.search(r"[a-z]", parol) or not re.search(r"[A-Z]", parol):
        return 'Пароль должен содержать буквы верхнего и нижнего регистра'

    if not re.search(r"\W", parol):
        return 'Пароль должен содержать специальные символы'

    return 'Вы успешно заригистрированы'


class Window_osnownoe(object):
    def setupUI(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)
        flayout = QVBoxLayout(self.centralwidget)
        self.nnnn = QLabel('CryptoQuest', self.centralwidget)
        self.nnnn.setFixedSize(350, 60)
        self.nnnn.setAlignment(Qt.AlignCenter)
        self.nnnn.setStyleSheet("QLabel"
                                "{color:#ff9900; font:50px bold; font-weight:bold;}")
        self.b1 = QPushButton('Профиль', self.centralwidget)
        self.b2 = QPushButton('Обучение', self.centralwidget)
        self.b3 = QPushButton('Играть', self.centralwidget)
        self.b1.setStyleSheet("QPushButton"
                              "{border : 3px solid #66ffff;"
                              "color:#0a4761; font:16px bold; font-weight:bold;"
                              "background-color: rgba(102, 255, 255, 0.5);}"
                              "QPushButton::hover{"
                              "background-color: rgba(51, 205, 255, 0.5);}")
        self.b4 = QPushButton('Рейтинг', self.centralwidget)
        self.b4.setStyleSheet("QPushButton"
                              "{border : 3px solid #66ffff;"
                              "color:#0a4761; font:16px bold; font-weight:bold;"
                              "background-color: rgba(102, 255, 255, 0.5);}"
                              "QPushButton::hover{"
                              "background-color: rgba(51, 205, 255, 0.5);}")
        self.b2.setStyleSheet("QPushButton"
                              "{border : 3px solid #66ffff;"
                              "color:#0a4761; font:16px bold; font-weight:bold;"
                              "background-color: rgba(102, 255, 255, 0.5);}"
                              "QPushButton::hover{"
                              "background-color: rgba(51, 205, 255, 0.5);}")
        self.b3.setStyleSheet("QPushButton"
                              "{border : 3px solid #66ffff;"
                              "color:#0a4761; font:16px bold; font-weight:bold;"
                              "background-color: rgba(102, 255, 255, 0.5);}"
                              "QPushButton::hover{"
                              "background-color: rgba(51, 205, 255, 0.5);}")
        flayout.addWidget(self.nnnn)
        flayout.addWidget(self.b1)
        flayout.addWidget(self.b2)
        flayout.addWidget(self.b3)
        self.b1.setFixedSize(350, 60)
        flayout.addWidget(self.b4)
        self.b4.setFixedSize(350, 60)
        self.b2.setFixedSize(350, 60)
        self.b3.setFixedSize(350, 60)
        flayout.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)


class Vhod_polzovatel(object):
    def setupUI(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)
        lay2 = QVBoxLayout(self.centralwidget)
        self.vhod = QPushButton("ВХОД", self.centralwidget)
        self.CPSBTN = QPushButton("РЕГИСТРАЦИЯ", self.centralwidget)
        self.vhod.setStyleSheet("QPushButton"
                                "{border : 3px solid #66ffff;"
                                "color:#0a4761; font:16px bold; font-weight:bold;"
                                "background-color: rgba(102, 255, 255, 0.5);}"
                                "QPushButton::hover{"
                                "background-color: rgba(51, 205, 255, 0.5);}")
        self.CPSBTN.setStyleSheet("QPushButton"
                                  "{border : 3px solid #66ffff;"
                                  "color:#0a4761; font:16px bold; font-weight:bold;"
                                  "background-color: rgba(102, 255, 255, 0.5);}"
                                  "QPushButton::hover{"
                                  "background-color: rgba(51, 205, 255, 0.5);}")
        self.vhod.setFixedSize(300, 50)
        self.CPSBTN.setFixedSize(300, 50)
        self.label_name = QLabel('NAME:', self.centralwidget)
        self.lineEdit_name = QLineEdit(self.centralwidget)
        self.lineEdit_name.setFixedSize(300, 30)
        self.label_name.setStyleSheet("QLabel"
                                      "{color:#001524; font:16px bold; font-weight:bold;}")
        self.label_name.setAlignment(Qt.AlignCenter)
        self.label_password = QLabel('PASSWORD:', self.centralwidget)
        self.label_password.setStyleSheet("QLabel"
                                          "{color:#001524; font:16px bold; font-weight:bold;}")
        self.label_password.setAlignment(Qt.AlignCenter)
        self.lineEdit_password = QLineEdit(self.centralwidget)
        self.lineEdit_password.setFixedSize(300, 30)
        lay2.addWidget(self.label_name)
        lay2.addWidget(self.lineEdit_name)
        lay2.addWidget(self.label_password)
        lay2.addWidget(self.lineEdit_password)
        lay2.addWidget(self.vhod)
        lay2.addWidget(self.CPSBTN)
        lay2.setAlignment(Qt.AlignCenter)
        self.exit = QPushButton('назад', self.centralwidget)
        self.exit.setGeometry(10, 10, 60, 60)
        self.exit.setStyleSheet("QPushButton"
                                "{border-radius: 30px;"
                                "color:#0a4761; font:14px bold; font-weight:bold;"
                                "background-color: rgba(102, 255, 255, 0.5);}"
                                "QPushButton::hover{"
                                "background-color: rgba(51, 205, 255, 0.5);}")
        MainWindow.setCentralWidget(self.centralwidget)


class Window_obytchenie(object):
    def setupUI(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)
        flayout = QVBoxLayout(self.centralwidget)
        self.button1 = QPushButton('Решетка Кардано', self.centralwidget)
        self.button2 = QPushButton('Шифр Виженера', self.centralwidget)
        self.button3 = QPushButton('Шифр Плейфера', self.centralwidget)
        self.button4 = QPushButton('Шифр Вернама', self.centralwidget)
        self.button5 = QPushButton('Шифр Полибия', self.centralwidget)
        self.button1.setStyleSheet("QPushButton"
                                   "{border : 3px solid #66ffff;"
                                   "color:#0a4761; font:16px bold; font-weight:bold;"
                                   "background-color: rgba(102, 255, 255, 0.5);}"
                                   "QPushButton::hover{"
                                   "background-color: rgba(51, 205, 255, 0.5);}")
        self.button2.setStyleSheet("QPushButton"
                                   "{border : 3px solid #66ffff;"
                                   "color:#0a4761; font:16px bold; font-weight:bold;"
                                   "background-color: rgba(102, 255, 255, 0.5);}"
                                   "QPushButton::hover{"
                                   "background-color: rgba(51, 205, 255, 0.5);}")
        self.button3.setStyleSheet("QPushButton"
                                   "{border : 3px solid #66ffff;"
                                   "color:#0a4761; font:16px bold; font-weight:bold;"
                                   "background-color: rgba(102, 255, 255, 0.5);}"
                                   "QPushButton::hover{"
                                   "background-color: rgba(51, 205, 255, 0.5);}")
        self.button4.setStyleSheet("QPushButton"
                                   "{border : 3px solid #66ffff;"
                                   "color:#0a4761; font:16px bold; font-weight:bold;"
                                   "background-color: rgba(102, 255, 255, 0.5);}"
                                   "QPushButton::hover{"
                                   "background-color: rgba(51, 205, 255, 0.5);}")
        self.button5.setStyleSheet("QPushButton"
                                   "{border : 3px solid #66ffff;"
                                   "color:#0a4761; font:16px bold; font-weight:bold;"
                                   "background-color: rgba(102, 255, 255, 0.5);}"
                                   "QPushButton::hover{"
                                   "background-color: rgba(51, 205, 255, 0.5);}")

        flayout.addWidget(self.button1)
        flayout.addWidget(self.button2)
        flayout.addWidget(self.button3)
        flayout.addWidget(self.button4)
        flayout.addWidget(self.button5)
        self.button1.setFixedSize(350, 60)
        self.button2.setFixedSize(350, 60)
        self.button3.setFixedSize(350, 60)
        self.button4.setFixedSize(350, 60)
        self.button5.setFixedSize(350, 60)
        flayout.setAlignment(Qt.AlignCenter)
        self.exit = QPushButton('назад', self.centralwidget)
        self.exit.setGeometry(10, 10, 60, 60)
        self.exit.setStyleSheet("QPushButton"
                                "{border-radius: 30px;"
                                "color:#0a4761; font:14px bold; font-weight:bold;"
                                "background-color: rgba(102, 255, 255, 0.5);}"
                                "QPushButton::hover{"
                                "background-color: rgba(51, 205, 255, 0.5);}")
        MainWindow.setCentralWidget(self.centralwidget)

class Reiting(object):
    def setupUI(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)
        flayout = QVBoxLayout(self.centralwidget)
        c = sqlite3.connect('users.sqlite')
        a = c.cursor()
        itog = a.execute('''SELECT name,rez FROM u ''').fetchall()
        itog.sort(key=lambda a: a[1], reverse=True)
        for i in range(len(itog)):
            self.button1 = QPushButton(str(itog[i][0]) + ' . '* 10  + str(itog[i][1]), self.centralwidget)
            self.button1.setStyleSheet("QPushButton"
                                       "{border : 3px solid #66ffff;"
                                       "color:#0a4761; font:16px bold; font-weight:bold;"
                                       "background-color: rgba(102, 255, 255, 0.5);}"
                                       "QPushButton::hover{"
                                       "background-color: rgba(51, 205, 255, 0.5);}")

            flayout.addWidget(self.button1)

            self.button1.setFixedSize(350, 60)
        flayout.setAlignment(Qt.AlignCenter)
        self.exit = QPushButton('назад', self.centralwidget)
        self.exit.setGeometry(10, 10, 60, 60)
        self.exit.setStyleSheet("QPushButton"
                                "{border-radius: 30px;"
                                "color:#0a4761; font:14px bold; font-weight:bold;"
                                "background-color: rgba(102, 255, 255, 0.5);}"
                                "QPushButton::hover{"
                                "background-color: rgba(51, 205, 255, 0.5);}")
        MainWindow.setCentralWidget(self.centralwidget)

class Play(object):
    def setupUI(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)
        flayout = QVBoxLayout(self.centralwidget)
        self.n = QLabel('Баллы ' + str(ch), self.centralwidget)
        self.n.setGeometry(800, 20, 70, 50)
        self.n.setAlignment(Qt.AlignCenter)
        self.n.setStyleSheet("QLabel"
                                "{color:#ff9900; font:12px bold; font-weight:bold;}")
        self.button1 = QPushButton('Решетка Кардано', self.centralwidget)
        self.button2 = QPushButton('Шифр Виженера', self.centralwidget)
        self.button3 = QPushButton('Шифр Плейфера', self.centralwidget)
        self.button4 = QPushButton('Шифр Вернама', self.centralwidget)
        self.button5 = QPushButton('Шифр Полибия', self.centralwidget)
        self.button1.setStyleSheet("QPushButton"
                                   "{border : 3px solid #66ffff;"
                                   "color:#0a4761; font:16px bold; font-weight:bold;"
                                   "background-color: rgba(102, 255, 255, 0.5);}"
                                   "QPushButton::hover{"
                                   "background-color: rgba(51, 205, 255, 0.5);}")
        self.button2.setStyleSheet("QPushButton"
                                   "{border : 3px solid #66ffff;"
                                   "color:#0a4761; font:16px bold; font-weight:bold;"
                                   "background-color: rgba(102, 255, 255, 0.5);}"
                                   "QPushButton::hover{"
                                   "background-color: rgba(51, 205, 255, 0.5);}")
        self.button3.setStyleSheet("QPushButton"
                                   "{border : 3px solid #66ffff;"
                                   "color:#0a4761; font:16px bold; font-weight:bold;"
                                   "background-color: rgba(102, 255, 255, 0.5);}"
                                   "QPushButton::hover{"
                                   "background-color: rgba(51, 205, 255, 0.5);}")
        self.button4.setStyleSheet("QPushButton"
                                   "{border : 3px solid #66ffff;"
                                   "color:#0a4761; font:16px bold; font-weight:bold;"
                                   "background-color: rgba(102, 255, 255, 0.5);}"
                                   "QPushButton::hover{"
                                   "background-color: rgba(51, 205, 255, 0.5);}")
        self.button5.setStyleSheet("QPushButton"
                                   "{border : 3px solid #66ffff;"
                                   "color:#0a4761; font:16px bold; font-weight:bold;"
                                   "background-color: rgba(102, 255, 255, 0.5);}"
                                   "QPushButton::hover{"
                                   "background-color: rgba(51, 205, 255, 0.5);}")

        self.pbar4 = QProgressBar(self.centralwidget)
        self.pbar4.setValue(protcent[4])
        self.pbar4.setFixedSize(384, 30)
        self.pbar0 = QProgressBar(self.centralwidget)
        self.pbar0.setValue(protcent[0])
        self.pbar0.setFixedSize(384, 30)
        self.pbar1 = QProgressBar(self.centralwidget)
        self.pbar1.setValue(protcent[1])
        self.pbar1.setFixedSize(384, 30)
        self.pbar2 = QProgressBar(self.centralwidget)
        self.pbar2.setValue(protcent[2])
        self.pbar2.setFixedSize(384, 30)
        self.pbar3 = QProgressBar(self.centralwidget)
        self.pbar3.setValue(protcent[3])
        self.pbar3.setFixedSize(384, 30)

        flayout.addWidget(self.button1)
        flayout.addWidget(self.pbar0)
        flayout.addWidget(self.button2)
        flayout.addWidget(self.pbar1)
        flayout.addWidget(self.button3)
        flayout.addWidget(self.pbar2)
        flayout.addWidget(self.button4)
        flayout.addWidget(self.pbar3)
        flayout.addWidget(self.button5)
        flayout.addWidget(self.pbar4)
        self.button1.setFixedSize(350, 60)
        self.button2.setFixedSize(350, 60)
        self.button3.setFixedSize(350, 60)
        self.button4.setFixedSize(350, 60)
        self.button5.setFixedSize(350, 60)
        flayout.setAlignment(Qt.AlignCenter)
        self.exit3 = QPushButton('назад', self.centralwidget)
        self.exit3.setGeometry(10, 10, 60, 60)
        self.exit3.setStyleSheet("QPushButton"
                                "{border-radius: 30px;"
                                "color:#0a4761; font:14px bold; font-weight:bold;"
                                "background-color: rgba(102, 255, 255, 0.5);}"
                                "QPushButton::hover{"
                                "background-color: rgba(51, 205, 255, 0.5);}")
        MainWindow.setCentralWidget(self.centralwidget)

class Choice(object):
    def setupUI(self, MainWindow):
        global pk, ppo, pve, pvi, ppl
        pk = 0
        ppo = 0
        pve = 0
        pvi = 0
        ppl = 0
        self.centralwidget = QWidget(MainWindow)
        self.scroll = QScrollArea(self.centralwidget)
        self.widget = QWidget()
        self.vbox = QVBoxLayout()
        self.n = QLabel('Баллы ' + str(ch), self.centralwidget)
        self.n.setGeometry(800, 20, 70, 50)
        self.n.setAlignment(Qt.AlignCenter)
        self.n.setStyleSheet("QLabel"
                             "{color:#ff9900; font:12px bold; font-weight:bold;}")
        self.x = QLabel(zadacha[0])
        self.x.setFixedSize(400, 60)
        self.x.setAlignment(Qt.AlignCenter)
        self.x.setStyleSheet("QLabel"
                                "{color:#ff9900; font:20px bold; font-weight:bold;}")
        self.vbox.addWidget(self.x)

        for i in range(1, 10):
            self.b = QPushButton("Задача " + str(i))
            if zadacha[0] == 'Решетка Кардано':
                if str(i) + '1' in t[0]:
                    self.b.setStyleSheet("QPushButton"
                                    "{border-radius: 30px;"
                                    "color:#0a4761; font:14px bold; font-weight:bold;"
                                    "background-color: rgba(0, 255, 0, 0.5);}"
                                    "QPushButton::hover{"
                                    "background-color: rgba(0, 255, 50, 0.5);}")
                elif str(i) + '2' in t[0]:
                    self.b.setStyleSheet("QPushButton"
                                    "{border-radius: 30px;"
                                    "color:#0a4761; font:14px bold; font-weight:bold;"
                                    "background-color: rgba(255, 0, 0, 0.5);}"
                                    "QPushButton::hover{"
                                    "background-color: rgba(250, 0, 50, 0.5);}")
                else:
                    self.b.setStyleSheet("QPushButton"
                                         "{border-radius: 30px;"
                                         "color:#0a4761; font:14px bold; font-weight:bold;"
                                         "background-color: rgba(102, 255, 255, 0.5);}"
                                         "QPushButton::hover{"
                                         "background-color: rgba(51, 205, 255, 0.5);}")
            if zadacha[0] == 'Шифр Виженера':
                if str(i) + '1' in t[1]:
                    self.b.setStyleSheet("QPushButton"
                                    "{border-radius: 30px;"
                                    "color:#0a4761; font:14px bold; font-weight:bold;"
                                    "background-color: rgba(0, 255, 0, 0.5);}"
                                    "QPushButton::hover{"
                                    "background-color: rgba(0, 255, 50, 0.5);}")
                elif str(i) + '2' in t[1]:
                    self.b.setStyleSheet("QPushButton"
                                    "{border-radius: 30px;"
                                    "color:#0a4761; font:14px bold; font-weight:bold;"
                                    "background-color: rgba(255, 0, 0, 0.5);}"
                                    "QPushButton::hover{"
                                    "background-color: rgba(250, 0, 50, 0.5);}")
                else:
                    self.b.setStyleSheet("QPushButton"
                                         "{border-radius: 30px;"
                                         "color:#0a4761; font:14px bold; font-weight:bold;"
                                         "background-color: rgba(102, 255, 255, 0.5);}"
                                         "QPushButton::hover{"
                                         "background-color: rgba(51, 205, 255, 0.5);}")
            if zadacha[0] == 'Шифр Плейфера':
                if str(i) + '1' in t[2]:
                    self.b.setStyleSheet("QPushButton"
                                    "{border-radius: 30px;"
                                    "color:#0a4761; font:14px bold; font-weight:bold;"
                                    "background-color: rgba(0, 255, 0, 0.5);}"
                                    "QPushButton::hover{"
                                    "background-color: rgba(0, 255, 50, 0.5);}")
                elif str(i) + '2' in t[2]:
                    self.b.setStyleSheet("QPushButton"
                                    "{border-radius: 30px;"
                                    "color:#0a4761; font:14px bold; font-weight:bold;"
                                    "background-color: rgba(255, 0, 0, 0.5);}"
                                    "QPushButton::hover{"
                                    "background-color: rgba(250, 0, 50, 0.5);}")
                else:
                    self.b.setStyleSheet("QPushButton"
                                         "{border-radius: 30px;"
                                         "color:#0a4761; font:14px bold; font-weight:bold;"
                                         "background-color: rgba(102, 255, 255, 0.5);}"
                                         "QPushButton::hover{"
                                         "background-color: rgba(51, 205, 255, 0.5);}")
            if zadacha[0] == 'Шифр Вернама':
                if str(i) + '1' in t[3]:
                    self.b.setStyleSheet("QPushButton"
                                    "{border-radius: 30px;"
                                    "color:#0a4761; font:14px bold; font-weight:bold;"
                                    "background-color: rgba(0, 255, 0, 0.5);}"
                                    "QPushButton::hover{"
                                    "background-color: rgba(0, 255, 50, 0.5);}")
                elif str(i) + '2' in t[3]:
                    self.b.setStyleSheet("QPushButton"
                                    "{border-radius: 30px;"
                                    "color:#0a4761; font:14px bold; font-weight:bold;"
                                    "background-color: rgba(255, 0, 0, 0.5);}"
                                    "QPushButton::hover{"
                                    "background-color: rgba(250, 0, 50, 0.5);}")
                else:
                    self.b.setStyleSheet("QPushButton"
                                         "{border-radius: 30px;"
                                         "color:#0a4761; font:14px bold; font-weight:bold;"
                                         "background-color: rgba(102, 255, 255, 0.5);}"
                                         "QPushButton::hover{"
                                         "background-color: rgba(51, 205, 255, 0.5);}")
            if zadacha[0] == 'Шифр Полибия':
                if str(i) + '1' in t[4]:
                    self.b.setStyleSheet("QPushButton"
                                    "{border-radius: 30px;"
                                    "color:#0a4761; font:14px bold; font-weight:bold;"
                                    "background-color: rgba(0, 255, 0, 0.5);}"
                                    "QPushButton::hover{"
                                    "background-color: rgba(0, 255, 50, 0.5);}")
                elif str(i) + '2' in t[4]:
                    self.b.setStyleSheet("QPushButton"
                                    "{border-radius: 30px;"
                                    "color:#0a4761; font:14px bold; font-weight:bold;"
                                    "background-color: rgba(255, 0, 0, 0.5);}"
                                    "QPushButton::hover{"
                                    "background-color: rgba(250, 0, 50, 0.5);}")
                else:
                    self.b.setStyleSheet("QPushButton"
                                         "{border-radius: 30px;"
                                         "color:#0a4761; font:14px bold; font-weight:bold;"
                                         "background-color: rgba(102, 255, 255, 0.5);}"
                                         "QPushButton::hover{"
                                         "background-color: rgba(51, 205, 255, 0.5);}")

            self.b.setFixedSize(400, 30)
            self.b.clicked.connect(MainWindow.zzz)
            self.vbox.addWidget(self.b)

        self.widget.setLayout(self.vbox)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.scroll.setGeometry(250, 100, 400, 400)
        self.exit3 = QPushButton('назад', self.centralwidget)
        self.exit3.setGeometry(10, 10, 60, 60)
        self.exit3.setStyleSheet("QPushButton"
                                 "{border-radius: 30px;"
                                 "color:#0a4761; font:14px bold; font-weight:bold;"
                                 "background-color: rgba(102, 255, 255, 0.5);}"
                                 "QPushButton::hover{"
                                 "background-color: rgba(51, 205, 255, 0.5);}")

        MainWindow.setCentralWidget(self.centralwidget)

class Kardano(object):
    def setupUI(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)
        flayout = QVBoxLayout(self.centralwidget)
        self.nazv = QLabel('. '.join(zadacha), self.centralwidget)
        self.nazv.setFixedSize(450, 60)
        self.nazv.setAlignment(Qt.AlignCenter)
        self.nazv.setStyleSheet("QLabel"
                                "{color:#ff9900; font:20px bold; font-weight:bold;}")
        self.bpod1 = QPushButton('ПОДСКАЗКА', self.centralwidget)
        self.bpod1.setStyleSheet("QPushButton"
                                   "{border : 3px solid #66ffff;"
                                   "color:#0a4761; font:16px bold; font-weight:bold;"
                                   "background-color: rgba(102, 255, 255, 0.5);}"
                                   "QPushButton::hover{"
                                   "background-color: rgba(51, 205, 255, 0.5);}")
        self.button5 = QPushButton('ПРОВЕРИТЬ', self.centralwidget)
        self.button5.setStyleSheet("QPushButton"
                                   "{border : 3px solid #66ffff;"
                                   "color:#0a4761; font:16px bold; font-weight:bold;"
                                   "background-color: rgba(102, 255, 255, 0.5);}"
                                   "QPushButton::hover{"
                                   "background-color: rgba(51, 205, 255, 0.5);}")
        self.kartinka = QLabel(self.centralwidget)
        d = zadacha[1].split(' ')[1]
        pixmap = QPixmap(f'z{d}_kard.png')
        self.kartinka.setPixmap(pixmap)
        self.kartinka.setFixedSize(450, 200)
        self.textt = QLineEdit(self.centralwidget)
        self.textt.setFixedSize(450, 30)
        self.p = int(d) - 1
        if reshenie[0][self.p] == '*':
            self.textt.setStyleSheet("QLineEdit {background-color: white;}")

        self.textEdit = QPlainTextEdit('Используя знания о шифре Кардано расшифруйте данное сообщение.', self.centralwidget)
        self.textEdit.setFixedSize(450, 50)
        self.textEdit.setReadOnly(True)
        self.textEdit.setStyleSheet("QPlainTextEdit"
                                    "{border : 3px solid #66ffff;"
                                    "background-color: rgba(255, 255, 255); font:14px;}")



        flayout.addWidget(self.nazv)
        flayout.addWidget(self.textEdit)
        flayout.addWidget(self.kartinka)
        flayout.addWidget(self.textt)
        flayout.addWidget(self.bpod1)
        flayout.addWidget(self.button5)
        self.button5.setFixedSize(450, 60)
        self.bpod1.setFixedSize(450, 60)
        flayout.setAlignment(Qt.AlignCenter)
        self.exitk = QPushButton('назад', self.centralwidget)
        self.exitk.setGeometry(10, 10, 60, 60)
        self.exitk.setStyleSheet("QPushButton"
                                "{border-radius: 30px;"
                                "color:#0a4761; font:14px bold; font-weight:bold;"
                                "background-color: rgba(102, 255, 255, 0.5);}"
                                "QPushButton::hover{"
                                "background-color: rgba(51, 205, 255, 0.5);}")
        MainWindow.setCentralWidget(self.centralwidget)

class Pleifer(object):
    def setupUI(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)
        flayout = QVBoxLayout(self.centralwidget)
        self.nazv = QLabel('. '.join(zadacha), self.centralwidget)
        self.nazv.setFixedSize(450, 60)
        self.nazv.setAlignment(Qt.AlignCenter)
        self.button4 = QPushButton('ПРОВЕРИТЬ', self.centralwidget)
        self.button4.setStyleSheet("QPushButton"
                                   "{border : 3px solid #66ffff;"
                                   "color:#0a4761; font:16px bold; font-weight:bold;"
                                   "background-color: rgba(102, 255, 255, 0.5);}"
                                   "QPushButton::hover{"
                                   "background-color: rgba(51, 205, 255, 0.5);}")

        self.nazv.setStyleSheet("QLabel"
                                "{color:#ff9900; font:20px bold; font-weight:bold;}")

        self.kartinka = QLabel(self.centralwidget)
        d = zadacha[1].split(' ')[1]
        pixmap = QPixmap(f'z{d}_ple.png')
        self.kartinka.setPixmap(pixmap)
        self.kartinka.setFixedSize(450, 200)
        self.kartinka.setAlignment(Qt.AlignCenter)
        self.textt = QLineEdit(self.centralwidget)
        self.textt.setFixedSize(450, 30)
        self.p = int(d) - 1
        if reshenie[2][self.p] == '*':
            self.textt.setStyleSheet("QLineEdit {background-color: white;}")
        self.textEdit = QPlainTextEdit('Используя знания о шифре Плейфера зашифруйте данное сообщение.', self.centralwidget)
        self.textEdit.setFixedSize(450, 50)
        self.textEdit.setReadOnly(True)
        self.textEdit.setStyleSheet("QPlainTextEdit"
                                    "{border : 3px solid #66ffff;"
                                    "background-color: rgba(255, 255, 255); font:14px;}")
        flayout.addWidget(self.nazv)
        flayout.addWidget(self.textEdit)
        flayout.addWidget(self.kartinka)
        flayout.addWidget(self.textt)
        self.bpod3 = QPushButton('ПОДСКАЗКА', self.centralwidget)
        self.bpod3.setStyleSheet("QPushButton"
                                 "{border : 3px solid #66ffff;"
                                 "color:#0a4761; font:16px bold; font-weight:bold;"
                                 "background-color: rgba(102, 255, 255, 0.5);}"
                                 "QPushButton::hover{"
                                 "background-color: rgba(51, 205, 255, 0.5);}")
        self.bpod3.setFixedSize(450, 60)
        flayout.addWidget(self.bpod3)
        flayout.addWidget(self.button4)
        self.button4.setFixedSize(450, 60)

        flayout.setAlignment(Qt.AlignCenter)
        self.exitpl = QPushButton('назад', self.centralwidget)
        self.exitpl.setGeometry(10, 10, 60, 60)
        self.exitpl.setStyleSheet("QPushButton"
                                "{border-radius: 30px;"
                                "color:#0a4761; font:14px bold; font-weight:bold;"
                                "background-color: rgba(102, 255, 255, 0.5);}"
                                "QPushButton::hover{"
                                "background-color: rgba(51, 205, 255, 0.5);}")
        MainWindow.setCentralWidget(self.centralwidget)


class Vigener(object):
    def setupUI(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)
        flayout = QVBoxLayout(self.centralwidget)
        self.nazv = QLabel('. '.join(zadacha), self.centralwidget)
        self.nazv.setFixedSize(450, 60)
        self.nazv.setAlignment(Qt.AlignCenter)
        self.nazv.setStyleSheet("QLabel"
                                "{color:#ff9900; font:20px bold; font-weight:bold;}")
        self.button3= QPushButton('ПРОВЕРИТЬ', self.centralwidget)
        self.button3.setStyleSheet("QPushButton"
                                   "{border : 3px solid #66ffff;"
                                   "color:#0a4761; font:16px bold; font-weight:bold;"
                                   "background-color: rgba(102, 255, 255, 0.5);}"
                                   "QPushButton::hover{"
                                   "background-color: rgba(51, 205, 255, 0.5);}")
        self.kartinka = QLabel(self.centralwidget)
        d = zadacha[1].split(' ')[1]
        pixmap = QPixmap(f'z{d}_vi.png')
        self.kartinka.setPixmap(pixmap)
        self.kartinka.setFixedSize(450, 200)
        self.kartinka.setAlignment(Qt.AlignCenter)
        self.textt = QLineEdit(self.centralwidget)
        self.textt.setFixedSize(450, 30)
        self.p = int(d) - 1
        if reshenie[1][self.p] == '*':
            self.textt.setStyleSheet("QLineEdit {background-color: white;}")

        self.textEdit = QPlainTextEdit('Используя знания о шифре Виженера зашифруйте данное сообщение.', self.centralwidget)
        self.textEdit.setFixedSize(450, 50)
        self.textEdit.setReadOnly(True)
        self.textEdit.setStyleSheet("QPlainTextEdit"
                                    "{border : 3px solid #66ffff;"
                                    "background-color: rgba(255, 255, 255); font:14px;}")
        flayout.addWidget(self.nazv)
        flayout.addWidget(self.textEdit)
        flayout.addWidget(self.kartinka)
        flayout.addWidget(self.textt)
        self.bpod2 = QPushButton('ПОДСКАЗКА', self.centralwidget)
        self.bpod2.setStyleSheet("QPushButton"
                                 "{border : 3px solid #66ffff;"
                                 "color:#0a4761; font:16px bold; font-weight:bold;"
                                 "background-color: rgba(102, 255, 255, 0.5);}"
                                 "QPushButton::hover{"
                                 "background-color: rgba(51, 205, 255, 0.5);}")
        self.bpod2.setFixedSize(450, 60)
        flayout.addWidget(self.bpod2)
        flayout.addWidget(self.button3)
        self.button3.setFixedSize(450, 60)
        flayout.setAlignment(Qt.AlignCenter)
        self.exitvi = QPushButton('назад', self.centralwidget)
        self.exitvi.setGeometry(10, 10, 60, 60)
        self.exitvi.setStyleSheet("QPushButton"
                                "{border-radius: 30px;"
                                "color:#0a4761; font:14px bold; font-weight:bold;"
                                "background-color: rgba(102, 255, 255, 0.5);}"
                                "QPushButton::hover{"
                                "background-color: rgba(51, 205, 255, 0.5);}")
        MainWindow.setCentralWidget(self.centralwidget)

class Vernam(object):
    def setupUI(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)
        flayout = QVBoxLayout(self.centralwidget)
        self.nazv = QLabel('. '.join(zadacha), self.centralwidget)
        self.nazv.setFixedSize(450, 60)
        self.nazv.setAlignment(Qt.AlignCenter)
        self.nazv.setStyleSheet("QLabel"
                                "{color:#ff9900; font:20px bold; font-weight:bold;}")
        self.button2 = QPushButton('ПРОВЕРИТЬ', self.centralwidget)
        self.button2.setStyleSheet("QPushButton"
                                   "{border : 3px solid #66ffff;"
                                   "color:#0a4761; font:16px bold; font-weight:bold;"
                                   "background-color: rgba(102, 255, 255, 0.5);}"
                                   "QPushButton::hover{"
                                   "background-color: rgba(51, 205, 255, 0.5);}")
        self.kartinka = QLabel(self.centralwidget)
        d = zadacha[1].split(' ')[1]
        pixmap = QPixmap(f'z{d}_ve.png')
        self.kartinka.setPixmap(pixmap)
        self.kartinka.setFixedSize(450, 200)
        self.textt = QLineEdit(self.centralwidget)
        self.textt.setFixedSize(450, 30)
        self.p = int(d) - 1
        if reshenie[3][self.p] == '*':
            self.textt.setStyleSheet("QLineEdit {background-color: white;}")
        self.textEdit = QPlainTextEdit('Используя знания о шифре Вернама определите какое сообщение было защифровано.', self.centralwidget)
        self.textEdit.setFixedSize(450, 50)
        self.textEdit.setReadOnly(True)
        self.textEdit.setStyleSheet("QPlainTextEdit"
                                    "{border : 3px solid #66ffff;"
                                    "background-color: rgba(255, 255, 255); font:14px;}")
        flayout.addWidget(self.nazv)
        flayout.addWidget(self.textEdit)
        flayout.addWidget(self.kartinka)
        flayout.addWidget(self.textt)
        self.bpod4 = QPushButton('ПОДСКАЗКА', self.centralwidget)
        self.bpod4.setStyleSheet("QPushButton"
                                 "{border : 3px solid #66ffff;"
                                 "color:#0a4761; font:16px bold; font-weight:bold;"
                                 "background-color: rgba(102, 255, 255, 0.5);}"
                                 "QPushButton::hover{"
                                 "background-color: rgba(51, 205, 255, 0.5);}")
        self.bpod4.setFixedSize(450, 60)
        flayout.addWidget(self.bpod4)
        flayout.addWidget(self.button2)
        self.button2.setFixedSize(450, 60)
        flayout.setAlignment(Qt.AlignCenter)
        self.exitve = QPushButton('назад', self.centralwidget)
        self.exitve.setGeometry(10, 10, 60, 60)
        self.exitve.setStyleSheet("QPushButton"
                                "{border-radius: 30px;"
                                "color:#0a4761; font:14px bold; font-weight:bold;"
                                "background-color: rgba(102, 255, 255, 0.5);}"
                                "QPushButton::hover{"
                                "background-color: rgba(51, 205, 255, 0.5);}")
        MainWindow.setCentralWidget(self.centralwidget)

class Poliby(object):
    def setupUI(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)
        flayout = QVBoxLayout(self.centralwidget)
        self.nazv = QLabel('. '.join(zadacha), self.centralwidget)
        self.nazv.setFixedSize(450, 60)
        self.nazv.setAlignment(Qt.AlignCenter)
        self.nazv.setStyleSheet("QLabel"
                                "{color:#ff9900; font:20px bold; font-weight:bold;}")
        self.button1 = QPushButton('ПРОВЕРИТЬ', self.centralwidget)
        self.button1.setStyleSheet("QPushButton"
                                   "{border : 3px solid #66ffff;"
                                   "color:#0a4761; font:16px bold; font-weight:bold;"
                                   "background-color: rgba(102, 255, 255, 0.5);}"
                                   "QPushButton::hover{"
                                   "background-color: rgba(51, 205, 255, 0.5);}")
        self.kartinka = QLabel(self.centralwidget)
        d = zadacha[1].split(' ')[1]
        pixmap = QPixmap(f'z{d}_po.png')
        self.kartinka.setPixmap(pixmap)
        self.kartinka.setFixedSize(450, 200)
        self.kartinka.setAlignment(Qt.AlignCenter)
        self.textt = QLineEdit(self.centralwidget)
        self.textt.setFixedSize(450, 30)
        self.p = int(d) - 1
        if reshenie[4][self.p] == '*':
            self.textt.setStyleSheet("QLineEdit {background-color: white;}")
        self.textEdit = QPlainTextEdit('Используя знания о шифре Полибия зашифруйте данное сообщение.', self.centralwidget)
        self.textEdit.setFixedSize(450, 50)
        self.textEdit.setReadOnly(True)
        self.textEdit.setStyleSheet("QPlainTextEdit"
                                    "{border : 3px solid #66ffff;"
                                    "background-color: rgba(255, 255, 255); font:14px;}")
        flayout.addWidget(self.nazv)
        flayout.addWidget(self.textEdit)
        flayout.addWidget(self.kartinka)
        flayout.addWidget(self.textt)
        self.bpod5 = QPushButton('ПОДСКАЗКА', self.centralwidget)
        self.bpod5.setStyleSheet("QPushButton"
                                 "{border : 3px solid #66ffff;"
                                 "color:#0a4761; font:16px bold; font-weight:bold;"
                                 "background-color: rgba(102, 255, 255, 0.5);}"
                                 "QPushButton::hover{"
                                 "background-color: rgba(51, 205, 255, 0.5);}")
        self.bpod5.setFixedSize(450, 60)
        flayout.addWidget(self.bpod5)
        flayout.addWidget(self.button1)
        self.button1.setFixedSize(450, 60)
        flayout.setAlignment(Qt.AlignCenter)
        self.exitpo = QPushButton('назад', self.centralwidget)
        self.exitpo.setGeometry(10, 10, 60, 60)
        self.exitpo.setStyleSheet("QPushButton"
                                "{border-radius: 30px;"
                                "color:#0a4761; font:14px bold; font-weight:bold;"
                                "background-color: rgba(102, 255, 255, 0.5);}"
                                "QPushButton::hover{"
                                "background-color: rgba(51, 205, 255, 0.5);}")
        MainWindow.setCentralWidget(self.centralwidget)

class Teoriya(object):
    def setupUI(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName('play')
        self.centralwidget.setStyleSheet('#play{border-image:url(fon2.png);}')
        self.kartinka = QLabel(self.centralwidget)
        pixmap = QPixmap(k)
        self.kartinka.setPixmap(pixmap)
        self.kartinka.setFixedSize(900, 600)
        self.kartinka.setAlignment(Qt.AlignCenter)
        self.exit2 = QPushButton('назад', self.centralwidget)
        self.exit2.setGeometry(10, 10, 60, 60)

        self.exit2.setStyleSheet("QPushButton"
                                 "{border-radius: 30px;"
                                 "color:#0a4761; font:14px bold; font-weight:bold;"
                                 "background-color: rgba(102, 255, 255, 0.5);}"
                                 "QPushButton::hover{"
                                 "background-color: rgba(51, 205, 255, 0.5);}")
        MainWindow.setCentralWidget(self.centralwidget)


class Profil(object):
    def setupUI(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)
        lay2 = QVBoxLayout(self.centralwidget)
        self.ex = QPushButton("Выйти из профиля", self.centralwidget)
        self.ex.setStyleSheet("QPushButton"
                              "{border : 3px solid #66ffff;"
                              "color:#0a4761; font:16px bold; font-weight:bold;"
                              "background-color: rgba(102, 255, 255, 0.5);}"
                              "QPushButton::hover{"
                              "background-color: rgba(51, 205, 255, 0.5);}")

        self.ex.setFixedSize(300, 50)
        self.kartinka = QLabel(self.centralwidget)
        pixmap = QPixmap('profil.png')
        self.kartinka.setPixmap(pixmap)
        self.kartinka.setFixedSize(300, 100)
        self.kartinka.setAlignment(Qt.AlignCenter)
        self.label_name = QLabel(name_player, self.centralwidget)
        self.label_name.setStyleSheet("QLabel"
                                      "{color:#ff9900; font:16px bold; font-weight:bold;}")
        self.label_name.setAlignment(Qt.AlignCenter)
        self.label_password = QLabel('Количество накопленных баллов:  ' + str(polzovatel[2]), self.centralwidget)
        self.label_password.setStyleSheet("QLabel"
                                          "{color:#ff9900; font:16px bold; font-weight:bold;}")
        self.label_password.setAlignment(Qt.AlignCenter)
        lay2.addWidget(self.kartinka)
        lay2.addWidget(self.label_name)
        lay2.addWidget(self.label_password)
        lay2.addWidget(self.ex)
        lay2.setAlignment(Qt.AlignCenter)
        self.exitt = QPushButton('назад', self.centralwidget)
        self.exitt.setGeometry(10, 10, 60, 60)
        self.exitt.setStyleSheet("QPushButton"
                                 "{border-radius: 30px;"
                                 "color:#0a4761; font:14px bold; font-weight:bold;"
                                 "background-color: rgba(102, 255, 255, 0.5);}"
                                 "QPushButton::hover{"
                                 "background-color: rgba(51, 205, 255, 0.5);}")
        MainWindow.setCentralWidget(self.centralwidget)


def fix():
    c = sqlite3.connect('users.sqlite')
    cursor = c.cursor()
    a1 = ', '.join(t[0])
    a2 = ', '.join(t[1])
    a3 = ', '.join(t[2])
    a4 = ', '.join(t[3])
    a5 = ', '.join(t[4])
    cursor.execute('UPDATE u SET rez = ? WHERE name = ?',(ch, name_player))
    cursor.execute('UPDATE u SET z1 = ?,z2 = ?,z3 = ?,z4 = ?,z5 = ? WHERE name = ?', (a1, a2, a3, a4, a5, name_player))
    c.commit()
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setFixedSize(900, 600)
        self.center()
        self.setWindowTitle("CryptoQuest")
        self.setObjectName('f')
        self.setStyleSheet('#f{border-image:url(fon.png);}')
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(152, 230, 255))
        self.setPalette(palette)
        self.uiWindow = Window_osnownoe()
        self.uiToolTab = Vhod_polzovatel()
        self.uiObytchenie = Window_obytchenie()
        self.play = Play()
        self.teoriya = Teoriya()
        self.profil = Profil()
        self.chouse = Choice()
        self.kardano = Kardano()
        self.pleifer = Pleifer()
        self.vigener = Vigener()
        self.vernam = Vernam()
        self.poliby = Poliby()
        self.reiting = Reiting()
        self.startWindow()

    def closeEvent(self, event):
        if fl_profil:
            fix()
        event.accept()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def reting(self):

        self.reiting.setupUI(self)
        self.reiting.exit.clicked.connect(self.startWindow)
        self.show()

    def zk(self):
        self.kardano.setupUI(self)
        self.kardano.exitk.clicked.connect(self.ch)
        self.kardano.button5.clicked.connect(self.prov)
        self.kardano.bpod1.clicked.connect(self.podskazka)
        self.show()

    def zple(self):
        self.pleifer.setupUI(self)
        self.pleifer.exitpl.clicked.connect(self.ch)
        self.pleifer.button4.clicked.connect(self.prov)
        self.pleifer.bpod3.clicked.connect(self.podskazka)
        self.show()

    def zvi(self):
        self.vigener.setupUI(self)
        self.vigener.exitvi.clicked.connect(self.ch)
        self.vigener.button3.clicked.connect(self.prov)
        self.vigener.bpod2.clicked.connect(self.podskazka)
        self.show()

    def zpo(self):
        self.poliby.setupUI(self)
        self.poliby.exitpo.clicked.connect(self.ch)
        self.poliby.button1.clicked.connect(self.prov)
        self.poliby.bpod5.clicked.connect(self.podskazka)
        self.show()

    def zve(self):
        self.vernam.setupUI(self)
        self.vernam.exitve.clicked.connect(self.ch)
        self.vernam.button2.clicked.connect(self.prov)
        self.vernam.bpod4.clicked.connect(self.podskazka)
        self.show()


    def oshibka(self):
        name = self.uiToolTab.lineEdit_name.text()
        password = self.uiToolTab.lineEdit_password.text()
        d = proverka(password, name)
        if d == 'Вы успешно заригистрированы':
            registratcia(name, password)

            QMessageBox.information(
                self, 'Error', d)
        else:
            QMessageBox.warning(
                self, 'Error', d)

    def vhod_v_sistemy(self):
        name = self.uiToolTab.lineEdit_name.text()
        password = self.uiToolTab.lineEdit_password.text()
        s = proverka_vhod(name, password)
        if s == 'Вы вошли в систему':
            QMessageBox.information(
                self, 'Error', s)
            global name_player, fl_profil
            fl_profil = True
            name_player = name
            self.prof()
            self.show()
        else:
            QMessageBox.warning(
                self, 'Error', s)

    def exx(self):
        global fl_profil
        fl_profil = False
        fix()
        self.startUIToolTab()

    def prof(self):
        self.profil.setupUI(self)
        self.profil.exitt.clicked.connect(self.startWindow)
        self.profil.ex.clicked.connect(self.exx)
        self.show()

    def ch(self):
        button = QApplication.instance().sender()
        aaa = button.text()
        if aaa != 'назад':
            global zadacha
            zadacha[0] = aaa
        self.chouse.setupUI(self)
        self.chouse.exit3.clicked.connect(self.plaing)
        self.show()

    def zzz(self):
        button = QApplication.instance().sender()
        k = button.text()
        global zadacha
        zadacha[1] = k
        if 'Решетка Кардано' == zadacha[0]:
            self.zk()
        elif 'Шифр Плейфера' == zadacha[0]:
            self.zple()
        elif 'Шифр Виженера' == zadacha[0]:
            self.zvi()
        elif 'Шифр Вернама' == zadacha[0]:
            self.zve()
        elif 'Шифр Полибия' == zadacha[0]:
            self.zpo()

    def plaing(self):
        self.play.setupUI(self)
        self.play.exit3.clicked.connect(self.startWindow)
        self.play.button1.clicked.connect(self.ch)
        self.play.button2.clicked.connect(self.ch)
        self.play.button3.clicked.connect(self.ch)
        self.play.button4.clicked.connect(self.ch)
        self.play.button5.clicked.connect(self.ch)
        self.show()

    def reading(self):
        button = QApplication.instance().sender()
        k = sozt(button.text())
        self.teoriya.setupUI(self)
        self.teoriya.exit2.clicked.connect(self.obytchenie)

        self.show()


    def prov(self):
        global t, protcent, ch, otvets
        v = proverka_reshenie()
        if zadacha[0] == 'Решетка Кардано':
            h = self.kardano.textt.text()
            if h == v[0][1]:
                t[0].append(zadacha[1].split(' ')[1] + '1')
                self.kardano.textt.setStyleSheet("QLineEdit {background-color: green;}")
                if zadacha[1].split(' ')[1] + h not in otvets[0]:
                    protcent[0] += 10
                    ch += 10
                    otvets[0].append(zadacha[1].split(' ')[1] + h)
            else:
                t[0].append(zadacha[1].split(' ')[1] + '2')
                self.kardano.textt.setStyleSheet("QLineEdit {background-color: red;}")
        if zadacha[0] == 'Шифр Плейфера':
            h = self.pleifer.textt.text()
            if h == v[0][1]:
                if zadacha[1].split(' ')[1] + h not in otvets[0]:
                    protcent[2] += 10
                    ch += 10
                    otvets[2].append(zadacha[1].split(' ')[1] + h)
                t[2].append(zadacha[1].split(' ')[1] + '1')
                self.pleifer.textt.setStyleSheet("QLineEdit {background-color: green;}")
            else:
                t[2].append(zadacha[1].split(' ')[1] + '2')
                self.pleifer.textt.setStyleSheet("QLineEdit {background-color: red;}")
        if zadacha[0] == 'Шифр Виженера':
            h = self.vigener.textt.text()
            if h == v[0][1]:
                if zadacha[1].split(' ')[1] + h not in otvets[0]:
                    protcent[1] += 10
                    ch += 10
                    otvets[1].append(zadacha[1].split(' ')[1] + h)
                t[1].append(zadacha[1].split(' ')[1] + '1')
                self.vigener.textt.setStyleSheet("QLineEdit {background-color: green;}")
            else:
                t[1].append(zadacha[1].split(' ')[1] + '2')
                self.vigener.textt.setStyleSheet("QLineEdit {background-color: red;}")
        elif zadacha[0] == 'Шифр Вернама':
            h = self.vernam.textt.text()
            if h == v[0][1]:
                if zadacha[1].split(' ')[1] + h not in otvets[0]:
                    protcent[3] += 10
                    ch += 10
                    otvets[3].append(zadacha[1].split(' ')[1] + h)
                t[3].append(zadacha[1].split(' ')[1] + '1')
                self.vernam.textt.setStyleSheet("QLineEdit {background-color: green;}")
            else:
                t[3].append(zadacha[1].split(' ')[1] + '2')
                self.vernam.textt.setStyleSheet("QLineEdit {background-color: red;}")
        elif zadacha[0] == 'Шифр Полибия':
            h = self.poliby.textt.text()
            if h == v[0][1]:
                if zadacha[1].split(' ')[1] + h not in otvets[0]:
                    protcent[4] += 10
                    ch += 10
                    otvets[4].append(zadacha[1].split(' ')[1] + h)
                t[4].append(zadacha[1].split(' ')[1] + '1')
                self.poliby.textt.setStyleSheet("QLineEdit {background-color: green;}")
            else:
                t[4].append(zadacha[1].split(' ')[1] + '2')
                self.poliby.textt.setStyleSheet("QLineEdit {background-color: red;}")


    def podskazka(self):
        x = proverka_reshenie()[0][1]
        global pk, ppl, pvi, pve, ppo, ch
        if ch >= 10:
            if zadacha[0] == 'Решетка Кардано':
                self.kardano.textt.setText(x[:(pk + 1)])
                pk += 1
            elif zadacha[0] == 'Шифр Виженера':
                self.vigener.textt.setText(x[:(pvi + 1)])
                pvi += 1
            elif zadacha[0] == 'Шифр Плейфера':
                self.pleifer.textt.setText(x[:(ppl + 1)])
                ppl += 1
            elif zadacha[0] == 'Шифр Вернама':
                self.vernam.textt.setText(x[:(pve + 1)])
                pve += 1
            elif zadacha[0] == 'Шифр Полибия':
                self.poliby.textt.setText(str(x)[:(ppo + 1)])
                ppo += 1
            ch -= 10
        else:
            QMessageBox.warning(
                self, 'Error', 'Недостаточно баллов для подсказки')

    def startUIToolTab(self):
        self.uiToolTab.setupUI(self)
        self.uiToolTab.exit.clicked.connect(self.startWindow)
        self.uiToolTab.CPSBTN.clicked.connect(self.oshibka)
        self.uiToolTab.vhod.clicked.connect(self.vhod_v_sistemy)

        self.show()

    def obytchenie(self):
        self.uiObytchenie.setupUI(self)
        self.uiObytchenie.exit.clicked.connect(self.startWindow)
        self.uiObytchenie.button1.clicked.connect(self.reading)
        self.uiObytchenie.button2.clicked.connect(self.reading)
        self.uiObytchenie.button3.clicked.connect(self.reading)
        self.uiObytchenie.button4.clicked.connect(self.reading)
        self.uiObytchenie.button5.clicked.connect(self.reading)
        self.show()

    def ddd(self):
        if fl_profil:
            self.prof()
        else:
            self.startUIToolTab()

    def startWindow(self):
        self.uiWindow.setupUI(self)
        self.uiWindow.b1.clicked.connect(self.ddd)
        self.uiWindow.b2.clicked.connect(self.obytchenie)
        self.uiWindow.b3.clicked.connect(self.plaing)
        self.uiWindow.b4.clicked.connect(self.reting)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindow()
    sys.exit(app.exec_())
