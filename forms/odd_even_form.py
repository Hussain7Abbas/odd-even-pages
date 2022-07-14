# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designs/odd_even.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MergeWindow(object):
    def setupUi(self, MergeWindow):
        MergeWindow.setObjectName("MergeWindow")
        MergeWindow.resize(742, 295)
        font = QtGui.QFont()
        font.setPointSize(14)
        MergeWindow.setFont(font)
        MergeWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.mainWidget = QtWidgets.QWidget(MergeWindow)
        self.mainWidget.setObjectName("mainWidget")
        self.merge_btn = QtWidgets.QPushButton(self.mainWidget)
        self.merge_btn.setGeometry(QtCore.QRect(300, 200, 141, 51))
        self.merge_btn.setToolTip("")
        self.merge_btn.setAutoDefault(False)
        self.merge_btn.setFlat(False)
        self.merge_btn.setObjectName("merge_btn")
        self.title_lbl = QtWidgets.QLabel(self.mainWidget)
        self.title_lbl.setGeometry(QtCore.QRect(20, 20, 691, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.title_lbl.setFont(font)
        self.title_lbl.setAutoFillBackground(False)
        self.title_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.title_lbl.setObjectName("title_lbl")
        self.progressBar = QtWidgets.QProgressBar(self.mainWidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 260, 721, 31))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.odd_btn = QtWidgets.QPushButton(self.mainWidget)
        self.odd_btn.setGeometry(QtCore.QRect(600, 80, 121, 31))
        self.odd_btn.setToolTip("")
        self.odd_btn.setAutoDefault(False)
        self.odd_btn.setFlat(False)
        self.odd_btn.setObjectName("odd_btn")
        self.even_btn = QtWidgets.QPushButton(self.mainWidget)
        self.even_btn.setGeometry(QtCore.QRect(600, 120, 121, 31))
        self.even_btn.setToolTip("")
        self.even_btn.setAutoDefault(False)
        self.even_btn.setFlat(False)
        self.even_btn.setObjectName("even_btn")
        self.out_btn = QtWidgets.QPushButton(self.mainWidget)
        self.out_btn.setGeometry(QtCore.QRect(600, 160, 121, 31))
        self.out_btn.setToolTip("")
        self.out_btn.setAutoDefault(False)
        self.out_btn.setFlat(False)
        self.out_btn.setObjectName("out_btn")
        self.count_lbl = QtWidgets.QLabel(self.mainWidget)
        self.count_lbl.setGeometry(QtCore.QRect(10, 230, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.count_lbl.setFont(font)
        self.count_lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.count_lbl.setAutoFillBackground(False)
        self.count_lbl.setObjectName("count_lbl")
        self.even_tx = QtWidgets.QLineEdit(self.mainWidget)
        self.even_tx.setGeometry(QtCore.QRect(10, 120, 581, 31))
        self.even_tx.setObjectName("even_tx")
        self.odd_tx = QtWidgets.QLineEdit(self.mainWidget)
        self.odd_tx.setGeometry(QtCore.QRect(10, 80, 581, 31))
        self.odd_tx.setObjectName("odd_tx")
        self.out_tx = QtWidgets.QLineEdit(self.mainWidget)
        self.out_tx.setGeometry(QtCore.QRect(10, 160, 581, 31))
        self.out_tx.setObjectName("out_tx")
        MergeWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(MergeWindow)
        QtCore.QMetaObject.connectSlotsByName(MergeWindow)

    def retranslateUi(self, MergeWindow):
        _translate = QtCore.QCoreApplication.translate
        MergeWindow.setWindowTitle(_translate("MergeWindow", "برنامج دمج الصفحات الفردي والزوجي"))
        self.merge_btn.setText(_translate("MergeWindow", "بدء الدمج"))
        self.title_lbl.setText(_translate("MergeWindow", "دمج الصفحات الفردية والزوجية"))
        self.odd_btn.setText(_translate("MergeWindow", "ملف الفردي"))
        self.even_btn.setText(_translate("MergeWindow", "ملف الزوجي"))
        self.out_btn.setText(_translate("MergeWindow", "ملف الاخراج"))
        self.count_lbl.setText(_translate("MergeWindow", "Done: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MergeWindow = QtWidgets.QMainWindow()
    ui = Ui_MergeWindow()
    ui.setupUi(MergeWindow)
    MergeWindow.show()
    sys.exit(app.exec_())
