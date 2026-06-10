class MedicalRecord:
    def __init__(self, record_id, diagnosis, treatment, test_reports):
        self.__record_id = record_id
        self.__diagnosis = diagnosis
        self.__treatment = treatment
        self.__test_reports = test_reports

        # =====================================
        # GETTERS SECTION
        # =======================================
    def get_record_id(self):
        return self.__record_id

    def get_diagnosis(self):
        return self.__diagnosis

    def get_treatment(self):
        return self.__treatment

    def get_test_reports(self):
        return self.__test_reports

    # ====================================
    # SETTER SECTION
    # =====================================
    def set_diagnosis(self, new_diagnosis):
        if new_diagnosis:
            print(f"diagnosis updated{new_diagnosis}")
        else:
            print("dignosis cant be empty!")

    def set_treatment(self, new_treatment):
        if new_treatment:
            print(f"treatment updated {new_treatment}")
        else:
            print("treatment cant be empty!")

    def set_test_reports(self, new_report):
        if new_report:
            print(f"Report has Updated {new_report}")
        else:
            print("Report Cant be Empty!")

    # =====================================
    # method section
    # ====================================
    def update_record(self, new_diagnosis, new_treatment, new_reports):
        if not new_diagnosis:
            print("Diagnosis is necessary!")
            return
        # new treatment check krne k liyai
        if not new_treatment:
            print("Treatment is necessary!")
            return
        if not new_reports:
            print("report is necessary!")
            return

        # purane values save kro sirif dikhane k liyai
        old_diagnosis = self.__diagnosis
        old_treatment = self.__treatment

        # ab new values save kro
        self.__diagnosis = new_diagnosis
        self.__treatment = new_treatment
        self.__test_reports = new_reports

        # detai likho
        print("\n" + "="*45)
        print("   RECORD UPDATED")
        print("="*45)
        print(f"  Record ID  : {self.__record_id}")
        print(f" Old diagnosis : {old_diagnosis}")
        print(f"  New diagnosis : {self.__diagnosis}")
        print(f" Old Treatment  : {old_treatment}")
        print(f"  New Treatment  :  {self.__treatment}")
        print("="*45)

    def view_record(self):
        print("\n" + "="*45)
        print(" MEDICAL RECORD")
        print("="*45)
        print(f" Record Id : {self.__record_id}")
        print(f" diagnosis :{self.__diagnosis}")
        print(f" treatment : {self.__treatment}")
        print(f" Test Reports : {self.__test_reports}")
        print("="*45)

        # -----------------------------------------
        # str method
        # ------------------------------------
    def __str__(self):
        return (f"\nMedical record info:"
                f"\n ID  : {self.__record_id}"
                f"\n Diagnosis : {self.__diagnosis}"
                f"\n Treatment : {self.__treatment}"
                f"\n Test Reports : {self.__test_reports}")


# =======================================================
# TESTING SECTION
# ======================================================
if __name__ == "__main__":
    print("\n" + "="*50)
    print(" MEDICAL RECORD TESTING")
    print("="*50)

    # ---------------------------------------
    # TEST 1 OBJECT BNANA
    # ------------------------------------
    print("\n TEST 1: OBJECT BNANA")
    print("-"*40)
    record1 = MedicalRecord(
        record_id=801,
        diagnosis="Hepatitis C with chronic stage",
        treatment="vaccines",
        test_reports="Ciroasis of Liver with multicentric hepatoma"

    )
    print("record1 ban gya")
    print(record1)

    # ------------------------------------
    # TEST 2 : GETTER TEST
    # ------------------------------------
    print("\n TEST 2: Getters Test")
    print("-"*40)
    print(f"get_record_id()  = {record1.get_record_id()}")
    print(f" get_diagnosis()    = {record1.get_diagnosis()}")
    print(f" get_treatment()  = {record1.get_treatment()}")
    print(f"get_test_reports()  = {record1.get_test_reports()} ")
    print("All getter methods are working!")

    # ------------------------------------
    # TEST 2 : SETTER TEST
    # -----------------------------------
    print("\n  SETTER TEST")
    print("-"*40)
    print("--- CORRECT CASE ---")
    record1.set_diagnosis("multicentric with pvt")

    print("--- Empty Case ---")
    record1.set_diagnosis("")

    print(" Correct case for treatment")
    record1.set_treatment("anitiviral drugs")

    print("Incorrect Case")
    record1.set_treatment("")

    print("Correct case for test report")
    record1.set_test_reports("ciroasis with pvt")
    print("Incorect case")
    record1.set_test_reports("")

    # ---------------------------------
    # Test 4 update record method()
    # ---------------------------------
    print("\n TEST 4: update record()")
    print("-"*40)
    # Sahi case
    print("--- Correct Diagnosis ---")
    record1.update_record(
        new_diagnosis="multicentric with pvt",
        new_treatment="antiviral drugs",
        new_reports="Ciroasis with pvt"

    )
    # incorrect case khaali diagnosis
    print("\n  Empty diagnosis ---")
    record1.update_record(
        new_diagnosis="",
        new_treatment="antiviral drugs",
        new_reports="Ciroasis with pvt"
    )
    # Galat case khaali treatment
    print("Empty treatment")
    record1.update_record(
        new_diagnosis="multicentric with pvt",
        new_treatment="",
        new_reports="Ciroasis with pvt"
    )
    # galat case khaali medical reports
    print("Empty medical reports")
    record1.update_record(
        new_diagnosis="multicentric with pvt",
        new_treatment="antiviral drugs",
        new_reports=""

    )
    # ---------------------------------
    # TEST 5 VIEW RECORD()
    # -----------------------------------
    print("\n Test 5 view medical record()")
    print("-"*40)
    record1.view_record()
