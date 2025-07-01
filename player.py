import pygame
import os
import pickle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QModelIndex
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 840)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        Dialog.setStyleSheet("")
        self.sheet_default = "QPushButton {border-radius:25; border:2px solid black; font-size: 12px} QPushButton:hover {border:2px solid green;}"
        self.sheet_green = "border-radius:25; border:2px solid black; background-color: green"
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 180, 120, 50))
        self.pushButton.setStyleSheet(self.sheet_default)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 390, 120, 50))
        self.pushButton_2.setStyleSheet(self.sheet_default)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 250, 50, 120))
        self.pushButton_3.setStyleSheet(self.sheet_default)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 250, 50, 120))
        self.pushButton_4.setStyleSheet(self.sheet_default)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 240, 140, 140))
        self.pushButton_5.setStyleSheet(self.sheet_default)
        self.pushButton_5.setObjectName("pushButton_5")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(190, 80, 101, 41))
        self.lcdNumber.setStyleSheet("border-radius:10; border: 2px solid black")
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 370, 50, 50))
        self.pushButton_6.setStyleSheet(self.sheet_default)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 370, 50, 50))
        self.pushButton_7.setStyleSheet(self.sheet_default)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(50, 200, 50, 50))
        self.pushButton_8.setStyleSheet(self.sheet_default)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(220, 200, 50, 50))
        self.pushButton_9.setStyleSheet(self.sheet_default)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 140, 261, 22))
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.horizontalSlider.setMouseTracking(False)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider.setTickInterval(5)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMaximum(100)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:10; border: 2px solid black")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 80, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius:10; border: 2px solid black")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 470, 261, 351))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("border: 2px solid black")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # старт окна по центру экрана
        x = (app.desktop().availableGeometry().width() - Dialog.width()) // 2
        y = (app.desktop().availableGeometry().height() - Dialog.height()) // 2
        Dialog.move(x, y)


        # инициализация pygame
        pygame.init()
        pygame.mixer.init()
        self.number_of_song = 0
        self.volume_value = 50
        self.lcdNumber.display(self.volume_value)
        pygame.mixer.music.set_volume(self.volume_value/100)
        
        self.pushButton.clicked.connect(self.pause)
        self.pushButton_2.clicked.connect(self.stop)
        self.pushButton_3.clicked.connect(self.next)
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton_5.clicked.connect(self.play)
        self.pushButton_6.clicked.connect(self.open)
        self.pushButton_7.clicked.connect(self.min_max)
        self.pushButton_9.clicked.connect(self.volume_up)
        self.pushButton_8.clicked.connect(self.volume_down)
        self.horizontalSlider.sliderReleased.connect(self.move)
        self.tableWidget.itemDoubleClicked.connect(self.double_click)

        self.pushButton.pressed.connect(lambda: self.press(self.pushButton))
        self.pushButton.released.connect(lambda: self.releas(self.pushButton))
        self.pushButton_2.pressed.connect(lambda: self.press(self.pushButton_2))
        self.pushButton_2.released.connect(lambda: self.releas(self.pushButton_2))
        self.pushButton_3.pressed.connect(lambda: self.press(self.pushButton_3))
        self.pushButton_3.released.connect(lambda: self.releas(self.pushButton_3))
        self.pushButton_4.pressed.connect(lambda: self.press(self.pushButton_4))
        self.pushButton_4.released.connect(lambda: self.releas(self.pushButton_4))
        self.pushButton_5.pressed.connect(lambda: self.press(self.pushButton_5))
        self.pushButton_5.released.connect(lambda: self.releas(self.pushButton_5))
        self.pushButton_6.pressed.connect(lambda: self.press(self.pushButton_6))
        self.pushButton_6.released.connect(lambda: self.releas(self.pushButton_6))
        self.pushButton_7.pressed.connect(lambda: self.press(self.pushButton_7))
        self.pushButton_7.released.connect(lambda: self.releas(self.pushButton_7))
        self.pushButton_8.pressed.connect(lambda: self.press(self.pushButton_8))
        self.pushButton_8.released.connect(lambda: self.releas(self.pushButton_8))
        self.pushButton_9.pressed.connect(lambda: self.press(self.pushButton_9))
        self.pushButton_9.released.connect(lambda: self.releas(self.pushButton_9))

        # таймер продолжительности трека  
        self.timer = QTimer()
        self.timer.timeout.connect(self.play_timer)

        # таймер обратного отсчета       
        self.timer_cd = QTimer()
        self.timer_cd.timeout.connect(self.countdown)

        # шаг увеличения/уменьшения громкости
        self.delta_volume = 5
        # условие проигрывания трека
        self.click = 0
        # условие изменения размеров окна
        self.close = 0
        # условие загрузки плейлиста
        self.start = 0
        # условие перемещения ползунка во время паузы
        self.move_check = 0

        # получения директории с программой
        self.path = os.getcwd()
        # чтение директории плейлиста из файла
        try:
            with open(self.path+'\playlistdir.pld', "rb") as file:
                directory = pickle.load(file)
            self.open_directory(directory)
        except:
            pass


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Pause"))
        self.pushButton_2.setText(_translate("Dialog", "Stop"))
        self.pushButton_3.setText(_translate("Dialog", "N"))
        self.pushButton_4.setText(_translate("Dialog", "B"))
        self.pushButton_5.setText(_translate("Dialog", "Play"))
        self.pushButton_6.setText(_translate("Dialog", "Open"))
        self.pushButton_7.setText(_translate("Dialog", "Close"))
        self.pushButton_8.setText(_translate("Dialog", "-"))
        self.pushButton_9.setText(_translate("Dialog", "+"))


    # загрузка плейлиста из выбранной директории
    def open_directory(self,directory):
        listdir = os.chdir(directory)
        self.song_list = os.listdir()
        for name in reversed(self.song_list):
            if '.mp3' not in name:
                self.song_list.remove(name)
        if len(self.song_list) == 0:
            self.lineEdit.clear()
            self.lineEdit_2.clear()
        self.start = len(self.song_list)
        self.horizontalSlider.setValue(0)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(len(self.song_list))
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnWidth(0, 270)
        i = 0
        for song in self.song_list:
            self.tableWidget.setItem(i,0, QTableWidgetItem(song))
            i += 1
        self.song_info()
        self.tableWidget.item(0, 0).setBackground(QtGui.QColor("cyan"))
        self.song1 = 0        


    # обработка нажатия кнопки 'Open'
    def open(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory()
        try:
            self.open_directory(directory)
            if len(self.song_list) != 0 :
                with open(self.path+'\playlistdir.pld', "wb") as file:
                    pickle.dump(directory, file)
        except:
            pass


    # получение информации о длине трека
    def song_info(self):
        self.total_time_track = int(pygame.mixer.Sound(self.song_list[self.number_of_song]).get_length())
        if self.horizontalSlider.value() == 0:
            self.total_time_track1 = int(pygame.mixer.Sound(self.song_list[self.number_of_song]).get_length())
            self.play_time = 0
        self.lineEdit.setText(self.song_list[self.number_of_song])
        self.lineEdit.setCursorPosition(0)
        self.condition_cd()


    # отображение обратного отсчета
    def condition_cd(self):
        self.lineEdit_2.setText(f'{self.total_time_track1//60:02}:{self.total_time_track1%60:02} / {self.total_time_track//60:02}:{self.total_time_track%60:02}')


    # обработка нажатия кнопки 'Play'
    def play(self):
        if self.start != 0:
            pygame.mixer.music.load(self.song_list[self.number_of_song])
            pygame.mixer.music.play(start=self.play_time)
            self.song_info()
            self.condition_play()


    # дополнительные условия для кнопоки 'Play'
    def condition_play(self):
        self.click = 1
        self.pushButton.setStyleSheet(self.sheet_default)
        self.pushButton_5.setStyleSheet(self.sheet_green)
        self.timer.start(self.total_time_track*10)
        self.timer_cd.start(1000)

    
    # обработка нажатия кнопки 'Stop'
    def stop(self):
        pygame.mixer.music.stop()
        self.pushButton.setStyleSheet(self.sheet_default)
        self.condition_stop()
        self.click = 0


    # дополнительные условия для кнопоки 'Stop'
    def condition_stop(self):
        self.pushButton_5.setStyleSheet(self.sheet_default)
        self.timer_cd.stop()
        self.timer.stop()


    # обработка нажатия кнопки 'Pause'
    def pause(self):
        if self.click == 1:
            pygame.mixer.music.pause()
            self.pushButton.setStyleSheet(self.sheet_green)
            self.condition_stop()
            self.click = 2
        elif self.click == 2:
            if self.move_check == 0:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.play(start=self.play_time)
            self.condition_play()


    # обработка нажатия кнопки 'N'
    def next(self):
        if self.start != 0:
            self.horizontalSlider.setValue(0)
            self.number_of_song += 1
            if self.number_of_song > len(self.song_list)-1:
                self.number_of_song = 0
            self.tableWidget.item(self.number_of_song, 0).setBackground(QtGui.QColor("cyan"))
            number_of_song1 = self.number_of_song - 1
            if number_of_song1 < 0:
                number_of_song1 = len(self.song_list)-1
            self.condition_button(number_of_song1)
            

    # обработка нажатия кнопки 'B'
    def back(self):
        if self.start != 0:
            self.horizontalSlider.setValue(0)
            self.number_of_song -= 1
            if self.number_of_song < 0:
                self.number_of_song = len(self.song_list)-1
            self.tableWidget.item(self.number_of_song, 0).setBackground(QtGui.QColor("cyan"))
            number_of_song1 = self.number_of_song + 1
            if number_of_song1 > len(self.song_list)-1:
                number_of_song1 = 0
            self.condition_button(number_of_song1)


    # дополнительные условия для кнопок 'N'/'B'
    def condition_button(self, number_of_song1):
        self.tableWidget.item(number_of_song1, 0).setBackground(QtGui.QColor("white"))
        self.song1 = self.number_of_song
        if self.click == 0:
            self.song_info()
        if self.click == 1:
            self.horizontalSlider.setValue(0)
            self.play_time = 0
            self.play()


    # обработка нажатия кнопки 'Close'
    def min_max(self):
        if self.close == 0:
            Dialog.resize(320, 470)
            self.pushButton_7.setStyleSheet(self.sheet_green)
            self.close = 1
        elif self.close == 1:
            self.pushButton_7.setStyleSheet(self.sheet_default)
            self.close = 0
            Dialog.resize(320, 840)
            x = Dialog.geometry().x() - 1
            y = (app.desktop().availableGeometry().height() - Dialog.height()) // 2
            Dialog.move(x, y)


    # обработка нажатия кнопки '+'
    def volume_up(self):
        self.volume_value += self.delta_volume
        if self.volume_value >= 100:
            self.volume_value = 100
        self.volume_lcd()


    # обработка нажатия кнопки '-'
    def volume_down(self):
        self.volume_value -= self.delta_volume
        if self.volume_value <= 0:
            self.volume_value = 0
        self.volume_lcd()


    # вывод уровня громкости
    def volume_lcd(self):
        self.lcdNumber.display(self.volume_value)
        pygame.mixer.music.set_volume(self.volume_value/100)


    # изменение стиля кнопки при наведении курсора
    def press(self, button):
        button.setStyleSheet(self.sheet_green)


    # изменение стиля кнопки при снятии фокуса (курсора)
    def releas(self, button):
        button.setStyleSheet(self.sheet_default)


    # обработка двойного нажатия на таблицу с плейлистом
    def double_click(self):
        self.number_of_song = self.tableWidget.currentRow()
        self.tableWidget.item(self.song1, 0).setBackground(QtGui.QColor("white"))
        self.tableWidget.item(self.number_of_song, 0).setBackground(QtGui.QColor("cyan"))
        self.horizontalSlider.setValue(0)
        self.play_time = 0
        self.song1 = self.number_of_song
        self.tableWidget.setCurrentIndex(QModelIndex())
        self.play()


    # обработка перемещения ползунка слайдера
    def move(self):
        if self.start != 0:
            self.play_time = self.horizontalSlider.value() * self.total_time_track / 100
            if self.total_time_track > self.play_time:
                self.total_time_track1 = self.total_time_track - int(self.play_time)
            else:
                self.total_time_track1 = self.total_time_track1 + int(self.play_time)
            if self.click == 1:
                pygame.mixer.music.stop()
                pygame.mixer.music.play(start=self.play_time)
            elif self.click == 2:
                self.move_check = 1
                self.condition_cd()
            else:
                self.condition_cd()


    # перемещение ползунка, отслеживание конца трека для перехода на следующий
    def play_timer(self):
        self.horizontalSlider.setValue(self.horizontalSlider.value() + 1)
        if self.horizontalSlider.value() == 100:
            self.next()


    # визуализация обратного отсчета
    def countdown(self):
        self.total_time_track1 -= 1
        self.condition_cd()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.setWindowTitle('MP3 player')
    Dialog.show()
    sys.exit(app.exec_())
