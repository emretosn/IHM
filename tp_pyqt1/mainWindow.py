import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

"""
    Q1: Pour pouvoir exécuter notre code, nous devons être dans le même chemin que notre code, 
    nous devons donc cd dans le dossier dans lequel se trouve le fichier. Si nous exécutons le programme, 
    le message print() s'affiche sur la console.
    Q2.1: ?
    Q2.2: On doit rajouter QApplication
    Q4: On les relie par triggered.connect(self.*)
    Q6: On doit créer une fonction d'edition
"""
    
class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()

        openAct = QAction(QIcon("open.png"),'&Open...', self)
        openAct.setShortcut("Ctrl+O")
        openAct.setStatusTip('Open ')
        openAct.setToolTip('Open ')
        openAct.triggered.connect(self.openFile)
        
        saveAct = QAction(QIcon("save.png"),'&Save...', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('Save ')
        saveAct.setToolTip('Save ')
        saveAct.triggered.connect(self.saveFile)
        
        copyAct = QAction(QIcon("copy.png"),'&Copy...', self)
        copyAct.setShortcut('Ctrl+C')
        copyAct.setStatusTip('Copy ')
        copyAct.setToolTip('Copy ')
        
        quitAct = QAction(QIcon("quit.png"),'&Quit...', self)
        quitAct.setShortcut('Ctrl+Q')
        quitAct.setStatusTip('Exit ')
        quitAct.setToolTip('Exit ')
        quitAct.triggered.connect(self.quitApp)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(copyAct)
        fileMenu.addAction(quitAct)
        
        self.toolbar = self.addToolBar('Open')
        self.toolbar.addAction(openAct)

        self.toolbar = self.addToolBar('Save')
        self.toolbar.addAction(saveAct)

        self.toolbar = self.addToolBar('Copy')
        self.toolbar.addAction(copyAct)
        
        self.toolbar = self.addToolBar('Quit')
        self.toolbar.addAction(quitAct)

        self.text_edit()

    def text_edit(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        
    def openFile(self):
        fileName = QFileDialog.getOpenFileName(self, "Open File", "","(*.txt);;( *.html)")
        print(fileName[0])
        self.text_edit()
        file = QFile(fileName[0])
        file.open(QFile.ReadOnly | QFile.Text)
        f_text = QTextStream(file).readAll()
        self.textEdit.setHtml(f_text)

    def saveFile(self):
        fileName = QFileDialog.getSaveFileName(self, "Save File", "", "(*.txt);;( *.html)")
        print(fileName[0])
        file = open(fileName[0],'w')
        text = self.textEdit.setHtml()
        file.write(text)
        file.close()

    def quitApp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Quit App")
        msg.setText("Quit?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        answer = msg.exec()
        if answer == QMessageBox.Yes:
            QCoreApplication.quit()
        else:
            self.close    
        
    def closeEvent(self, event):
        msg = QMessageBox()
        msg.setWindowTitle("Quit App")
        msg.setText("Quit?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        answer = msg.exec()
        if answer == QMessageBox.No:
           event.ignore()
        else:  
            event.accept()

def main(args):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(200,200)
    window.show()
    app.exec() 

if __name__ == "__main__":
    args = sys.argv
    main(args)

    
    
    
    