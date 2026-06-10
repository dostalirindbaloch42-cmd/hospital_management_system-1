class Patient:

    def __init__(self, patient_id, name, age, gender, contact, medical_History):

        self.__patient_id = patient_id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__contact = contact
        self.__medical_History = medical_History

        # =========================================
        # GETTER SECTION
        # GETTER = to read private variable from outside
        # ===================================================================
    def get_patient_id(self):

        return self.__patient_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_contact(self):
        return self.__contact

    def get_medical_History(self):
        return self.__medical_History

        # ==================================
        # SETTER SECTION: use for update private variable

    def set_patient_contact(self, new_contact):
        if len(new_contact) >= 10:
            self.__contact = new_contact
            print(f"Contact has updated: {new_contact}")

        else:
            print("wrong number at least 10 digit recquired")

    def set_medical_history(self, new_history):
        self.__medical_History = new_history
        print(f"Medical history updated: {new_history}")

    def set_age(self, new_age):
        try:
            new_age = int(new_age)
        except ValueError:
            print("Age must be a number!")
        if new_age > 0 and new_age < 150:
            self.__age = new_age
            print(f"Age is updated: {new_age}")
        else:
            print("Wrong Age entered!")

        # =============================================#
        # METHODS/OPERATION SECTIONS:
        # METHOD 1: REGISTER:

    def register(self):
        # all information will be print
        print("\n" + "="*45)
        print("     PATIENT REGISTRATION FORM")
        print(f"  PATIENT ID : {self.__patient_id}")
        print(f"  NAME : {self.__name}")
        print(f"  AGE  : {self.__age}")
        print(f"   GENDER : {self.__gender}")
        print(f"  CONTACT : {self.__contact}")
        print(f"   MEDICAL HISTORY : {self.__medical_History}")
        print("="*45)
        print("Registration Completed!")
        print("="*45)

        # ================================#
        # METHOD 2: view history
        # patient can see his/her old disease history
        # Return type: None void

    def view_history(self):
        print("\n" + "="*45)
        print(f"  {self.__name} medical history")
        print("-"*45)

        if self.__medical_History:
            print(f"  {self.__medical_History}")

        else:
            print("Medical History Not Found")

        print("-"*45)

        # METHOD 3: bookAppointment()
        # patient doctor se milne ki appointment leta hai
        # Return type int id wapis bhejta hai
        # ================================================

    def book_appointment(self, doctor_name, date, time):
        if not doctor_name:
            print("doctor name is must for appointment!")
            return -1

            # check kro k koi date di hai ya nhin
        if not date:
            print(" date is must for appointment!")
            return -1

            # Appointment ID bnao
            # Formula : patientid * 100 +1
        appointment_id = self.__patient_id * 100 + 1

        # appointment ki detail
        print("\n" + "="*45)
        print("   APPOINTMENT CONFORMATION")
        print("="*45)
        print(f"\n  Appointment booked!")
        print(f" patient name : {self.__name}")
        print(f" DOCTOR : {doctor_name}")
        print(f" Date : {date}")
        print(f" TIME : {time}")
        print(f" STATUS : CONFIRMED")
        return appointment_id

    # -------------------------------------------
    # str method
    # yeh special method hai
    # patient object ko print krte waqt chlta hai
    # ---------------------------------------------
    def __str__(self):
        return (f"Patient [{self.__patient_id}]"
                f"Name: {self.__name}, "
                f"Age: {self.__age}, "
                f"Contact: {self.__contact} ,")


# =================================================
# TESTING - patient class testing code
# ================================================

if __name__ == "__main__":
    print("=" * 50)
    print("  PATIENT CLASS TEST")
    print("=" * 50)

    # TEST 1

    # NAYA PATIENT BNAYE
    p1 = Patient(patient_id=101, name="Ali Rind", age=22, gender="Male", contact="03052069475",
                 medical_History="Diabtese - 2019")

    print("patient object!")
    print(p1)

    # ---------------------------------------------
    # GETTER TEST
    # Private value ko getter se lena
    # -----------------------------------
    print("\n TEST 2: Getter Test")
    print("-"*40)
    # har getter ko call kro aur value lo
    print(f"  get_patient_id()  = {p1.get_patient_id()}")
    print(f"   get_name()       = {p1.get_name()}")
    print(f"  get_age()        = {p1.get_age()}")
    print(f"  get_gender()     = {p1.get_gender()}")
    print(f"  get_contact()    = {p1.get_contact()}")
    print(f"   medical_history() = {p1.get_medical_History()}")
    print("ALL METHODS OF GETTER ARE WORKING!")

    # ----------------------------------------------------
    #  TEST 3: Setter Test:
    # Values Update karo
    # ------------------------------------------------------
    print("\n TEST 3: Setter Test")
    print("-"*40)

    # sahi contact number
    print(" Valid number:")
    p1.set_patient_contact("03093477027")

    # galat contact test
    print("wrong number:")
    p1.set_patient_contact("123")

    print(" Medical History Updated:")
    p1.set_medical_history("diabties 2019, Flu 2023, bp 2024")

    print("Age has been updated:")
    p1.set_age("36")

    print("Wrong age updated")
    p1.set_age("-5")

    # --------------------------------------------
    # TEST 4: Register method() test
    # patient register form dikhana
    # ---------------------------------------------

    print("\n  Test 4 register method() test")
    print("-"*40)
    p1.register()

    # ---------------------------------------
    # TEST 5: view history method
    # ------------------------------------

    print("\n    view history method test")
    print("-"*40)
    p1.view_history()

    # ab 2nd condition not found else wala part
    # jiski koi history na ho wo show krna
    print("\n  no history")
    p2_no_history = Patient(
        patient_id=102,
        name="Bakhtawar",
        age=17,
        gender="Female",
        contact="030123456789",
        medical_History=""  # empty show hoga
    )
    p2_no_history.view_history()
    # -----------------------------------
    # TEST 6: book appointment method()
    # doctor se appointment book krna
    # ---------------------------------

    print("\n  TEST: 6 bookAppointment()")
    print("-"*40)

    # condition 1 sahi appointment
    print(" --- correct appointment ---")
    appointment_id = p1.book_appointment(
        doctor_name="Muhammad Ali",
        date="2026-5-26",
        time="10:30 AM"

    )
    # ye return function hai isliayi hum isko wapis bejege print krege
    print(f" return appointment id {appointment_id}")

    # galat appointment doctor nam nhin diya
    print("\n  wrong appointment doctor name not mentined")
    bad_appointment = p1.book_appointment(
        doctor_name="",
        date="26-5-26",
        time="11:00 AM"

    )
    print(f"return: {bad_appointment}")
