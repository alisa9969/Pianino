import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import Qt
from functools import partial
from PyQt5 import QtCore, QtMultimedia


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('piano.ui', self)
        self.do_2.clicked.connect(partial(self.f, 'do.mp3'))
        self.do2.clicked.connect(partial(self.f, 'do2.mp3'))
        self.fa.clicked.connect(partial(self.f, 'fa.mp3'))
        self.mi.clicked.connect(partial(self.f, 'mi.mp3'))
        self.si.clicked.connect(partial(self.f, 'si.mp3'))
        self.la.clicked.connect(partial(self.f, 'la.mp3'))
        self.re.clicked.connect(partial(self.f, 're.mp3'))
        self.sol.clicked.connect(partial(self.f, 'sol.mp3'))
        self.dodiez.clicked.connect(partial(self.f, 'dd.mp3'))
        self.rediez.clicked.connect(partial(self.f, 'rd.mp3'))
        self.fadiez.clicked.connect(partial(self.f, 'fd.mp3'))
        self.ladiez.clicked.connect(partial(self.f, 'ld.mp3'))
        self.soldiez.clicked.connect(partial(self.f, 'sd.mp3'))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A:
            self.f('do.mp3')
        if event.key() == Qt.Key_K:
            self.f('do2.mp3')
        if event.key() == Qt.Key_S:
            self.f('re.mp3')
        if event.key() == Qt.Key_D:
            self.f('mi.mp3')
        if event.key() == Qt.Key_F:
            self.f('fa.mp3')
        if event.key() == Qt.Key_G:
            self.f('sol.mp3')
        if event.key() == Qt.Key_H:
            self.f('la.mp3')
        if event.key() == Qt.Key_J:
            self.f('si.mp3')
        if event.key() == Qt.Key_Q:
            self.f('dd.mp3')
        if event.key() == Qt.Key_W:
            self.f('rd.mp3')
        if event.key() == Qt.Key_E:
            self.f('fd.mp3')
        if event.key() == Qt.Key_R:
            self.f('ld.mp3')
        if event.key() == Qt.Key_T:
            self.f('sd.mp3')

    def f(self, m):
        media = QtCore.QUrl.fromLocalFile(m)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(QtMultimedia.QMediaContent(media))
        self.player.play()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
