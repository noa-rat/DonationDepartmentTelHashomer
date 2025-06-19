from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QFont, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QMessageBox, QDialog, QFormLayout, \
    QLineEdit, QDialogButtonBox, QComboBox, QTableWidgetItem, QTableWidget, QInputDialog, QHBoxLayout, QListWidget, \
    QAbstractItemView, QCheckBox, QGridLayout
import db

class DonorsWindow(QWidget):
    def __init__(self, main_window=None, previous_window=None):
        super().__init__()
        self.main_window = main_window
        self.previous_window = previous_window

        self.setWindowTitle("Managing Donors")
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
        label = QLabel("Donor Options")
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

        self.btn_add_donors = QPushButton("Add Donor")
        self.btn_add_donors.setStyleSheet(btn_style)
        self.btn_add_donors.clicked.connect(self.add_donors)

        self.btn_delete_donors = QPushButton("Delete Donor")
        self.btn_delete_donors.setStyleSheet(btn_style)
        self.btn_delete_donors.clicked.connect(self.delete_donors)

        self.btn_update_donors = QPushButton("Update Donor")
        self.btn_update_donors.setStyleSheet(btn_style)
        self.btn_update_donors.clicked.connect(self.update_donors)

        self.btn_select_donors = QPushButton("Select Donor")
        self.btn_select_donors.setStyleSheet(btn_style)
        self.btn_select_donors.clicked.connect(self.select_donors)

        btn_grid.addWidget(self.btn_add_donors, 0, 0)
        btn_grid.addWidget(self.btn_delete_donors, 0, 1)
        btn_grid.addWidget(self.btn_update_donors, 1, 0)
        btn_grid.addWidget(self.btn_select_donors, 1, 1)

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

    def add_donors(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Add Donor")
        form_layout = QFormLayout()

        # Name (required)
        name_input = QLineEdit()
        # Phone (optional)
        phone_input = QLineEdit()
        # Email (optional)
        email_input = QLineEdit()
        # Address (optional)
        address_input = QLineEdit()
        # City (optional)
        city_input = QLineEdit()
        # Country (optional)
        country_input = QLineEdit()
        # Is Member (boolean, checkbox or combobox)
        is_member_input = QComboBox()
        is_member_input.addItems(["False", "True"])
        # Donor Type from enum donor_type
        d_type_input = QComboBox()
        try:
            conn = db.connect_to_db()
            cur = conn.cursor()
            cur.execute("SELECT unnest(enum_range(NULL::donor_type));")
            donor_types = cur.fetchall()
            d_type_input.addItems([dt[0] for dt in donor_types])
            cur.close()
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to load donor types:\n{e}")
            return

        # Fundraiser ID dropdown (editable with autofill)
        fundraiser_id_input = QComboBox()
        fundraiser_id_input.setEditable(True)
        try:
            conn = db.connect_to_db()
            cur = conn.cursor()
            cur.execute("SELECT employee_id FROM fundraiser ORDER BY employee_id;")
            fundraiser_ids = cur.fetchall()
            fundraiser_id_input.addItems([str(fid[0]) for fid in fundraiser_ids])
            cur.close()
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to load fundraiser IDs:\n{e}")
            return

        # Add all widgets to the form
        form_layout.addRow("Name:", name_input)
        form_layout.addRow("Phone:", phone_input)
        form_layout.addRow("Email:", email_input)
        form_layout.addRow("Address:", address_input)
        form_layout.addRow("City:", city_input)
        form_layout.addRow("Country:", country_input)
        form_layout.addRow("Is Member:", is_member_input)
        form_layout.addRow("Donor Type:", d_type_input)
        form_layout.addRow("Fundraiser ID:", fundraiser_id_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        form_layout.addWidget(buttons)

        dialog.setLayout(form_layout)

        if dialog.exec_() == QDialog.Accepted:
            name = name_input.text().strip()
            phone = phone_input.text().strip() or None
            email = email_input.text().strip() or None
            address = address_input.text().strip() or None
            city = city_input.text().strip() or None
            country = country_input.text().strip() or None
            is_member = is_member_input.currentText() == "True"
            d_type = d_type_input.currentText()
            fundraiser_id_text = fundraiser_id_input.currentText().strip()
            fundraiser_id = int(fundraiser_id_text) if fundraiser_id_text.isdigit() else None

            if not name:
                QMessageBox.warning(self, "Input Error", "Name is required.")
                return

            try:
                conn = db.connect_to_db()
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO donor (name, p_phone, p_email, p_address, p_city, p_country, is_member, d_type, fundraiser_id)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    name,
                    phone,
                    email,
                    address,
                    city,
                    country,
                    is_member,
                    d_type,
                    fundraiser_id
                ))
                conn.commit()
                cur.close()
                conn.close()
                QMessageBox.information(self, "Success", "Donor added successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"Failed to insert donor:\n{e}")

    def delete_donors(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Delete Donor")
        form_layout = QFormLayout()

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

        form_layout.addRow("Select Donor ID:", donor_id_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        form_layout.addWidget(buttons)

        dialog.setLayout(form_layout)

        def on_ok_clicked():
            donor_id = donor_id_input.currentText().strip()
            if not donor_id.isdigit():
                QMessageBox.warning(self, "Input Error", "Donor ID must be a number.")
                return

            try:
                conn = db.connect_to_db()
                cur = conn.cursor()

                cur.execute("SELECT COUNT(*) FROM donor WHERE donor_id = %s;", (donor_id,))
                count = cur.fetchone()[0]
                if count == 0:
                    QMessageBox.warning(self, "Not Found", f"No donor found with ID {donor_id}.")
                    cur.close()
                    conn.close()
                    return

                # Confirm deletion
                reply = QMessageBox.question(
                    self, "Confirm Delete",
                    f"Are you sure you want to delete donor with ID {donor_id}?",
                    QMessageBox.Yes | QMessageBox.No
                )
                if reply == QMessageBox.No:
                    cur.close()
                    conn.close()
                    return

                # Perform delete
                cur.execute("DELETE FROM donor WHERE donor_id = %s;", (donor_id,))
                conn.commit()
                QMessageBox.information(self, "Success", f"Donor with ID {donor_id} deleted successfully.")
                cur.close()
                conn.close()
                dialog.accept()  # close the dialog
            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"Failed to delete donor:\n{e}")

        buttons.accepted.connect(on_ok_clicked)
        buttons.rejected.connect(dialog.reject)

        dialog.exec_()

    def update_donors(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Update Donor")
        form_layout = QFormLayout()

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

        form_layout.addRow("Select Donor ID:", donor_id_input)

        load_button = QPushButton("Load Donor Info")
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

        def load_donor_info():
            donor_id = donor_id_input.currentText().strip()
            if not donor_id.isdigit():
                QMessageBox.warning(self, "Input Error", "Donor ID must be a number.")
                return

            try:
                conn = db.connect_to_db()
                cur = conn.cursor()
                cur.execute("""
                    SELECT name, p_phone, p_email, p_address, p_city, p_country, is_member, d_type, fundraiser_id
                    FROM donor WHERE donor_id = %s
                """, (int(donor_id),))
                donor = cur.fetchone()

                if not donor:
                    QMessageBox.warning(self, "Not Found", f"No donor found with ID {donor_id}.")
                    return

                name, phone, email, address, city, country, is_member, d_type, fundraiser_id = donor

                # Clear old rows except first two
                while form_layout.rowCount() > 2:
                    form_layout.removeRow(2)

                # --- Donor Type ComboBox ---
                d_type_input = QComboBox()
                try:
                    cur.execute("SELECT unnest(enum_range(NULL::donor_type));")
                    donor_types = cur.fetchall()
                    d_type_input.addItems([d[0] for d in donor_types])
                    d_type_input.setCurrentText(d_type)
                except Exception as e:
                    QMessageBox.critical(self, "Database Error", f"Failed to load donor types:\n{e}")
                    return

                # --- Fundraiser ID ComboBox ---
                fundraiser_id_input = QComboBox()
                fundraiser_id_input.setEditable(True)
                fundraiser_id_input.addItem("")
                try:
                    cur.execute("SELECT employee_id FROM fundraiser ORDER BY employee_id;")
                    fundraiser_ids = cur.fetchall()
                    fundraiser_id_input.addItems([str(f[0]) for f in fundraiser_ids])
                    if fundraiser_id:
                        fundraiser_id_input.setCurrentText(str(fundraiser_id))
                except Exception as e:
                    QMessageBox.critical(self, "Database Error", f"Failed to load fundraiser IDs:\n{e}")
                    return

                cur.close()
                conn.close()

                # Create editable inputs and add rows
                name_input = add_side_by_side("Name", name, QLineEdit(name))
                phone_input = add_side_by_side("Phone", phone, QLineEdit(phone or ""))
                email_input = add_side_by_side("Email", email, QLineEdit(email or ""))
                address_input = add_side_by_side("Address", address, QLineEdit(address or ""))
                city_input = add_side_by_side("City", city, QLineEdit(city or ""))
                country_input = add_side_by_side("Country", country, QLineEdit(country or ""))

                is_member_input = QComboBox()
                is_member_input.addItems(["False", "True"])
                is_member_input.setCurrentText("True" if is_member else "False")
                add_side_by_side("Is Member", is_member, is_member_input)

                add_side_by_side("Donor Type", d_type, d_type_input)
                add_side_by_side("Fundraiser ID", fundraiser_id, fundraiser_id_input)

                # OK/Cancel buttons
                buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
                buttons.accepted.connect(dialog.accept)
                buttons.rejected.connect(dialog.reject)
                form_layout.addWidget(buttons)

                # Store inputs on dialog to access later
                dialog.name_input = name_input
                dialog.phone_input = phone_input
                dialog.email_input = email_input
                dialog.address_input = address_input
                dialog.city_input = city_input
                dialog.country_input = country_input
                dialog.is_member_input = is_member_input
                dialog.d_type_input = d_type_input
                dialog.fundraiser_id_input = fundraiser_id_input

            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"Error loading donor info:\n{e}")

        load_button.clicked.connect(load_donor_info)

        if dialog.exec_() == QDialog.Accepted:
            donor_id = donor_id_input.currentText().strip()
            if not donor_id.isdigit():
                QMessageBox.warning(self, "Input Error", "Donor ID must be a number.")
                return

            # Retrieve updated values
            name = dialog.name_input.text().strip()
            if not name:
                QMessageBox.warning(self, "Input Error", "Name is required.")
                return

            phone = dialog.phone_input.text().strip() or None
            email = dialog.email_input.text().strip() or None
            address = dialog.address_input.text().strip() or None
            city = dialog.city_input.text().strip() or None
            country = dialog.country_input.text().strip() or None
            is_member = dialog.is_member_input.currentText() == "True"
            d_type = dialog.d_type_input.currentText()
            fundraiser_id_text = dialog.fundraiser_id_input.currentText().strip()
            fundraiser_id = int(fundraiser_id_text) if fundraiser_id_text.isdigit() else None

            try:
                conn = db.connect_to_db()
                cur = conn.cursor()
                cur.execute("""
                    UPDATE donor SET
                        name = %s,
                        p_phone = %s,
                        p_email = %s,
                        p_address = %s,
                        p_city = %s,
                        p_country = %s,
                        is_member = %s,
                        d_type = %s,
                        fundraiser_id = %s
                    WHERE donor_id = %s
                """, (
                    name, phone, email, address, city, country,
                    is_member, d_type, fundraiser_id, int(donor_id)
                ))

                if cur.rowcount == 0:
                    QMessageBox.warning(self, "Not Found", f"No donor found with ID {donor_id}.")
                else:
                    conn.commit()
                    QMessageBox.information(self, "Success", f"Donor with ID {donor_id} updated successfully.")

                cur.close()
                conn.close()
            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"Failed to update donor:\n{e}")

    def select_donors(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Select Donors")
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # All filter options
        filter_options = {
            "Donor ID": {
                "query": "SELECT donor_id FROM donor ORDER BY donor_id;",
                "column": "donor_id",
                "type": int
            },
            "Country": {
                "query": "SELECT DISTINCT p_country FROM donor WHERE p_country IS NOT NULL ORDER BY p_country;",
                "column": "p_country",
                "type": str
            },
            "Member Status": {
                "query": "SELECT DISTINCT is_member FROM donor ORDER BY is_member;",
                "column": "is_member",
                "type": lambda x: x.lower() == 'true'
            },
            "Donor Type": {
                "query": "SELECT unnest(enum_range(NULL::donor_type));",
                "column": "d_type",
                "type": str
            },
            "Guiding Fundraiser": {
                "query": "SELECT fundraiser_id FROM fundraiser ORDER BY fundraiser_id;",
                "column": "fundraiser_id",
                "type": int
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
            query = "SELECT * FROM donor"
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
                    QMessageBox.information(dialog, "No Results", "No matching donors found.")
                    return

                # Show results
                result_dialog = QDialog(self)
                result_dialog.setWindowTitle("Donor Results")
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
                QMessageBox.critical(dialog, "Database Error", f"Failed to retrieve donors:\n{e}")