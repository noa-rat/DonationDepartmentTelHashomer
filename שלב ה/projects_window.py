from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QFont, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QMessageBox, QDialog, QFormLayout, \
    QLineEdit, QDialogButtonBox, QComboBox, QTableWidgetItem, QTableWidget, QInputDialog, QHBoxLayout, QListWidget, \
    QAbstractItemView, QCheckBox, QGridLayout, QDateEdit
import db

class ProjectsWindow(QWidget):
    def __init__(self, main_window=None, previous_window=None):
        super().__init__()
        self.main_window = main_window
        self.previous_window = previous_window

        self.setWindowTitle("Managing  Projects")
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

        self.back_button = QPushButton("⬅️ Back")
        self.back_button.setFixedSize(190, 70)
        self.back_button.setStyleSheet("""
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
        self.back_button.clicked.connect(self.go_back)

        top_bar.addWidget(self.home_button)
        top_bar.addWidget(self.back_button)
        top_bar.addStretch()  # This pushes buttons to left side

        # Main vertical layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(40)

        # Header label font (same style as main window header)
        header_font = QFont("Palatino Linotype", 36, QFont.Bold)
        label = QLabel("Projects Options")
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

        self.btn_add_projects = QPushButton("Add Project")
        self.btn_add_projects.setStyleSheet(btn_style)
        self.btn_add_projects.clicked.connect(self.add_projects)

        self.btn_delete_projects = QPushButton("Delete Project")
        self.btn_delete_projects.setStyleSheet(btn_style)
        self.btn_delete_projects.clicked.connect(self.delete_projects)

        self.btn_update_projects = QPushButton("Update Project")
        self.btn_update_projects.setStyleSheet(btn_style)
        self.btn_update_projects.clicked.connect(self.update_projects)

        self.btn_select_projects = QPushButton("Select Project")
        self.btn_select_projects.setStyleSheet(btn_style)
        self.btn_select_projects.clicked.connect(self.select_projects)

        btn_grid.addWidget(self.btn_add_projects, 0, 0)
        btn_grid.addWidget(self.btn_delete_projects, 0, 1)
        btn_grid.addWidget(self.btn_update_projects, 1, 0)
        btn_grid.addWidget(self.btn_select_projects, 1, 1)

        main_layout.addLayout(btn_grid)
        self.setLayout(main_layout)

    def go_back(self):
        self.previous_window.show()
        self.close()

    def go_home(self):
        if self.previous_window and self.previous_window != self.main_window:
            self.previous_window.close()
        self.main_window.show()

    def closeEvent(self, event):
        if self.previous_window:
            self.previous_window.show()
        event.accept()

    def add_projects(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Add Project")
        form_layout = QFormLayout()

        p_name_input = QLineEdit()
        p_description_input = QLineEdit()
        start_date_input = QDateEdit()
        end_date_input = QDateEdit()
        end_date_input.setCalendarPopup(True)

        # Add checkbox to disable end date
        no_end_date_checkbox = QCheckBox("No End Date")

        def toggle_end_date(checked):
            end_date_input.setEnabled(not checked)

        no_end_date_checkbox.toggled.connect(toggle_end_date)

        fundraising_goal_input = QLineEdit()

        # --- Project Status ComboBox ---
        status_input = QComboBox()
        try:
            conn = db.connect_to_db()
            cur = conn.cursor()
            cur.execute("SELECT unnest(enum_range(NULL::project_status));")
            statuses = cur.fetchall()
            status_input.addItems([s[0] for s in statuses])
            cur.close()
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to load project statuses:\n{e}")
            return

        # --- Add Widgets to Form ---
        form_layout.addRow("Project Name:", p_name_input)
        form_layout.addRow("Project Description:", p_description_input)
        form_layout.addRow("Start Date:", start_date_input)
        form_layout.addRow("End Date:", end_date_input)
        form_layout.addRow("", no_end_date_checkbox)
        form_layout.addRow("Fundraising Goal:", fundraising_goal_input)
        form_layout.addRow("Project Status:", status_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        form_layout.addWidget(buttons)

        dialog.setLayout(form_layout)

        if dialog.exec_() == QDialog.Accepted:
            p_name = p_name_input.text()
            p_description = p_description_input.text()
            start_date = start_date_input.date().toPyDate()
            fundraising_goal = fundraising_goal_input.text()
            status = status_input.currentText()

            # Handle optional end_date
            end_date = None if no_end_date_checkbox.isChecked() else end_date_input.date().toPyDate()

            if not p_name or not fundraising_goal:
                QMessageBox.warning(self, "Input Error", "Project Name and Fundraising Goal are required.")
                return

            try:
                conn = db.connect_to_db()
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO project (p_name, p_description, start_date, end_date, fundraising_goal, status)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """, (
                    p_name,
                    p_description if p_description else None,
                    start_date,
                    end_date,
                    int(fundraising_goal),
                    status
                ))

                conn.commit()
                cur.close()
                conn.close()
                QMessageBox.information(self, "Success", "Project added successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"Failed to insert project:\n{e}")

    def delete_projects(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Delete Project")
        form_layout = QFormLayout()

        p_id_input = QComboBox()
        p_id_input.setEditable(True)
        try:
            conn = db.connect_to_db()
            cur = conn.cursor()
            cur.execute("SELECT p_id FROM project ORDER BY p_id;")
            p_ids = cur.fetchall()
            p_id_input.addItems([str(p[0]) for p in p_ids])
            cur.close()
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to load project IDs:\n{e}")
            return

        form_layout.addRow("Select Project ID:", p_id_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        form_layout.addWidget(buttons)

        dialog.setLayout(form_layout)

        def on_ok_clicked():
            p_id = p_id_input.currentText().strip()
            if not p_id.isdigit():
                QMessageBox.warning(self, "Input Error", "Project ID must be a number.")
                return

            try:
                conn = db.connect_to_db()
                cur = conn.cursor()

                cur.execute("SELECT COUNT(*) FROM project WHERE p_id = %s;", (p_id,))
                count = cur.fetchone()[0]
                if count == 0:
                    QMessageBox.warning(self, "Not Found", f"No project found with ID {p_id}.")
                    cur.close()
                    conn.close()
                    return

                # Confirm deletion
                reply = QMessageBox.question(
                    self, "Confirm Delete",
                    f"Are you sure you want to delete project with ID {p_id}?",
                    QMessageBox.Yes | QMessageBox.No
                )
                if reply == QMessageBox.No:
                    cur.close()
                    conn.close()
                    return

                # Perform delete
                cur.execute("DELETE FROM project WHERE p_id = %s;", (p_id,))
                conn.commit()
                QMessageBox.information(self, "Success", f"Project with ID {p_id} deleted successfully.")
                cur.close()
                conn.close()
                dialog.accept()  # close the dialog
            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"Failed to delete project:\n{e}")

        buttons.accepted.connect(on_ok_clicked)
        buttons.rejected.connect(dialog.reject)

        dialog.exec_()

    def update_projects(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Update Project")
        form_layout = QFormLayout()

        # --- Project ID ComboBox ---
        p_id_input = QComboBox()
        p_id_input.setEditable(True)
        try:
            conn = db.connect_to_db()
            cur = conn.cursor()
            cur.execute("SELECT p_id FROM project ORDER BY p_id;")
            p_ids = cur.fetchall()
            p_id_input.addItems([str(p[0]) for p in p_ids])
            cur.close()
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to load project IDs:\n{e}")
            return

        form_layout.addRow("Select Project ID:", p_id_input)

        load_button = QPushButton("Load Project Info")
        form_layout.addRow(load_button)

        dialog.setLayout(form_layout)

        def add_side_by_side(label, original_value, new_widget):
            row_widget = QWidget()
            row_layout = QHBoxLayout()
            row_layout.setContentsMargins(0, 0, 0, 0)
            old_label = QLabel(str(original_value) if original_value is not None else "")
            old_label.setFixedWidth(150)
            old_label.setStyleSheet("color: gray;")
            row_layout.addWidget(old_label)
            row_layout.addWidget(new_widget)
            row_widget.setLayout(row_layout)
            form_layout.addRow(f"{label} (Original → New):", row_widget)
            return new_widget

        def load_project_info():
            p_id = p_id_input.currentText().strip()
            if not p_id.isdigit():
                QMessageBox.warning(self, "Input Error", "Project ID must be a number.")
                return

            try:
                conn = db.connect_to_db()
                cur = conn.cursor()
                cur.execute("""
                    SELECT p_name, p_description, start_date, end_date,
                           fundraising_goal, status
                    FROM project WHERE p_id = %s
                """, (int(p_id),))
                project = cur.fetchone()

                if not project:
                    QMessageBox.warning(self, "Not Found", f"No project found with ID {p_id}.")
                    return

                p_name, p_description, start_date, end_date, fundraising_goal, status = project

                # Clear old form rows (except p_id and Load button)
                while form_layout.rowCount() > 2:
                    form_layout.removeRow(2)

                # Status ComboBox
                status_input = QComboBox()
                cur.execute("SELECT unnest(enum_range(NULL::project_status));")
                statuses = cur.fetchall()
                status_input.addItems([s[0] for s in statuses])
                status_input.setCurrentText(status)

                # Create editable inputs
                dialog.p_name_input = add_side_by_side("Project Name", p_name, QLineEdit(p_name))
                dialog.p_description_input = add_side_by_side("Description", p_description, QLineEdit(p_description))

                start_date_edit = QDateEdit()
                start_date_edit.setDate(start_date)
                start_date_edit.setCalendarPopup(True)
                dialog.start_date_input = add_side_by_side("Start Date", start_date, start_date_edit)

                end_date_edit = QDateEdit()
                if end_date:
                    end_date_edit.setDate(end_date)
                end_date_edit.setCalendarPopup(True)
                no_end_date_checkbox = QCheckBox("No End Date")
                no_end_date_checkbox.setChecked(end_date is None)
                end_date_edit.setEnabled(end_date is not None)
                no_end_date_checkbox.toggled.connect(end_date_edit.setDisabled)

                dialog.end_date_input = add_side_by_side("End Date", end_date, end_date_edit)
                form_layout.addRow("", no_end_date_checkbox)

                dialog.fundraising_goal_input = add_side_by_side("Fundraising Goal", fundraising_goal,
                                                                 QLineEdit(str(fundraising_goal)))
                dialog.status_input = add_side_by_side("Status", status, status_input)

                # OK/Cancel buttons
                buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
                buttons.accepted.connect(dialog.accept)
                buttons.rejected.connect(dialog.reject)
                form_layout.addWidget(buttons)

            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"Error loading project info:\n{e}")

        load_button.clicked.connect(load_project_info)

        if dialog.exec_() == QDialog.Accepted:
            p_id = p_id_input.currentText().strip()
            if not p_id.isdigit():
                QMessageBox.warning(self, "Input Error", "Project ID must be a number.")
                return

            try:
                conn = db.connect_to_db()
                cur = conn.cursor()

                cur.execute("""
                    UPDATE project
                    SET p_name = %s,
                        p_description = %s,
                        start_date = %s,
                        end_date = %s,
                        fundraising_goal = %s,
                        status = %s
                    WHERE p_id = %s
                """, (
                    dialog.p_name_input.text(),
                    dialog.p_description_input.text() or None,
                    dialog.start_date_input.date().toPyDate(),
                    None if dialog.findChild(QCheckBox).isChecked() else dialog.end_date_input.date().toPyDate(),
                    int(dialog.fundraising_goal_input.text()),
                    dialog.status_input.currentText(),
                    int(p_id)
                ))

                if cur.rowcount == 0:
                    QMessageBox.warning(self, "Not Found", f"No project found with ID {p_id}.")
                else:
                    conn.commit()
                    QMessageBox.information(self, "Success", f"Project with ID {p_id} updated successfully.")

                cur.close()
                conn.close()
            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"Failed to update project:\n{e}")

    def select_projects(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Select Projects")
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # All filter options
        filter_options = {
            "Project ID": {
                "query": "SELECT p_id FROM project ORDER BY p_id;",
                "column": "p_id",
                "type": int
            },
            "Project Name": {
                "query": "SELECT DISTINCT p_name FROM project ORDER BY p_name;",
                "column": "p_name",
                "type": str
            },
            "Start Date": {
                "query": "SELECT DISTINCT start_date FROM project ORDER BY start_date;",
                "column": "start_date",
                "type": str
            },
            "End Date": {
                "query": "SELECT DISTINCT end_date FROM project ORDER BY end_date;",
                "column": "start_date",
                "type": str
            },
            "Fundraising Goal": {
                "query": "SELECT fundraising_goal FROM project ORDER BY fundraising_goal;",
                "column": "fundraising_goal",
                "type": int
            },
            "Status": {
                "query": "SELECT unnest(enum_range(NULL::project_status));",
                "column": "status",
                "type": str
            }
        }

        # Widget to select which filters to enable (checkbox list)
        filter_checkboxes = {}
        value_selectors = {}

        for filter_name, info in filter_options.items():
            checkbox = QCheckBox(filter_name)
            filter_checkboxes[filter_name] = checkbox

            # Multi-select list for filter values, disabled initially
            list_widget = QListWidget()
            list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
            list_widget.setEnabled(False)
            value_selectors[filter_name] = list_widget

            # When checkbox toggled, enable/disable value selector and load values if enabling
            def on_checkbox_toggled(checked, fn=filter_name):
                list_widget = value_selectors[fn]
                list_widget.setEnabled(checked)
                if checked and list_widget.count() == 0:
                    # Load values from DB
                    try:
                        conn = db.connect_to_db()
                        cur = conn.cursor()
                        cur.execute(filter_options[fn]["query"])
                        results = cur.fetchall()
                        cur.close()
                        conn.close()

                        list_widget.clear()
                        for r in results:
                            if r[0] is not None:
                                list_widget.addItem(str(r[0]))
                    except Exception as e:
                        QMessageBox.critical(dialog, "Database Error", f"Failed to load {fn} values:\n{e}")

            checkbox.toggled.connect(on_checkbox_toggled)

            # Add to form: checkbox + value selector side by side
            row_widget = QWidget()
            row_layout = QHBoxLayout()
            row_layout.addWidget(checkbox)
            row_layout.addWidget(list_widget)
            row_widget.setLayout(row_layout)

            form_layout.addRow(row_widget)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)

        layout.addLayout(form_layout)
        layout.addWidget(buttons)
        dialog.setLayout(layout)

        if dialog.exec_() == QDialog.Accepted:
            query = "SELECT * FROM project"
            clauses = []
            params = []

            for filter_name, checkbox in filter_checkboxes.items():
                if checkbox.isChecked():
                    list_widget = value_selectors[filter_name]
                    selected_items = list_widget.selectedItems()
                    if not selected_items:
                        QMessageBox.warning(dialog, "Input Error",
                                            f"Please select at least one value for {filter_name}.")
                        return

                    values = [filter_options[filter_name]["type"](item.text()) for item in selected_items]
                    placeholders = ','.join(['%s'] * len(values))
                    column = filter_options[filter_name]["column"]
                    clauses.append(f"{column} IN ({placeholders})")
                    params.extend(values)

            if clauses:
                query += " WHERE " + " AND ".join(clauses)

            try:
                conn = db.connect_to_db()
                cur = conn.cursor()
                cur.execute(query, tuple(params))
                results = cur.fetchall()
                colnames = [desc[0] for desc in cur.description]
                cur.close()
                conn.close()

                if not results:
                    QMessageBox.information(dialog, "No Results", "No matching projects found.")
                    return

                # Show results
                result_dialog = QDialog(self)
                result_dialog.setWindowTitle("Project Results")
                layout = QVBoxLayout()

                table = QTableWidget()
                table.setColumnCount(len(colnames))
                table.setRowCount(len(results))
                table.setHorizontalHeaderLabels(colnames)

                for row_idx, row_data in enumerate(results):
                    for col_idx, value in enumerate(row_data):
                        item = QTableWidgetItem(str(value) if value is not None else "")
                        table.setItem(row_idx, col_idx, item)

                layout.addWidget(table)
                close_button = QPushButton("Close")
                close_button.clicked.connect(result_dialog.close)
                layout.addWidget(close_button)

                result_dialog.setLayout(layout)
                result_dialog.resize(800, 400)
                result_dialog.exec_()

            except Exception as e:
                QMessageBox.critical(dialog, "Database Error", f"Failed to retrieve projects:\n{e}")