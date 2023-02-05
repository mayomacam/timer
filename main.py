# timer for 15 min
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
import sys
import os, time
from plyer import notification

class windows(QWidget):
    def __init__(self, parent):
        super(windows, self).__init__(parent=parent)
        self.parent = parent
        self.count = 0
        self.start = False
        
        button = QPushButton("Set time(s)", self)
        # setting geometry to the push button
        button.setGeometry(80, 10, 150, 40)
        # adding action to the button
        button.clicked.connect(self.get_seconds)
        # creating label to show the seconds
        self.label = QLabel("seconds", self)
        # setting geometry of label
        self.label.setGeometry(60, 80, 200, 50)
        # setting border to the label
        self.label.setStyleSheet("border : 3px solid black")
        # setting font to the label
        self.label.setFont(QFont('Times', 15))
        # setting alignment to the label
        self.label.setAlignment(Qt.AlignCenter)
        # creating start button
        start_button = QPushButton("Start", self)
        # setting geometry to the button
        start_button.setGeometry(80, 160, 150, 40)
        # adding action to the button
        start_button.clicked.connect(self.start_action)
        # creating pause button
        pause_button = QPushButton("Pause", self)
        # setting geometry to the button
        pause_button.setGeometry(80, 200, 150, 40)
        # adding action to the button
        pause_button.clicked.connect(self.pause_action)
        # creating reset  button
        reset_button = QPushButton("Reset", self)
        # setting geometry to the button
        reset_button.setGeometry(80, 240, 150, 40)
        # adding action to the button
        reset_button.clicked.connect(self.reset_action)
        # creating a timer object
        timer = QTimer(self)
        # adding action to timer
        timer.timeout.connect(self.showTime)
        # update the timer every tenth second
        timer.start(100)
        # play sound 
        filename = os.path.abspath("mic_up_sing_success.mp3")
        url = QUrl.fromLocalFile(r""+filename)
        content =QMediaContent(url)
        self.player = QMediaPlayer()
        self.player.setMedia(content)
        self.player.setVolume(50)
        

# method called by timer
    def showTime(self):
        # checking if flag is true
        if self.start:
            # incrementing the counter
            self.count -= 1
            # timer is completed
            if self.count == 0:
                # making flag false
                self.start = False
                # setting text to the label
                self.label.setText("Completed !!!! ")
                title = 'timer'
                message = "timer completed"
                notification.notify(title=title, message=message)
                self.player.play()
        if self.start:
            # getting text from count
            text = str(self.count / 10) + " s"
            # showing text
            self.label.setText(text)
 
 
    # method called by the push button
    def get_seconds(self):
        # making flag false
        self.start = False
        # getting seconds and flag
        second, done = QInputDialog.getInt(self, 'Seconds', 'Enter Seconds:')
        # if flag is true
        if done:
            # changing the value of count
            self.count = second * 10
            # setting text to the label
            self.label.setText(str(second))
 
    def start_action(self):
        # making flag true
        self.start = True
        # count = 0
        if self.count == 0:
            self.start = False
 
    def pause_action(self):
        # making flag false
        self.start = False
 
    def reset_action(self):
        # making flag false
        self.start = False
        # setting count value to 0
        self.count = 0
        # setting label text
        self.label.setText("second")

class UIManager(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        # including Window class
        self.viewer = windows(parent=self)
        self.setCentralWidget(self.viewer)
        self.resize(320, 320)
        self.setWindowTitle('Timer')
        """if 'nt' in os.name:
            self.setWindowIcon(QIcon('icons/download.png'))
        elif 'mac' in os.name:
            self.setWindowIcon(QIcon('icons/download-mac-os.png'))
        else:
            self.setWindowIcon(QIcon('icons/download-linux.png'))"""

        # exit
        exit_act = QAction('Exit', self)
        exit_act.setShortcut('Ctrl+X')
        exit_act.triggered.connect(self.close)

        # Create menubar
        menu_bar = self.menuBar()
        # For MacOS users, places menu bar in main window
        menu_bar.setNativeMenuBar(False)
        # Create file menu and add actions
        menu_bar.addAction(exit_act)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(style_sheet)
    app.setStyle("Fusion")
    window = UIManager()
    window.show()
    sys.exit(app.exec_())