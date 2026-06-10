from patient import Patient
from doctor import Doctor
from nurse import Nurse
from department import Department
from appointment import Appointment
from medical_record import MedicalRecord
from prescription import Prescription
from ward import Ward
from bed import Bed
from admin import Admin

# ==================================================================
# DEPARTMENTS OBJECTS
# pehle department object q k doctor aur nurse department me ate hain
# ==================================================================
dept1 = Department(402, "Neurology")
dept2 = Department(403, "Surgery")

# -----------------------------------------
# Doctor object
# -----------------------------------------
doctor1 = Doctor(201, "Muhammad Ali", "Neurology", "03123456789")
doctor2 = Doctor(202, "Ahmed Ali Ansari", "Surgery", "03023456789")
doctor3 = Doctor(203, "Basheer Abbasi", " Neurology", "03127777777")
doctor4 = Doctor(204,  "Asif Baloch",  "Surgery", "031222222333")
doctor5 = Doctor(205, "Ali Rind Baloch", "Neurology", "03052069475")

# doctor department me append krna
dept1.add_doctor("Basherr abbasi")
dept2.add_doctor("Asif Baloch")
dept1.add_doctor("Ali Rind Baloch")
# --------------------------------------
# Nurse object
# nurse bhi department hote hain to ye bhi link hoga
# -----------------------------------------------
nurse1 = Nurse(105, "Safia bibi", "Evening")
nurse2 = Nurse(106, "Bakhtawar bibi", "Morning")
# Nurse department me add karo
dept1.add_nurse("Safia Bibi")
dept2.add_nurse("Bakhtawar bibi")

# -----------------------------------------
# patient object
# -----------------------------------------
patient1 = Patient(101, "bakhtoo", 21, "Female",
                   "0309-3477027", "diabtetes 2019")
patient2 = Patient(102, "Bakhtawar", 17, "Female", "03266777766", "Flu - 2026")
patient3 = Patient(103, "Imran Ali", 35, "Male",
                   "0322222222666", "Heptitis - 2025")

# --------------------------------------------
# APPOINTMENT OBJECTS
# -------------------------------------------
appt1 = Appointment(701, "2025-12-6", "10 :00 AM", "Bakhtoo", "Muhammad Ali")
appt2 = Appointment(702, "2026-5-31", "11 :00 AM",
                    "Bakhtawar", "Ali Rind Baloch")

# ===========================================
# MEDICAL RECORD OBJECT
# ============================================
record1 = MedicalRecord(
    801, "hcv with chronic stage mhcv pvt", "Vaccines+Sonib", "hcv")
record2 = MedicalRecord(802, " Liver Failure",
                        "Go for transplantation", "Liver Failure")

# ===========================================
# Prescription object
# ==========================================
pres1 = Prescription(901, "Sonib", "2 times a day", "After meal")
pres2 = Prescription(902, "Rifaximine", "2 times a day", "Before meal")

# ----------------------------------------------------
# ward object
# ----------------------------------------------------
ward1 = Ward(501, "General", 10)
ward2 = Ward(502, "ICU", 5)

# -------------------------------------
bed1 = Bed(601, "Availaible/occupied")
bed2 = Bed(602, "Availaible/occupied")
bed3 = Bed(603, "Availaible/occupied")

# ----------------------------------
# ADMIN OBJECT
# ------------------------------------
admin1 = Admin(1001, "admin123", "pass123")

# ======================================
# Function section
# ======================================
# ------------------------------------
# Patient menu
# -------------------------------------


def patient_menu():
    while True:
        # patient menu dikhao
        print("\n" + "="*45)
        print(" PATIENT MENU")
        print("="*45)
        print(" 1. Register Patient")
        print(" 2. Show Medical History")
        print(" 3. Book Appointment")
        print(" 4. Show Patient Info")
        print(" 0.  Exit")
        print("="*45)

        # take choice from user
        choice = input(" take choice:")
        if choice == "1":
            # register patient
            print("\n WHICH PATIENT")
            print("  1.bakhtoo")
            print("  2.Bakhtawar")
            p = input("Choice")
            if p == "1":
                patient1.register()
            elif p == "2":
                patient2.register()
            else:
                print("Wrong Choice")
        elif choice == "2":
            # Medical history
            print("\n Which Patient")
            print("  1.bakhtoo")
            print("  2.bakhtawar")
            p = input("  Choice:")
            if p == "1":
                patient1.view_history()

            elif p == "2":
                patient2.view_history()
            else:
                print(" Wrong Choice!")

        elif choice == "3":
            # Appointment book karo
            # user se detail lo
            doc = input(" Doctor name:")
            date = input("Date (YYYY-MM-DD):")
            time = input("Time (HH:MM:AM/PM):")
            print("\n Which Patient")
            print("  1.bakhtoo")
            print("  2.Bakhtawar")
            p = input(" Choice :")
            if p == "1":
                patient1.book_appointment(doc, date, time)
            elif p == "2":
                patient2.book_appointment(doc, date, time)
            else:
                print("Wrong Choice")
        elif choice == "4":
            # patient info karo
            print(patient1)
            print(patient2)
        elif choice == "4":
            break

        else:
            print(" Wrong choice try again")

# ------------------------------------
# Doctor Menu
# -------------------------------------


def doctor_menu():
    while True:
        print("\n" + "="*45)
        print("  Doctor Menu")
        print("="*45)
        print("  1. Diagnose Patient")
        print("  2.Write Medicine")
        print("  3. Check Schedule")
        print("  4. Doctor Info")
        print("  0. Exit")
        print(""*45)
        choice = input("take choice:")
        if choice == "1":
            # diagnose karo
            patient = input(" Patient name")

            print("\n Which doctor")
            print(" 1.Dr Muhammad Ali")
            print(" 2.Dr Ahmed Ali Ansari")
            print("3.Basheer Abbasi")
            print("4.Asif Baloch")
            print("5. Ali Rind Baloch")
            d = input("take Choice:")

            if d == "1":
                doctor1.diagnose(patient)
            elif d == "2":
                doctor2.diagnose(patient)
            elif d == "3":
                doctor3.diagnose(patient)
            elif d == "4":
                doctor4.diagnose(patient)
            elif d == "5":
                doctor5.diagnose(patient)
            else:
                print("Wrong Choice")
        elif choice == "2":
            # Medicine Likho
            med = input(" Medicine name:")
            dosage = input(" Dosage:")
            print("\n Which doctor")
            print("  1.Dr Muhammad Ali")
            print("  2.Dr Ahmed Ali Ansari")
            print("3.Basheer Abbasi")
            print("4.Asif Baloch")
            print("5.Ali Rind Baloch")
            d = input(" Choice")
            if d == "1":
                doctor1.prescribe_medicine(med, dosage)

            elif d == "2":
                doctor2.prescribe_medicine(med, dosage)
            elif d == "3":
                doctor3.prescribe_medicine(med, dosage)
            elif d == "4":
                doctor4.prescribe_medicine(med, dosage)
            elif d == "5":
                doctor5.prescribe_medicine(med, dosage)
            else:
                print("Wrong Choice")

        elif choice == "3":
            # check schedule
            print("\n Which doctor")
            print("  1.Dr Muhammad Ali")
            print("  2.Dr Ahmed Ali Ansari")
            print("   3. Basheer abbasi")
            print("  4.Asif Baloch")
            print("  5. Ali Rind Baloch")
            d = input(" Choice")
            if d == "1":
                doctor1.check_schedule()
            elif d == "2":
                doctor2.check_schedule()
            elif d == "3":
                doctor3.check_schedule()
            elif d == "4":
                doctor4.check_schedule()
            elif d == "5":
                doctor5.check_schedule()
            else:
                print("Wrong Choice")
        elif choice == "4":
            # Doctor info
            print(doctor1)
            print(doctor2)
            print(doctor3)
            print(doctor4)
            print(doctor5)
        elif choice == "0":
            break

        else:
            print("Wrong Choice")

# -----------------------------------------
# APPOINTMENT MENU
# ----------------------------------------


def appointment_menu():
    while True:
        print("\n" + "="*45)
        print("  APPOINTMENT MENU")
        print("="*45)
        print(" 1. Appointment Schedule")
        print(" 2. Cancel appointment")
        print(" 3. Appointment Reschedule ")
        print(" 4. Appointment Info")
        print(" 0. Exit")

        choice = input("Take choice:")
        if choice == "1":
            # schedule karo
            print("\n which appointment?")
            print("1. Bakhtoo")
            print("2. Bakhtawar")
            a = input("Choice:")
            if a == "1":
                appt1.schedule()
            elif a == "2":
                appt2.schedule()
            else:
                print("Wrong Choice")
        elif choice == "2":
            # cancel appointment
            print("\n  Which appointment")
            print("1. Bakhtoo")
            print("2. Bakhtawar")
            a = input("Choice:")
            if a == "1":
                appt1.cancel()
            elif a == "2":
                appt2.cancel()
            else:
                print("Wrong choice")
        elif choice == "3":
            # reschedule karo
            new_date = input("new date:")
            new_time = input("new time")
            print("\n Which Appointment?")
            print(" 1.Bakhtoo")
            print(" 2. Bakhtawar")
            a = input("Choice:")
            if a == "1":
                appt1.reschedule(new_date, new_time)
            elif a == "2":
                appt2.reschedule(new_date, new_time)
            else:
                print("Wrong Choice")
        elif choice == "4":
            # Info Print karo
            print(appt1)
            print(appt2)
        elif choice == "0":
            break
        else:
            print("Wrong Choice")

# -------------------------------------------------
# ward menu
# ------------------------------------------------


def ward_menu():
    while True:
        print("\n" + "="*45)
        print("  WARD MENU ")
        print("="*45)
        print("1.Check Availaiblity")
        print("2.get Availaibility_beds")
        print("3.add_beds")
        print("4. Show Ward Info")
        print("0.Exit")
        print("="*45)
        choice = input("Choice:")
        if choice == "1":
            # availaibility check karo
            print("\n Which Ward?")
            print(" 1. General")
            print("2. ICU")
            w = input(" choice:")
            if w == "1":
                ward1.check_availability()
            elif w == "2":
                ward2.check_availability()
            else:
                print("Wrong Choice")
        elif choice == "2":
            # Available beds dekho
            print("\n Which ward?")
            print(" 1.General")
            print(" 2. ICU")
            w = input("Choice:")
            if w == "1":
                ward1.get_available_beds()
            elif w == "2":
                ward2.get_available_beds()
            else:
                print("Wrong Choice")
        elif choice == "3":
            # bed add karo
            bed_id = int(input("Bed ID:"))
            print("\n Which ward?")
            print("1.General")
            print("2.ICU")
            w = input("Choice")
            if w == "1":
                ward1.add_bed(bed_id)
            elif w == "2":
                ward2.add_bed(bed_id)
            else:
                print("Wrong Choice")
        elif choice == "4":
            # ward info str method wala
            print(ward1)
            print(ward2)
        elif choice == "0":
            break

        else:
            print("Wrong Choice")

# ----------------------------------------
# ADMIN MENU
# -----------------------------------------


def admin_menu():
    while True:
        print("\n" + "="*45)
        print("  ADMIN MENU")
        print("="*45)
        print("1.Manage Records")
        print("2. Generate Bill")
        print("3. Manage beds")
        print("4. Manage Users")
        print("0.Exit")
        print("="*45)
        choice = input("take choice:")
        if choice == "1":
            # manage record
            patient = input("Patient name")
            record = input("Record info:")
            admin1.manage_record(patient, record)
        elif choice == "2":
            # Bill generate karo
            patient = input("patient name:")
            amount = int(input("Amount:"))
            admin1.generate_bill(patient, amount)

        elif choice == "3":
            # manage beds
            ward = input(" Ward name!")
            status = input("Status (Availaible/Occupied):")
            admin1.manage_beds(ward, status)

        elif choice == "4":
            # user manage kro
            user = input(" User name :")
            action = input("Action(Add/Remove):")
            admin1.manage_users(user, action)

        elif choice == "0":
            break
        else:
            print("Wrong Choice")
# --------------------------------------------
# MAIN MENU FUNCTION
# ----------------------------------------------


def main_menu():
    # main menu dikhao
    while True:
        print("\n" + "="*45)
        print("#  HOSPITAL MANAGEMENT SYSTEM      #")
        print("="*45)
        print("1. Patient Menu")
        print("2. Doctor Manu")
        print("3. Appointment Menu")
        print("4. Ward Menu")
        print("5. Admin Menu")
        print("0. Exit")
        print("="*45)
        # user choice
        choice = input("User Choice:")
        if choice == "1":
            patient_menu()

        elif choice == "2":
            doctor_menu()

        elif choice == "3":
            appointment_menu()

        elif choice == "4":
            ward_menu()

        elif choice == "5":
            admin_menu()

        elif choice == "0":
            print("\n  THANK YOU! GOOD BYE!")
            print(" DEVELOPED BY ! Ali Rind Baloch!")
            break
        else:
            print("Wrong Choice! Try again")


if __name__ == "__main__":
    main_menu()
