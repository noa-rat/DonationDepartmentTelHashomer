from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QFont, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QMessageBox, QDialog, QTableWidget, \
    QAbstractItemView, QGridLayout, QHeaderView, QTableWidgetItem, QHBoxLayout
import db

class EventsWindow(QWidget):
    def __init__(self, main_window=None, previous_window=None):
        super().__init__()
        self.main_window = main_window
        self.previous_window = previous_window

        self.setWindowTitle("Managing Fundraising Events")

        # Set white background
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#ffffff"))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # Top Bar Layout
        top_bar = QHBoxLayout()
        top_bar.setContentsMargins(0, 0, 0, 0)
        top_bar.setSpacing(10)

        self.home_button = QPushButton("🏠 Home")
        self.home_button.setFixedSize(190, 70)
        self.home_button.setStyleSheet("background-color: #003366; color: white; font-size: 14pt;")
        self.home_button.clicked.connect(self.go_home)

        self.back_button = QPushButton("⬅️ Back")
        self.back_button.setFixedSize(190, 70)
        self.back_button.setStyleSheet("background-color: #003366; color: white; font-size: 14pt;")
        self.back_button.clicked.connect(self.go_back)

        top_bar.addWidget(self.home_button)
        top_bar.addWidget(self.back_button)
        top_bar.addStretch()

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(30)

        # "View All Events" Button (moved to the top)
        self.btn_view_all = QPushButton("View All Events")
        self.btn_view_all.setStyleSheet("font-size: 18pt; padding: 15px; background-color: #4caf50; color: white;")
        self.btn_view_all.clicked.connect(self.view_all)
        main_layout.addWidget(self.btn_view_all, alignment=Qt.AlignHCenter)

        # Header Label (Smaller & Moved to Top)
        header_font = QFont("Palatino Linotype", 24, QFont.Bold)
        label = QLabel("Fundraising Event Options")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(header_font)

        container_layout = QVBoxLayout()
        container_layout.addLayout(top_bar)
        container_layout.addWidget(label)
        main_layout.addLayout(container_layout)

        # Buttons Grid Layout (Fixed Spacing)
        btn_grid = QGridLayout()
        btn_grid.setSpacing(30)
        main_layout.addLayout(btn_grid)

        self.setLayout(main_layout)

    def go_back(self):
        if self.previous_window:
            self.previous_window.show()
        self.close()

    def go_home(self):
        if self.previous_window and self.previous_window != self.main_window:
            self.previous_window.close()
        if self.main_window:
            self.main_window.show()
        self.close()

    def view_all(self):
        query = "SELECT * FROM fundraisingevent ORDER BY e_id"
        try:
            conn = db.connect_to_db()
            cur = conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            cur.close()
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Query Error", f"Failed to run query:\n{e}")
            return

        # Create dialog to display the table
        dialog = QDialog(self)
        dialog.setWindowTitle("All Fundraising Events")
        dialog.setMinimumSize(900, 500)

        layout = QVBoxLayout()
        table = QTableWidget()
        table.setRowCount(len(rows))
        table.setColumnCount(len(column_names))
        table.setHorizontalHeaderLabels(column_names)
        table.setEditTriggers(QTableWidget.NoEditTriggers)
        table.setSelectionMode(QAbstractItemView.NoSelection)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(str(value)))

        layout.addWidget(table)
        dialog.setLayout(layout)
        dialog.exec_()
