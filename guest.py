# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guest.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QDesktopWidget
import sqlite3
from PyQt5.QtGui import QIcon







class mywindow(QtWidgets.QWidget):      #实例化窗口
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)                      #绘制界面
        #对事件和响应函数建立连接
        self.pushButton_2.clicked.connect(lambda: self.guest_operation("delete"))
        self.pushButton_3.clicked.connect(lambda: self.guest_operation("add"))
        self.pushButton_4.clicked.connect(lambda: self.guest_operation("refresh"))
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1800, 900)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(1160, 230, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        #与表格栏对齐的信息，便于查填删改
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(70, 770, 170, 41))
        self.lineEdit1 = QtWidgets.QLineEdit(Form)
        self.lineEdit1.setGeometry(QtCore.QRect(250, 770, 490, 41))
        self.lineEdit2 = QtWidgets.QLineEdit(Form)
        self.lineEdit2.setGeometry(QtCore.QRect(750, 770, 540, 41))
        self.lineEdit3 = QtWidgets.QLineEdit(Form)
        self.lineEdit3.setGeometry(QtCore.QRect(1300, 770, 220, 41))
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(190, 40, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.graphicsView = QtWidgets.QLabel(Form)
        self.graphicsView.setGeometry(QtCore.QRect(1000, 30, 121, 121))
        self.graphicsView.setObjectName("graphicsView")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(70, 190, 1650, 550))
        self.tableWidget.setObjectName("tableWidget")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 825, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(1180, 825, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(1410, 825, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.showguest()
        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)
        self.center()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "公司管理系统"))
        Form.setWindowIcon(QIcon('icon/web.png'))
        self.graphicsView.setPixmap(QtGui.QPixmap('icon/micon.jpg'))
        self.pushButton.setText(_translate("Form", "查看"))
        self.label_3.setText(_translate("Form", "客户管理"))
        #item = self.tableWidget.verticalHeaderItem(0)
        #item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "客户"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "公司"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "地址"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "电话"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "产品"))
        self.pushButton_2.setText(_translate("Form", "删除客户"))
        self.pushButton_3.setText(_translate("Form", "增加客户"))
        self.pushButton_4.setText(_translate("Form", "更新客户"))

    def buttonForRow(self, name):
        widget=QtWidgets.QWidget()
        self.viewBtn = QtWidgets.QPushButton('查看')
        self.viewBtn.setStyleSheet(''' text-align : center;
                                        background-color : DarkSeaGreen;
                                        height : 30px;
                                        border-style: outset;
                                        font : 24px; ''')
        self.viewBtn.clicked.connect(lambda: self.gotoitem(name))
        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.viewBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return(widget)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showguest(self):
        conn = sqlite3.connect('data/database.db')
        c = conn.cursor()
        cursor = c.execute("SELECT COUNT(NAME) FROM   GUEST")
        if(cursor):
            for row in cursor:
                self.tableWidget.setRowCount(row[0])
        else:
            self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 500)
        self.tableWidget.setColumnWidth(2, 550)
        self.tableWidget.setColumnWidth(3, 240)
        self.tableWidget.setColumnWidth(4, 120)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        conn.close()
        self.refreshByDB()

    def refreshByDB(self):
        conn = sqlite3.connect('data/database.db')
        c = conn.cursor()
        cursor = c.execute("SELECT *  FROM GUEST")
        if(cursor):
            i = 0
            for row in cursor:
                for j in range(5):
                    if j < 4:
                        self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(row[j]))
                    else:
                        # print(row[0])
                        self.tableWidget.setCellWidget(i, 4, self.buttonForRow(row[0]))
                i += 1
        conn.close()

    def guest_operation(self,op):
        guest  =  "'"+self.lineEdit.text()+ "'"
        company=  "'"+self.lineEdit1.text()+"'"
        address=  "'"+self.lineEdit2.text()+"'"
        phone  =  "'"+self.lineEdit3.text()+"'"



        conn = sqlite3.connect('data/database.db')
        c = conn.cursor()
        if(op=="delete"):
            cursor = c.execute("SELECT * FROM GUEST WHERE NAME=" + guest)
            row = [r for r in cursor]
            if (len(row) > 0):
                c.execute("DELETE FROM GUEST WHERE NAME =" + guest)
                reply = QMessageBox.information(self,  # 使用infomation信息框
                                                "通知",
                                                "删除成功！")
            else:
                reply = QMessageBox.information(self,  # 使用infomation信息框
                                                "警告！",
                                                "查找不到该客户！请确认您的输入是否正确：）")
        elif(op=="add"):
            cursor = c.execute("SELECT * FROM GUEST WHERE NAME=" + guest)
            row = [r for r in cursor]
            if (len(row) == 0):
                c.execute("INSERT INTO GUEST (NAME,COMPANY,ADDRESS,PHONE) \
                      VALUES ({myname},{mycompany}, {myaddress}, {myphone} )" \
                          .format(myname=guest, mycompany=company, myaddress=address, myphone=phone))
                reply = QMessageBox.information(self,  # 使用infomation信息框
                                                "通知",
                                                "增加成功！")
            else:
                reply = QMessageBox.information(self,  # 使用infomation信息框
                                                "警告！",
                                                "该客户已存在！请确认您的输入是否正确：）")
        elif(op=="refresh"):
            cursor = c.execute("SELECT * FROM GUEST WHERE NAME=" + guest)
            row = [r for r in cursor]
            if (len(row) > 0):
                if (len(company) == 2): company = "'" + row[0][1] + "'"
                if (len(address) == 2): address = "'" + row[0][2] + "'"
                if (len(phone) == 2):   phone   = "'" + row[0][3] + "'"
                c.execute("UPDATE GUEST set COMPANY={mycompany}, ADDRESS={myaddress}, PHONE={myphone} \
                           where NAME={myname}".format(myname=guest,mycompany=company,myaddress=address,myphone=phone))
                reply = QMessageBox.information(self,  # 使用infomation信息框
                                                "通知",
                                                "更新成功！")
            else:
                reply = QMessageBox.information(self,  # 使用infomation信息框
                                                "警告！",
                                                "查找不到该客户！请确认您的输入是否正确：）")
        conn.commit()

        cursor = c.execute("SELECT COUNT(NAME) FROM   GUEST")
        for row in cursor:
            self.tableWidget.setRowCount(row[0])
        conn.close()
        self.refreshByDB()

    def gotoitem(self,name):

        import subprocess
        ps = subprocess.Popen(r"python product.py "+str(name));  # 执行cmd命令












if __name__=="__main__":    #文件主函数入口
    import sys
    app=QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())