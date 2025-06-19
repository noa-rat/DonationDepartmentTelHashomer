from PyQt5.QtWidgets import (
    QWidget, QLabel, QGridLayout, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

from donations_window import DonationsWindow
from donors_window import DonorsWindow
from projects_window import ProjectsWindow

class DonationsDeptWindow(QWidget):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Donations Department")

        self.donations_window = None
        self.donors_window = None
        self.projects_window = None
        self.events_window = None
        self.fundraises_window = None
        self.departments_window = None

        # Set white background
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#ffffff"))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # Horizontal layout for top bar (Home button)
        top_bar = QHBoxLayout()
        top_bar.setContentsMargins(0, 0, 0, 0)
        top_bar.setSpacing(0)

        # Home button with emoji and distinct style
        self.home_button = QPushButton("🏠 Home")
        self.home_button.setFixedSize(190, 70)  # small size
        self.home_button.setStyleSheet("""
            QPushButton {
                background-color: #003366;  /* dark blue */
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

        # Add Home button aligned left in the top bar
        top_bar.addWidget(self.home_button, alignment=Qt.AlignLeft)

        # Main vertical layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(40)

        # Header label font (same style as main window header)
        header_font = QFont("Palatino Linotype", 36, QFont.Bold)
        label = QLabel("Donations Department Options")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(header_font)

        # Add the top bar and header label to a container vertical layout
        container_layout = QVBoxLayout()
        container_layout.addLayout(top_bar)
        container_layout.addWidget(label)

        main_layout.addLayout(container_layout)

        # Grid layout for buttons (2x2)
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

        self.btn_manage_donations = QPushButton("Manage Donations")
        self.btn_manage_donations.setStyleSheet(btn_style)
        self.btn_manage_donations.clicked.connect(self.manage_donations)

        self.btn_manage_donors = QPushButton("Manage Donors")
        self.btn_manage_donors.setStyleSheet(btn_style)
        self.btn_manage_donors.clicked.connect(self.manage_donors)

        self.btn_manage_projects = QPushButton("Manage Projects")
        self.btn_manage_projects.setStyleSheet(btn_style)
        self.btn_manage_projects.clicked.connect(self.manage_projects)

        btn_grid.addWidget(self.btn_manage_donations, 0, 0)
        btn_grid.addWidget(self.btn_manage_donors, 0, 1)  # Shifted to accommodate new center button
        btn_grid.addWidget(self.btn_manage_projects, 0, 2)

        main_layout.addLayout(btn_grid)
        self.setLayout(main_layout)

    def go_home(self):
        # Close this window and show the main window again
        if self.main_window:
            self.main_window.show()
        self.close()

    def closeEvent(self, event):
        if self.main_window:
            self.main_window.show()
        event.accept()

    def manage_donations(self):
        self.donations_window = DonationsWindow(self.main_window, self)
        self.donations_window.setGeometry(self.geometry())
        self.donations_window.show()
        self.hide()  # hide main window

    def manage_donors(self):
        self.donors_window = DonorsWindow(self.main_window, self)
        self.donors_window.setGeometry(self.geometry())
        self.donors_window.show()
        self.hide()

    def manage_projects(self):
        self.projects_window = ProjectsWindow(self.main_window, self)
        self.projects_window.setGeometry(self.geometry())
        self.projects_window.show()
        self.hide()