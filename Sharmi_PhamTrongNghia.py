# Form implementation generated from reading ui file 'ListView.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6.QtWidgets import QMessageBox
from PyQt6 import QtCore, QtGui, QtWidgets
import random
import numpy as np
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Lược đồ shamir")
        MainWindow.resize(1001, 675)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 461, 581))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.label_5.setObjectName("label_5")
        self.txt_khoa_can_chia_se = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_khoa_can_chia_se.setGeometry(QtCore.QRect(290, 40, 113, 22))
        self.txt_khoa_can_chia_se.setObjectName("txt_khoa_can_chia_se")
        self.txt_so_thanh_vien_giu_khoa = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_so_thanh_vien_giu_khoa.setGeometry(QtCore.QRect(290, 70, 113, 22))
        self.txt_so_thanh_vien_giu_khoa.setObjectName("txt_so_thanh_vien_giu_khoa")
        self.txt_so_thanh_vien_toi_thieu = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_so_thanh_vien_toi_thieu.setGeometry(QtCore.QRect(290, 110, 113, 22))
        self.txt_so_thanh_vien_toi_thieu.setObjectName("txt_so_thanh_vien_toi_thieu")
        self.btn_chia_se_khoa = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_chia_se_khoa.setGeometry(QtCore.QRect(20, 170, 93, 28))
        self.btn_chia_se_khoa.setObjectName("btn_chia_se_khoa")
        self.btn_nhap_lai = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_nhap_lai.setGeometry(QtCore.QRect(200, 170, 93, 28))
        self.btn_nhap_lai.setObjectName("btn_nhap_lai")
        self.table_chia_khoa = QtWidgets.QTableView(parent=self.groupBox)
        self.table_chia_khoa.setGeometry(QtCore.QRect(30, 260, 331, 301))
        self.table_chia_khoa.setObjectName("table_chia_khoa")
        self.label_giatri_p = QtWidgets.QLabel(parent=self.groupBox)
        self.label_giatri_p.setGeometry(QtCore.QRect(290, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_giatri_p.setFont(font)
        self.label_giatri_p.setText("")
        self.label_giatri_p.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.label_giatri_p.setObjectName("label_giatri_p")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(520, 20, 461, 581))
        self.groupBox_2.setObjectName("groupBox_2")
        self.table_ghep_khoa = QtWidgets.QTableView(parent=self.groupBox_2)
        self.table_ghep_khoa.setGeometry(QtCore.QRect(50, 20, 331, 311))
        self.table_ghep_khoa.setObjectName("table_ghep_khoa")
        self.btn_khoi_phuc_khoa = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.btn_khoi_phuc_khoa.setGeometry(QtCore.QRect(150, 360, 93, 28))
        self.btn_khoi_phuc_khoa.setObjectName("btn_khoi_phuc_khoa")
        self.btn_chuyen = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_chuyen.setGeometry(QtCore.QRect(370, 500, 83, 28))
        self.btn_chuyen.setObjectName("btn_chuyen")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(50, 450, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.label_6.setObjectName("label_6")
        self.label_giai_ma = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_giai_ma.setGeometry(QtCore.QRect(160, 450, 300, 35))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_giai_ma.setFont(font)
        self.label_giai_ma.setText("")
        self.label_giai_ma.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.label_giai_ma.setObjectName("label_giai_ma")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1001, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_giai_ma.setStyleSheet("color: red;font-weight:bold; font-size: 27px;")
        self.model_giai_ma = QtGui.QStandardItemModel()
        self.model_giai_ma.setHorizontalHeaderLabels(["Lựa chọn", "xi", "pi"])
        self.model_chia_se= QtGui.QStandardItemModel()
        self.model_chia_se.setHorizontalHeaderLabels([ "xi", "pi"])
        self.table_chia_khoa.setModel(self.model_chia_se)
        self.table_ghep_khoa.setModel(self.model_giai_ma)

        self.K = 0
        self.t = 0
        self.m = 0
        self.p = 0
        self.he_so_phuong_trinh=[]

        self.btn_nhap_lai.clicked.connect(self.nhap_lai)
        self.btn_chia_se_khoa.clicked.connect(self.chia_se_shamir)
        self.btn_chuyen.clicked.connect(self.chuyen_du_lieu)
        self.btn_khoi_phuc_khoa.clicked.connect(self.khoi_phuc_khoa)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Chia khóa"))
        self.label_2.setText(_translate("MainWindow", "Số thành viên giữ khóa:"))
        self.label_3.setText(_translate("MainWindow", "Khóa cần chia sẽ:"))
        self.label_4.setText(_translate("MainWindow", "Số thành viên tối thiểu để mở khóa:"))
        self.label_5.setText(_translate("MainWindow", "Giá trị p:"))
        self.btn_chia_se_khoa.setText(_translate("MainWindow", "Chia sẻ khóa"))
        self.btn_nhap_lai.setText(_translate("MainWindow", "Nhập lại"))
        self.btn_chuyen.setText(_translate("MainWindow", "Chuyển"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Ghép khóa"))
        self.btn_khoi_phuc_khoa.setText(_translate("MainWindow", "Khôi phục khóa"))
        self.label_6.setText(_translate("MainWindow", "Khóa bí mật:"))
    
    def nhap_lai(self):
        self.txt_khoa_can_chia_se.clear()
        self.txt_so_thanh_vien_giu_khoa.clear()
        self.txt_so_thanh_vien_toi_thieu.clear()
        self.label_giatri_p.clear()
        self.label_giai_ma.clear()
        self.clear_table(self.table_chia_khoa)
        self.clear_table(self.table_ghep_khoa)

    def clear_table(self, table):
        model = table.model()
        if model is not None:
            model.removeRows(0, model.rowCount())

    
    def decompose(self,n):
        s = 0
        d = n - 1
        while d % 2 == 0:
            d //= 2
            s += 1
        return s, d
    
    def miller_test(self,d, n, a):
        x = pow(a, d, n) 
        if x == 1 or x == n - 1:
            return True
        while d != n - 1:
            x = pow(x, 2, n)
            d *= 2
            if x == n - 1:
                return True
            if x == 1:
                return False
        return False
    
    def miller_rabin(self,n, k=5):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False

        s, d = self.decompose(n)

        for _ in range(k):
            a = random.randint(2, n - 2)
            if not self.miller_test(d, n, a):
                return False

        return True
    
    def generate_random(self):
        try:
            self.K = int(self.txt_khoa_can_chia_se.text())
            self.m = int(self.txt_so_thanh_vien_giu_khoa.text())
            self.t = int(self.txt_so_thanh_vien_toi_thieu.text())
            max_value = 2**1000 
            self.p = random.randint(max(self.K ,self.m) + 1,max_value)
            while not self.miller_rabin(self.p):
                self.p = random.randint(max(self.K ,self.m) + 1,max_value )
            
            self.label_giatri_p.setText(str(self.p))
            self.label_giatri_p.setText(str(self.p))
            self.he_so_phuong_trinh = [random.randint(1, self.p - 1) for _ in range(self.t - 1)]
            print(self.he_so_phuong_trinh)
            return True
        except ValueError:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Icon.Warning)
            dialog.setText("Vui lòng kiểm tra dữ liệu nhập vào")
            dialog.setWindowTitle("Lỗi")
            dialog.exec()
            return False
        
    def tinh_y(self,x):
        y = 0
        for i in range(len(self.he_so_phuong_trinh)):
            y += self.he_so_phuong_trinh[i]*pow(x,i+1)
        y = y + self.K
        y = y%self.p
        return y
    
    def chia_se_shamir(self):
        chia_se = []
        if(self.generate_random() == False): return
        for i in range(1,self.m+1):
            x = i
            y = self.tinh_y(x)
            chia_se.append((x,y))
        self.hien_thi_shares(chia_se)

    def hien_thi_shares(self, shares):
        self.model_chia_se.clear()
        self.model_chia_se.setHorizontalHeaderLabels(["xi", "pi"])
        for x, y in shares:
            x_item = QtGui.QStandardItem(str(x))
            y_item = QtGui.QStandardItem(str(y))   
            self.model_chia_se.appendRow([x_item, y_item])
        self.table_chia_khoa.setModel(self.model_chia_se)

    def lay_du_lieu_tu_table_chia_khoa(self):
        model = self.table_chia_khoa.model()
        data = []
        for row in range(model.rowCount()):
            x = int(model.item(row, 0).text())
            y = int(model.item(row, 1).text())
            data.append((x, y))
        return data
    
    def hien_thi_du_lieu_len_table_ghep_khoa(self, data):
        self.model_giai_ma.clear()
        self.model_giai_ma.setHorizontalHeaderLabels(["Lựa chọn", "xi", "pi"])
        for x, y in data:
            checkbox_item = QtGui.QStandardItem()
            checkbox_item.setCheckable(True)
            checkbox_item.setCheckState(QtCore.Qt.CheckState.Unchecked)
            x_item = QtGui.QStandardItem(str(x))
            y_item = QtGui.QStandardItem(str(y))
            self.model_giai_ma.appendRow([checkbox_item, x_item, y_item])
        
        self.table_ghep_khoa.setModel(self.model_giai_ma)

    def chuyen_du_lieu(self):
        data = self.lay_du_lieu_tu_table_chia_khoa()
        self.hien_thi_du_lieu_len_table_ghep_khoa(data)

    def lay_cac_dong_duoc_chon(self):
        model = self.table_ghep_khoa.model()
        selected_data = []
        for row in range(model.rowCount()):
            checkbox_item = model.item(row, 0)
            if checkbox_item.checkState() == QtCore.Qt.CheckState.Checked:
                x = int(model.item(row, 1).text())
                y = int(model.item(row, 2).text())
                selected_data.append((x, y))
        return selected_data
    
    def gcd(self, a, b):
        if a == 0: return b
        if b == 0: return a
        while b != 0:
            tmp = a % b
            a = b
            b = tmp
        return a
    
    def mod_inverse(self,a, p):
        if self.gcd(a, p) != 1:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Icon.Warning)
            dialog.setText("Vui lòng kiểm tra dữ liệu nhập vào")
            dialog.setWindowTitle("Lỗi")
            dialog.exec()
            return
        m0, x0, x1 = p, 0, 1
        if p == 1:
            return 0
        while a > 1:
            q = a // p
            a, p = p, a % p
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += m0
        return x1
    
    def noi_suy_lagrange_tren_vanh_Zp(self,xs, ys, p):
        def noi_suy(x):
            ket_qua = 0
            for i in range(len(xs)):
                xi, yi = xs[i], ys[i]
                li = 1
                for j in range(len(xs)):
                    if i != j:
                        xj = xs[j]
                        tu_so = (x - xj + p) % p
                        mau_so = self.mod_inverse((xi - xj + p) % p, p)
                        li = (li * tu_so * mau_so) % p
                ket_qua = (ket_qua + yi * li) % p
            return ket_qua
        return noi_suy
    
    

    def khoi_phuc_khoa(self, selected_data):
        x_values = [int(item[0]) for item in selected_data]
        y_values = [int(item[1]) for item in selected_data]
        noi_suy = self.noi_suy_lagrange_tren_vanh_Zp(x_values, y_values, self.p)
        return noi_suy(0)
     


if __name__ == "__main__":
    number = 2 ** 1000

    # Chuyển số thành chuỗi và đếm số lượng chữ số
    num_digits = len(str(number))

    # In kết quả
    print(f"Số {2**1000} có {num_digits} chữ số.")

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
    # Tính giá trị của 2^1000
   