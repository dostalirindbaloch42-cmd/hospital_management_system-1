class Department:
    def __init__(self, department_id, name):
        self.__department_id = department_id
        self.__name = name

    # department mein doctors ki list
    # department mein nurse ki khali list
        self.__doctors = []
        self.__nurses = []

    # =====================================
    # GETTER SECTION
    # ====================================
    def get_department_id(self):
        return self.__department_id

    def get_name(self):
        return self.__name

    def get_doctors(self):
        return self.__doctors

    def get_nurses(self):
        return self.__nurses

    # ================================
    # SETTER SECTION
    # =================================
    def set_name(self, new_name):
        if new_name:
            self.__name = new_name
            print(f"department name has updated :{new_name}")
        else:
            print("404 error name cant be empty!")

    # ===========================================
    # METHOD SECTION
    # METHOD 1 addDoctor()
    # Return type just add not any return
    # ========================================
    def add_doctor(self, doctor_name):
        if not doctor_name:
            print("404 error Doctor name is necessary!")
            return
        # Doctor ki list me append karo
        self.__doctors.append(doctor_name)
        # Confirmation dikhao
        print("\n" + "="*45)
        print("    DOCTOR ADDED")
        print("="*45)
        print(f"Department  : {self.__name}")
        print(f"Doctor   : Dr.{doctor_name}")
        print(f"Total Doctors : {len(self.__doctors)}")
        print(f" Status:   Added")
        print("="*45)

        # -----------------------------------------
        # Method 2: AddNurse()
        # return none
        # -------------------------------------------
    def add_nurse(self, nurse_name):
        if not nurse_name:
            print("404 error nurse name cant be empty!")
            return

        self.__nurses.append(nurse_name)

        print("\n" + "="*45)
        print("   NURSE ADDED")
        print("="*45)
        print(f"Department : {self.__name}")
        print(f" Nurse  : {nurse_name}")
        print(f" Total Nurse : {len(self.__nurses)}")
        print(f" Status : added")
        print("="*45)

        # ---------------------------------------
        # Method 3
        #  Return type none
        # --------------------------------------------

    def manage_staff(self):
        # staff ki detail
        print("\n" + "="*45)
        print("   STAFF MANAGEMENT")
        print(f" Department : {self.__name}")
        print(f" ID       :   {self.__department_id}")
        print("-"*45)

        # Doctors dikhao
        print(f"Doctors dikhao ({len(self.__doctors)}):")

        # agar doctor hain to dikhao
        if self.__doctors:
            for doctor in self.__doctors:
                print(f"   -Dr.{doctor}")
        else:
            print(" no doctor found")

        print("-"*45)

        # nurses dikhao
        print(f"Nurses ({len(self.__nurses)}):")

        # agar nurses hain to dikhao
        if self.__nurses:
            for nurse in self.__nurses:
                print(f" {nurse}")
        else:
            print(" no nurse found!")
        print("="*45)

        # -----------------------------------------
        # str Method for department basic info
        # ------------------------------------------
    def __str__(self):
        return (f"\nDepartment Info:"
                f"\n  ID  :    {self.__department_id}"
                f"\n  name   : {self.__name}"
                f"\n   doctors  :  {len(self.__doctors)}"
                f"\n    Nurses  :  {len(self.__nurses)}")


# ====================================================
# TESTING SECTION
# =====================================================
if __name__ == "__main__":
    print("\n" + "="*50)
    print("=   department class testing started")
    print("="*50)

    print("\n Test 1: create a department object!")
    print("-"*40)

    # department ka object bnaye
    dept1 = Department(
        department_id=402,
        name="Hepotology"

    )
    print("Department object created successfully")
    print(dept1)

    # -----------------------------------------
    # GETTER SECTION TEST
    # ----------------------------------------
    print("\n test 2 : getter test")
    print("-"*45)

    print(f"get_department_id = {dept1.get_department_id()}")
    print(f"get_name  = {dept1.get_name()}")
    print(f" get_doctors = {dept1.get_doctors()}")
    print(f"get_nurses = {dept1.get_nurses()}")
    print("All Getter Section is working")

    # -----------------------------------
    # METHOD 3: SETTER SECTION
    # -----------------------------------
    print("\n TEST 3: SETTER TEST")
    print("-"*40)

    print("valid name")
    dept1.set_name("Neurology")

    # khaali naam
    print("empty name")
    dept1.set_name("")

    # -----------------------------------
    # METHOD 4: AddDOCTOR()
    # ------------------------------
    print("\n TEST 4: Add doctor()")
    print("-"*40)

    # valid doctor name
    print(" correct doctor info!")
    dept1.add_doctor("Aslam abro")
    dept1.add_doctor("Basheer abbasi")

    # wrong info
    print("404 Error Occured Invalid name!")
    dept1.add_doctor("")

    # -----------------------------------
    # Method 5: add_nurse()
    # ----------------------------------

    print("\n TEST 5: add_nurse()")
    print("-"*40)

    # valid context
    print(" Correct Nurse info!")
    dept1.add_nurse("Bakhtoo")
    dept1.add_nurse("Mahnoor bibi")

    # invalid context
    print("Incorect Nurse Info!")
    dept1.add_nurse("")

    # ------------------------------------
    # METHOD 6 : Manage_staff()
    # -----------------------------------
    print("\n Manage staff test()")
    print("-"*40)
    dept1.manage_staff()

    # ab else part k test k liyai khali department benga
    print("Khali department")
    dept2 = Department(
        department_id=403,
        name="Surgery"
    )
    dept2.manage_staff()

    print("\n" + "="*50)
    print("  DEPARTMENT CLASS TESTING COMPLETED!")
    print("-"*50)
