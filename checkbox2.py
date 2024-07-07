import sys
from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QTableView, QVBoxLayout, QWidget, QStyledItemDelegate, QCheckBox
from functools import reduce
from operator import mul
class MyTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def rowCount(self, parent=None):
        return len(self.data)

    def columnCount(self, parent=None):
        return len(self.data[0])

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if index.column() == 0:
                return None  # Trả về None để chỉ hiển thị checkbox
            return self.data[index.row()][index.column()]
        elif role == Qt.ItemDataRole.CheckStateRole and index.column() == 0:
            return Qt.CheckState.Checked if self.data[index.row()][0] else Qt.CheckState.Unchecked
        return None

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.CheckStateRole and index.column() == 0:
            # Xác định giá trị mới của checkbox từ giá trị `value`
            #new_value = (value == Qt.CheckState.Checked)
            
            # Lấy vị trí hàng của ô cần cập nhật
            row = index.row()
            if  self.data[row][0] == False:
                value = Qt.CheckState.Checked
                self.data[row][0] = True
            else:
                self.data[row][0] = False
                value = Qt.CheckState.Checked
            # Cập nhật dữ liệu tại vị trí hàng và cột checkbox
            
            # Phát tín hiệu thông báo rằng dữ liệu đã thay đổi
            self.dataChanged.emit(index, index, [Qt.ItemDataRole.CheckStateRole])
            
            return True

    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsUserCheckable
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return ["Lựa chọn", "Tên", "Tuổi"][section]
            else:
                return str(section + 1)
        return None

class CheckBoxDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        if index.column() == 0:
            checkbox = QCheckBox(parent)
            checkbox.setStyleSheet("margin-left:25%;")
            return checkbox
        return super().createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        if index.column() == 0:
            checked = index.model().data(index, Qt.ItemDataRole.CheckStateRole)
            editor.setChecked(checked == Qt.CheckState.Checked)
        else:
            super().setEditorData(editor, index)

    def setModelData(self, editor, model, index):
        if index.column() == 0:
            model.setData(index, Qt.CheckState.Checked if editor.isChecked() else Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)
        else:
            super().setModelData(editor, model, index)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Tạo dữ liệu mẫu với tất cả checkbox ban đầu là unchecked (False)
        data = [
            [False, "Alice", 30],
            [False, "Bob", 25],
            [False, "Charlie", 22],
        ]

        # Tạo model bảng
        self.model = MyTableModel(data)

        # Tạo QTableView
        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setStretchLastSection(True)
        self.table_view.resizeColumnsToContents()

        # Thiết lập delegate để hiển thị checkbox trong cột đầu tiên
        delegate = CheckBoxDelegate(self.table_view)
        self.table_view.setItemDelegateForColumn(0, delegate)

        # Thiết lập giao diện
        self.setWindowTitle("Bảng với Lựa chọn, Tên và Tuổi")
        self.setFixedSize(500, 150)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.table_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
