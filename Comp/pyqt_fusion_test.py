from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class UiObject(QDialog):
    def __init__(self, parent=None):
        super(UiObject, self).__init__(parent=None)
        self.setWindowTitle("Fusion QT Test")
        
        main_ui_layout = QGridLayout()
        
        shot_label = QLabel(self)
        shot_label.setText("Shot Name")
        main_ui_layout.addWidget(shot_label, 0, 0)
        
        shot_lineedit = QLineEdit(self)
        shot_lineedit.setPlaceholderText("XX_xxxx")
        main_ui_layout.addWidget(shot_lineedit, 0, 1)
        
        
        loader_pushbutton = QPushButton(self)
        loader_pushbutton.setText("Add Loader")
        loader_pushbutton.clicked.connect(self.add_loaders_to_comp)
        main_ui_layout.addWidget(loader_pushbutton, 1, 1)
        
        
        self.setLayout(main_ui_layout)
        
    def add_loaders_to_comp(self):
        comp.Lock()
        
        comp.AddTool("Loader")

        comp.Unlock()
        

def main():
    app = QApplication(sys.argv)
    window = UiObject()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()