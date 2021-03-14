from PyQt5.Qt import *
import sys
import urllib.request


class DF (QDialog):
    def __init__(self):
        QDialog.__init__(self)
        layout = QVBoxLayout()

        self.url = QLineEdit()
        self.Location = QLineEdit()
        self.Progress = QProgressBar()
        btn_download = QPushButton("Download")

        self.Progress.setValue(0)
        self.Progress.setAlignment(Qt.AlignHCenter)

        self.url.setPlaceholderText("URL")
        self.Location.setPlaceholderText("File location")

        layout.addWidget(self.url)
        layout.addWidget(self.Location)
        layout.addWidget(self.Progress)
        layout.addWidget(btn_download)

        self.setLayout(layout)
        self.setWindowTitle("File Downloader")
        self.setFocus()

        btn_download.clicked.connect(self.download)



    def download(self):
        l_url = self.url.text()
        l_location = self.Location.text()

        try:
            urllib.request.urlretrieve(l_url, l_location)
        except Exception:
            QMessageBox.warning(self, "Warning", "The download failed")
            self.Progress.setValue(0)
            self.url.setText("")
            self.location.setText("")
            return

        QMessageBox.information(self, "information", "The download is complete")
        self.Progress.setValue(0)
        self.url.setText("")
        self.location.setText("")
        
    def report(self, blockmun, blocksize, totalsize):

        result = blockmun * blocksize

        if totalsize > 0:
            percent = result * 100 / totalsize
            self.Progress.setValue(int(percent))


app = QApplication(sys.argv)

dialog = DF()

dialog.show()

app.exec_()