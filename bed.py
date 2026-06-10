class Bed:
    def __init__(self, bed_id, status):
        self.__bed_id = bed_id
        self.__status = "Availaible"

        # ===============================
        # GETTER SECTION
        # # ==============================

    def get_bed_id(self):
        return self.__bed_id

    def get_status(self):
        return self.__status

    # =====================================
    # Setter Section
    # =======================================
    def set_status(self, new_status):
        if new_status in ["Availaible", "Occupied"]:
            self.__status = new_status
            print(f" Status updated: {new_status}")
        else:
            print(" wrong info")
            print(" write availaible or occupied!")

            # ====================================
            # METHOD OPERATION SECTION
            # ======================================
    def allocate_bed(self, patient_name):
        # pehle status check kro k bad available hai ya nhi
        if self.__status != "Availaible":
            print("bed is not availaible")
            print(f" Bed ID: {self.__bed_id}")
            print(f"Staus : {self.__status}")
            return
        if not patient_name:
            print("Patient name is necessary!")
            return

        # bed allocate karo
        self.__status = "Occupied"
        # show detail
        print("\n" + "="*45)
        print("   Bed Allocated!")
        print("="*45)
        print(f" Bed ID : {self.__bed_id}")
        print(f"  Patient name : {patient_name}")
        print(f" Status : {self.__status}")

        # ========================================

        # METHOD 3: releasebed()
        # patient chla gya ab bad release kro
        # =======================================
    def release_bed(self):
        if self.__status == "Availaible":
            print(" Bed is availaible!")
            print(f"  Bed ID: {self.__bed_id}")
            return

        # bed release kro
        # status availaible krp
        self.__status = "Availaible"
        # Detail likho
        print("\n" + "="*45)
        print("  Bed RELEASED!")
        print("="*45)
        print(f" ID :  {self.__bed_id}")
        print(f"  STATUS: {self.__status}")
        print("Bed has been released")
        print("="*45)

        # ===================================
        # bed status update karo
        # ==================================
    def update_status(self, new_status):
        if new_status in ["Availaible", "Occupied"]:
            # purana status dikhane k liyai save karo
            old_status = self.__status

            # new status dikhao
            self.__status = new_status
            # detai likho
            print("\n" + "="*45)
            print(f" Bed {self.__bed_id} status updated")
            print("="*45)
            print(f" old status: {old_status}")
            print(f" new status  : {self.__status}")
            print("-"*45)
        else:
            print(" Wrong status!")
            print(" Just Availaible or Occupied")

    def __str__(self):
        return (f"\nBed Info:"
                f"\nBed ID : {self.__bed_id}"
                f"\nStatus :  {self.__status}")

    # ==========================================
    # TESTING SECTION
    # ============================================
if __name__ == "__main__":
    print("\n" + "="*50)
    print("  Bed class Testing")
    print("="*50)

    print("\n Test 1 : Create new object!")
    print("="*40)

    bed1 = Bed(
        bed_id=602,
        status="avalaible"

    )
    print("bed object created")
    print(bed1)

    # ---------------------------------
    # TEST2 GETTER TEST
    # -----------------------------------
    print("\nGETTER TEST")
    print("-"*40)
    print(f" get_bed_id = {bed1.get_bed_id()}")
    print(f" get_status = {bed1.get_status()}")
    print("All Getters Are Working")

    # ---------------------------------------
    # SETTER TEST
    # ----------------------------------------
    print("\n TEST3: Setter Test")
    print(""*40)
    print("Scorrect status Occupied!")
    bed1.set_status("Occupied")

    # wapas availaible kro
    print("correct status availaible")
    bed1.set_status("Availaible")

    print("wrong info!")
    bed1.set_status("Broken")

    # ------------------------------------
    # TEST 4: allocatebed method test
    # patient ko bed dena

    print("\nAllocate bed Method")
    print("-"*40)

    # for correct case
    print("--- Correct Case ---")
    bed1.allocate_bed("Ali Hassan")

    # for wrong case
    print("--- incorrect Case bad already Occupied---")
    bed1.allocate_bed("Ahmed Khan")

    # not patient name case
    print("--- Empty Patient Name ---")
    bed1.allocate_bed("")

    # --------------------------------------
    # TEST 5: Release bed Method test
    # --------------------------------------
    print("\n TEST 5: releaseBed() Method Test")
    print("-"*40)
    print("--- Correct Case ---")
    bed1.release_bed()

    print("\n bed is empty before")
    bed1.release_bed()

    # -------------------------------
    # TEST 6: update status
    # ------------------------------
    print("\n TEST 6: updateStaus")
    print("--- Availaible to occupied ---")
    bed1.update_status("occupied")
    print("--- occupied to availaible ---")
    bed1.update_status("Availaible")

    # wrong case
    print("\n --- wrong info ---")
    bed1.update_status("broken")
