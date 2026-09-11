# Это программа на Python
# Импортируем модуль PyQt6
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtGui import QIcon
import os

# Путь к иконке — рядом со скриптом, чтобы находился при любом запуске
ICON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "favicon.jpg")


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

        # Накопленные миллисекунды (для паузы) и монотонный таймер для точного счёта
        self.accumulated_ms = 0
        self.elapsed_timer = QtCore.QElapsedTimer()

        # Создаем виджеты для отображения времени
        # В PyQt6 шрифт задаётся через setFont(), а не аргументом конструктора
        font = QtGui.QFont("Arial", 50)
        self.hours_label = QtWidgets.QLabel("00")
        self.minutes_label = QtWidgets.QLabel("00")
        self.seconds_label = QtWidgets.QLabel("00")
        self.colon1 = QtWidgets.QLabel(":")
        self.colon2 = QtWidgets.QLabel(":")
        for lbl in (self.hours_label, self.minutes_label,
                    self.seconds_label, self.colon1, self.colon2):
            lbl.setFont(font)

        # Создаем кнопки запуска/остановки и сброса
        self.start_button = QtWidgets.QPushButton("Запуск")
        self.reset_button = QtWidgets.QPushButton("Сброс")
        self.start_button.clicked.connect(self.start_stop_time)
        self.reset_button.clicked.connect(self.reset_time)

        # Вертикальный компоновщик для окна
        self.main_layout = QtWidgets.QVBoxLayout()

        # Горизонтальный компоновщик для времени в одной строке
        self.time_layout = QtWidgets.QHBoxLayout()
        self.time_layout.addWidget(self.hours_label)
        self.time_layout.addWidget(self.colon1)
        self.time_layout.addWidget(self.minutes_label)
        self.time_layout.addWidget(self.colon2)
        self.time_layout.addWidget(self.seconds_label)
        self.main_layout.addLayout(self.time_layout)

        # Горизонтальный компоновщик для кнопок, выравниваем по центру
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.addWidget(self.start_button)
        self.button_layout.addWidget(self.reset_button)
        self.button_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addLayout(self.button_layout)

        # Устанавливаем вертикальный компоновщик в окно
        self.setLayout(self.main_layout)

        # Цвет фона окна
        self.setStyleSheet("background-color: #272727;")
        # Цвет и жирность шрифта для виджетов времени
        for lbl in (self.hours_label, self.minutes_label,
                    self.seconds_label, self.colon1, self.colon2):
            lbl.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.reset_button.setStyleSheet("color: #FFFFFF; font-weight: bold;")
        self.start_button.setStyleSheet("color: #FFFFFF; font-weight: bold;")

        # Таймер обновления надписи (счёт идёт по QElapsedTimer, поэтому точность не страдает)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.update_time)

    # Функция обновления отображаемого времени
    def update_time(self):
        total_seconds = (self.accumulated_ms + self.elapsed_timer.elapsed()) // 1000
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60
        self.hours_label.setText(f"{self.hours:02d}")
        self.minutes_label.setText(f"{self.minutes:02d}")
        self.seconds_label.setText(f"{self.seconds:02d}")

    # Функция сброса времени
    def reset_time(self):
        self.timer.stop()
        self.accumulated_ms = 0
        self.hours_label.setText("00")
        self.minutes_label.setText("00")
        self.seconds_label.setText("00")
        self.start_button.setText("Запуск")

    # Функция для запуска и остановки времени
    def start_stop_time(self):
        if not self.timer.isActive():
            self.elapsed_timer.start()
            self.timer.start()
            self.start_button.setText("Стоп")
        else:
            self.accumulated_ms += self.elapsed_timer.elapsed()
            self.timer.stop()
            self.start_button.setText("Запуск")


# Создаем приложение и задаем иконку
app = QtWidgets.QApplication([])
app.setWindowIcon(QIcon(ICON_PATH))

# Создаем и показываем окно секундомера
stopwatch = Stopwatch()
stopwatch.show()

# Запускаем главный цикл приложения
app.exec()
