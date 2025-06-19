from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QFont, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QMessageBox, QDialog, QFormLayout, \
    QLineEdit, QDialogButtonBox, QComboBox, QTableWidgetItem, QTableWidget, QInputDialog, QHBoxLayout, QListWidget, \
    QAbstractItemView, QCheckBox, QGridLayout, QDateEdit, QHeaderView
import db

class DonationsAnalysis(QWidget):
    def __init__(self, main_window=None, previous_window=None):
        super().__init__()
        self.main_window = main_window
        self.previous_window = previous_window

        self.setWindowTitle("Donations Analysis")

        # Set white background
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#ffffff"))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        top_bar = QHBoxLayout()
        top_bar.setContentsMargins(0, 0, 0, 0)
        top_bar.setSpacing(10)

        self.home_button = QPushButton("🏠 Home")
        self.home_button.setFixedSize(190, 70)
        self.home_button.setStyleSheet("""
            QPushButton {
                background-color: #003366;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                font-size: 14pt;
            }
            QPushButton:hover {
                background-color: #0059b3;
            }
            QPushButton:pressed {
                background-color: #002244;
            }
        """)
        self.home_button.clicked.connect(self.go_home)

        top_bar.addWidget(self.home_button)
        top_bar.addStretch()

        # Main vertical layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(40)

        header_font = QFont("Palatino Linotype", 36, QFont.Bold)
        label = QLabel("Analysis Options")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(header_font)

        container_layout = QVBoxLayout()
        container_layout.addLayout(top_bar)
        container_layout.addWidget(label)

        main_layout.addLayout(container_layout)

        # Grid layout for buttons
        btn_grid = QGridLayout()
        btn_grid.setSpacing(40)

        btn_style = """
            QPushButton {
                font-size: 22pt;
                font-family: 'Calibri', 'Segoe UI', sans-serif;
                font-weight: 700;
                padding: 60px;
                border: none;
                border-radius: 20px;
                color: white;
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #4caf50,
                    stop:1 #2196f3
                );
                min-width: 300px;
                min-height: 80px;
                max-width: 400px;
                max-height: 300px;
                text-align: center;
                qproperty-alignment: 'AlignCenter';
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #66bb6a,
                    stop:1 #42a5f5
                );
            }
            QPushButton:pressed {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #388e3c,
                    stop:1 #1976d2
                );
            }
        """

        self.btn_big_donors = QPushButton("Biggest Donors\n Per Department")
        self.btn_big_donors.setStyleSheet(btn_style)
        self.btn_big_donors.clicked.connect(self.big_donors_query)

        self.btn_event_success = QPushButton("Success of\n Fundraising Events")
        self.btn_event_success.setStyleSheet(btn_style)
        self.btn_event_success.clicked.connect(self.event_success_query)

        btn_grid.addWidget(self.btn_big_donors, 0, 0)  # Add to grid layout
        btn_grid.addWidget(self.btn_event_success, 0, 1)  # Add to grid layout
        main_layout.addLayout(btn_grid)

        # Table for displaying query results
        self.table = QTableWidget()
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Expands to fit the table

        main_layout.addWidget(self.table)
        self.setLayout(main_layout)

    def go_home(self):
        if self.previous_window and self.previous_window != self.main_window:
            self.previous_window.close()
        self.main_window.show()

    def closeEvent(self, event):
        if self.previous_window:
            self.previous_window.show()
        event.accept()

    def big_donors_query(self):
        query = """
        SELECT 
            donor_id, 
            name, 
            d_name, 
            SUM(d_amount) AS donor_total_to_department,
            total_department_donations,
            ROUND(SUM(d_amount) * 100.0 / total_department_donations,2) AS donation_percentage
        FROM donor NATURAL JOIN donation NATURAL JOIN towards
            NATURAL JOIN (
                SELECT d_name, SUM(d_amount) AS total_department_donations
                FROM donation NATURAL JOIN towards
                GROUP BY d_name
            ) AS dept_totals
        GROUP BY donor_id, name, d_name, total_department_donations
        HAVING SUM(d_amount) >= 0.6 * total_department_donations 
        ORDER BY donation_percentage DESC;
        """
        try:
            conn = db.connect_to_db()
            cur = conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            cur.close()
            conn.close()

            self.table.setRowCount(len(rows))
            self.table.setColumnCount(len(column_names))
            self.table.setHorizontalHeaderLabels(column_names)

            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(str(value)))

        except Exception as e:
            QMessageBox.critical(self, "Query Error", f"Failed to run query:\n{e}")

    def event_success_query(self):
        query = """
        SELECT
            d.e_id,
            d.d_name,
            SUM(d.d_amount) AS total_amount,
            'Department' AS target_type 
            FROM (donation NATURAL JOIN towards NATURAL JOIN department) AS d
            GROUP BY d.e_id, d.d_name
            HAVING SUM(d.d_amount) = (
                SELECT MAX(sum_amount)
                FROM (
                    SELECT SUM(d2.d_amount) AS sum_amount
                    FROM (donation NATURAL JOIN towards NATURAL JOIN department) AS d2
                    WHERE d2.e_id = d.e_id
                    GROUP BY d2.d_name
                    ) AS subquery
            )
        UNION ALL
        SELECT
            dp.e_id,
            dp.p_name,
            SUM(dp.d_amount) AS total_amount,
            'Project' AS target_type 
        FROM (donation NATURAL JOIN project) AS dp
        GROUP BY dp.e_id, dp.p_name
        HAVING SUM(dp.d_amount) = (
            SELECT MAX(sum_amount)
            FROM (
                SELECT SUM(dp2.d_amount) AS sum_amount
                FROM (donation NATURAL JOIN project) AS dp2
                WHERE dp2.e_id = dp.e_id
                GROUP BY dp2.p_name
                ) AS subquery
        );

        """
        try:
            conn = db.connect_to_db()
            cur = conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            cur.close()
            conn.close()

            self.table.setRowCount(len(rows))
            self.table.setColumnCount(len(column_names))
            self.table.setHorizontalHeaderLabels(column_names)

            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(str(value)))

        except Exception as e:
            QMessageBox.critical(self, "Query Error", f"Failed to run query:\n{e}")