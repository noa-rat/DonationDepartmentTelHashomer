from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QLabel, QGridLayout, QTableWidget, \
    QAbstractItemView, QHeaderView, QTableWidgetItem
import db


class FundraisingEventOptimization(QWidget):
    def __init__(self, main_window=None, previous_window=None):
        super().__init__()
        self.main_window = main_window
        self.previous_window = previous_window

        self.setWindowTitle("Fundraising Event Optimization")

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
        label = QLabel("Fundraising Event Optimization")
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

        self.btn_automate = QPushButton("Start Process")
        self.btn_automate.setStyleSheet(btn_style)
        self.btn_automate.clicked.connect(self.process)

        # Table for displaying query results
        self.noticeTable = QTableWidget()
        self.noticeTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.noticeTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.noticeTable.setAlternatingRowColors(True)
        self.noticeTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Expands to fit the table

        self.resultTable = QTableWidget()
        self.resultTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.resultTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.resultTable.setAlternatingRowColors(True)
        self.resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Expands to fit the table

        btn_grid.addWidget(self.btn_automate, 0, 0)
        btn_grid.addWidget(self.resultTable, 1, 0)
        btn_grid.addWidget(self.noticeTable, 1, 1)
        main_layout.addLayout(btn_grid)

        self.setLayout(main_layout)
        self.load_events_table()

    def go_home(self):
        if self.main_window:
            self.main_window.show()
        self.close()
    # מציגה את תוצאות השאילתא של אירועי הגיוס בטבלה הראשונה
    def load_events_table(self):
        conn = db.connect_to_db()
        if not conn:
            print("Connection failed")
            return

        cursor = None
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    fe.e_id,
                    fe.e_name,
                    o.fundraiser_id
                FROM fundraisingEvent fe
                JOIN organizes o ON fe.e_id = o.e_id
                ORDER BY fe.e_id;
            """)
            results = cursor.fetchall()
            results.reverse()
            self.resultTable.clear()
            self.resultTable.setRowCount(len(results))
            self.resultTable.setColumnCount(3)
            self.resultTable.setHorizontalHeaderLabels(["Event ID", "Event Name", "Fundraiser ID"])
            for row, (e_id, e_name, fundraiser_id) in enumerate(results):
                self.resultTable.setItem(row, 0, QTableWidgetItem(str(e_id)))
                self.resultTable.setItem(row, 1, QTableWidgetItem(e_name))
                self.resultTable.setItem(row, 2, QTableWidgetItem(str(fundraiser_id)))
        except Exception as e:
            print("Error loading events:", e)
        finally:
            if cursor:
                cursor.close()
            conn.close()

    # מציגה את ההודעות שהתקבלו מבסיס הנתונים בטבלה השניה
    def update_notices_table(self, notices):
        self.noticeTable.clear()
        self.noticeTable.setRowCount(len(notices))
        self.noticeTable.setColumnCount(1)
        self.noticeTable.setHorizontalHeaderLabels(["Notices"])
        for row, notice in enumerate(notices):
            notice_text = notice.strip()
            self.noticeTable.setItem(row, 0, QTableWidgetItem(notice_text))

    # מריצה את תהליך יצירת האירועים ומעדכנת את הטבלאות
    def process(self):
        conn = db.connect_to_db()
        if not conn:
            print("Connection failed.")
            return

        cursor = None
        try:
            cursor = conn.cursor()
            conn.notices.clear()

            # קבלת רשימת מחלקות
            cursor.execute("SELECT department_name FROM get_departments_below_budget();")
            departments = cursor.fetchall()

            count_departments = 0
            for (dept_name,) in departments:
                count_departments += 1
                print(f"Handling department: {dept_name}")
                cursor.execute("CALL create_fundraisingEvent_for_department(%s);", (dept_name,))
                conn.commit()
                # מעדכן את ההודעות והטבלה
                self.update_notices_table(conn.notices)
                self.load_events_table()

            if count_departments == 0:
                print("All departments have reached their fundraising goals.")
            else:
                print(f"Processed {count_departments} departments with unmet fundraising goals.")

            print("Process completed successfully")

        except Exception as e:
            print("Error during process:", e)

        finally:
            if cursor:
                cursor.close()
            conn.close()