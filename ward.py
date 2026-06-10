class Ward:
    def __init__(self, ward_id, ward_name, capicity):
        self.__ward_id = ward_id
        self.__ward_name = ward_name
        self.__capicity = capicity

        self.__beds = []  # khali list for bed tracking

    # =======================================
    # GETTER SECTION
    # =========================================
    def get_ward_id(self):
        return self.__ward_id

    def get_ward_name(self):
        return self.__ward_name

    def get_capicity(self):
        return self.__capicity

    def get_beds(self):
        return self.__beds

    # ===============================
    # SETTER SECTION
    # ==============================
    def set_ward_name(self, new_name):
        if new_name:
            self.__ward_name = new_name
            print(f"ward name updated sucessfully: {new_name}")
        else:
            print("ward is not availaible")

    def set_capicity(self, new_capicity):
        if new_capicity > 0:
            self.__capicity = new_capicity
            print(f"capicity is availaible: {new_capicity}")
        else:
            print("not availaible")

    # ---------------------------------------
    # METHOD 1: CheckAvailability()
    # return type int
    # -----------------------------------------
    def check_availability(self):
        # Capicity me se occupied bed ghtao
        # jitni bad list me hain wo occupied hain
        availaible = self.__capicity - len(self.__beds)

        # Availability dikhao
        print("\n" + "="*45)
        print("   Ward Availability")
        print("="*45)
        print(f" WARD  : {self.__ward_name}")
        print(f" TOTAL BEDS : {self.__capicity}")
        print(f" Occupied  : {len(self.__beds)}")
        print(f" Available: {availaible}")

        # Agar beds availaible hain
        if availaible > 0:
            print(f" status:   Availaible")
        else:
            print(f" Status  :  Full")
        print("="*45)
        return availaible
    # ---------------------------------
    # METHOD 2 : getAvailaibleBeds()
    # Availaible beds ki list dikhao
    # -----------------------------------

    def get_available_beds(self):
        availaible = self.__capicity - len(self.__beds)

        # availibilty ki detail
        print("\n" + "="*45)
        print(f"  {self.__ward_name} available beds!")
        print("="*45)
        print(f" Total Capicity : {self.__capicity}")
        print(f" Occupied Beds  : {len(self.__beds)}")
        print(f"  Availaible Beds  : {availaible}")
        print("-"*45)

        return availaible

    # --------------------------------
    # METHOD 3: addBed()
    # --------------------------------
    def add_bed(self, bed_id):
        if len(self.__beds) >= self.__capicity:
            print(" ward is full bed can not be empty!")
            return

        # wrna bad list me bed add kro
        self.__beds.append(bed_id)
        print(f" Bed {bed_id} added successfully")

    # ----------------------------------------
    # str method for ward info
    # --------------------------------

    def __str__(self):
        return (f"\n Ward Info:"
                f"\n  ID  : {self.__ward_id}"
                f"\n   Name : {self.__ward_name}"
                f"\n   Capicity : {self.__capicity}"
                f"\n   Beds : {len(self.__beds)} ")


# ======================================================
# TESTING SECTION
# ====================================================
if __name__ == "__main__":
    print("\n" + "#"*50)
    print("  WARD CLASS TEST")
    print("#"*50)

    # -------------------------------
    # TEST 1 WARD OBJECT
    # -----------------------------
    print(" Create ward object!")
    print("-"*40)

    ward1 = Ward(
        ward_id=201,
        ward_name="Medical ward",
        capicity=10
    )
    print("ward object created successfully!")
    print(ward1)

    # -----------------------------------------
    # TEST 2: GETTER TEST
    # -----------------------------------
    print("\n Getter Test")
    print("-"*40)
    print(f"get_ward_id()  = {ward1.get_ward_id()}")
    print(f"get_ward_name() = {ward1.get_ward_name()}")
    print(f"get_capicity  = {ward1.get_capicity()}")
    print(f"get_beds()    = {ward1.get_beds()}")
    print("All getters are working!")

    # ---------------------------------------------
    # TEST 3 SETTER TEST
    # ---------------------------------------------
    print("\n SETTER TEST")
    print("-"*40)

    # Correct method condition: 1
    print("correct info!")
    ward1.set_ward_name("General")

    # condition 2 wrong info
    print("wrong info name cant be empty")
    ward1.set_ward_name("")

    # set capicity conditon1 for correct method
    print("capicity updated!")
    ward1.set_capicity(15)

    # second conditin wrong capicity
    print("wrong capicity name")
    ward1.set_capicity(-5)

    # -------------------------------
    # add bed method call
    # ____________________________--
    print("\n  Beds add karo")
    ward1.add_bed(1)
    ward1.add_bed(2)
    ward1.add_bed(3)
    ward1.add_bed(4)
    ward1.add_bed(5)
    ward1.add_bed(6)
    ward1.add_bed(7)
    ward1.add_bed(8)
    ward1.add_bed(9)
    ward1.add_bed(10)
    ward1.add_bed(11)
    ward1.add_bed(12)
    ward1.add_bed(13)
    ward1.add_bed(14)
    ward1.add_bed(15)

    # ------------------------------------
    # CheckAvaikability
    # -----------------------------------
    print("\n Check Availablity")
    print("-"*45)
    available = ward1.check_availability()
    print(f"return : {available} beds available")

    # ---------------------------------------
    # GET AVAILABLE BEDS METHOD()
    # ----------------------------------------
    print("\n  Test 6 get_available_beds()")
    print("-"*40)

    ward2 = Ward(
        ward_id=502,
        ward_name="Surgery",
        capicity=3

    )
    ward2.add_bed(1)
    beds = ward2.get_available_beds()
    print(f"return : {beds} beds available")
