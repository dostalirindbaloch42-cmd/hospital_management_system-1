class Nurse:
    def __init__(self, name, nurse_id, shift):
        self.__name = name
        self.__nurse_id = nurse_id
        self.__shift = shift

        # =================================
      # Getter SECTION
      # ===================================

    def get_name(self):
        return self.__name

    def get_nurse_id(self):
        return self.__nurse_id

    def get_shift(self):
        return self.__shift

    # ====================================
    # Setter Section
    # ==================================

    def set_name(self, new_name):
        if new_name:
            self.__name = new_name
            print(f"name updated {new_name}")

        else:
            print("empty name not found!")

    def set_shift(self, new_shift):
        # shift update kro
        # sirif 3 shift valid hai morning evening night
        if new_shift in ["Morning", "Evening", "Night"]:
            self.__shift = new_shift
            print(f"shift updated : {new_shift}")
        else:
            print("Wrong Shift!")

    # -------------------------------------
    # Method Section
    # Method 1 Assist doctor
    # return type none
    # ----------------------------------

    def assist_doctor(self, doctor_name):
        if not doctor_name:
            print("doctor name is missing")
            return
        # Assitance ki detail
        print("\n" + "="*45)
        print(" DOCTOR ASSISTANCE  ")
        print("="*45)
        print(f"  Nurse : {self.__name}")
        print(f" Shift : {self.__shift}")
        print(f" Doctor:Dr. {doctor_name}")
        print("Status  : Assisting")

        # ------------------------------------
        # Method 2: Check patiennt()
    # return none sirif check krta hai kuch wapis nhin krta
    # -------------------------------------------------
    def check_patient(self, patient_name):
        if not patient_name:
            print("patient name is necessary")

        # Patient ki detail
        print("\n" + "="*45)
        print(" PATIRNT CHECKUP")
        print(f"Nurse : {self.__name}")
        print(f" Shift : {self.__shift}")
        print(f" Patient name : {patient_name}")
        print("Status  : Checked")
        print("="*45)

        # -----------------------------

    # str method nurse ki info k liyai
    # jab print narse kro to ye ayega
    # ---------------------------------
    def __str__(self):
        return (f"\nNurse Info:"
                f"\n  ID : {self.__nurse_id}"
                f"\n  Name : {self.__name}"
                f"\n Shift : {self.__shift}")

# =============================================


if __name__ == "__main__":
    print("\n" + "="*50)
    print("  NURSE CLASS TESTING")
    print("="*50)

# Testing section
# Test 1 create a nurse object
# ===================================

print("\n Test 1: nurse object")
print("-"*40)

nurse1 = Nurse(
    nurse_id=102,
    name="Bakhtawar",
    shift="Morning"
)
print("nurse object created!")
print(nurse1)

# --------------------------------
# Test 2
# Getter test
# -------------------------------
print("\n  TEST 2: Getters Test")
print("-"*40)

# getter call
print(f" get_nurse_id() = {nurse1.get_nurse_id()}")
print(f" get_name() ={nurse1.get_name()} ")
print(f" get_shift() = {nurse1.get_shift()}")

# ---------------------------------------
# Test 3
# Setter Section
# ------------------------------------------
print("\n TEST 3: Setter section")
print("-"*45)
print("Correct name updated")
nurse1.set_name("Safia Bibi")

# Naam update kro khalo
print("name updated")
nurse1.set_name("")

# shift update kro sahi
print("shift has been updated")
nurse1.set_shift("Evening")

# shift update karo ghalat
print("shift updated")
nurse1.set_shift("Afternoon")

# ----------------------------------------
# assist doctor() Method Test
# ------------------------------------

print("\n  TEST 5: checkPatient()")
print("-"*40)

# Sahi case
print("right case")
nurse1.check_patient("Ali Hassan")

# Galat Case
print("\n --- galat case ---")
nurse1.check_patient("")
