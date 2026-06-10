class Admin:
    def __init__(self, admin_id, username, password):
        self.__admin_id = admin_id
        self.__username = username
        self.__password = password

        # =============================
        # GETTER SECTION
        # =============================
    def get_admin_id(self):
        return self.__admin_id

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    # =================================
    # SETTER SECTION
    # ==================================
    def set_username(self, new_username):
        if new_username:
            self.__username = new_username
            print(f" username updated : {new_username}")
        else:
            print("Username Cant be Empty!")

    def set_password(self, new_password):
        if len(new_password) >= 6:
            self.__password = new_password
            print(f"Password Updated : {new_password}")
        else:
            print("Minimum 6 digit Recquired!")

        # ===========================================
        # METHODS SECTION
        # ===========================================
        # Method 1 : manageRecord()
        # Patient ka Record manage krna
        # ================================
    def manage_record(self, patient_name, record_info):
        # patient nam check karo
        if not patient_name:
            print("patient name is necessary")
            return
        # Record info check karo
        if not record_info:
            print("record info is necessary")
            return
        # Record manage karo
        print("\n" + "="*45)
        print(" RECORD MANAGEMENT")
        print(f" Patient_name : {patient_name}")
        print(f" Record Info : {record_info}")
        print(f" Status       : Updated")
        print("="*45)

        # ------------------------------------
        # METHOD 2: generateBill()
        # ---------------------------------------
    def generate_bill(self, patient_name, amount):
        if not patient_name:
            print("patient name is necessary!")
            return
        # Amount check karo
        if amount <= 0:
            print("Amount should be greater than zero!")
            return
        # Bill generate karo
        print("\n" + "="*45)
        print("  BILL GENERATED")
        print("="*45)
        print(f" Patient  :  {patient_name}")
        print(f" Amount  :  Rs.{amount}")
        print(f"  Status  : Generated")
        print("="*45)

        # --------------------------------------------------
        # METHOD 3 : managedBeds()
        # ------------------------------------------------
    def manage_beds(self, ward_name, bed_status):
        if not ward_name:
            print(" Ward name is necessary!")
            return
            # Bed Status Check Karo
        if bed_status not in ["Availaible", "Occupied!"]:
            print(" Wrong Status ! Availaible or Occupied!")
            return

            # Beds manage karo
        print("\n" + "="*45)
        print(" BEDS MANAGEMENT")
        print("="*45)
        print(f" Ward  : {ward_name}")
        print(f" Bed Status  : {bed_status}")
        print(f" Status  : Updated")
        print("="*45)

        # ---------------------------------
        # METHOD 4
        # ---------------------------------
    def manage_users(self, user_name, action):
        if not user_name:
            print("user name is necessory")
            return
        if action not in ["Add", "Remove!"]:
            print("Wrong Action! Add or Remove!")
            return

        print("\n" + "="*45)
        print("  USER MANAGEMENT")
        print("="*45)
        print(f" User   : {user_name}")
        print(f" Action  :  {action}")
        print(f"Status   : Done")
        print("="*45)

    # -----------------------------------
    # Str method
    # ---------------------------------
    def __str__(self):
        return (f"\nAdmin Info:"
                f"\n  ID : {self.__admin_id}"
                f"\n   Username : {self.__username}"
                f"\n  Password : *******")


    # ========================================
    # TESTING SECTION
    # ========================================
if __name__ == "__main__":
    print("\n" + "="*50)
    print("   ADMIN CLASS TESTING")
    print("="*50)
    print("\n TEST 1: CREATE OBJECT!")
    print("="*50)
    admin1 = Admin(
        admin_id=1001,
        username="admin1234",
        password="pass123"

    )
    print("admin object created!")
    print(admin1)

    # --------------------------------
    # GETTER TEST
    # -------------------------------
    print("\n  Getter Test")
    print("="*40)
    print(f"  ID   = {admin1.get_admin_id()}")
    print(f" Username = {admin1.get_username()}")
    print("All Getters working!")

    # -----------------------------------
    # SETTER TEST
    # -------------------------------------
    print("\n TEST3 : SETTERS TEST")
    print("-"*40)
    print(" Correct Username:")
    admin1.set_username("superadmin")
    # khaali username
    print(" khaali username")
    admin1.set_username("")

    # sahi password 6 se ziyada
    print("Correct Password")
    admin1.set_password("newpass123")

    # -----------------------------------------
    # TEST 4: manageRecords()
    # -----------------------------------------
    print("\n TEST 4: manageRecords()")
    print("-"*40)

    # Sahi Case
    admin1.manage_record(
        patient_name="Ali Hassan",
        record_info="Diabtes updated",

    )
    # Galat case
    print("\n  --- Empty Patient ---")
    admin1.manage_record(
        patient_name="",
        record_info="Hepaticellular Carcinoma"
    )
    # Galat case 2
    print("\n  Empty Record")
    admin1.manage_record(
        patient_name="Ali hassan",
        record_info=""

    )

    # -----------------------------------------
    # Test 5 generate bill method test
    # ---------------------------------------
    print("\n📌 TEST 5: generateBill() Method Test")
    print("-"*40)

    # Sahi Case
    print("  --- Sahi Case ---")
    admin1.generate_bill(
        patient_name="Ali Hassan",
        amount=5000
    )                                   # ✅

    # Galat Case 1 - Khaali Naam
    print("\n  --- Khaali Patient Naam ---")
    admin1.generate_bill(
        patient_name="",
        amount=5000
    )                                   # ❌

    # Galat Case 2 - Galat Amount
    print("\n  --- Galat Amount ---")
    admin1.generate_bill(
        patient_name="Ali Hassan",
        amount=0
    )                                   # ❌

    # ----------------------------------------------------------
    # TEST 6: manageBeds() Method Test
    # 2 Conditions = 3 Cases
    # ----------------------------------------------------------
    print("\n📌 TEST 6: manageBeds() Method Test")
    print("-"*40)

    # Sahi Case
    print("  --- Sahi Case ---")
    admin1.manage_beds(
        ward_name="General",
        bed_status="Available"
    )                                   # ✅

    # Galat Case 1 - Khaali Ward
    print("\n  --- Khaali Ward Naam ---")
    admin1.manage_beds(
        ward_name="",
        bed_status="Available"
    )                                   # ❌

    # Galat Case 2 - Galat Status
    print("\n  --- Galat Bed Status ---")
    admin1.manage_beds(
        ward_name="General",
        bed_status="Broken"
    )                                   # ❌

    # ----------------------------------------------------------
    # TEST 7: manageUsers() Method Test
    # 2 Conditions = 3 Cases
    # ----------------------------------------------------------
    print("\n📌 TEST 7: manageUsers() Method Test")
    print("-"*40)

    # Sahi Case - Add
    print("  --- Sahi Case Add ---")
    admin1.manage_users(
        user_name="Dr. Ahmed",
        action="Add"
    )                                   # ✅

    # Sahi Case - Remove
    print("  --- Sahi Case Remove ---")
    admin1.manage_users(
        user_name="Dr. Ahmed",
        action="Remove"
    )                                   # ✅

    # Galat Case 1 - Khaali Naam
    print("\n  --- Khaali User Naam ---")
    admin1.manage_users(
        user_name="",
        action="Add"
    )                                   # ❌

    # Galat Case 2 - Galat Action
    print("\n  --- Galat Action ---")
    admin1.manage_users(
        user_name="Dr. Ahmed",
        action="Update"
    )
