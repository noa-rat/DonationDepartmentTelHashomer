# החלון הראשי
import sys
import db
from donations_analysis import DonationsAnalysis
from donations_dept_window import DonationsDeptWindow
from fundraising_event_optimization import FundraisingEventOptimization
from PyQt5.QtWidgets import (
    QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QMessageBox,
    QTableWidget, QTableWidgetItem, QGridLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.fundraising_event_optimization = None
        self.donations_analysis = None
        self.donations_dept_window = None

        # Get screen size and set window to 3/4 of screen width and height
        # קבל את גודל המסך והגדר את החלון ל-3/4 מרוחב וגובה המסך
        screen = QApplication.primaryScreen()
        screen_size = screen.size()
        w, h = screen_size.width() * 3 // 4, screen_size.height() * 3 // 4
        self.resize(w, h)
        self.setWindowTitle("Sheba Tel HaShomer")

        # Set white background
        # הגדר רקע לבן
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#ffffff"))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(40)

        # Script-style font for welcome label (large size)
        # גופן בסגנון סקריפט עבור תווית ברוכים הבאים (גודל גדול)
        welcome_font = QFont("Palatino Linotype", 42, QFont.Bold)

        label = QLabel("Welcome to Tel HaShomer Hospital!")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(welcome_font)
        main_layout.addWidget(label)

        # Grid layout for buttons 2x2
        # פריסת רשת עבור כפתורים 2x2
        btn_grid = QGridLayout()
        btn_grid.setSpacing(40)

        btn_style = """
            QPushButton {
                font-size: 36pt;
                font-family: 'Calibri', 'Segoe UI', sans-serif;
                font-weight: 700;
                padding: 60px;
                border: none;
                border-radius: 20px;
                color: white;
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #4caf50,  /* green */
                    stop:1 #2196f3   /* blue */
                );
                min-width: 300px;
                min-height: 80px;
                max-width: 400px;
                max-height: 300px;
                text-align: center;
                qproperty-alignment: 'AlignCenter';
                transition-duration: 0.3s;
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

        self.view_manage_btn = QPushButton("Manage")
        self.view_manage_btn.setStyleSheet(btn_style)
        self.view_manage_btn.clicked.connect(self.view_manage)

        self.view_analyze_btn = QPushButton("Analyze")
        self.view_analyze_btn.setStyleSheet(btn_style)
        self.view_analyze_btn.clicked.connect(self.view_analyze)

        self.view_automate_btn = QPushButton("Automate")
        self.view_automate_btn.setStyleSheet(btn_style)
        self.view_automate_btn.clicked.connect(self.view_automate)

        btn_grid.addWidget(self.view_manage_btn, 0, 0)
        btn_grid.addWidget(self.view_analyze_btn, 0, 1)
        btn_grid.addWidget(self.view_automate_btn, 0, 2)

        main_layout.addLayout(btn_grid)
        self.setLayout(main_layout)

    # DonationsDeptWindow פותח את החלון
    def view_manage(self):
        print("manage view clicked")
        self.donations_dept_window = DonationsDeptWindow(self)
        # Move and resize donations window to main window geometry
        # העברה ושינוי גודל של חלון התרומות לגודל של החלון הראשי
        self.donations_dept_window.setGeometry(self.geometry())
        self.donations_dept_window.show()
        # hide main window
        # הסתר את החלון הראשי
        self.hide()

    # פותח את החלון DonationAnalysis
    def view_analyze(self):
        print("analyze view clicked")
        self.donations_analysis = DonationsAnalysis(self)
        self.donations_analysis.setGeometry(self.geometry())
        self.donations_analysis.show()
        self.hide()

    # פותח את החלון FundraisingEventOptimization
    def view_automate(self):
        print("automate view clicked")
        self.fundraising_event_optimization = FundraisingEventOptimization(self)
        self.fundraising_event_optimization.setGeometry(self.geometry())
        self.fundraising_event_optimization.show()
        self.hide()

# מריץ את החלון הראשי
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())