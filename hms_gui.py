import tkinter as tk
from tkinter import messagebox, ttk
import tkinter.font as tkfont

# ============================================================
#   HOSPITAL MANAGEMENT SYSTEM
#   Developed by Ali Rind Baloch
# ============================================================

# ============================================================
# BACKEND CLASSES
# ============================================================


class Patient:
    def __init__(self, patient_id, name, age, gender, contact, medical_History):
        self.__patient_id = patient_id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__contact = contact
        self.__medical_History = medical_History

    def get_patient_id(self): return self.__patient_id
    def get_name(self): return self.__name
    def get_age(self): return self.__age
    def get_gender(self): return self.__gender
    def get_contact(self): return self.__contact
    def get_medical_History(self): return self.__medical_History

    def set_patient_contact(self, new_contact):
        if len(new_contact) >= 10:
            self.__contact = new_contact
            return True, f"Contact updated: {new_contact}"
        return False, "Wrong number! At least 10 digits required."

    def set_medical_history(self, new_history):
        self.__medical_History = new_history
        return True, f"Medical history updated."

    def set_age(self, new_age):
        try:
            new_age = int(new_age)
            if 0 < new_age < 150:
                self.__age = new_age
                return True, f"Age updated: {new_age}"
            return False, "Wrong age entered!"
        except ValueError:
            return False, "Age must be a number!"

    def register(self):
        return (f"Patient ID : {self.__patient_id}\n"
                f"Name       : {self.__name}\n"
                f"Age        : {self.__age}\n"
                f"Gender     : {self.__gender}\n"
                f"Contact    : {self.__contact}\n"
                f"History    : {self.__medical_History}")

    def view_history(self):
        if self.__medical_History:
            return self.__medical_History
        return "Medical History Not Found"

    def book_appointment(self, doctor_name, date, time):
        if not doctor_name:
            return -1, "Doctor name is required!"
        if not date:
            return -1, "Date is required!"
        appointment_id = self.__patient_id * 100 + 1
        info = (f"Appointment ID : {appointment_id}\n"
                f"Patient        : {self.__name}\n"
                f"Doctor         : {doctor_name}\n"
                f"Date           : {date}\n"
                f"Time           : {time}\n"
                f"Status         : CONFIRMED")
        return appointment_id, info

    def __str__(self):
        return (f"Patient [{self.__patient_id}]  Name: {self.__name}  "
                f"Age: {self.__age}  Contact: {self.__contact}")


class Doctor:
    def __init__(self, doctor_id, name, specialization, contact):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__specialization = specialization
        self.__contact = contact

    def get_doctor_id(self): return self.__doctor_id
    def get_name(self): return self.__name
    def get_specialization(self): return self.__specialization
    def get_contact(self): return self.__contact

    def set_contact(self, new_contact):
        if len(new_contact) >= 10:
            self.__contact = new_contact
            return True, f"Contact updated: {new_contact}"
        return False, "Invalid Contact Number"

    def set_specialization(self, new_spec):
        if new_spec:
            self.__specialization = new_spec
            return True, f"Specialization updated: {new_spec}"
        return False, "Specialization can't be empty!"

    def diagnose(self, patient_name):
        if not patient_name:
            return False, "Patient name is necessary!"
        return True, (f"Doctor      : Dr. {self.__name}\n"
                      f"Specialization : {self.__specialization}\n"
                      f"Patient     : {patient_name}\n"
                      f"Status      : Examined")

    def prescribe_medicine(self, medicine, dosage):
        if not medicine:
            return -1, "Medicine name is required!"
        if not dosage:
            return -1, "Dosage is required!"
        prescription_id = self.__doctor_id * 100 + 1
        info = (f"Doctor          : Dr. {self.__name}\n"
                f"Prescription ID : {prescription_id}\n"
                f"Medicine        : {medicine}\n"
                f"Dosage          : {dosage}\n"
                f"Status          : Issued")
        return prescription_id, info

    def check_schedule(self):
        return (f"Doctor         : Dr. {self.__name}\n"
                f"Specialization : {self.__specialization}\n"
                f"Contact        : {self.__contact}\n"
                f"Timing         : 9:00 AM to 5:00 PM\n"
                f"Days           : Monday to Saturday")

    def __str__(self):
        return (f"ID: {self.__doctor_id}  Dr. {self.__name}  "
                f"Spec: {self.__specialization}  Contact: {self.__contact}")


class Nurse:
    def __init__(self, nurse_id, name, shift):
        self.__nurse_id = nurse_id
        self.__name = name
        self.__shift = shift

    def get_name(self): return self.__name
    def get_nurse_id(self): return self.__nurse_id
    def get_shift(self): return self.__shift

    def set_name(self, new_name):
        if new_name:
            self.__name = new_name
            return True, f"Name updated: {new_name}"
        return False, "Empty name not allowed!"

    def set_shift(self, new_shift):
        if new_shift in ["Morning", "Evening", "Night"]:
            self.__shift = new_shift
            return True, f"Shift updated: {new_shift}"
        return False, "Wrong Shift! Use Morning, Evening or Night."

    def assist_doctor(self, doctor_name):
        if not doctor_name:
            return False, "Doctor name is missing!"
        return True, (f"Nurse  : {self.__name}\n"
                      f"Shift  : {self.__shift}\n"
                      f"Doctor : Dr. {doctor_name}\n"
                      f"Status : Assisting")

    def check_patient(self, patient_name):
        if not patient_name:
            return False, "Patient name is required!"
        return True, (f"Nurse   : {self.__name}\n"
                      f"Shift   : {self.__shift}\n"
                      f"Patient : {patient_name}\n"
                      f"Status  : Checked")

    def __str__(self):
        return f"ID: {self.__nurse_id}  {self.__name}  Shift: {self.__shift}"


class Department:
    def __init__(self, department_id, name):
        self.__department_id = department_id
        self.__name = name
        self.__doctors = []
        self.__nurses = []

    def get_department_id(self): return self.__department_id
    def get_name(self): return self.__name
    def get_doctors(self): return self.__doctors
    def get_nurses(self): return self.__nurses

    def set_name(self, new_name):
        if new_name:
            self.__name = new_name
            return True, f"Department name updated: {new_name}"
        return False, "Name can't be empty!"

    def add_doctor(self, doctor_name):
        if not doctor_name:
            return False, "Doctor name is required!"
        self.__doctors.append(doctor_name)
        return True, f"Dr. {doctor_name} added to {self.__name}"

    def add_nurse(self, nurse_name):
        if not nurse_name:
            return False, "Nurse name can't be empty!"
        self.__nurses.append(nurse_name)
        return True, f"{nurse_name} added to {self.__name}"

    def manage_staff(self):
        doc_list = "\n".join(
            [f"  • Dr. {d}" for d in self.__doctors]) if self.__doctors else "  No doctors found"
        nur_list = "\n".join(
            [f"  • {n}" for n in self.__nurses]) if self.__nurses else "  No nurses found"
        return (f"Department : {self.__name}  (ID: {self.__department_id})\n\n"
                f"Doctors ({len(self.__doctors)}):\n{doc_list}\n\n"
                f"Nurses ({len(self.__nurses)}):\n{nur_list}")

    def __str__(self):
        return (f"ID: {self.__department_id}  {self.__name}  "
                f"Doctors: {len(self.__doctors)}  Nurses: {len(self.__nurses)}")


class Ward:
    def __init__(self, ward_id, ward_name, capacity):
        self.__ward_id = ward_id
        self.__ward_name = ward_name
        self.__capacity = capacity
        self.__beds = []

    def get_ward_id(self): return self.__ward_id
    def get_ward_name(self): return self.__ward_name
    def get_capacity(self): return self.__capacity
    def get_beds(self): return self.__beds

    def set_ward_name(self, new_name):
        if new_name:
            self.__ward_name = new_name
            return True, f"Ward name updated: {new_name}"
        return False, "Ward name not available!"

    def set_capacity(self, new_capacity):
        if new_capacity > 0:
            self.__capacity = new_capacity
            return True, f"Capacity updated: {new_capacity}"
        return False, "Invalid capacity!"

    def check_availability(self):
        available = self.__capacity - len(self.__beds)
        status = "Available" if available > 0 else "Full"
        return (f"Ward        : {self.__ward_name}\n"
                f"Total Beds  : {self.__capacity}\n"
                f"Occupied    : {len(self.__beds)}\n"
                f"Available   : {available}\n"
                f"Status      : {status}"), available

    def get_available_beds(self):
        available = self.__capacity - len(self.__beds)
        return (f"Ward            : {self.__ward_name}\n"
                f"Total Capacity  : {self.__capacity}\n"
                f"Occupied Beds   : {len(self.__beds)}\n"
                f"Available Beds  : {available}"), available

    def add_bed(self, bed_id):
        if len(self.__beds) >= self.__capacity:
            return False, "Ward is full! Bed cannot be added."
        self.__beds.append(bed_id)
        return True, f"Bed {bed_id} added successfully!"

    def __str__(self):
        return (f"ID: {self.__ward_id}  {self.__ward_name}  "
                f"Capacity: {self.__capacity}  Beds: {len(self.__beds)}")


class Bed:
    def __init__(self, bed_id, status="Available"):
        self.__bed_id = bed_id
        self.__status = "Available"

    def get_bed_id(self): return self.__bed_id
    def get_status(self): return self.__status

    def set_status(self, new_status):
        if new_status in ["Available", "Occupied"]:
            self.__status = new_status
            return True, f"Status updated: {new_status}"
        return False, "Wrong status! Use Available or Occupied."

    def allocate_bed(self, patient_name):
        if self.__status != "Available":
            return False, f"Bed {self.__bed_id} is not available! Status: {self.__status}"
        if not patient_name:
            return False, "Patient name is required!"
        self.__status = "Occupied"
        return True, (f"Bed ID  : {self.__bed_id}\n"
                      f"Patient : {patient_name}\n"
                      f"Status  : {self.__status}")

    def release_bed(self):
        if self.__status == "Available":
            return False, f"Bed {self.__bed_id} is already available!"
        self.__status = "Available"
        return True, f"Bed {self.__bed_id} has been released. Status: {self.__status}"

    def update_status(self, new_status):
        if new_status in ["Available", "Occupied"]:
            old = self.__status
            self.__status = new_status
            return True, f"Bed {self.__bed_id}: {old} → {self.__status}"
        return False, "Wrong status! Use Available or Occupied."

    def __str__(self):
        return f"Bed ID: {self.__bed_id}  Status: {self.__status}"


class Appointment:
    def __init__(self, appointment_id, date, time, patient_name, doctor_name):
        self.__appointment_id = appointment_id
        self.__date = date
        self.__time = time
        self.__status = "Scheduled"
        self.__patient_name = patient_name
        self.__doctor_name = doctor_name

    def get_appointment_id(self): return self.__appointment_id
    def get_date(self): return self.__date
    def get_time(self): return self.__time
    def get_status(self): return self.__status
    def get_patient_name(self): return self.__patient_name
    def get_doctor_name(self): return self.__doctor_name

    def set_date(self, new_date):
        if new_date:
            self.__date = new_date
            return True, f"Date updated: {new_date}"
        return False, "Date is empty!"

    def set_time(self, new_time):
        if new_time:
            self.__time = new_time
            return True, f"Time updated: {new_time}"
        return False, "Time is empty!"

    def schedule(self):
        if self.__status != "Canceled":
            return False, "Only canceled appointments can be rescheduled!"
        self.__status = "Scheduled"
        return True, (f"Appointment ID : {self.__appointment_id}\n"
                      f"Patient        : {self.__patient_name}\n"
                      f"Doctor         : Dr. {self.__doctor_name}\n"
                      f"Date           : {self.__date}\n"
                      f"Time           : {self.__time}\n"
                      f"Status         : {self.__status}")

    def cancel(self):
        if self.__status == "Canceled":
            return False, "Appointment is already canceled!"
        self.__status = "Canceled"
        return True, (f"Appointment ID : {self.__appointment_id}\n"
                      f"Patient        : {self.__patient_name}\n"
                      f"Doctor         : Dr. {self.__doctor_name}\n"
                      f"Status         : {self.__status}")

    def reschedule(self, new_date, new_time):
        if self.__status == "Cancelled":
            return False, "Canceled appointment can't be rescheduled!"
        if not new_date:
            return False, "Date is required!"
        if not new_time:
            return False, "Time is required!"
        old_date, old_time = self.__date, self.__time
        self.__date = new_date
        self.__time = new_time
        self.__status = "Rescheduled"
        return True, (f"Appointment ID : {self.__appointment_id}\n"
                      f"Patient        : {self.__patient_name}\n"
                      f"Doctor         : {self.__doctor_name}\n"
                      f"Old Date       : {old_date}  →  New Date: {new_date}\n"
                      f"Old Time       : {old_time}  →  New Time: {new_time}\n"
                      f"Status         : {self.__status}")

    def __str__(self):
        return (f"ID: {self.__appointment_id}  Patient: {self.__patient_name}  "
                f"Doctor: {self.__doctor_name}  Date: {self.__date}  Status: {self.__status}")


class MedicalRecord:
    def __init__(self, record_id, diagnosis, treatment, test_reports):
        self.__record_id = record_id
        self.__diagnosis = diagnosis
        self.__treatment = treatment
        self.__test_reports = test_reports

    def get_record_id(self): return self.__record_id
    def get_diagnosis(self): return self.__diagnosis
    def get_treatment(self): return self.__treatment
    def get_test_reports(self): return self.__test_reports

    def set_diagnosis(self, new_diagnosis):
        if new_diagnosis:
            self.__diagnosis = new_diagnosis
            return True, f"Diagnosis updated!"
        return False, "Diagnosis can't be empty!"

    def set_treatment(self, new_treatment):
        if new_treatment:
            self.__treatment = new_treatment
            return True, "Treatment updated!"
        return False, "Treatment can't be empty!"

    def set_test_reports(self, new_report):
        if new_report:
            self.__test_reports = new_report
            return True, "Report updated!"
        return False, "Report can't be empty!"

    def update_record(self, new_diagnosis, new_treatment, new_reports):
        if not new_diagnosis:
            return False, "Diagnosis is required!"
        if not new_treatment:
            return False, "Treatment is required!"
        if not new_reports:
            return False, "Report is required!"
        old_d, old_t = self.__diagnosis, self.__treatment
        self.__diagnosis = new_diagnosis
        self.__treatment = new_treatment
        self.__test_reports = new_reports
        return True, (f"Record ID     : {self.__record_id}\n"
                      f"Old Diagnosis : {old_d}\n"
                      f"New Diagnosis : {self.__diagnosis}\n"
                      f"Old Treatment : {old_t}\n"
                      f"New Treatment : {self.__treatment}")

    def view_record(self):
        return (f"Record ID    : {self.__record_id}\n"
                f"Diagnosis    : {self.__diagnosis}\n"
                f"Treatment    : {self.__treatment}\n"
                f"Test Reports : {self.__test_reports}")

    def __str__(self):
        return (f"ID: {self.__record_id}  Diagnosis: {self.__diagnosis}  "
                f"Treatment: {self.__treatment}")


class Prescription:
    def __init__(self, prescription_id, medicine, dosage, instruction):
        self.__prescription_id = prescription_id
        self.__medicine = medicine
        self.__dosage = dosage
        self.__instruction = instruction

    def get_prescription_id(self): return self.__prescription_id
    def get_medicine(self): return self.__medicine
    def get_dosage(self): return self.__dosage
    def get_instruction(self): return self.__instruction

    def set_medicine(self, new_medicine):
        if new_medicine:
            self.__medicine = new_medicine
            return True, f"Medicine updated: {new_medicine}"
        return False, "Medicine can't be empty!"

    def set_dosage(self, new_dosage):
        if new_dosage:
            self.__dosage = new_dosage
            return True, f"Dosage updated: {new_dosage}"
        return False, "Dosage is empty!"

    def set_instruction(self, new_instruction):
        if new_instruction:
            self.__instruction = new_instruction
            return True, f"Instruction updated!"
        return False, "Instruction is empty!"

    def generate_prescription(self):
        if not self.__medicine:
            return False, "Medicine name is required!"
        if not self.__dosage:
            return False, "Dosage is required!"
        if not self.__instruction:
            return False, "Instruction is required!"
        return True, (f"Prescription ID : {self.__prescription_id}\n"
                      f"Medicine        : {self.__medicine}\n"
                      f"Dosage          : {self.__dosage}\n"
                      f"Instruction     : {self.__instruction}\n"
                      f"Status          : Generated")

    def print_prescription(self):
        return (f"Prescription ID : {self.__prescription_id}\n"
                f"Medicine        : {self.__medicine}\n"
                f"Dosage          : {self.__dosage}\n"
                f"Instruction     : {self.__instruction}")

    def __str__(self):
        return (f"ID: {self.__prescription_id}  Medicine: {self.__medicine}  "
                f"Dosage: {self.__dosage}")


class Admin:
    def __init__(self, admin_id, username, password):
        self.__admin_id = admin_id
        self.__username = username
        self.__password = password

    def get_admin_id(self): return self.__admin_id
    def get_username(self): return self.__username

    def verify_login(self, username, password):
        return self.__username == username and self.__password == password

    def manage_record(self, patient, record):
        if not patient or not record:
            return False, "Patient name and record info required!"
        return True, f"Record managed for {patient}:\n{record}"

    def generate_bill(self, patient, amount):
        if not patient:
            return False, "Patient name required!"
        if amount <= 0:
            return False, "Invalid amount!"
        return True, (f"Patient : {patient}\n"
                      f"Amount  : Rs. {amount}\n"
                      f"Status  : Bill Generated")

    def manage_beds(self, ward, status):
        if not ward or not status:
            return False, "Ward name and status required!"
        return True, f"Ward '{ward}' status set to: {status}"

    def manage_users(self, user, action):
        if not user or not action:
            return False, "User name and action required!"
        return True, f"User '{user}' action '{action}' performed."


# ============================================================
# PRE-LOADED DATA OBJECTS
# ============================================================
dept1 = Department(402, "Neurology")
dept2 = Department(403, "Surgery")

doctor1 = Doctor(201, "Muhammad Ali", "Neurology", "03123456789")
doctor2 = Doctor(202, "Ahmed Ali Ansari", "Surgery", "03023456789")
doctor3 = Doctor(203, "Basheer Abbasi", "Neurology", "03127777777")
doctor4 = Doctor(204, "Asif Baloch", "Surgery", "031222222333")
doctor5 = Doctor(205, "Ali Rind Baloch", "Neurology", "03052069475")

dept1.add_doctor("Basheer Abbasi")
dept2.add_doctor("Asif Baloch")
dept1.add_doctor("Ali Rind Baloch")

nurse1 = Nurse(105, "Safia Bibi", "Evening")
nurse2 = Nurse(106, "Bakhtawar Bibi", "Morning")
dept1.add_nurse("Safia Bibi")
dept2.add_nurse("Bakhtawar Bibi")

patient1 = Patient(101, "Bakhtoo", 21, "Female",
                   "0309-3477027", "Diabetes 2019")
patient2 = Patient(102, "Bakhtawar", 17, "Female", "03266777766", "Flu - 2026")
patient3 = Patient(103, "Imran Ali", 35, "Male",
                   "0322222222666", "Hepatitis - 2025")

appt1 = Appointment(701, "2025-12-06", "10:00 AM", "Bakhtoo", "Muhammad Ali")
appt2 = Appointment(702, "2026-05-31", "11:00 AM",
                    "Bakhtawar", "Ali Rind Baloch")

record1 = MedicalRecord(801, "HCV with chronic stage",
                        "Vaccines + Sonib", "HCV")
record2 = MedicalRecord(802, "Liver Failure",
                        "Go for transplantation", "Liver Failure")

pres1 = Prescription(901, "Sonib", "2 times a day", "After meal")
pres2 = Prescription(902, "Rifaximin", "2 times a day", "Before meal")

ward1 = Ward(501, "General", 10)
ward2 = Ward(502, "ICU", 5)

bed1 = Bed(601)
bed2 = Bed(602)
bed3 = Bed(603)

admin1 = Admin(1001, "admin123", "pass123")
all_doctors = [doctor1, doctor2, doctor3, doctor4, doctor5]
all_patients = [patient1, patient2, patient3]
all_nurses = [nurse1, nurse2]
all_appointments = [appt1, appt2]
all_records = [record1, record2]
all_prescriptions = [pres1, pres2]
all_wards = [ward1, ward2]
all_beds = [bed1, bed2, bed3]
all_departments = [dept1, dept2]

# ============================================================
# COLOR PALETTE & FONTS
# ============================================================
BG = "#0b1120"
SIDEBAR = "#0d1526"
CARD = "#111e35"
CARD2 = "#162040"
TEAL = "#00c9b1"
TEAL_D = "#00a896"
BLUE = "#1a73e8"
BLUE_D = "#1557b0"
GOLD = "#f5c518"
TEXT = "#e8f0fe"
MUTED = "#7a8fb5"
GREEN = "#00e676"
RED = "#ff5252"
BORDER = "#1e2d4a"
INP_BG = "#0d1a30"
INP_FG = "#e8f0fe"
ACCENT = "#00c9b1"
WHITE = "#ffffff"

FT = ("Palatino Linotype", 22, "bold")
FT_SUB = ("Palatino Linotype", 10, "italic")
FT_BTN = ("Consolas", 11, "bold")
FT_LABEL = ("Consolas", 10)
FT_INPUT = ("Consolas", 11)
FT_SMALL = ("Consolas", 8)
FT_CARD = ("Palatino Linotype", 13, "bold")
FT_MONO = ("Courier New", 10)

# ============================================================
# HELPER UTILITIES
# ============================================================


def center_window(win, w, h):
    win.update_idletasks()
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    x = (sw // 2) - (w // 2)
    y = (sh // 2) - (h // 2)
    win.geometry(f"{w}x{h}+{x}+{y}")


def make_popup(title, w=580, h=700):
    win = tk.Toplevel()
    win.title(title)
    win.configure(bg=BG)
    win.resizable(False, False)
    win.grab_set()
    center_window(win, w, h)
    return win


def draw_header(parent, icon, title, subtitle=""):
    hf = tk.Frame(parent, bg=CARD2, pady=18)
    hf.pack(fill="x")
    tk.Label(hf, text=icon, font=("Segoe UI Emoji", 30),
             bg=CARD2, fg=TEAL).pack()
    tk.Label(hf, text=title, font=FT,
             bg=CARD2, fg=TEAL).pack(pady=(2, 0))
    if subtitle:
        tk.Label(hf, text=subtitle, font=FT_SUB,
                 bg=CARD2, fg=MUTED).pack(pady=(1, 0))
    c = tk.Canvas(hf, height=2, bg=CARD2, highlightthickness=0)
    c.pack(fill="x", padx=20, pady=(10, 0))
    c.create_line(0, 1, 2000, 1, fill=TEAL, width=2)


def make_label_entry(parent, label, show=None):
    tk.Label(parent, text=label, font=FT_LABEL,
             bg=CARD, fg=MUTED, anchor="w").pack(fill="x", pady=(10, 2))
    e = tk.Entry(parent, font=FT_INPUT, bg=INP_BG, fg=INP_FG,
                 insertbackground=TEAL, relief="flat", bd=8)
    if show:
        e.config(show=show)
    e.pack(fill="x", ipady=7)
    sep = tk.Frame(parent, bg=TEAL, height=1)
    sep.pack(fill="x")
    return e


def make_dropdown(parent, label, options, var):
    tk.Label(parent, text=label, font=FT_LABEL,
             bg=CARD, fg=MUTED, anchor="w").pack(fill="x", pady=(10, 2))
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Custom.TCombobox",
                    fieldbackground=INP_BG,
                    background=INP_BG,
                    foreground=INP_FG,
                    selectbackground=TEAL,
                    selectforeground=BG,
                    arrowcolor=TEAL,
                    bordercolor=BORDER,
                    lightcolor=BORDER,
                    darkcolor=BORDER)
    cb = ttk.Combobox(parent, textvariable=var, values=options,
                      font=FT_INPUT, style="Custom.TCombobox",
                      state="readonly")
    cb.pack(fill="x", ipady=6)
    return cb


def action_btn(parent, text, cmd, color=TEAL, fg=BG):
    def on_e(e): btn.config(bg=TEAL_D if color == TEAL else color)
    def on_l(e): btn.config(bg=color)
    btn = tk.Button(parent, text=text, font=FT_BTN,
                    bg=color, fg=fg, relief="flat", cursor="hand2",
                    pady=11, command=cmd,
                    activebackground=TEAL_D, activeforeground=BG)
    btn.pack(fill="x", pady=(8, 2))
    btn.bind("<Enter>", on_e)
    btn.bind("<Leave>", on_l)
    return btn


def result_box(parent, text):
    """Show result in styled text box"""
    tf = tk.Frame(parent, bg=INP_BG, bd=0)
    tf.pack(fill="x", pady=(10, 0))
    txt = tk.Text(tf, font=FT_MONO, bg=INP_BG, fg=GREEN,
                  relief="flat", bd=10, height=7, wrap="word")
    txt.pack(fill="x")
    txt.insert("1.0", text)
    txt.config(state="disabled")


def show_info(title, msg):
    messagebox.showinfo(title, msg)


def show_error(title, msg):
    messagebox.showerror(title, msg)


def scrollable_form(win):
    """Return a scrollable canvas + inner frame for long forms"""
    canvas = tk.Canvas(win, bg=BG, highlightthickness=0)
    sb = tk.Scrollbar(win, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=sb.set)
    sb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    inner = tk.Frame(canvas, bg=BG)
    win_id = canvas.create_window((0, 0), window=inner, anchor="nw")

    def on_resize(e):
        canvas.itemconfig(win_id, width=e.width)

    def on_frame(e):
        canvas.configure(scrollregion=canvas.bbox("all"))

    canvas.bind("<Configure>", on_resize)
    inner.bind("<Configure>", on_frame)

    def _on_mousewheel(e):
        canvas.yview_scroll(int(-1*(e.delta/120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)
    return inner


# ============================================================
# PATIENT WINDOWS
# ============================================================

def open_patient_menu():
    win = make_popup("Patient Menu", 580, 480)
    draw_header(win, "🏥", "PATIENT MENU", "Manage patient operations")

    card = tk.Frame(win, bg=CARD, padx=30, pady=25)
    card.pack(fill="both", expand=True, padx=25, pady=20)

    def btn_row(icon, txt, cmd):
        f = tk.Frame(card, bg=CARD2, cursor="hand2")
        f.pack(fill="x", pady=6)
        def on_e(e, fr=f): fr.config(bg=BORDER)
        def on_l(e, fr=f): fr.config(bg=CARD2)
        f.bind("<Enter>", on_e)
        f.bind("<Leave>", on_l)
        f.bind("<Button-1>", lambda e, c=cmd: c())
        inner = tk.Frame(f, bg=CARD2)
        inner.pack(fill="x", padx=15, pady=12)
        inner.bind("<Enter>", on_e)
        inner.bind("<Leave>", on_l)
        inner.bind("<Button-1>", lambda e, c=cmd: c())
        tk.Label(inner, text=icon, font=("Segoe UI Emoji", 18),
                 bg=CARD2, fg=TEAL).pack(side="left", padx=(0, 12))
        tk.Label(inner, text=txt, font=FT_BTN,
                 bg=CARD2, fg=TEXT).pack(side="left")
        for w in [inner]:
            w.bind("<Button-1>", lambda e, c=cmd: c())

    btn_row("📋", "Register Patient", open_register_patient)
    btn_row("📜", "Show Medical History", open_view_history)
    btn_row("📅", "Book Appointment", open_book_appointment)
    btn_row("👤", "Show Patient Info", open_patient_info)

    tk.Button(card, text="✖  CLOSE", font=FT_BTN,
              bg=RED, fg=WHITE, relief="flat", cursor="hand2",
              pady=9, command=win.destroy).pack(fill="x", pady=(18, 0))


def open_register_patient():
    win = make_popup("Register Patient", 580, 700)
    draw_header(win, "📋", "REGISTER PATIENT",
                "View patient registration details")
    inner = scrollable_form(win)
    card = tk.Frame(inner, bg=CARD, padx=28, pady=20)
    card.pack(fill="x", padx=20, pady=15)

    tk.Label(card, text="Select Patient", font=FT_LABEL,
             bg=CARD, fg=MUTED, anchor="w").pack(fill="x", pady=(0, 6))
    var = tk.StringVar(value="Bakhtoo (101)")
    make_dropdown(card, "Choose Patient",
                  ["Bakhtoo (101)", "Bakhtawar (102)", "Imran Ali (103)"], var)

    res_frame = tk.Frame(card, bg=CARD)
    res_frame.pack(fill="x")

    def submit():
        for w in res_frame.winfo_children():
            w.destroy()
        choice = var.get()
        p = patient1 if "101" in choice else patient2 if "102" in choice else patient3
        info = p.register()
        tk.Label(res_frame, text="Registration Details",
                 font=FT_CARD, bg=CARD, fg=TEAL).pack(anchor="w", pady=(14, 4))
        result_box(res_frame, info)

    action_btn(card, "✔  SHOW REGISTRATION", submit)


def open_view_history():
    win = make_popup("Medical History", 580, 560)
    draw_header(win, "📜", "MEDICAL HISTORY",
                "View patient's past medical records")
    inner = scrollable_form(win)
    card = tk.Frame(inner, bg=CARD, padx=28, pady=20)
    card.pack(fill="x", padx=20, pady=15)

    var = tk.StringVar(value="Bakhtoo (101)")
    make_dropdown(card, "Select Patient",
                  ["Bakhtoo (101)", "Bakhtawar (102)", "Imran Ali (103)"], var)

    res_frame = tk.Frame(card, bg=CARD)
    res_frame.pack(fill="x")

    def submit():
        for w in res_frame.winfo_children():
            w.destroy()
        choice = var.get()
        p = patient1 if "101" in choice else patient2 if "102" in choice else patient3
        hist = p.view_history()
        tk.Label(res_frame, text="Medical History:",
                 font=FT_CARD, bg=CARD, fg=TEAL).pack(anchor="w", pady=(14, 4))
        result_box(res_frame, hist)

    action_btn(card, "🔍  VIEW HISTORY", submit)


def open_book_appointment():
    win = make_popup("Book Appointment", 580, 780)
    draw_header(win, "📅", "BOOK APPOINTMENT", "Schedule a new appointment")
    inner = scrollable_form(win)
    card = tk.Frame(inner, bg=CARD, padx=28, pady=20)
    card.pack(fill="x", padx=20, pady=15)

    var_p = tk.StringVar(value="Bakhtoo (101)")
    make_dropdown(card, "Select Patient",
                  ["Bakhtoo (101)", "Bakhtawar (102)", "Imran Ali (103)"], var_p)

    e_doc = make_label_entry(card, "Doctor Name")
    e_date = make_label_entry(card, "Date (YYYY-MM-DD)")
    e_time = make_label_entry(card, "Time (e.g. 10:00 AM)")

    res_frame = tk.Frame(card, bg=CARD)
    res_frame.pack(fill="x")

    def submit():
        for w in res_frame.winfo_children():
            w.destroy()
        choice = var_p.get()
        p = patient1 if "101" in choice else patient2 if "102" in choice else patient3
        aid, info = p.book_appointment(e_doc.get().strip(),
                                       e_date.get().strip(),
                                       e_time.get().strip())
        if aid == -1:
            show_error("Error", info)
        else:
            tk.Label(res_frame, text="Appointment Confirmed!",
                     font=FT_CARD, bg=CARD, fg=GREEN).pack(anchor="w", pady=(14, 4))
            result_box(res_frame, info)

    action_btn(card, "✔  BOOK APPOINTMENT", submit)


def open_patient_info():
    win = make_popup("Patient Info", 580, 520)
    draw_header(win, "👤", "PATIENT INFO", "All registered patients")
    card = tk.Frame(win, bg=CARD, padx=28, pady=20)
    card.pack(fill="both", expand=True, padx=20, pady=15)

    for p in all_patients:
        f = tk.Frame(card, bg=CARD2, padx=15, pady=10)
        f.pack(fill="x", pady=5)
        tk.Label(f, text=str(p), font=FT_MONO, bg=CARD2, fg=TEXT,
                 anchor="w", justify="left", wraplength=480).pack(fill="x")


# ============================================================
# DOCTOR WINDOWS
# ============================================================

def open_doctor_menu():
    win = make_popup("Doctor Menu", 580, 480)
    draw_header(win, "👨‍⚕️", "DOCTOR MENU", "Manage doctor operations")

    card = tk.Frame(win, bg=CARD, padx=30, pady=25)
    card.pack(fill="both", expand=True, padx=25, pady=20)

    def go(fn): fn()

    for icon, txt, fn in [
        ("🔬", "Diagnose Patient", open_diagnose),
        ("💊", "Write Medicine / Prescribe", open_prescribe),
        ("🗓", "Check Doctor Schedule", open_schedule),
        ("👨‍⚕️", "View All Doctors Info", open_doctor_info),
    ]:
        f = tk.Frame(card, bg=CARD2, cursor="hand2")
        f.pack(fill="x", pady=6)
        inner = tk.Frame(f, bg=CARD2)
        inner.pack(fill="x", padx=15, pady=12)
        tk.Label(inner, text=icon, font=("Segoe UI Emoji", 18),
                 bg=CARD2, fg=TEAL).pack(side="left", padx=(0, 12))
        tk.Label(inner, text=txt, font=FT_BTN,
                 bg=CARD2, fg=TEXT).pack(side="left")
        f.bind("<Button-1>", lambda e, f=fn: go(f))
        inner.bind("<Button-1>", lambda e, f=fn: go(f))

    tk.Button(card, text="✖  CLOSE", font=FT_BTN,
              bg=RED, fg=WHITE, relief="flat", cursor="hand2",
              pady=9, command=win.destroy).pack(fill="x", pady=(18, 0))


def open_diagnose():
    win = make_popup("Diagnose Patient", 580, 680)
    draw_header(win, "🔬", "DIAGNOSE PATIENT", "Doctor examines the patient")
    inner = scrollable_form(win)
    card = tk.Frame(inner, bg=CARD, padx=28, pady=20)
    card.pack(fill="x", padx=20, pady=15)

    doc_names = [
        f"Dr. {d.get_name()} ({d.get_doctor_id()})" for d in all_doctors]
    var_d = tk.StringVar(value=doc_names[0])
    make_dropdown(card, "Select Doctor", doc_names, var_d)
    e_pat = make_label_entry(card, "Patient Name")

    res_frame = tk.Frame(card, bg=CARD)
    res_frame.pack(fill="x")

    def submit():
        for w in res_frame.winfo_children():
            w.destroy()
        idx = doc_names.index(var_d.get())
        ok, info = all_doctors[idx].diagnose(e_pat.get().strip())
        if not ok:
            show_error("Error", info)
        else:
            tk.Label(res_frame, text="Diagnosis Report",
                     font=FT_CARD, bg=CARD, fg=TEAL).pack(anchor="w", pady=(14, 4))
            result_box(res_frame, info)

    action_btn(card, "🔬  DIAGNOSE", submit)


def open_prescribe():
    win = make_popup("Prescribe Medicine", 580, 720)
    draw_header(win, "💊", "PRESCRIBE MEDICINE", "Doctor writes prescription")
    inner = scrollable_form(win)
    card = tk.Frame(inner, bg=CARD, padx=28, pady=20)
    card.pack(fill="x", padx=20, pady=15)

    doc_names = [
        f"Dr. {d.get_name()} ({d.get_doctor_id()})" for d in all_doctors]
    var_d = tk.StringVar(value=doc_names[0])
    make_dropdown(card, "Select Doctor", doc_names, var_d)
    e_med = make_label_entry(card, "Medicine Name")
    e_dos = make_label_entry(card, "Dosage (e.g. 2 times a day)")

    res_frame = tk.Frame(card, bg=CARD)
    res_frame.pack(fill="x")

    def submit():
        for w in res_frame.winfo_children():
            w.destroy()
        idx = doc_names.index(var_d.get())
        pid, info = all_doctors[idx].prescribe_medicine(
            e_med.get().strip(), e_dos.get().strip())
        if pid == -1:
            show_error("Error", info)
        else:
            tk.Label(res_frame, text="Prescription Issued",
                     font=FT_CARD, bg=CARD, fg=GREEN).pack(anchor="w", pady=(14, 4))
            result_box(res_frame, info)

    action_btn(card, "💊  PRESCRIBE", submit)


def open_schedule():
    win = make_popup("Doctor Schedule", 580, 600)
    draw_header(win, "🗓", "DOCTOR SCHEDULE", "View availability and timing")
    inner = scrollable_form(win)
    card = tk.Frame(inner, bg=CARD, padx=28, pady=20)
    card.pack(fill="x", padx=20, pady=15)

    doc_names = [
        f"Dr. {d.get_name()} ({d.get_doctor_id()})" for d in all_doctors]
    var_d = tk.StringVar(value=doc_names[0])
    make_dropdown(card, "Select Doctor", doc_names, var_d)

    res_frame = tk.Frame(card, bg=CARD)
    res_frame.pack(fill="x")

    def submit():
        for w in res_frame.winfo_children():
            w.destroy()
        idx = doc_names.index(var_d.get())
        info = all_doctors[idx].check_schedule()
        tk.Label(res_frame, text="Schedule Details",
                 font=FT_CARD, bg=CARD, fg=TEAL).pack(anchor="w", pady=(14, 4))
        result_box(res_frame, info)

    action_btn(card, "🗓  CHECK SCHEDULE", submit)


def open_doctor_info():
    win = make_popup("Doctor Info", 580, 560)
    draw_header(win, "👨‍⚕️", "ALL DOCTORS", "Hospital medical staff")
    card = tk.Frame(win, bg=CARD, padx=28, pady=20)
    card.pack(fill="both", expand=True, padx=20, pady=15)

    for d in all_doctors:
        f = tk.Frame(card, bg=CARD2, padx=15, pady=10)
        f.pack(fill="x", pady=5)
        tk.Label(f, text=str(d), font=FT_MONO, bg=CARD2, fg=TEXT,
                 anchor="w", justify="left", wraplength=480).pack(fill="x")


# ============================================================
# APPOINTMENT WINDOWS
# ============================================================

def open_appointment_menu():
    win = make_popup("Appointment Menu", 580, 480)
    draw_header(win, "📅", "APPOINTMENT MENU", "Schedule, cancel, reschedule")
    card = tk.Frame(win, bg=CARD, padx=30, pady=25)
    card.pack(fill="both", expand=True, padx=25, pady=20)

    for icon, txt, fn in [
        ("✅", "Schedule Appointment", open_schedule_appt),
        ("❌", "Cancel Appointment", open_cancel_appt),
        ("🔄", "Reschedule Appointment", open_reschedule_appt),
        ("ℹ️", "Appointment Info", open_appt_info),
    ]:
        f = tk.Frame(card, bg=CARD2, cursor="hand2")
        f.pack(fill="x", pady=6)
        inner = tk.Frame(f, bg=CARD2)
        inner.pack(fill="x", padx=15, pady=12)
        tk.Label(inner, text=icon, font=("Segoe UI Emoji", 18),
                 bg=CARD2, fg=TEAL).pack(side="left", padx=(0, 12))
        tk.Label(inner, text=txt, font=FT_BTN,
                 bg=CARD2, fg=TEXT).pack(side="left")
        f.bind("<Button-1>", lambda e, f=fn: f())
        inner.bind("<Button-1>", lambda e, f=fn: f())

    tk.Button(card, text="✖  CLOSE", font=FT_BTN,
              bg=RED, fg=WHITE, relief="flat", cursor="hand2",
              pady=9, command=win.destroy).pack(fill="x", pady=(18, 0))


def open_schedule_appt():
    win = make_popup("Schedule Appointment", 580, 580)
    draw_header(win, "✅", "SCHEDULE APPOINTMENT",
                "Re-activate a canceled appointment")
    inner = scrollable_form(win)
    card = tk.Frame(inner, bg=CARD, padx=28, pady=20)
    card.pack(fill="x", padx=20, pady=15)

    appt_names = [
        f"Appt {a.get_appointment_id()} - {a.get_patient_name()}" for a in all_appointments]
    var = tk.StringVar(value=appt_names[0])
    make_dropdown(card, "Select Appointment", appt_names, var)

    res_frame = tk.Frame(card, bg=CARD)
    res_frame.pack(fill="x")

    def submit():
        for w in res_frame.winfo_children():
            w.destroy()
        idx = appt_names.index(var.get())
        ok, info = all_appointments[idx].schedule()
        if not ok:
            show_error("Error", info)
        else:
            tk.Label(res_frame, text="Appointment Scheduled!",
                     font=FT_CARD, bg=CARD, fg=GREEN).pack(anchor="w", pady=(14, 4))
            result_box(res_frame, info)

    action_btn(card, "✅  SCHEDULE", submit)


def open_cancel_appt():
    win = make_popup("Cancel Appointment", 580, 580)
    draw_header(win, "❌", "CANCEL APPOINTMENT", "Cancel a booked appointment")
    inner = scrollable_form(win)
    card = tk.Frame(inner, bg=CARD, padx=28, pady=20)
    card.pack(fill="x", padx=20, pady=15)

    appt_names = [
        f"Appt {a.get_appointment_id()} - {a.get_patient_name()}" for a in all_appointments]
    var = tk.StringVar(value=appt_names[0])
    make_dropdown(card, "Select Appointment", appt_names, var)

    res_frame = tk.Frame(card, bg=CARD)
    res_frame.pack(fill="x")

    def submit():
        for w in res_frame.winfo_children():
            w.destroy()
        idx = appt_names.index(var.get())
        ok, info = all_appointments[idx].cancel()
        if not ok:
            show_error("Error", info)
        else:
            tk.Label(res_frame, text="Appointment Canceled",
                     font=FT_CARD, bg=CARD, fg=RED).pack(anchor="w", pady=(14, 4))
            result_box(res_frame, info)

    action_btn(card, "❌  CANCEL", submit, color=RED, fg=WHITE)


def open_reschedule_appt():
    win = make_popup("Reschedule Appointment", 580, 760)
    draw_header(win, "🔄", "RESCHEDULE", "Change appointment date and time")
    inner = scrollable_form(win)
    card = tk.Frame(inner, bg=CARD, padx=28, pady=20)
    card.pack(fill="x", padx=20, pady=15)

    appt_names = [
        f"Appt {a.get_appointment_id()} - {a.get_patient_name()}" for a in all_appointments]
    var = tk.StringVar(value=appt_names[0])
    make_dropdown(card, "Select Appointment", appt_names, var)
    e_date = make_label_entry(card, "New Date (YYYY-MM-DD)")
    e_time = make_label_entry(card, "New Time (e.g. 02:00 PM)")

    res_frame = tk.Frame(card, bg=CARD)
    res_frame.pack(fill="x")

    def submit():
        for w in res_frame.winfo_children():
            w.destroy()
        idx = appt_names.index(var.get())
        ok, info = all_appointments[idx].reschedule(
            e_date.get().strip(), e_time.get().strip())
        if not ok:
            show_error("Error", info)
        else:
            tk.Label(res_frame, text="Appointment Rescheduled!",
                     font=FT_CARD, bg=CARD, fg=GREEN).pack(anchor="w", pady=(14, 4))
            result_box(res_frame, info)

    action_btn(card, "🔄  RESCHEDULE", submit, color=BLUE, fg=WHITE)


def open_appt_info():
    win = make_popup("Appointment Info", 580, 500)
    draw_header(win, "ℹ️", "APPOINTMENT INFO", "All appointments")
    card = tk.Frame(win, bg=CARD, padx=28, pady=20)
    card.pack(fill="both", expand=True, padx=20, pady=15)
    for a in all_appointments:
        f = tk.Frame(card, bg=CARD2, padx=15, pady=10)
        f.pack(fill="x", pady=5)
        tk.Label(f, text=str(a), font=FT_MONO, bg=CARD2, fg=TEXT,
                 anchor="w", justify="left", wraplength=480).pack(fill="x")


# ============================================================
# WARD WINDOWS
# ============================================================

def open_ward_menu():
    win = make_popup("Ward Menu", 580, 480)
    draw_header(win, "🛏", "WARD MENU", "Manage hospital wards and beds")
    card = tk.Frame(win, bg=CARD, padx=30, pady=25)
    card.pack(fill="both", expand=True, padx=25, pady=20)

    for icon, txt, fn in [
        ("🔍", "Check Ward Availability", open_check_availability),
        ("🛏", "Get Available Beds", open_available_beds),
        ("➕", "Add Bed to Ward", open_add_bed),
        ("📋", "Show Ward Info", open_ward_info),
    ]:
        f = tk.Frame(card, bg=CARD2, cursor="hand2")
        f.pack(fill="x", pady=6)
        inner = tk.Frame(f, bg=CARD2)
        inner.pack(fill="x", padx=15, pady=12)
        tk.Label(inner, text=icon, font=("Segoe UI Emoji", 18),
                 bg=CARD2, fg=TEAL).pack(side="left", padx=(0, 12))
        tk.Label(inner, text=txt, font=FT_BTN,
                 bg=CARD2, fg=TEXT).pack(side="left")
        f.bind("<Button-1>", lambda e, f=fn: f())
        inner.bind("<Button-1>", lambda e, f=fn: f())

    tk.Button(card, text="✖  CLOSE", font=FT_BTN,
              bg=RED, fg=WHITE, relief="flat", cursor="hand2",
              pady=9, command=win.destroy).pack(fill="x", pady=(18, 0))


def open_check_availability():
    win = make_popup("Ward Availability", 580, 580)
    draw_header(win, "🔍", "CHECK AVAILABILITY", "See available beds in ward")
    inner = scrollable_form(win)
    card = tk.Frame(inner, bg=CARD, padx=28, pady=20)
    card.pack(fill="x", padx=20, pady=15)

    ward_names = [
        f"{w.get_ward_name()} (ID: {w.get_ward_id()})" for w in all_wards]
    var = tk.StringVar(value=ward_names[0])
    make_dropdown(card, "Select Ward", ward_names, var)

    res_frame = tk.Frame(card, bg=CARD)
    res_frame.pack(fill="x")

    def submit():
        for w in res_frame.winfo_children():
            w.destroy()
        idx = ward_names.index(var.get())
        info, avail = all_wards[idx].check_availability()
        color = GREEN if avail > 0 else RED
        tk.Label(res_frame, text="Availability Report",
                 font=FT_CARD, bg=CARD, fg=color).pack(anchor="w", pady=(14, 4))
        result_box(res_frame, info)

    action_btn(card, "🔍  CHECK", submit)


def open_available_beds():
    win = make_popup("Available Beds", 580, 580)
    draw_header(win, "🛏", "AVAILABLE BEDS", "Bed count per ward")
    inner = scrollable_form(win)
    card = tk.Frame(inner, bg=CARD, padx=28, pady=20)
    card.pack(fill="x", padx=20, pady=15)

    ward_names = [
        f"{w.get_ward_name()} (ID: {w.get_ward_id()})" for w in all_wards]
    var = tk.StringVar(value=ward_names[0])
    make_dropdown(card, "Select Ward", ward_names, var)

    res_frame = tk.Frame(card, bg=CARD)
    res_frame.pack(fill="x")

    def submit():
        for w in res_frame.winfo_children():
            w.destroy()
        idx = ward_names.index(var.get())
        info, _ = all_wards[idx].get_available_beds()
        tk.Label(res_frame, text="Beds Report",
                 font=FT_CARD, bg=CARD, fg=TEAL).pack(anchor="w", pady=(14, 4))
        result_box(res_frame, info)

    action_btn(card, "🛏  GET BEDS", submit)


def open_add_bed():
    win = make_popup("Add Bed", 580, 680)
    draw_header(win, "➕", "ADD BED", "Add a bed to selected ward")
    inner = scrollable_form(win)
    card = tk.Frame(inner, bg=CARD, padx=28, pady=20)
    card.pack(fill="x", padx=20, pady=15)

    ward_names = [
        f"{w.get_ward_name()} (ID: {w.get_ward_id()})" for w in all_wards]
    var = tk.StringVar(value=ward_names[0])
    make_dropdown(card, "Select Ward", ward_names, var)
    e_bed = make_label_entry(card, "Bed ID (number)")

    res_frame = tk.Frame(card, bg=CARD)
    res_frame.pack(fill="x")

    def submit():
        for w in res_frame.winfo_children():
            w.destroy()
        try:
            bid = int(e_bed.get().strip())
        except ValueError:
            show_error("Error", "Bed ID must be a number!")
            return
        idx = ward_names.index(var.get())
        ok, msg = all_wards[idx].add_bed(bid)
        color = GREEN if ok else RED
        tk.Label(res_frame, text=msg,
                 font=FT_CARD, bg=CARD, fg=color).pack(anchor="w", pady=(14, 4))

    action_btn(card, "➕  ADD BED", submit)


def open_ward_info():
    win = make_popup("Ward Info", 580, 460)
    draw_header(win, "📋", "WARD INFO", "All wards overview")
    card = tk.Frame(win, bg=CARD, padx=28, pady=20)
    card.pack(fill="both", expand=True, padx=20, pady=15)
    for w in all_wards:
        f = tk.Frame(card, bg=CARD2, padx=15, pady=10)
        f.pack(fill="x", pady=5)
        tk.Label(f, text=str(w), font=FT_MONO, bg=CARD2, fg=TEXT,
                 anchor="w").pack(fill="x")


# ============================================================
# ADMIN WINDOW
# ============================================================

def open_admin_menu():
    win = make_popup("Admin Login", 500, 500)
    draw_header(win, "🔐", "ADMIN LOGIN", "Enter admin credentials")
    inner = scrollable_form(win)
    card = tk.Frame(inner, bg=CARD, padx=28, pady=25)
    card.pack(fill="x", padx=20, pady=20)

    e_user = make_label_entry(card, "Username")
    e_pass = make_label_entry(card, "Password", show="●")

    def login():
        u = e_user.get().strip()
        p = e_pass.get().strip()
        if admin1.verify_login(u, p):
            win.destroy()
            open_admin_panel()
        else:
            show_error("Login Failed", "Wrong username or password!")

    action_btn(card, "🔐  LOGIN AS ADMIN", login)


def open_admin_panel():
    win = make_popup("Admin Panel", 580, 560)
    draw_header(win, "⚙️", "ADMIN PANEL", "Hospital administration controls")
    card = tk.Frame(win, bg=CARD, padx=30, pady=25)
    card.pack(fill="both", expand=True, padx=25, pady=20)

    for icon, txt, fn in [
        ("📁", "Manage Medical Records", open_manage_records),
        ("💵", "Generate Bill", open_generate_bill),
        ("🛏", "Manage Beds", open_manage_beds_admin),
        ("👥", "Manage Users", open_manage_users),
    ]:
        f = tk.Frame(card, bg=CARD2, cursor="hand2")
        f.pack(fill="x", pady=6)
        inner = tk.Frame(f, bg=CARD2)
        inner.pack(fill="x", padx=15, pady=12)
        tk.Label(inner, text=icon, font=("Segoe UI Emoji", 18),
                 bg=CARD2, fg=GOLD).pack(side="left", padx=(0, 12))
        tk.Label(inner, text=txt, font=FT_BTN,
                 bg=CARD2, fg=TEXT).pack(side="left")
        f.bind("<Button-1>", lambda e, f=fn: f())
        inner.bind("<Button-1>", lambda e, f=fn: f())

    tk.Button(card, text="✖  LOGOUT", font=FT_BTN,
              bg=RED, fg=WHITE, relief="flat", cursor="hand2",
              pady=9, command=win.destroy).pack(fill="x", pady=(18, 0))


def open_manage_records():
    win = make_popup("Manage Records", 580, 740)
    draw_header(win, "📁", "MANAGE RECORDS", "Update patient medical records")
    inner = scrollable_form(win)
    card = tk.Frame(inner, bg=CARD, padx=28, pady=20)
    card.pack(fill="x", padx=20, pady=15)

    e_pat = make_label_entry(card, "Patient Name")
    e_rec = make_label_entry(card, "Record Info")

    res_frame = tk.Frame(card, bg=CARD)
    res_frame.pack(fill="x")

    def submit():
        for w in res_frame.winfo_children():
            w.destroy()
        ok, msg = admin1.manage_record(
            e_pat.get().strip(), e_rec.get().strip())
        color = GREEN if ok else RED
        tk.Label(res_frame, text="Result:",
                 font=FT_CARD, bg=CARD, fg=color).pack(anchor="w", pady=(14, 4))
        result_box(res_frame, msg)

    action_btn(card, "📁  MANAGE RECORD", submit, color=GOLD, fg=BG)


def open_generate_bill():
    win = make_popup("Generate Bill", 580, 700)
    draw_header(win, "💵", "GENERATE BILL", "Create patient billing statement")
    inner = scrollable_form(win)
    card = tk.Frame(inner, bg=CARD, padx=28, pady=20)
    card.pack(fill="x", padx=20, pady=15)

    e_pat = make_label_entry(card, "Patient Name")
    e_amt = make_label_entry(card, "Amount (Rs.)")

    res_frame = tk.Frame(card, bg=CARD)
    res_frame.pack(fill="x")

    def submit():
        for w in res_frame.winfo_children():
            w.destroy()
        try:
            amt = int(e_amt.get().strip())
        except ValueError:
            show_error("Error", "Amount must be a number!")
            return
        ok, msg = admin1.generate_bill(e_pat.get().strip(), amt)
        color = GREEN if ok else RED
        tk.Label(res_frame, text="Bill Generated!" if ok else "Error",
                 font=FT_CARD, bg=CARD, fg=color).pack(anchor="w", pady=(14, 4))
        result_box(res_frame, msg)

    action_btn(card, "💵  GENERATE BILL", submit, color=GOLD, fg=BG)


def open_manage_beds_admin():
    win = make_popup("Manage Beds", 580, 700)
    draw_header(win, "🛏", "MANAGE BEDS", "Update bed status in ward")
    inner = scrollable_form(win)
    card = tk.Frame(inner, bg=CARD, padx=28, pady=20)
    card.pack(fill="x", padx=20, pady=15)

    e_ward = make_label_entry(card, "Ward Name")
    var_s = tk.StringVar(value="Available")
    make_dropdown(card, "Status", ["Available", "Occupied"], var_s)

    res_frame = tk.Frame(card, bg=CARD)
    res_frame.pack(fill="x")

    def submit():
        for w in res_frame.winfo_children():
            w.destroy()
        ok, msg = admin1.manage_beds(e_ward.get().strip(), var_s.get())
        color = GREEN if ok else RED
        tk.Label(res_frame, text="Result:",
                 font=FT_CARD, bg=CARD, fg=color).pack(anchor="w", pady=(14, 4))
        result_box(res_frame, msg)

    action_btn(card, "🛏  UPDATE BED", submit, color=GOLD, fg=BG)


def open_manage_users():
    win = make_popup("Manage Users", 580, 700)
    draw_header(win, "👥", "MANAGE USERS", "Add or remove system users")
    inner = scrollable_form(win)
    card = tk.Frame(inner, bg=CARD, padx=28, pady=20)
    card.pack(fill="x", padx=20, pady=15)

    e_user = make_label_entry(card, "User Name")
    var_a = tk.StringVar(value="Add")
    make_dropdown(card, "Action", ["Add", "Remove"], var_a)

    res_frame = tk.Frame(card, bg=CARD)
    res_frame.pack(fill="x")

    def submit():
        for w in res_frame.winfo_children():
            w.destroy()
        ok, msg = admin1.manage_users(e_user.get().strip(), var_a.get())
        color = GREEN if ok else RED
        tk.Label(res_frame, text="Result:",
                 font=FT_CARD, bg=CARD, fg=color).pack(anchor="w", pady=(14, 4))
        result_box(res_frame, msg)

    action_btn(card, "👥  PERFORM ACTION", submit, color=GOLD, fg=BG)


# ============================================================
# MAIN WINDOW
# ============================================================

def build_main_window():
    root = tk.Tk()
    root.title("Hospital Management System")
    root.configure(bg=BG)
    root.resizable(False, False)

    W, H = 700, 920
    center_window(root, W, H)

    # ── TOP DEVELOPER BANNER ──────────────────────────────
    banner = tk.Frame(root, bg="#05080f", pady=6)
    banner.pack(fill="x")
    tk.Label(banner,
             text="✦  Developed by Ali Rind Baloch  ✦",
             font=("Consolas", 9, "bold"),
             bg="#05080f", fg=TEAL).pack()

    # ── HERO HEADER ───────────────────────────────────────
    hero = tk.Frame(root, bg=CARD2, pady=28)
    hero.pack(fill="x")

    tk.Label(hero, text="🏥", font=("Segoe UI Emoji", 46),
             bg=CARD2, fg=TEAL).pack()
    tk.Label(hero,
             text="HOSPITAL MANAGEMENT SYSTEM",
             font=("Palatino Linotype", 20, "bold"),
             bg=CARD2, fg=TEAL).pack(pady=(6, 2))
    tk.Label(hero,
             text="Complete Healthcare Administration Platform",
             font=("Palatino Linotype", 10, "italic"),
             bg=CARD2, fg=MUTED).pack()

    # Gold divider
    c = tk.Canvas(hero, height=2, bg=CARD2, highlightthickness=0)
    c.pack(fill="x", padx=40, pady=(14, 0))
    c.create_line(0, 1, 2000, 1, fill=TEAL, width=2)

    # ── STATS BAR ─────────────────────────────────────────
    stats = tk.Frame(root, bg=SIDEBAR, pady=10)
    stats.pack(fill="x")
    stats.columnconfigure((0, 1, 2, 3, 4), weight=1)

    stat_data = [
        ("👨‍⚕️", str(len(all_doctors)), "Doctors"),
        ("🏥", str(len(all_patients)), "Patients"),
        ("👩‍⚕️", str(len(all_nurses)), "Nurses"),
        ("🛏", str(len(all_wards)), "Wards"),
        ("📅", str(len(all_appointments)), "Appts"),
    ]
    for i, (icon, val, lbl) in enumerate(stat_data):
        sf = tk.Frame(stats, bg=SIDEBAR)
        sf.grid(row=0, column=i, padx=8, pady=4, sticky="nsew")
        tk.Label(sf, text=icon, font=("Segoe UI Emoji", 16),
                 bg=SIDEBAR, fg=TEAL).pack()
        tk.Label(sf, text=val, font=("Consolas", 14, "bold"),
                 bg=SIDEBAR, fg=WHITE).pack()
        tk.Label(sf, text=lbl, font=("Consolas", 8),
                 bg=SIDEBAR, fg=MUTED).pack()

    # ── MENU SECTION LABEL ────────────────────────────────
    tk.Label(root, text="SELECT A MODULE",
             font=("Consolas", 9, "bold"),
             bg=BG, fg=MUTED).pack(pady=(18, 6))

    # ── MENU BUTTONS GRID ─────────────────────────────────
    grid = tk.Frame(root, bg=BG)
    grid.pack(padx=30, fill="x")

    menu_items = [
        ("🏥", "PATIENT\nMENU",     TEAL,  open_patient_menu),
        ("👨‍⚕️", "DOCTOR\nMENU",     BLUE,  open_doctor_menu),
        ("📅", "APPOINTMENT\nMENU", "#9c27b0", open_appointment_menu),
        ("🛏", "WARD\nMENU",        "#ff9800", open_ward_menu),
        ("🔐", "ADMIN\nMENU",       GOLD,  open_admin_menu),
    ]

    for i, (icon, label, color, cmd) in enumerate(menu_items):
        col = i % 3
        row = i // 3

        card_f = tk.Frame(grid, bg=CARD2, cursor="hand2",
                          relief="flat", bd=0)
        card_f.grid(row=row, column=col, padx=8, pady=8,
                    sticky="nsew", ipadx=10, ipady=14)
        grid.columnconfigure(col, weight=1)

        # Colored top accent bar
        accent = tk.Frame(card_f, bg=color, height=3)
        accent.pack(fill="x")

        tk.Label(card_f, text=icon,
                 font=("Segoe UI Emoji", 30),
                 bg=CARD2, fg=color).pack(pady=(14, 4))
        tk.Label(card_f, text=label,
                 font=("Consolas", 10, "bold"),
                 bg=CARD2, fg=TEXT,
                 justify="center").pack(pady=(0, 10))

        def make_click(c=cmd, cf=card_f, col=color):
            def on_click(e=None): c()
            def on_e(e): cf.config(bg=BORDER)
            def on_l(e): cf.config(bg=CARD2)
            cf.bind("<Button-1>", on_click)
            cf.bind("<Enter>", on_e)
            cf.bind("<Leave>", on_l)
            for child in cf.winfo_children():
                child.bind("<Button-1>", on_click)
                child.bind("<Enter>", on_e)
                child.bind("<Leave>", on_l)

        make_click()

    # ── EXIT BUTTON ───────────────────────────────────────
    exit_f = tk.Frame(root, bg=BG)
    exit_f.pack(padx=30, pady=(16, 10), fill="x")

    def on_exit():
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            root.destroy()

    exit_btn = tk.Button(exit_f,
                         text="✖   EXIT SYSTEM",
                         font=("Consolas", 12, "bold"),
                         bg=RED, fg=WHITE, relief="flat",
                         cursor="hand2", pady=13,
                         command=on_exit,
                         activebackground="#cc0000",
                         activeforeground=WHITE)
    exit_btn.pack(fill="x")

    # ── FOOTER ────────────────────────────────────────────
    footer = tk.Frame(root, bg="#05080f", pady=8)
    footer.pack(fill="x", side="bottom")
    tk.Label(footer,
             text="© 2026  Ali Rind Baloch  |  Hospital Management System  |  All Rights Reserved",
             font=("Consolas", 8),
             bg="#05080f", fg=MUTED).pack()

    root.mainloop()


if __name__ == "__main__":
    build_main_window()
