class Prescription:
    def __init__(self, prescription_id, medicine, dosage, instruction):
        self.__prescription_id = prescription_id
        self.__medicine = medicine
        self.__dosage = dosage
        self.__instruction = instruction

        # =====================================
        # GETTER SECTION
        # =====================================
    def get_prescription_id(self):
        return self.__prescription_id

    def get_medicine(self):
        return self.__medicine

    def get_dosage(self):
        return self.__dosage

    def get_instruction(self):
        return self.__instruction

    # ==================================
    # SETTER SECTION
    # =================================
    def set_medicine(self, new_medicine):
        if new_medicine:
            self.__medicine = new_medicine
            print(f"Medicine Updated {new_medicine}")
        else:
            print("Medicine cant be empty")

    def set_dosage(self, new_dosage):
        if new_dosage:
            self.__dosage = new_dosage
            print(f" Dosage is Updated {new_dosage}")
        else:
            print("Dosage is Empty!")

    def set_instruction(self, new_instruction):
        if new_instruction:
            print(f"Instruction is Updated {new_instruction}")
        else:
            print("instruction is empty")

    # ========================================
    # Method Section
    # ========================================
    def generate_prescription(self):
        if not self.__medicine:
            print("Medicine name is Necessary")
            return
        if not self.__dosage:
            print("dosage name is necessary")

        if not self.__instruction:
            print("Instruction is necessary")
        # prescription generate karo
        print("\n" + "="*45)
        print("  PRESCRIPTION GENERATED")
        print("="*45)
        print(f" Prescription ID : {self.__prescription_id}")
        print(f" Medicine  : {self.__medicine}")
        print(f" Dosage  : {self.__medicine}")
        print(f" Instruction : {self.__instruction}")
        print(f" Status :  Generated")
        print("="*45)

    def print_prescription(self):
        print("\n" + "="*45)
        print("  Prescripton Slip")
        print(f" Prescription ID: {self.__prescription_id}")
        print(f" Medicine : {self.__medicine}")
        print(f" Dosage : {self.__dosage}")
        print(f" Instruction : {self.__instruction}")
        print("="*45)

    # ===================================
    # STR METHOD
    # ================================
    def __str__(self):
        return ("\nPrescription Info:"
                f"\n ID  : {self.__prescription_id}"
                f"\n  Medicine : {self.__medicine}"
                f"\n  Dosage  : {self.__dosage}"
                f"\n  Instruction : {self.__instruction}")

        # ==============================================
        # TESTING SECTION
        # ===============================================
if __name__ == "__main__":
    print("\n" + "="*50)
    print("PRESSCRIPTION CLASS TESTING")
    print("="*50)
    # ==================================
    # TEST 1 OBJECT BNANA
    # ===================================
    print("\n  TEST 1: OBJECT BNANA")
    print("-"*40)
    pres1 = Prescription(
        prescription_id=901,
        medicine=" Panadol",
        dosage="2 times a day",
        instruction="After a Meal"
    )
    print("Prescription object created!")
    print(pres1)


# --------------------------------------
# TEST 2 GETTER TEST
# -----------------------------------
    print("\n TEST 2: Getter Test")
    print("-"*40)
    print(f" get_prescription_id() = {pres1.get_prescription_id()}")
    print(f" get_mediciene  = {pres1.get_medicine()}")
    print(f" get_dosage()  = {pres1.get_dosage()}")
    print(f" get_instructions()  = {pres1.get_instruction()}")
    print(" all getters are working!")

    # ==========================================
    # TEST 3: SETTER TEST
    # =========================================
    print("\n TEST 3: Setters Test")
    print("-"*40)

    # sahi dwai
    print(" Correct Medicine:")
    pres1.set_medicine("Paracetamol")

    # Khaali dwai
    print(" Empty Medicine")
    pres1.set_medicine("")

    # sahi dosage
    print(" correct dosage")
    pres1.set_dosage("3 times a day")

    # Khaali Dosage
    print(" Incorrect dosage")
    pres1.set_dosage("")

    # Sahi Instruction
    print(" Correct Instruction")
    pres1.set_instruction("Before meal")

    # khaali instruction
    print(" khaali instruction")
    pres1.set_instruction("")

    # --------------------------------
    # TEST 4 generatePrescription()
    # -------------------------------
    # CASE 1 -Sahi Case
    print("--- Sahi Case ---")
    pres1.generate_prescription()

    # CASE 2 KHAALI DWAI
    print(" Empty Medicine")
    pres1.generate_prescription()

    # CASE 3 KHAALI DOSAGE
    print(" empty dosage")
    pres1.generate_prescription()

    # Case 4 empty instruction
    print(" Empty instruction")
    pres1.generate_prescription()

    # ---------------------------------
    # Print Prescription
    # ----------------------------------
    print("\n  TEST 5: printPrescription()")
    print("="*40)
    pres1.print_prescription()
