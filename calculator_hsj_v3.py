import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic  # .ui 불러오기
import math

from_class = uic.loadUiType("/home/hsj/dev_ws/pyqt/src/calculator_hsj_v3.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Calculator")

        # 0 ~ 9 버튼
        self.pushButton_0.clicked.connect(lambda: self.user_input("0"))
        self.pushButton_1.clicked.connect(lambda: self.user_input("1"))
        self.pushButton_2.clicked.connect(lambda: self.user_input("2"))
        self.pushButton_3.clicked.connect(lambda: self.user_input("3"))
        self.pushButton_4.clicked.connect(lambda: self.user_input("4"))
        self.pushButton_5.clicked.connect(lambda: self.user_input("5"))
        self.pushButton_6.clicked.connect(lambda: self.user_input("6"))
        self.pushButton_7.clicked.connect(lambda: self.user_input("7"))
        self.pushButton_8.clicked.connect(lambda: self.user_input("8"))
        self.pushButton_9.clicked.connect(lambda: self.user_input("9"))

        # 괄호
        self.pushButton_open_par.clicked.connect(lambda: self.user_input("("))
        self.pushButton_close_par.clicked.connect(lambda: self.user_input(")"))

        # 사칙연산 버튼
        self.pushButton_plus.clicked.connect(self.btn_plus)
        self.pushButton_minus.clicked.connect(self.btn_minus)
        self.pushButton_mul.clicked.connect(self.btn_mul)
        self.pushButton_div.clicked.connect(self.btn_div)
        
        # ANS 버튼 (최신 결과 값)
        self.pushButton_answer.clicked.connect(self.display_ans)

        # 입력창 초기화 버튼
        self.pushButton_clear.clicked.connect(self.clear)

        # = 버튼
        self.pushButton_equal.clicked.connect(self.calculate_result)

        # 소수점, log, pi, root, square 버튼
        self.pushButton_point.clicked.connect(self.btn_point)
        self.pushButton_log.clicked.connect(self.btn_log)
        self.pushButton_pi.clicked.connect(self.btn_pi)
        self.pushButton_root.clicked.connect(self.btn_root)
        self.pushButton_square.clicked.connect(self.btn_square)

    # 유저로 받은 입력 값을 출력
    def user_input(self, text):
        current_text = self.lineEdit_input.text()
        new_text = current_text + text
        self.lineEdit_input.setText(new_text)

    # eval() 함수를 통해 계산
    def calculate_result(self):
        try:
            problem = self.lineEdit_input.text()
            expression = self.lineEdit_input.text()
            expression = expression.replace('√','math.sqrt')
            expression = expression.replace('log','math.log')
            expression = expression.replace('π','math.pi')
            expression = expression.replace('^','**')

            result = round(eval(expression),4)
            self.ans = str(result)
            self.textEdit_2.append(f'{problem} = {str(result)}')

        except Exception as e:
            self.lineEdit_input.setText('Error: Press Clear Button')

    # 가장 최근 결과값 저장 
    def display_ans(self):
        if self.ans is not None:
            self.lineEdit_input.setText(str(self.ans))
        else:
            self.lineEdit_input.setText('No data: Press Clear Button')

# 버튼에 대한 함수

    ## 여러번 눌러도 상관 없는 버튼
    def clear(self):
        self.lineEdit_input.setText("")

    def btn_pi(self):
        self.lineEdit_input.setText(self.lineEdit_input.text() + '(π)')
    
    def btn_log(self):
        self.lineEdit_input.setText(self.lineEdit_input.text() + 'log(')

    def btn_root(self):
        self.lineEdit_input.setText(self.lineEdit_input.text() + '√(')

    ## 한번만 눌러야 해야하는 버튼

    def btn_square(self):
        if self.lineEdit_input.text() == '':
            pass
        else:
            last_char = self.lineEdit_input.text()[-1]
            if last_char.isdigit() or last_char == ')':
                self.lineEdit_input.setText(self.lineEdit_input.text() + '^(')
            else:
                pass

    def btn_point(self):
        if self.lineEdit_input.text() == '':
            pass
        else:
            last_char = self.lineEdit_input.text()[-1]
            if last_char.isdigit() or last_char == ')':
                self.lineEdit_input.setText(self.lineEdit_input.text() + '.')
            else:
                pass

    def btn_plus(self):
        if self.lineEdit_input.text() == '':
            pass
        else:
            last_char = self.lineEdit_input.text()[-1]
            if last_char.isdigit() or last_char == ')':
                self.lineEdit_input.setText(self.lineEdit_input.text() + '+')
            else:
                pass

    def btn_minus(self):
        if self.lineEdit_input.text() == '':
            pass
        else:
            last_char = self.lineEdit_input.text()[-1]
            if last_char.isdigit() or last_char == ')':
                self.lineEdit_input.setText(self.lineEdit_input.text() + '-')
            else:
                pass

    def btn_div(self):
        if self.lineEdit_input.text() == '':
            pass
        else:
            last_char = self.lineEdit_input.text()[-1]
            if last_char.isdigit() or last_char == ')':
                self.lineEdit_input.setText(self.lineEdit_input.text() + '/')
            else:
                pass

    def btn_mul(self):
        if self.lineEdit_input.text() == '':
            pass
        else:
            last_char = self.lineEdit_input.text()[-1]
            if last_char.isdigit() or last_char == ')':
                self.lineEdit_input.setText(self.lineEdit_input.text() + '*')
            else:
                passjj


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())