import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt
import subprocess

class ArpTableApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('ARP Table Viewer')
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['IP Address', 'MAC Address', 'Type'])

        self.layout.addWidget(self.table)

        self.load_button = QPushButton('Load ARP Table', self)
        self.load_button.clicked.connect(self.load_arp_table)
        self.layout.addWidget(self.load_button)

        self.central_widget.setLayout(self.layout)

    def load_arp_table(self):
        try:
            # Run the arp -a command to get ARP table information
            arp_output = subprocess.check_output(['arp', '-a'], universal_newlines=True)
            arp_lines = arp_output.split('\n')[3:-2]  # Extract relevant lines

            self.table.setRowCount(len(arp_lines))

            for row, line in enumerate(arp_lines):
                # Split the line into columns
                columns = line.split()
                ip_item = QTableWidgetItem(columns[0])
                mac_item = QTableWidgetItem(columns[1])
                type_item = QTableWidgetItem(columns[2])

                # Set alignment to center
                ip_item.setTextAlignment(Qt.AlignCenter)
                mac_item.setTextAlignment(Qt.AlignCenter)
                type_item.setTextAlignment(Qt.AlignCenter)

                self.table.setItem(row, 0, ip_item)
                self.table.setItem(row, 1, mac_item)
                self.table.setItem(row, 2, type_item)

            self.table.resizeColumnsToContents()

        except subprocess.CalledProcessError as e:
            print(f"Error running 'arp -a': {e}")

def main():
    app = QApplication(sys.argv)
    window = ArpTableApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
