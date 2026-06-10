class Appointment:
    def __init__(self, appointment_id, date, time, patient_name, doctor_name):
        self.__appointment_id = appointment_id
        self.__date = date
        self.__time = time
        self.__status = "Scheduled"
        self.__patient_name = patient_name
        self.__doctor_name = doctor_name

        # =========================================
        # GETTER SECTION
        # ========================================
    def get_appointment_id(self):
        return self.__appointment_id

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def get_status(self):
        return self.__status

    def get_patient_name(self):
        return self.__patient_name

    def get_doctor_name(self):
        return self.__doctor_name

    # ===================================
    # SETTER SECTION
    # ===================================
    def set_date(self, new_date):
        if new_date:
            self.__date = new_date
            print(f" date updated {new_date}")
        else:
            print("date is empty 404 error occured")

    def set_time(self, new_time):
        if new_time:
            self.__time = new_time
            print(f" Time Updated {new_time}")
        # ======================================
        # METHOD SECTION
        # ===========================================

    def schedule(self):
        if self.__status != "Canceled":
            print(" just cancel appointment can be schedule")
            return

        # status schedule karo
        self.__status = "Scheduled"

        # Detail dikhao
        print("\n" + "="*45)
        print(" APPOINTMENT SCHEDULED")
        print("="*45)
        print(f" Appointment ID : {self.__appointment_id}")
        print(f" DATE : {self.__date}")
        print(f" TIME :  {self.__time}")
        print(f"Status: {self.__status}")
        print(f"Patient_name: {self.__patient_name}")
        print(f"doctor_name: {self.__doctor_name}")
        print("="*45)

        # -----------------------------------------
        # METHOD 2: cancel()
        # return type : none
        # ------------------------------------------
    def cancel(self):
        if self.__status == "Canceled":
            print("Appointment is already canceled")
        # Status canceled
        self.__status = "Canceled"
        # Detail dikhao
        print("\n" + "="*45)
        print("   APPOINTMENT CANCELED")
        print("="*45)
        print(f" Appointment ID : {self.__appointment_id}")
        print(f" Patient  : {self.__patient_name}")
        print(f" Doctor  : Dr.{self.__doctor_name}")
        print(f" Status : {self.__status}")
        print("="*45)

        # ------------------------------------------
        # Method 3 reschedule
        # return type none
        # -----------------------------------
    def reschedule(self, new_date, new_time):
        # pehle check kro cancel to nhin
        if self.__status == "Cancelled":
            print("cancel appointment cant be rescheduled")
            return
        if not new_date:
            print("date is necessary for appointment")

        if not new_time:
            print("time is necessary for appointment")

        # old values save kro take doctor ko pta lage new appointment kab start hogi
        old_date = self.__date
        old_time = self.__time
        # ab new values save kro
        self.__date = new_date
        self.__time = new_time
        self.__status = "Rescheduled"

        # detail dikhao
        print("\n" + "="*45)
        print("  APPOINTMENT RESCHEDULED")
        print("="*45)
        print(f"Appointment ID :{self.__appointment_id}")
        print(f" Patient : {self.__patient_name}")
        print(f" DOCTOR :{self.__doctor_name}")
        print(f" Old date: {old_date}")
        print(f" New date: {new_date}")
        print(f" old time : {old_time}")
        print(f" new_time: {self.__time}")
        print(f" Status: {self.__status}")
        print("="*45)

        # -------------------------------

        # str method
        # --------------------------------
    def __str__(self):
        return (f"\nAppointment Info:"
                f"\n ID : {self.__appointment_id}"
                f"\n Patient : {self.__patient_name}"
                f"\n Doctor   : {self.__doctor_name}"
                f"\n Date     : {self.__date}"
                f"\n  Time    :  {self.__time}"
                f"\n   Status :  {self.__status}")


    # =============================================
    # TESTING SECTION
    # =============================================
if __name__ == "__main__":
    print("\n" + "#"*50)
    print("  APPOINTMENT CLASS - TESTING")
    print("#"*50)

    # ------------------------------------
    # TEST 1: NEW APPOINTMENT OBJECT
    # ------------------------------------
    print("\n  TEST1 : NEW APPOINTMENT OBJECT")
    print("-"*40)
    appt1 = Appointment(
        appointment_id=701,
        date="2025-12-25",
        time="10 : 00 AM",
        patient_name="Bakhtawar",
        doctor_name="Aslam abro"
    )
    appt1.cancel()
    print("appt1 canceled!")

    # CANCEL K LIYAI SCHEDULE STATE CHAHIYAI
    appt2 = Appointment(
        appointment_id=702,
        date="2026-5-27",
        time="11 : 00 AM",
        patient_name="Bakhtawar",
        doctor_name="Ali Rind Baloch"

    )
    print("appt2 scheduled")

    # rescheduled k liyai scheduled chahiyai
    # ye method case 4 p chla rhe hain
    appt3 = Appointment(
        appointment_id=703,
        date="2026-5-27",
        time="12 : 00 PM",
        patient_name="Bilal Ahmed",
        doctor_name="Usman ali"
    )

    # ------------------------------------
    # GETTER TEST
    # -------------------------------------
    print("\n TEST 2 : GETTER TEST")
    print("-"*40)
    print(f" get_appointment_id() = {appt1.get_appointment_id()}")
    print(f" get_date()     = {appt1.get_date()}")
    print(f" get_time()    = {appt1.get_time()}")
    print(f" get_status  = {appt1.get_status()}")
    print(f"get_doctor_name = {appt1.get_doctor_name()}")
    print(f"get_patient_name = {appt1.get_patient_name()}")
    print("All getters are working ")

    # -----------------------------
    # SETTER TEST
    # ----------------------------
    print("\n  TEST 3 : SETTER TEST")
    print("-"*40)
    print("--- correct case ---")
    appt1.set_date("2026-6-2")

    print("--- 404 Error date cant be empty ---")
    appt1.set_date("")

    print("--- correct update ---")
    appt1.set_time("11: 00 AM")

    print("--- empty time ---")
    appt1.set_time("")

    # ----------------------------------
    # appt1 canceled hai sahi case
    # appt2 schedule hai galat case
    # --------------------------------------
    print("\n  TEST 4: schedule  method")
    print("="*40)
    # galat case
    print("--- incorrect case ---")
    appt2.schedule()
    # sahi case
    print("\n Correct Case ---")
    appt1.schedule()

    # --------------------------------------
    # Test 5 cancel method
    # -----------------------------
    print("\n TEST 5: cancel method()")
    print("-"*40)
    # sahi case schedule
    print("Correct case")
    appt2.cancel()

    # galat case scheduled
    print("\n  incorrect case scheduled ---")
    appt2.cancel()

    # ---------------------------------------
    # TEST 6 RESCHEDULE
    # ----------------------------------------
    print("\n TEST 6: reschduled method test ()")
    print(" correct case")
    appt3.reschedule("2025-12-31", "02 :00 PM")

    # Galat case 1 canceled
    print("\n --- Canceled Appointment ---")
    appt2.reschedule("2025-12-31", "02 :00 PM")

    # galat case 2 khali tareekh
    print("\n  empty date ---")
    appt3.reschedule("", "02:00 PM")

    # GALAT CASE 3 KHAALI WAQT
    print("--- empty time ---")
    appt3.reschedule("2024-12-31", "")
