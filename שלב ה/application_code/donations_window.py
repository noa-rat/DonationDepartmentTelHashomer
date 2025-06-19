from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QFont, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QMessageBox, QDialog, QFormLayout, \
    QLineEdit, QDialogButtonBox, QComboBox, QTableWidgetItem, QTableWidget, QHBoxLayout, QAbstractItemView, QListWidget, \
    QCheckBox, QGridLayout
import db
from datetime import date


class DonationsWindow(QWidget):
    def __init__(self, main_window=None, previous_window=None):
        super().__init__()
        self.main_window = main_window
        self.previous_window = previous_window

        self.setWindowTitle("Managing Donations")
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
        label = QLabel("Donations Options")
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

        self.btn_add_donations = QPushButton("Add Donation")
        self.btn_add_donations.setStyleSheet(btn_style)
        self.btn_add_donations.clicked.connect(self.add_donations)

        self.btn_delete_donations = QPushButton("Delete Donation")
        self.btn_delete_donations.setStyleSheet(btn_style)
        self.btn_delete_donations.clicked.connect(self.delete_donations)

        self.btn_update_donations = QPushButton("Update Donation")
        self.btn_update_donations.setStyleSheet(btn_style)
        self.btn_update_donations.clicked.connect(self.update_donations)

        self.btn_select_donations = QPushButton("Select Donation")
        self.btn_select_donations.setStyleSheet(btn_style)
        self.btn_select_donations.clicked.connect(self.select_donations)

        btn_grid.addWidget(self.btn_add_donations, 0, 0)
        btn_grid.addWidget(self.btn_delete_donations, 0, 1)
        btn_grid.addWidget(self.btn_update_donations, 1, 0)
        btn_grid.addWidget(self.btn_select_donations, 1, 1)

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

    def add_donations(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Add Donation")
        form_layout = QFormLayout()

        amount_input = QLineEdit()

        # --- Payment Method ComboBox ---
        method_input = QComboBox()
        try:
            conn = db.connect_to_db()
            cur = conn.cursor()
            cur.execute("SELECT unnest(enum_range(NULL::payment_method));")
            methods = cur.fetchall()
            method_input.addItems([m[0] for m in methods])
            cur.close()
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to load payment methods:\n{e}")
            return

        # --- Donor ID ComboBox ---
        donor_id_input = QComboBox()
        donor_id_input.setEditable(True)
        try:
            conn = db.connect_to_db()
            cur = conn.cursor()
            cur.execute("SELECT donor_id FROM donor ORDER BY donor_id;")
            donor_ids = cur.fetchall()
            donor_id_input.addItems([str(d[0]) for d in donor_ids])
            cur.close()
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to load donor IDs:\n{e}")
            return

        # --- Event ID ComboBox ---
        event_id_input = QComboBox()
        event_id_input.setEditable(True)
        event_id_input.addItem("")  # 👈 allows selecting "null"
        try:
            conn = db.connect_to_db()
            cur = conn.cursor()
            cur.execute("SELECT e_id FROM fundraisingevent ORDER BY e_id;")
            event_ids = cur.fetchall()
            event_id_input.addItems([str(e[0]) for e in event_ids])
            cur.close()
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to load event IDs:\n{e}")
            return

        # --- Project ID ComboBox ---
        project_id_input = QComboBox()
        project_id_input.setEditable(True)
        project_id_input.addItem("")  # 👈 allows selecting "null"
        try:
            conn = db.connect_to_db()
            cur = conn.cursor()
            cur.execute("SELECT p_id FROM project ORDER BY p_id;")
            project_ids = cur.fetchall()
            project_id_input.addItems([str(p[0]) for p in project_ids])
            cur.close()
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to load project IDs:\n{e}")
            return

        # --- Add Widgets to Form ---
        form_layout.addRow("Donor ID:", donor_id_input)
        form_layout.addRow("Amount:", amount_input)
        form_layout.addRow("Payment Method:", method_input)
        form_layout.addRow("Event ID:", event_id_input)
        form_layout.addRow("Project ID:", project_id_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        form_layout.addWidget(buttons)

        dialog.setLayout(form_layout)

        if dialog.exec_() == QDialog.Accepted:
            donor_id = donor_id_input.currentText()
            d_amount = amount_input.text()
            d_method = method_input.currentText()
            e_id = event_id_input.currentText()
            p_id = project_id_input.currentText()

            today = date.today()
            donation_date = today.strftime('%Y-%m-%d')

            if not donor_id or not d_amount or not d_method:
                QMessageBox.warning(self, "Input Error", "Donor ID, Amount, and Payment Method are required.")
                return

            try:
                conn = db.connect_to_db()
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO donation (donor_id, d_amount, d_method, d_date, e_id, p_id)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """, (
                    int(donor_id),
                    float(d_amount),
                    d_method,
                    donation_date,
                    int(e_id) if e_id else None,
                    int(p_id) if p_id else None
                ))

                conn.commit()
                cur.close()
                conn.close()
                QMessageBox.information(self, "Success", "Donation added successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"Failed to insert donation:\n{e}")

    def delete_donations(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Delete Donation")
        form_layout = QFormLayout()

        # Combo box to select existing donation_id
        donation_id_input = QComboBox()
        donation_id_input.setEditable(True)
        try:
            conn = db.connect_to_db()
            cur = conn.cursor()
            cur.execute("SELECT donation_id FROM donation ORDER BY donation_id;")
            donation_ids = cur.fetchall()
            donation_id_input.addItems([str(d[0]) for d in donation_ids])
            cur.close()
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to load donation IDs:\n{e}")
            return

        form_layout.addRow("Donation ID:", donation_id_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        form_layout.addWidget(buttons)

        dialog.setLayout(form_layout)

        if dialog.exec_() == QDialog.Accepted:
            donation_id = donation_id_input.currentText()
            if not donation_id:
                QMessageBox.warning(self, "Input Error", "Donation ID is required.")
                return

            try:
                conn = db.connect_to_db()
                cur = conn.cursor()
                cur.execute("DELETE FROM donation WHERE donation_id = %s", (int(donation_id),))
                if cur.rowcount == 0:
                    QMessageBox.information(self, "Not Found", f"No donation with ID {donation_id} was found.")
                else:
                    conn.commit()
                    QMessageBox.information(self, "Success", f"Donation with ID {donation_id} deleted successfully.")
                cur.close()
                conn.close()
            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"Failed to delete donation:\n{e}")

    def update_donations(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Update Donation")
        form_layout = QFormLayout()

        # --- Donation ID ComboBox ---
        donation_id_input = QComboBox()
        donation_id_input.setEditable(True)
        try:
            conn = db.connect_to_db()
            cur = conn.cursor()
            cur.execute("SELECT donation_id FROM donation ORDER BY donation_id;")
            donation_ids = cur.fetchall()
            donation_id_input.addItems([str(d[0]) for d in donation_ids])
            cur.close()
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to load donation IDs:\n{e}")
            return

        form_layout.addRow("Select Donation ID:", donation_id_input)

        load_button = QPushButton("Load Donation Info")
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

        def load_donation_info():
            donation_id = donation_id_input.currentText().strip()
            if not donation_id.isdigit():
                QMessageBox.warning(self, "Input Error", "Donation ID must be a number.")
                return

            try:
                conn = db.connect_to_db()
                cur = conn.cursor()
                cur.execute("""
                    SELECT d_method, e_id, p_id
                    FROM donation WHERE donation_id = %s
                """, (int(donation_id),))
                donation = cur.fetchone()

                if not donation:
                    QMessageBox.warning(self, "Not Found", f"No donation found with ID {donation_id}.")
                    return

                d_method, e_id, p_id = donation

                # Clear old rows except first two
                while form_layout.rowCount() > 2:
                    form_layout.removeRow(2)

                # --- Payment Method ComboBox ---
                method_input = QComboBox()
                try:
                    cur.execute("SELECT unnest(enum_range(NULL::payment_method));")
                    methods = cur.fetchall()
                    method_input.addItems([m[0] for m in methods])
                    method_input.setCurrentText(d_method)
                except Exception as e:
                    QMessageBox.critical(self, "Database Error", f"Failed to load payment methods:\n{e}")
                    return

                # --- Event ID ComboBox ---
                event_id_input = QComboBox()
                event_id_input.setEditable(True)
                event_id_input.addItem("")  # for NULL
                try:
                    cur.execute("SELECT e_id FROM fundraisingevent ORDER BY e_id;")
                    event_ids = cur.fetchall()
                    event_id_input.addItems([str(e[0]) for e in event_ids])
                    if e_id is not None:
                        event_id_input.setCurrentText(str(e_id))
                except Exception as e:
                    QMessageBox.critical(self, "Database Error", f"Failed to load event IDs:\n{e}")
                    return

                # --- Project ID ComboBox ---
                project_id_input = QComboBox()
                project_id_input.setEditable(True)
                project_id_input.addItem("")  # for NULL
                try:
                    cur.execute("SELECT p_id FROM project ORDER BY p_id;")
                    project_ids = cur.fetchall()
                    project_id_input.addItems([str(p[0]) for p in project_ids])
                    if p_id is not None:
                        project_id_input.setCurrentText(str(p_id))
                except Exception as e:
                    QMessageBox.critical(self, "Database Error", f"Failed to load project IDs:\n{e}")
                    return

                cur.close()
                conn.close()

                # Add side-by-side fields
                dialog.method_input = add_side_by_side("Payment Method", d_method, method_input)
                dialog.event_id_input = add_side_by_side("Event ID", e_id, event_id_input)
                dialog.project_id_input = add_side_by_side("Project ID", p_id, project_id_input)

                # OK/Cancel buttons
                buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
                buttons.accepted.connect(dialog.accept)
                buttons.rejected.connect(dialog.reject)
                form_layout.addWidget(buttons)

            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"Error loading donation info:\n{e}")

        load_button.clicked.connect(load_donation_info)

        if dialog.exec_() == QDialog.Accepted:
            donation_id = donation_id_input.currentText().strip()
            if not donation_id.isdigit():
                QMessageBox.warning(self, "Input Error", "Donation ID must be a number.")
                return

            d_method = dialog.method_input.currentText()
            e_id = dialog.event_id_input.currentText().strip()
            p_id = dialog.project_id_input.currentText().strip()

            if not d_method:
                QMessageBox.warning(self, "Input Error", "Payment Method is required.")
                return

            try:
                conn = db.connect_to_db()
                cur = conn.cursor()
                cur.execute("""
                    UPDATE donation
                    SET d_method = %s,
                        e_id = %s,
                        p_id = %s
                    WHERE donation_id = %s
                """, (
                    d_method,
                    int(e_id) if e_id else None,
                    int(p_id) if p_id else None,
                    int(donation_id)
                ))

                if cur.rowcount == 0:
                    QMessageBox.warning(self, "Not Found", f"No donation found with ID {donation_id}.")
                else:
                    conn.commit()
                    QMessageBox.information(self, "Success", f"Donation with ID {donation_id} updated successfully.")

                cur.close()
                conn.close()
            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"Failed to update donation:\n{e}")


    def select_donations(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Select Donations")
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        filter_options = {
            "Donation ID": {
                "query": "SELECT donation_id FROM donation ORDER BY donation_id;",
                "column": "donation_id",
                "type": int
            },
            "Donor ID": {
                "query": "SELECT donor_id FROM donor ORDER BY donor_id;",
                "column": "donor_id",
                "type": int
            },
            "Event ID": {
                "query": "SELECT e_id FROM fundraisingevent ORDER BY e_id;",
                "column": "e_id",
                "type": int
            },
            "Project ID": {
                "query": "SELECT p_id FROM project ORDER BY p_id;",
                "column": "p_id",
                "type": int
            },
            "Payment Method": {
                "query": "SELECT unnest(enum_range(NULL::payment_method));",
                "column": "d_method",
                "type": str
            },
            "Donation Date": {
                "query": "SELECT DISTINCT d_date FROM donation ORDER BY d_date;",
                "column": "d_date",
                "type": str
            },
            "Donation Amount": {
                "query": "SELECT DISTINCT d_amount FROM donation ORDER BY d_amount;",
                "column": "d_amount",
                "type": float
            }
        }

        filter_checkboxes = {}
        value_selectors = {}

        for filter_name, info in filter_options.items():
            checkbox = QCheckBox(filter_name)
            filter_checkboxes[filter_name] = checkbox

            list_widget = QListWidget()
            list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
            list_widget.setEnabled(False)
            value_selectors[filter_name] = list_widget

            def on_checkbox_toggled(checked, fn=filter_name):
                list_widget = value_selectors[fn]
                list_widget.setEnabled(checked)
                if checked and list_widget.count() == 0:
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
            query = "SELECT * FROM donation"
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

                    # Convert selected strings back to proper type
                    values = []
                    for item in selected_items:
                        val = item.text()
                        try:
                            values.append(filter_options[filter_name]["type"](val))
                        except Exception:
                            values.append(val)

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
                    QMessageBox.information(dialog, "No Results", "No matching donations found.")
                    return

                result_dialog = QDialog(self)
                result_dialog.setWindowTitle("Donation Results")
                result_layout = QVBoxLayout()

                table = QTableWidget()
                table.setColumnCount(len(colnames))
                table.setRowCount(len(results))
                table.setHorizontalHeaderLabels(colnames)

                for row_idx, row_data in enumerate(results):
                    for col_idx, value in enumerate(row_data):
                        item = QTableWidgetItem(str(value) if value is not None else "")
                        table.setItem(row_idx, col_idx, item)

                result_layout.addWidget(table)
                close_button = QPushButton("Close")
                close_button.clicked.connect(result_dialog.close)
                result_layout.addWidget(close_button)

                result_dialog.setLayout(result_layout)
                result_dialog.resize(800, 400)
                result_dialog.exec_()

            except Exception as e:
                QMessageBox.critical(dialog, "Database Error", f"Failed to retrieve donations:\n{e}")