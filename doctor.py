class Doctor:

    def __init__(self, doctor_id, name, specialization, contact):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__specialization = specialization
        self.__contact = contact

        # ===========================================
    # GETTER SECTION
    # PRIVATE VALUE KO BAHIR SE ACCESS KRNE K LIYAI
    # ============================================
    def get_doctor_id(self):
        return self.__doctor_id

    def get_name(self):
        return self.__name

    def get_specialization(self):
        return self.__specialization

    def get_contact(self):
        return self.__contact

    # ==========================================
    # SETTER SECTION
    # update private variable information
    # ===========================================

    def set_contact(self, new_contact):
        if len(new_contact) >= 10:
            self.__contact = new_contact
            print(f" contact has been updated: {new_contact}")
        else:
            print("Invalid Contact Number")

    def set_specialization(self, new_spec):
        if new_spec:
            self.__specialization = new_spec
            print(f" specialization has been updated: {new_spec}")

        else:
            print("specialization cant be empty!")

    # ====================================================
    # METHOD SECTION
    # ----------------------------------------------------

    # METHOD 1: diagnose()
    # doctor patient ko check krta hai
    # kuch wapis nhin krta return type void none

    def diagnose(self, patient_name):
        if not patient_name:
            print("patient name is necessary for diagnose")
            return

        # diagnose detail
        print("\n" + "="*45)
        print("   DIAGNOSE REPORT")
        print("="*45)
        print(f" doctor name : Dr. {self.__name}")
        print(f" Secialization : {self.__specialization}")
        print(f" patient : {patient_name}")
        print(f" Status  : Examined ")
        print("="*45)

        # ------------------------------------------
        # METHOD 2: prescribeMedicine()
        # doctor dwai likhta hai
        # Return type: int(prescription id wapis ata hai)
        # -------------------------------------------------
    def prescribe_medicine(self, medicine, dosage):
        if not medicine:
            print("medicine name is necessary for prescribe!")
            return -1
        if not dosage:
            print("dosage is necessary")
            return -1

        # prescription id bnao
        # Formula: doctor_id * 100 + 1

        prescription_id = self.__doctor_id*100+1

        # prescription detail likho
        print("\n" + "="*45)
        print("  PRESCRIPTION DETAIL ")
        print("="*45)
        print(f"  DOCTOR: Dr. {self.__name}")
        print(f"  PRESCRIPTION ID : {prescription_id}")
        print(f" MEDICINE: {medicine}")
        print(f" DOSAGE : {dosage}")
        print(f" STATUS : Issued")
        # prescription id return karo
        return prescription_id
# ------------------------------------------
# METHOD 3: checkschedule()
# doctor apne schedule dekhta hai
# return type : none
# sirif dikhana hai kuch wapis nhin
# ----------------------------------------

    def check_schedule(self):
        print("\n" + "="*45)
        print(f" Dr. {self.__name} ka schedule")
        print("="*45)
        print(f" specialization : {self.__specialization}")
        print(f" Contact : {self.__contact}")
        print(f" Contact: {self.__contact}")
        print(f" Timing : 9:00 AM to 5:00 PM")
        print(f" Days:  Monday to Saturday")
        print("="*45)
   # -----------------------------------------
    # str method
    # print doctor karo to ye chlta hai
    # --------------------------------------

    def __str__(self):
        return (f"\nDoctor Info:"
                f"\n  ID    : {self.__doctor_id}"
                f"\n   Name  :  Dr. {self.__name}"
                f"\n    Specialization : {self.__specialization}"
                f"\n    Contact        : {self.__contact}")
        # =============================================


        # TESTING SECTION
        # Doctor class k sab method test krege
        # --------------------------------------------
if __name__ == "__main__":
    print("\n" + "#"*50)
    print("#  Doctor class testing start")
    print("#"*45)

    # --------------------------------------------
    # TEST 1: Naya doctor bnae
    # Doctor ka object bnate hain
    # ------------------------------------------=
    print("\n  TEST 1: naya doctor bnate hain")
    print("-"*40)

    # create doctor object
    doctor1 = Doctor(
        doctor_id=201,
        name="Muhammad Ali",
        specialization="Hepatologist",
        contact="03123456789",
    )
    print("object has been created!")
    print(doctor1)  # yaha jo humne str method bnaya wo chalega

    # -------------------------------------------
    # Test 2: GETTER TEST
    # --------------------------

    print("\n Getters test")
    print("-"*40)

    print(f"  get_doctor_id = {doctor1.get_doctor_id()}")
    print(f" get_name()  = {doctor1.get_name()}")
    print(f"  get_specialization = {doctor1.get_specialization()}")
    print(f" get_contact()   = {doctor1.get_contact()}")
    print("All Done!")

    # ---------------------------------------
    # Test 3: Setter test
    # ----------------------------------------

    print("\n   TEST 3: setter test")
    print("-"*40)

    # contact update kro sahi number
    print("valid number provided by user!")
    doctor1.set_contact("03213456788")
    # iska result sahi ayega

    # galat number
    print("Invalid Number from user!")
    doctor1.set_contact("123")

    print(" specialization updated!")
    doctor1.set_specialization("Neurology")

    # for wrong data 2nd conditin else
    print("empty specialization")
    doctor1.set_specialization("")  # fail hoga

    # -----------------------------------------
    # Test 4 : diagnose method
    # patient ko check krna
    # -----------------------------------------
    print("\n  TEST 4: diagnose method")
    print("-"*40)

    # sahi diagnose
    print("diagnosed correctly!")
    doctor1.diagnose("Ali Rind")

    # galat diagnose
    print("empty diagnose")
    doctor1.diagnose("")  # ye fail hoga

    # -------------------------------------
    # Test 5: prescribe medicine()
    # -------------------------------

    print("\n  Test : 5 prescribe medicine()")
    print("-"*40)

    # sahi prescription
    print("--- sahi prescription -----")
    pres_id = doctor1.prescribe_medicine(
        medicine="panadol",
        dosage="2 times a day"
    )
    # ID return hogi isko print krege
    print(f" Prescription Id found: {pres_id}")

    # galat prescription mrdicine isme medicine khali hoga
    print("\n --- Galat prescription medicine ---")
    bad_pres = doctor1.prescribe_medicine(
        medicine="",
        dosage="2 times a day"
    )
    print(f"return : {bad_pres}")

    # --------------------------------------
    # Test 6: checkschedule()
    # doctor ka schedule dekhna
    # -------------------------------------

    print("\n TEST 6: checkschedule()")
    print("-"*40)

    doctor1.check_schedule()
