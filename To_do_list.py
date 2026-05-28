from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(660, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabTasks = QtWidgets.QTabWidget(self.centralwidget)
        self.tabTasks.setGeometry(QtCore.QRect(10, 9, 651, 601))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabTasks.setFont(font)
        self.tabTasks.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabTasks.setTabsClosable(False)
        self.tabTasks.setMovable(True)
        self.tabTasks.setObjectName("tabTasks")
        self.currentTasks = QtWidgets.QWidget()
        self.currentTasks.setObjectName("currentTasks")
        self.toDoButton = QtWidgets.QPushButton(self.currentTasks, clicked= self.add_task)
        self.toDoButton.setGeometry(QtCore.QRect(10, 70, 121, 41))
        self.toDoButton.setObjectName("toDoButton")
        self.inProgressButton = QtWidgets.QPushButton(self.currentTasks, clicked = self.move_task_progress)
        self.inProgressButton.setGeometry(QtCore.QRect(250, 70, 121, 41))
        self.inProgressButton.setObjectName("inProgressButton")
        self.DoneButton = QtWidgets.QPushButton(self.currentTasks, clicked= self.move_task_done)
        self.DoneButton.setGeometry(QtCore.QRect(500, 70, 121, 41))
        self.DoneButton.setObjectName("DoneButton")
        self.deleteTskButton = QtWidgets.QPushButton(self.currentTasks, clicked = self.delete_task)
        self.deleteTskButton.setGeometry(QtCore.QRect(10, 510, 121, 41))
        self.deleteTskButton.setObjectName("deleteTskButton")
        self.clearButton = QtWidgets.QPushButton(self.currentTasks, clicked =self.clear_tasks)
        self.clearButton.setGeometry(QtCore.QRect(140, 510, 121, 41))
        self.clearButton.setObjectName("clearButton")
        self.toDoLabel = QtWidgets.QListWidget(self.currentTasks)
        self.toDoLabel.setGeometry(QtCore.QRect(10, 130, 191, 361))
        self.toDoLabel.setObjectName("toDoLabel")
        self.inProgressLabel = QtWidgets.QListWidget(self.currentTasks)
        self.inProgressLabel.setGeometry(QtCore.QRect(220, 130, 191, 361))
        self.inProgressLabel.setObjectName("inProgressLabel")
        self.doneLabel = QtWidgets.QListWidget(self.currentTasks)
        self.doneLabel.setGeometry(QtCore.QRect(430, 130, 191, 361))
        self.doneLabel.setObjectName("doneLabel")
        self.lineEdit = QtWidgets.QLineEdit(self.currentTasks)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 611, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.tabTasks.addTab(self.currentTasks, "")
        self.historyTasks = QtWidgets.QWidget()
        self.historyTasks.setObjectName("historyTasks")
        self.historyTasks_2 = QtWidgets.QListWidget(self.historyTasks)
        self.historyTasks_2.setGeometry(QtCore.QRect(10, 40, 621, 491))
        self.historyTasks_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.historyTasks_2.setObjectName("historyTasks_2")
        self.tabTasks.addTab(self.historyTasks, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 675, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabTasks.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#============================================================== Assign unique object names===========================

        self.DoneButton.setObjectName("doneButton")
        self.toDoButton.setObjectName("toDoButton")
        self.inProgressButton.setObjectName("inProgressButton")
        self.deleteTskButton.setObjectName("deleteButton")
        self.clearButton.setObjectName("clearButton")
        self.toDoLabel.setObjectName("toDoLabel")
        self.inProgressLabel.setObjectName("inProgressLabel")
        self.doneLabel.setObjectName("doneLabel")
        self.historyTasks_2.setObjectName("historyTasks_2")

#============================================================== Methods ============================================
    def clear_input(self):
        self.lineEdit.setText("")

    def add_task(self):
        enteredTask = self.lineEdit.text()
        if enteredTask == "":
            QMessageBox.warning(None, "Error", "Please enter a valid value")
        else: 
            self.toDoLabel.addItem(enteredTask)
            self.clear_input()

    def move_task_progress(self):
        # print(self.toDoLabel.currentRow())
        selectedItems = self.toDoLabel.selectedItems()
        if selectedItems:
            selectedItem = selectedItems[0]
            self.inProgressLabel.addItem(selectedItem.text())
            self.delete_to_do_task()
        else:
            QMessageBox.warning(None, "Error", "No item selected")

    def move_task_done(self):
            selectedItems = self.inProgressLabel.selectedItems()
            if selectedItems:
                selectedItem = selectedItems[0]
                self.doneLabel.addItem(selectedItem.text())
                # print(selectedItem.text())
                self.delete_progress_task()
            else:
                QMessageBox.warning(None, "Error", "No item selected")

            # print("hello")

    def delete_to_do_task(self):
        indexItem = self.toDoLabel.currentRow()
        if indexItem >= 0:
            self.toDoLabel.takeItem(indexItem)
        else:
            QMessageBox.warning(None, "Error", "No item selected")
    
    def delete_progress_task(self):
        indexItem = self.inProgressLabel.currentRow()
        if indexItem >= 0:
            self.inProgressLabel.takeItem(indexItem)
        else:
            QMessageBox.warning(None, "Error", "No item selected")
        
    def delete_task(self):
        indexItem = self.toDoLabel.currentRow()
        if indexItem >= 0:
            reply = QMessageBox.question(None, "Confirm action", "Are you sure you want to delete this task?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.toDoLabel.takeItem(indexItem)
        else:
            QMessageBox.warning(None, "Error", "No item selected")

    def clear_tasks(self):

        listTaks = []
        reply = QMessageBox.question(None, "Confirm action", "Are you sure you want to delete all tasks?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:

            for i in range(self.doneLabel.count()):
                item = self.doneLabel.item(i)
                self.historyTasks_2.addItem(item.text())

            self.doneLabel.clear()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toDoButton.setText(_translate("MainWindow", "To do"))
        self.inProgressButton.setText(_translate("MainWindow", "In progress"))
        self.DoneButton.setText(_translate("MainWindow", "Done"))
        self.deleteTskButton.setText(_translate("MainWindow", "Delete Task"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.tabTasks.setTabText(self.tabTasks.indexOf(self.currentTasks), _translate("MainWindow", "Current tasks"))
        self.tabTasks.setTabText(self.tabTasks.indexOf(self.historyTasks), _translate("MainWindow", "History tasks"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())
    MainWindow.show()
    sys.exit(app.exec_())