# Это программа на Python
# Импортируем модуль PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon

# Создаем класс для секундомера
class Stopwatch(QtWidgets.QWidget):
    # Инициализируем класс
    def __init__(self):
        # Вызываем конструктор родительского класса
        super().__init__()
        # Устанавливаем заголовок и размер окна
        self.setWindowTitle("Секундомер")
        self.resize(300, 200)
        # Устанавливаем положение окна ниже и левее
        self.move(3, 625)
        # Создаем переменные для хранения времени
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        # Создаем виджеты для отображения времени
        self.hours_label = QtWidgets.QLabel(str(self.hours), font=QtGui.QFont("Arial", 50))
        self.minutes_label = QtWidgets.QLabel(str(self.minutes), font=QtGui.QFont("Arial", 50))
        self.seconds_label = QtWidgets.QLabel(str(self.seconds), font=QtGui.QFont("Arial", 50))
        self.colon1 = QtWidgets.QLabel(":", font=QtGui.QFont("Arial", 50))
        self.colon2 = QtWidgets.QLabel(":", font=QtGui.QFont("Arial", 50))
        # Создаем кнопку для запуска секундомера
        self.start_button = QtWidgets.QPushButton("Запуск")
        # Создаем кнопку для сброса времени
        self.reset_button = QtWidgets.QPushButton("Сброс")
        # Связываем кнопку с функцией сброса времени
        self.reset_button.clicked.connect(self.reset_time)
        # Создаем кнопку для запуска и остановки времени
        self.start_button = QtWidgets.QPushButton("Запуск")
        # Связываем кнопку с функцией запуска и остановки времени
        self.start_button.clicked.connect(self.start_stop_time)

        # Создаем вертикальный компоновщик для расположения виджетов в окне
        self.layout = QtWidgets.QVBoxLayout()

        # Создаем горизонтальный компоновщик для расположения виджетов времени в одной строке
        self.time_layout = QtWidgets.QHBoxLayout()

        # Добавляем виджеты времени в горизонтальный компоновщик
        self.time_layout.addWidget(self.hours_label)
        self.time_layout.addWidget(self.colon1)
        self.time_layout.addWidget(self.minutes_label)
        self.time_layout.addWidget(self.colon2)
        self.time_layout.addWidget(self.seconds_label)

        # Добавляем горизонтальный компоновщик в вертикальный компоновщик
        self.layout.addLayout(self.time_layout)

        # Создаем горизонтальный компоновщик для расположения кнопок в одной строке
        self.button_layout = QtWidgets.QHBoxLayout()

        # Добавляем кнопки в горизонтальный компоновщик
        self.button_layout.addWidget(self.start_button)
        self.button_layout.addWidget(self.reset_button)

        # Выравниваем по центру горизонтальный компоновщик с кнопками
        self.button_layout.setAlignment(QtCore.Qt.AlignCenter) 

        # Добавляем горизонтальный компоновщик в вертикальный компоновщик
        self.layout.addLayout(self.button_layout)

        # Устанавливаем вертикальный компоновщик в окно
        self.setLayout(self.layout)

        # Устанавливаем цвет фона окна
        self.setStyleSheet("background-color: #272727;")
        # Устанавливаем цвет и жирность шрифта для виджетов времени
        self.hours_label.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.minutes_label.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.seconds_label.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.colon1.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.colon2.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        # Устанавливаем цвет и жирность шрифта для кнопки сброса
        self.reset_button.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        # Устанавливаем цвет и жирность шрифта для кнопки "Запуск"
        self.start_button.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        # Создаем таймер для обновления времени
        self.timer = QtCore.QTimer()
        # Устанавливаем интервал таймера в 1 секунду
        self.timer.setInterval(1000)
        # Связываем таймер с функцией обновления времени
        self.timer.timeout.connect(self.update_time)

    # Определяем функцию для обновления времени
    def update_time(self):
         # Увеличиваем секунды на единицу
         self.seconds += 1
         # Если секунды равны 60, то увеличиваем минуты на единицу и обнуляем секунды
         if self.seconds == 60:
             self.minutes += 1
             self.seconds = 0
             # Если минуты равны 60, то увеличиваем часы на единицу и обнуляем минуты
             if self.minutes == 60:
                 self.minutes = 0
                 self.hours += 1
         # Обновляем текст виджетов времени
         self.hours_label.setText(str(self.hours))
         self.minutes_label.setText(str(self.minutes))
         self.seconds_label.setText(str(self.seconds))

    # Создаем функцию для сброса времени
    def reset_time(self):
         # Останавливаем таймер
         self.timer.stop()
         # Обнуляем все переменные времени
         self.hours = 0
         self.minutes = 0
         self.seconds = 0
         # Обновляем текст виджетов времени
         self.hours_label.setText(str(self.hours))
         self.minutes_label.setText(str(self.minutes))
         self.seconds_label.setText(str(self.seconds))
         # Меняем текст кнопки "Стоп" на "Запуск"
         self.start_button.setText("Запуск")

    # Создаем функцию для запуска и остановки времени
    def start_stop_time(self):
         # Если таймер не запущен
         if not self.timer.isActive():
             # Запускаем таймер
             self.timer.start()
             # Меняем текст кнопки "Запуск" на "Стоп"
             self.start_button.setText("Стоп")
         # Иначе
         else:
             # Останавливаем таймер
             self.timer.stop()
             # Меняем текст кнопки "Стоп" на "Запуск"
             self.start_button.setText("Запуск")

# Создаем приложение PyQt5
app = QtWidgets.QApplication([])

# Задаем иконку приложения из файла favicon.jpg
app.setWindowIcon(QIcon("favicon.jpg"))

# Создаем экземпляр класса секундомера
stopwatch = Stopwatch()

# Создаем объект QLabel
label = QtWidgets.QLabel()

# Задаем иконку окна из файла favicon.jpg
label.setWindowIcon(QIcon("favicon.jpg"))

# Показываем окно секундомера
stopwatch.show()

# Запускаем главный цикл приложения
app.exec_()