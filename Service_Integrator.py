import os
import sys
import tkinter as tk
import tkinter.messagebox
import ScrollableFrame
import pandas as pd
from CTkMessagebox import CTkMessagebox
import customtkinter
import messagebox
import mysql.connector
from PIL import Image
from datetime import date, timedelta, datetime
import time
import keyboard  # Import the keyboard module
import pandas as pd
from colorama import Fore, Style
import Appointment_Alignment_Scripts

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
#customtkinter.set_window_scaling(0.5)
#customtkinter.set_window_scaling(0.5)
#customtkinter.deactivate_automatic_dpi_awareness()

IMAGE_WIDTH = 630
IMAGE_HEIGHT = 130
IMAGE_PATH = 'images/clinical_app_align.png'


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        def show_top_window(self):
            # Lift and focus the top window when the main application button is clicked
            self.topwindow.lift()
            self.topwindow.focus_force()
            self.iconify()

        def bulk_search():
            self.topwindow_bulk = customtkinter.CTkToplevel(None)
            window_width1 = 450
            window_height1 = 110

            # Get the screen width and height
            screen_width1 = self.winfo_screenwidth()
            screen_height1 = self.winfo_screenheight()

            # Calculate the position for the window to be centered
            x1 = (screen_width1 // 2) - (window_width1 // 2.5)
            y1 = (screen_height1 // 2) - (window_height1 // 2)
            self.topwindow_bulk.geometry(f"{window_width1}x{window_height1}+{x1}+{y1}")
            # self.topwindow.geometry("350x100+400+200")
            self.topwindow_bulk.title("Bulk Search")
            self.grid_columnconfigure(1, weight=1)
            self.topwindow_bulk.iconbitmap("images/cihp.ico")
            self.topwindow_bulk.resizable(False, False)
            self.topwindow_bulk.lift()
            self.topwindow_bulk.focus_force()

            self.ids_label = customtkinter.CTkLabel(self.topwindow_bulk, text="Input/paste comma separted PEPID(s)",
                                                      font=customtkinter.CTkFont(size=12),
                                                      text_color=("gray10", "#DCE4EE"))
            self.ids_label.grid(row=0, column=0, padx=2, pady=(2, 0), sticky="w")

            self.ids_entry = customtkinter.CTkEntry(self.topwindow_bulk, placeholder_text="Input/paste comma separted PEPID(s)",
                                                   width=400,
                                                   height=40, font=customtkinter.CTkFont(size=15))
            self.ids_entry.grid(row=1, column=0, pady=0, padx=(2, 0), sticky="e")
            self.ids_entry.bind("<Return>", self.bulk_search_destroy_top)

            self.ids_entry_button = customtkinter.CTkButton(self.topwindow_bulk, text="Search",
                                                           width=200, font=customtkinter.CTkFont(size=15),
                                                           command=self.bulk_search_destroy_top)
            self.ids_entry_button.grid(row=2, column=0, padx=2, pady=(2, 5), sticky="w")

            self.bulk_search_button.configure(state="disabled")
            self.topwindow_bulk.lift()
            self.topwindow_bulk.focus_force()
            self.topwindow_bulk.focus()
            self.iconify()

        def connect_host():
            self.topwindow = customtkinter.CTkToplevel(None)
            window_width1 = 350
            window_height1 = 100

            # Get the screen width and height
            screen_width1 = self.winfo_screenwidth()
            screen_height1 = self.winfo_screenheight()

            # Calculate the position for the window to be centered
            x1 = (screen_width // 2) - (window_width // 2)
            y1 = (screen_height // 2) - (window_height // 2)
            self.topwindow.geometry(f"{window_width1}x{window_height1}+{x1}+{y1}")
            #self.topwindow.geometry("350x100+400+200")
            self.topwindow.title("Host IP Address")
            self.grid_columnconfigure(1, weight=1)
            self.topwindow.iconbitmap("images/cihp.ico")
            self.topwindow.resizable(False, False)
            self.topwindow.lift()
            self.topwindow.focus_force()


            self.break_label = customtkinter.CTkLabel(self.topwindow, text="Type in a host IP address:",
                                                      font=customtkinter.CTkFont(size=12),
                                                      text_color=("gray10", "#DCE4EE"))
            self.break_label.grid(row=0, column=0, padx=2, pady=(2, 0), sticky="w")

            self.ip_entry = customtkinter.CTkEntry(self.topwindow, placeholder_text="Enter IP address of host",
                                                   width=200,
                                                   height=20, font=customtkinter.CTkFont(size=15))
            self.ip_entry.grid(row=1, column=0, pady=0, padx=(2, 0), sticky="e")
            self.ip_entry.bind("<Return>", self.ip_get_destroy_top)

            self.ip_entry_button = customtkinter.CTkButton(self.topwindow, text="Connect to Host",
                                                           width=200, font=customtkinter.CTkFont(size=15),
                                                           command= self.ip_get_destroy_top)
            self.ip_entry_button.grid(row=2, column=0, padx=2, pady=(2, 5), sticky="e")

            self.con_host_button.configure(state="disabled")
            self.topwindow.lift()
            self.topwindow.focus_force()
            show_top_window(self)


            #def restore_win(self):
                #self.deiconify()


            # self.ip_request = customtkinter.CTkInputDialog(text="Type in a host IP address:", title="Host IP Address")
            # print("Dialog:", self.ip_request.get_input())

            # p_request_value = self.ip_request.get_input()
            # print(ip_request_value)

            # host_ip = ip_request.get_input()

            try:
                mydb1 = mysql.connector.connect(
                    host=self.ip_entry.get(),
                    user="root",
                    passwd="Admin123",
                    database='openmrs'
                )

                my_cursor1 = mydb1.cursor()

                # my_cursor1.close()
                # mydb1.close()
            except Exception as e:
                messagebox.showinfo('Info', "ERROR: {}".format(e))

        # connect_host()
        # configure window
        # Set the size of the window
        window_width = 1112
        window_height = 610

        # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the position for the window to be centered
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.title("Service Integrator v1.0.1")
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.iconbitmap("images/cihp.ico")
        #self.resizable(True, True)

        self.canvas = tk.Canvas(self)
        self.scrollbar_y = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar_x = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)

        # Create a frame to be placed on the canvas
        self.scrollable_frame = customtkinter.CTkFrame(self.canvas)

        # Create a window on the canvas to contain the frame
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Configure scrolling
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.configure(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)

        # Pack canvas and scrollbars using grid
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar_y.grid(row=0, column=1, sticky="ns")
        self.scrollbar_x.grid(row=1, column=0, sticky="ew")

        # Ensure the grid expands
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        #ctk_textbox_scrollbar = customtkinter.CTkScrollbar(self)
        #ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

        self.scrollable_frame1 = customtkinter.CTkScrollableFrame(self, width=1095, height=590, orientation=("horizontal"))
        self.scrollable_frame1.grid(row=0, column=0, sticky="nsew")


        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.scrollable_frame1, width=1090, height = 596)
        self.scrollable_frame.grid(row=0, column=0, sticky="nsew")



        self.bulk_search_button = customtkinter.CTkButton(self.scrollable_frame, text="Bulk \n Search",
                                                       width=100, height=130,
                                                       font=customtkinter.CTkFont(size=20, weight="bold"),
                                                       command=bulk_search)
        self.bulk_search_button.grid(row=0, column=1, padx=(2, 0), pady=(2, 0), sticky="nsew")

        self.con_host_button = customtkinter.CTkButton(self.scrollable_frame, text="Connect \n to Host",
                                                       width=80, height=130,
                                                       font=customtkinter.CTkFont(size=20, weight="bold"),
                                                       command=connect_host)
        self.con_host_button.grid(row=0, column=4, padx=(2, 0), pady=(2, 0), sticky="nsew")

        # configure grid layout (4x4)
        #self.grid_columnconfigure(1, weight=0)
        #self.grid_columnconfigure((2, 3), weight=0)
        #self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18), weight=0)





        # create sidebar frame with widgets
        self.clinicdays_frame = customtkinter.CTkFrame(self.scrollable_frame, width=140, fg_color='#2CC985')
        self.clinicdays_frame.grid(row=0, column=0, padx=(2, 0), pady=(0, 0), rowspan=14, sticky="nsew")
        self.clinicdays_frame.grid_rowconfigure(17, weight=1)
        self.clinicdays_label = customtkinter.CTkLabel(self.clinicdays_frame, text="Select facility clinic days:",
                                                       font=customtkinter.CTkFont(size=15, weight="bold"), text_color="white")
        self.clinicdays_label.grid(row=0, column=0, padx=2, pady=(5, 5), sticky="w")

        self.checkboxmonday_var = customtkinter.StringVar(value="off")
        self.monday_checkbox = customtkinter.CTkCheckBox(master=self.clinicdays_frame, text="Monday",
                                                         variable=self.checkboxmonday_var, onvalue="on", offvalue="off",
                                                         command=self.get_checked_days)
        self.monday_checkbox.grid(row=1, column=0, pady=(2, 0), padx=2, sticky="w")

        self.checkboxtuesday_var = customtkinter.StringVar(value="off")
        self.tuesday_checkbox = customtkinter.CTkCheckBox(master=self.clinicdays_frame, text="Tuesday",
                                                          variable=self.checkboxtuesday_var, onvalue="on",
                                                          offvalue="off", command=self.get_checked_days)
        self.tuesday_checkbox.grid(row=2, column=0, pady=(0, 0), padx=2, sticky="w")

        self.checkboxwednesday_var = customtkinter.StringVar(value="off")
        self.wednesday_checkbox = customtkinter.CTkCheckBox(master=self.clinicdays_frame, text="Wednesday",
                                                            variable=self.checkboxwednesday_var, onvalue="on",
                                                            offvalue="off", command=self.get_checked_days
                                                            )
        self.wednesday_checkbox.grid(row=3, column=0, pady=(0, 0), padx=2, sticky="w")

        self.checkboxthursday_var = customtkinter.StringVar(value="off")
        self.thursday_checkbox = customtkinter.CTkCheckBox(master=self.clinicdays_frame, text="Thursday",
                                                           variable=self.checkboxthursday_var, onvalue="on",
                                                           offvalue="off", command=self.get_checked_days
                                                           )
        self.thursday_checkbox.grid(row=4, column=0, pady=(0, 0), padx=2, sticky="w")

        self.checkboxfriday_var = customtkinter.StringVar(value="off")
        self.friday_checkbox = customtkinter.CTkCheckBox(master=self.clinicdays_frame, text="Friday",
                                                         variable=self.checkboxfriday_var, onvalue="on",
                                                         offvalue="off", command=self.get_checked_days
                                                         )
        self.friday_checkbox.grid(row=5, column=0, pady=(0, 0), padx=2, sticky="w")

        self.checkboxsaturday_var = customtkinter.StringVar(value="off")
        self.saturday_checkbox = customtkinter.CTkCheckBox(master=self.clinicdays_frame, text="Saturday",
                                                           variable=self.checkboxsaturday_var, onvalue="on",
                                                           offvalue="off", command=self.get_checked_days
                                                           )
        self.saturday_checkbox.grid(row=6, column=0, pady=(0, 0), padx=2, sticky="w")

        self.checkboxsunday_var = customtkinter.StringVar(value="off")
        self.sunday_checkbox = customtkinter.CTkCheckBox(master=self.clinicdays_frame, text="Sunday",
                                                         variable=self.checkboxsunday_var, onvalue="on",
                                                         offvalue="off", command=self.get_checked_days
                                                         )
        self.sunday_checkbox.grid(row=7, column=0, pady=(0, 0), padx=2, sticky="w")

        self.break_label = customtkinter.CTkLabel(self.clinicdays_frame, text="_____________________________",
                                                  font=customtkinter.CTkFont(size=15, weight="bold"),
                                                  text_color=("gray10", "#DCE4EE"))
        self.break_label.grid(row=8, column=0, padx=2, pady=(1, 1), sticky="w")

        # Bind the combined function to the <Return> event
        # self.pepid_entry.bind("<Return>", self.combined_function)

        self.pepid_entry = customtkinter.CTkEntry(self.clinicdays_frame, placeholder_text="Enter PEPID", width=200,
                                                  height=40, font=customtkinter.CTkFont(size=20, weight="bold"))
        self.pepid_entry.grid(row=9, column=0, pady=(10, 0), padx=(2, 0), sticky="w")
        self.pepid_entry.bind("<Return>", self.current_client_details)

        self.pepid_entry_button = customtkinter.CTkButton(self.clinicdays_frame, text=f"Suggest Appointment Date",
                                                          width=200, font=customtkinter.CTkFont(size=15), border_width= 1,
                                                          command=self.current_client_details)
        self.pepid_entry_button.grid(row=10, column=0, padx=2, pady=(2, 5), sticky="w")

        bleed_now_var = customtkinter.StringVar()

        def determinant(self):
            ip = self.ip_entry.get()
            try:
                mydb1 = mysql.connector.connect(
                    host=ip,
                    user="root",
                    passwd="Admin123",
                    database='openmrs'
                )
                my_cursor1 = mydb1.cursor()
                my_cursor2 = mydb1.cursor()
                my_cursor3 = mydb1.cursor()
                my_cursor4 = mydb1.cursor()
                my_cursor5 = mydb1.cursor()
                my_cursor6 = mydb1.cursor()
                my_cursor7 = mydb1.cursor()
                my_cursor8 = mydb1.cursor()
                my_cursor9 = mydb1.cursor()
                my_cursor10 = mydb1.cursor()
                # my_cursor1.close()
                # mydb1.close()
            except Exception as e:
                messagebox.showinfo('Info', "ERROR: {}".format(e))
            pepid = self.pepid_entry.get()
            get_patient_id = f"SELECT `patient_id` FROM `patient_identifier` WHERE `identifier` = '{pepid}' AND `voided`=0 AND `identifier_type` = 4;"
            run_set_patient_id = my_cursor1.execute(get_patient_id)
            result_patient_id1 = my_cursor1.fetchone()
            print(result_patient_id1)

            last_vl_date1 = my_cursor2.execute(Appointment_Alignment_Scripts.last_vl_date)
            last_vl_date1_mysql_result = my_cursor2.fetchone()

            last_vl_result1 = my_cursor3.execute(Appointment_Alignment_Scripts.last_vl_result)
            last_vl_result1_mysql_result = my_cursor3.fetchone()

            last_sample_date1 = my_cursor4.execute(Appointment_Alignment_Scripts.last_sample_date)
            last_sample_date1_mysql_result = my_cursor4.fetchone()

            last_refill_days = my_cursor5.execute(Appointment_Alignment_Scripts.last_refill_days)
            last_refill_days_mysql_result1 = my_cursor5.fetchone()

            # Calculate next appointment date
            last_pickup_date = my_cursor6.execute(Appointment_Alignment_Scripts.last_refill_date_raw)
            last_refill_date_raw_mysql_result = my_cursor6.fetchone()[0]
            print(f"Fetched data: {last_refill_date_raw_mysql_result},{last_refill_days_mysql_result1}")

            # Getting Drug refill date
            if last_refill_date_raw_mysql_result:  # Check if data is not None
                year, month, day = last_refill_date_raw_mysql_result.year, last_refill_date_raw_mysql_result.month, last_refill_date_raw_mysql_result.day  # Assuming date is the first element (index 0)
                last_pickup_date_convert = date(year, month, day)

            else:
                print("No data found.")
            next_appt = (last_pickup_date_convert) + timedelta(days=last_refill_days_mysql_result1)
            print(f"This is next appointment date {next_appt}")

            # Getting VL date
            last_vl_date = my_cursor7.execute(Appointment_Alignment_Scripts.last_vl_date_raw)
            last_vl_date_raw_mysql_result = my_cursor7.fetchone()[0]
            next_vl_date_ = last_vl_date_raw_mysql_result + timedelta(days=365.25)
            print(f"Fectched VL due date is: {next_vl_date_}")

            current_date = date.today()
            print(f"This is today's date {current_date}")

            pill_balance_cal = next_appt - current_date
            print(pill_balance_cal)
            pill_balance_cal1 = pill_balance_cal.days
            print(pill_balance_cal1)

            bleed_due_days = current_date - last_vl_date_raw_mysql_result
            bleed_alert_days = bleed_due_days.days
            print(f"Bleeding alerto - {bleed_alert_days}")

            range_0_60 = range(0, 61)  # Meaning 0-60

            if my_cursor1:
                my_cursor1.close()
            if my_cursor2:
                my_cursor2.close()
            if my_cursor3:
                my_cursor3.close()
            if my_cursor4:
                my_cursor4.close()
            if my_cursor5:
                my_cursor5.close()
            if my_cursor6:
                my_cursor6.close()
            if my_cursor7:
                my_cursor7.close()
            if my_cursor8:
                my_cursor8.close()
            if my_cursor9:
                my_cursor9.close()
            if my_cursor10:
                my_cursor10.close()


        align_logo = customtkinter.CTkImage(light_image=Image.open(os.path.join(IMAGE_PATH)),
                                            size=(IMAGE_WIDTH, IMAGE_HEIGHT))
        align_logo_label = customtkinter.CTkLabel(self.scrollable_frame, image=align_logo, text='')
        align_logo_label.grid(column=2, row=0, columnspan=2, padx=(0, 2), pady=(0, 0), sticky="w")

    def current_client_details(self, event=None):
        '''
        if self.client_name_label.winfo_exists() or self.last_pickup_label.winfo_exists() or self.last_pickup_duration.winfo_exists() or self.last_vl_date_label.winfo_exists() or self.last_vl_result_label.winfo_exists() or self.last_sample_label.winfo_exists() or self.bleeding_action1.winfo_exists() or self.appointment_sug_date.winfo_exists() or self.pill_balance_label.winfo_exists() or self.suggestionbox.winfo_exists() or self.eac_alert_yuletide_alert.winfo_exists() or self.suggestionbox_header.winfo_exists() or self.suggestionbox.winfo_exists():
            self.client_name_label.grid_forget()
            self.last_pickup_label.grid_forget()
            self.last_pickup_duration.grid_forget()
            self.last_vl_date_label.grid_forget()
            self.last_vl_result_label.grid_forget()
            self.last_sample_label.grid_forget()
            self.bleeding_action1.grid_forget()
            self.appointment_sug_date.grid_forget()
            self.pill_balance_label.grid_forget()
            self.suggestionbox.grid_forget()
            self.eac_alert_yuletide_alert.grid_forget()
            self.suggestionbox_header.grid_forget()
            self.suggestionbox.grid_forget()
        else:
            pass
'''

        ip = self.ip_entry.get()
        try:
            mydb1 = mysql.connector.connect(
                host=ip,
                user="root",
                passwd="Admin123",
                database='openmrs'
            )
            my_cursor1 = mydb1.cursor()
            my_cursor2 = mydb1.cursor()
            my_cursor3 = mydb1.cursor()
            my_cursor4 = mydb1.cursor()
            my_cursor5 = mydb1.cursor()
            my_cursor6 = mydb1.cursor()
            my_cursor7 = mydb1.cursor()
            my_cursor8 = mydb1.cursor()
            my_cursor9 = mydb1.cursor()
            my_cursor10 = mydb1.cursor()
            my_cursor11 = mydb1.cursor()
            my_cursor12 = mydb1.cursor()
            my_cursor13 = mydb1.cursor()
            my_cursor14 = mydb1.cursor()
            my_cursor15 = mydb1.cursor()
            my_cursor16 = mydb1.cursor()
            my_cursor17 = mydb1.cursor()
            my_cursor18 = mydb1.cursor()
            my_cursor19 = mydb1.cursor()
            my_cursor20 = mydb1.cursor()
            my_cursor21 = mydb1.cursor()
            my_cursor22 = mydb1.cursor()
            my_cursor23 = mydb1.cursor()
            my_cursor24 = mydb1.cursor()
            my_cursor25 = mydb1.cursor()
            # my_cursor1.close()
            # mydb1.close()
        except Exception as e:
            messagebox.showinfo('Info', "ERROR: {}".format(e))

        #if self.bulk_search_destroy_top.ids_get_loop is not None:
        #    pepid = self.bulk_search_destroy_top.ids_get_loop
        #else:
        pepid = self.pepid_entry.get()

        get_patient_id = f"SELECT `patient_id` FROM `patient_identifier` WHERE `identifier` = '{pepid}' AND " \
                         f"`voided`=0 and `identifier_type` = 4"
        run_set_patient_id = my_cursor1.execute(get_patient_id)
        result_patient_id1 = my_cursor1.fetchone()
        print(result_patient_id1)

        last_refill_date = my_cursor2.execute(Appointment_Alignment_Scripts.last_refill_date)
        last_refill_date_mysql_result = my_cursor2.fetchone()
        print(last_refill_date_mysql_result)

        last_vl_date1 = my_cursor3.execute(Appointment_Alignment_Scripts.last_vl_date)
        last_vl_date1_mysql_result = my_cursor3.fetchone()

        last_vl_result1 = my_cursor4.execute(Appointment_Alignment_Scripts.last_vl_result)
        last_vl_result1_mysql_result = my_cursor4.fetchone()

        last_sample_date1 = my_cursor5.execute(Appointment_Alignment_Scripts.last_sample_date)
        last_sample_date1_mysql_result = my_cursor5.fetchone()
        print(last_sample_date1_mysql_result)

        if result_patient_id1 is None:
            messagebox.showerror("Client details error!!!",
                                 f"Client with the PEPID: {pepid} not found")

            self.client_name_label.grid_forget()
            self.last_pickup_label.grid_forget()
            self.last_pickup_duration.grid_forget()
            self.last_vl_date_label.grid_forget()
            self.last_vl_result_label.grid_forget()
            self.last_sample_label.grid_forget()
            self.bleeding_action1.grid_forget()
            self.appointment_sug_date.grid_forget()
            self.pill_balance_label.grid_forget()
            self.suggestionbox.grid_forget()
            self.eac_alert_yuletide_alert.grid_forget()
            self.suggestionbox_header.grid_forget()
            self.suggestionbox.grid_forget()
        else:
            current_date1 = date.today()
            get_patient_id = f"SELECT `patient_id` FROM `patient_identifier` WHERE `identifier` = '{pepid}' AND `voided`=0 AND `identifier_type` = 4;"
            run_set_patient_id = my_cursor1.execute(get_patient_id)
            result_patient_id = my_cursor1.fetchone()[0]

            set_patient_id = f"SET @patient_id := '{result_patient_id}'"
            set_patient_id_mysql = my_cursor7.execute(set_patient_id)
            print(set_patient_id_mysql)

            check_tx_new = my_cursor8.execute(Appointment_Alignment_Scripts.tx_new)
            check_tx_new1 = my_cursor8.fetchone()
            if check_tx_new1 is not None:
                check_tx_new1_get = check_tx_new1[0]
                art_start_date_diff = current_date1 - check_tx_new1_get
                art_start_date_days = int(art_start_date_diff.days)
                if art_start_date_days <= 120:
                    messagebox.showinfo("TX_NEW!!!",
                                        f"Client with the PEPID: {pepid} is less than or equals 4 months ({art_start_date_days} day(s)) on ART. \n Please make a decision that best suits this client.")
            else:
                pass

            check_client_discont_status = my_cursor9.execute(Appointment_Alignment_Scripts.client_discontinued)
            check_client_discont_status1 = my_cursor9.fetchone()
            if check_client_discont_status1 is not None:
                check_client_discont_status1_ = check_client_discont_status1[0]
            else:
                check_client_discont_status1_ = ""
            print(f"Discontinued: {check_client_discont_status1}")

            # Execute the SQL script and fetch the result
            check_for_inh_start = my_cursor10.execute(Appointment_Alignment_Scripts.check_ihn_entry)
            check_for_inh_start1 = my_cursor10.fetchone()

            # Check the result and assign the appropriate value to start_client_on_inh
            if check_for_inh_start1 is not None:
                result = check_for_inh_start1[0]  # Assuming the result is in the first column
                if result == 2 or result == 3:
                    start_client_on_inh = "TPT Doc. Gap"
                elif result == 4:
                    start_client_on_inh = "Start client on TPT"
                else:
                    start_client_on_inh = "         "
            else:
                start_client_on_inh = "         "

            # Print the output
            print(f"What do we have on INH alert: {start_client_on_inh}")

            if check_client_discont_status1 is not None:
                messagebox.showinfo("Client Discontinued!!!",
                                    f"Client with the PEPID: {pepid} has '{check_client_discont_status1_}' status.")
                if check_client_discont_status1_ == "Death":
                    if self.client_name_label is not None:
                        self.client_name_label.destroy()
                        self.client_name_label = None
                    if self.art_start_date_label is not None:
                        self.art_start_date_label.destroy()
                        self.art_start_date_label = None
                    if self.last_pickup_label is not None:
                        self.last_pickup_label.destroy()
                        self.last_pickup_label = None
                    if self.last_pickup_duration is not None:
                        self.last_pickup_duration.destroy()
                        self.last_pickup_duration = None
                    if self.last_vl_date_label is not None:
                        self.last_vl_date_label.destroy()
                        self.last_vl_date_label = None
                    if self.last_vl_result_label is not None:
                        self.last_vl_result_label.destroy()
                        self.last_vl_result_label = None
                    if self.last_sample_label is not None:
                        self.last_sample_label.destroy()
                        self.last_sample_label = None
                    if self.bleeding_action1 is not None:
                        self.bleeding_action1.destroy()
                        self.bleeding_action1 = None
                    if self.appointment_sug_date is not None:
                        self.appointment_sug_date.destroy()
                        self.appointment_sug_date = None
                    if self.pill_balance_label is not None:
                        self.pill_balance_label.destroy()
                        self.pill_balance_label = None
                    if self.suggestionbox is not None:
                        self.suggestionbox.destroy()
                        self.suggestionbox = None
                    if self.eac_alert_yuletide_alert is not None:
                        self.eac_alert_yuletide_alert.destroy()
                        self.eac_alert_yuletide_alert = None
                    if self.suggestionbox_header is not None:
                        self.suggestionbox_header.destroy()
                        self.suggestionbox_header = None
                    if self.suggestionbox is not None:
                        self.suggestionbox.destroy()
                        self.suggestionbox = None
                    return



            '''try:
                my_cursor11.fetchall()  # fetch (and discard) remaining rows
            except mysql.connector.errors.InterfaceError as ie:
                if ie.msg == 'No result set to fetch from.':
                    # no problem, we were just at the end of the result set
                    pass
                else:
                    raise
            my_cursor11.execute(Appointment_Alignment_Scripts.client_name)  # OK now'''

            client_name_fetch = my_cursor11.execute(Appointment_Alignment_Scripts.client_name)
            client_name_fetch_mysql_result = my_cursor11.fetchone()[0]


            client_age_fetch = my_cursor12.execute(Appointment_Alignment_Scripts.client_age)
            client_age_fetch_mysql_result = my_cursor12.fetchone()[0]

            art_start_date = my_cursor13.execute(Appointment_Alignment_Scripts.art_start_date)
            art_start_date_mysql_result = my_cursor13.fetchone()
            if art_start_date_mysql_result is not None:
                art_start_date_mysql_result1 = art_start_date_mysql_result[0]
            else:
                art_start_date_mysql_result1 = "No ART Start Date."

            last_vl_date = my_cursor14.execute(Appointment_Alignment_Scripts.last_vl_date)
            last_vl_date_mysql_result = my_cursor14.fetchone()
            if last_vl_date_mysql_result is not None:
                last_vl_date_mysql_result1 = last_vl_date_mysql_result[0]
            else:
                last_vl_date_mysql_result1 = "No VL Date."

            last_vl_result = my_cursor15.execute(Appointment_Alignment_Scripts.last_vl_result)
            last_vl_result_mysql_result = my_cursor15.fetchone()
            if last_vl_result_mysql_result is not None:
                last_vl_result_mysql_result1 = last_vl_result_mysql_result[0]
            else:
                last_vl_result_mysql_result1 = "No VL Result."

            last_sample_date = my_cursor16.execute(Appointment_Alignment_Scripts.last_sample_date)
            last_sample_date_mysql_result = my_cursor16.fetchone()
            if last_sample_date_mysql_result is not None:
                last_sample_date_mysql_result1 = last_sample_date_mysql_result[0]
            else:
                last_sample_date_mysql_result1 = "No Sample Date."

            last_refill_date = my_cursor17.execute(Appointment_Alignment_Scripts.last_refill_date)
            last_refill_date_mysql_result = my_cursor17.fetchone()
            if last_refill_date_mysql_result is not None:
                last_refill_date_mysql_result1 = last_refill_date_mysql_result[0]
            else:
                last_refill_date_mysql_result1 = "No Refill Date."

            last_refill_days = my_cursor18.execute(Appointment_Alignment_Scripts.last_refill_days)
            last_refill_days_mysql_result = my_cursor18.fetchone()
            if last_refill_days_mysql_result is not None:
                last_refill_days_mysql_result1 = last_refill_days_mysql_result[0]
            else:
                last_refill_days_mysql_result1 = "No Refill Qty."

            # Calculate next appointment date
            last_pickup_date = my_cursor19.execute(Appointment_Alignment_Scripts.last_refill_date_raw)
            last_refill_date_raw_mysql_result = my_cursor19.fetchone()[0]
            print(f"Fetched data: {last_refill_date_raw_mysql_result},{last_refill_days_mysql_result1}")
            # Getting Drug refill date
            if last_refill_date_raw_mysql_result:  # Check if data is not None
                year, month, day = last_refill_date_raw_mysql_result.year, last_refill_date_raw_mysql_result.month, last_refill_date_raw_mysql_result.day  # Assuming date is the first element (index 0)
                last_pickup_date_convert = date(year, month, day)
                print(last_pickup_date_convert)
            else:
                print("No data found.")

            if last_refill_days_mysql_result1 is None:
                last_refill_days_mysql_result2 = 0
            else:
                last_refill_days_mysql_result2 = last_refill_days_mysql_result1

            next_appt = (last_pickup_date_convert) + timedelta(days=last_refill_days_mysql_result2)
            print(f"This is next appointment date {next_appt}")
            # Getting VL date
            last_vl_date = my_cursor20.execute(Appointment_Alignment_Scripts.last_vl_date_raw)
            if last_vl_date_mysql_result is not None:
                last_vl_date_raw_mysql_result = my_cursor20.fetchone()[0]
            else:
                last_vl_date_raw_mysql_result = date(1900, 1, 1)

            next_vl_date_ = last_vl_date_raw_mysql_result + timedelta(days=365)
            print(f"Fectched VL due date is: {next_vl_date_}")
            current_date = date.today()
            print(f"This is today's date {current_date}")
            pill_balance_cal = next_appt - current_date
            print(pill_balance_cal)
            pill_balance_cal1 = pill_balance_cal.days
            print(f"Pill bal. is {pill_balance_cal1}")

            bleed_due_days = next_vl_date_ - current_date
            bleed_alert_days = int(bleed_due_days.days)
            print(f"Bleeding days interval - {bleed_alert_days}")
            print(type(bleed_alert_days))

            my_cursor1.fetchall()

            try:
                # Execute the query
                my_cursor21.execute(Appointment_Alignment_Scripts.last_sample_date_raw)

                # Fetch the result
                result = my_cursor21.fetchone()

                # Check if result is not None before accessing it
                if result is not None:
                    last_sample_date_mysql_result_for_cal = result[0]
                else:
                    last_sample_date_mysql_result_for_cal = date(1900, 1, 1)

            except Exception as e:
                # Print the exception for debugging
                print("Error:", e)

            vls_bleed_due_days = current_date - last_sample_date_mysql_result_for_cal
            vls_bleed_alert_days = int(vls_bleed_due_days.days)
            print(f".....................{vls_bleed_alert_days}")

            # range_0_60 = range(-10000, 61)  # Meaning 0-60

            self.client_name_label = customtkinter.CTkLabel(self.clinicdays_frame,
                                                            text=f"{client_name_fetch_mysql_result}      ",
                                                            font=customtkinter.CTkFont(size=14, weight="bold"))
            self.client_name_label.grid(row=11, column=0, padx=2, pady=(1, 1), sticky="w")

            self.art_start_date_label = customtkinter.CTkLabel(self.clinicdays_frame,
                                                               text=f"ART Start Date:  {art_start_date_mysql_result1}  .",
                                                               font=customtkinter.CTkFont(size=13, weight="bold"))
            self.art_start_date_label.grid(row=12, column=0, padx=2, pady=(2, 1), sticky="w")

            self.last_pickup_label = customtkinter.CTkLabel(self.clinicdays_frame,
                                                            text=f"Last drug refill date:  {last_refill_date_mysql_result1}  .",
                                                            font=customtkinter.CTkFont(size=13, slant="italic"))
            self.last_pickup_label.grid(row=13, column=0, padx=2, pady=(2, 1), sticky="w")

            self.last_pickup_duration = customtkinter.CTkLabel(self.clinicdays_frame,
                                                               text=f"Last drug refill duration:  {last_refill_days_mysql_result1}",
                                                               font=customtkinter.CTkFont(size=13, slant="italic"))
            self.last_pickup_duration.grid(row=14, column=0, padx=2, pady=(1, 2), sticky="w")

            self.last_vl_date_label = customtkinter.CTkLabel(self.clinicdays_frame,
                                                             text=f"Last VL Date:  {last_vl_date_mysql_result1}'",
                                                             font=customtkinter.CTkFont(size=13, slant="italic"))
            self.last_vl_date_label.grid(row=15, column=0, padx=2, pady=(5, 0), sticky="w")

            self.last_vl_result_label = customtkinter.CTkLabel(self.clinicdays_frame,
                                                               text=f"Last VL Result:  {last_vl_result_mysql_result1}'",
                                                               font=customtkinter.CTkFont(size=13, slant="italic"))
            self.last_vl_result_label.grid(row=16, column=0, padx=2, pady=(0, 5), sticky="w")

            self.last_sample_label = customtkinter.CTkLabel(self.clinicdays_frame,
                                                            text=f"Last Sample date:  {last_sample_date_mysql_result1}'",
                                                            font=customtkinter.CTkFont(size=14, slant="italic"))
            self.last_sample_label.grid(row=17, column=0, padx=2, pady=(0, 5), sticky="w")

            self.pill_balance_label = customtkinter.CTkLabel(self.clinicdays_frame,
                                                             text=f"Pill Balance: {pill_balance_cal1} Pills",
                                                             font=customtkinter.CTkFont(size=14,
                                                                                        weight="bold"))
            self.pill_balance_label.grid(row=18, column=0, padx=2, pady=(2, 2), sticky="w")

            # self.suggested_appointment_date = customtkinter.CTkLabel(self.clinicdays_frame, text="00-00-0000",
            #                                                          font=customtkinter.CTkFont(size=18, weight="bold"))
            # self.suggested_appointment_date.grid(row=18, column=0, padx=2, pady=(2, 2), sticky="w")
            # self.align_logo_label.config(state="hidden")




            self.checkalert_frame = customtkinter.CTkFrame(self.scrollable_frame, height=70, width=400, fg_color='#B4B4B4')
            self.checkalert_frame.grid(row=2, column=1, padx=(2, 0), pady=2, columnspan=2, sticky="w")
            self.checkalert_frame.grid_propagate(False)

            self.checkalert_frame2 = customtkinter.CTkFrame(self.scrollable_frame, height=70, width=480,  fg_color='#B4B4B4')
            self.checkalert_frame2.grid(row=2, column=3, columnspan=2, padx=2, pady=(2, 0), sticky="w")
            self.checkalert_frame2.grid_propagate(False)

            def is_between_(check_date, start_date, end_date):
                print(start_date <= check_date <= end_date)

            year = current_date.year  # You can change this to any year you want
            year2 = current_date.year + 1  # You can change this to any year you want
            vl_sample_year = current_date.year
            vl_sample_year1 = current_date.year - 1
            # print(f"asfgvsdfbsdfbsdfb ---{year}")

            vls_q1_start_date = date(vl_sample_year1, 10, 1)
            vls_q1_end_date = date(vl_sample_year1, 12, 31)

            vls_q2_start_date = date(vl_sample_year, 1, 1)
            vls_q2_end_date = date(vl_sample_year, 3, 31)

            vls_q3_start_date = date(vl_sample_year, 4, 1)
            vls_q3_end_date = date(vl_sample_year, 6, 30)

            vls_q4_start_date = date(vl_sample_year, 7, 1)
            vls_q4_end_date = date(vl_sample_year, 9, 30)

            q1_start_date = date(year, 10, 1)
            q1_end_date = date(year, 12, 31)

            q2_start_date = date(year, 1, 1)
            q2_end_date = date(year, 3, 31)

            q3_start_date = date(year, 4, 1)
            q3_end_date = date(year, 6, 30)

            q4_start_date = date(year, 7, 1)
            q4_end_date = date(year, 9, 30)

            q1 = q1_start_date <= next_vl_date_ <= q1_end_date
            q2 = q2_start_date <= next_vl_date_ <= q2_end_date
            q3 = q3_start_date <= next_vl_date_ <= q3_end_date
            q4 = q4_start_date <= next_vl_date_ <= q4_end_date

            # q1 = is_between_(next_vl_date_, q1_start_date, q1_end_date)
            # q2 = is_between_(next_vl_date_, q2_start_date, q2_end_date)
            # q3 = is_between_(next_vl_date_, q3_start_date, q3_end_date)
            # q4 = is_between_(next_vl_date_, q4_start_date, q4_end_date)

            print(f"This is Q1........{q1}")
            print(f"This is Q2........{q2}")
            print(f"This is Q3........{q3}")
            print(f"This is Q4........{q4}")

            cur_date_q1 = q1_start_date <= current_date <= q1_end_date
            cur_date_q2 = q2_start_date <= current_date <= q2_end_date
            cur_date_q3 = q3_start_date <= current_date <= q3_end_date
            cur_date_q4 = q4_start_date <= current_date <= q4_end_date

            print(f"This is Q21111........{cur_date_q1}")
            print(f"This is Q21111........{cur_date_q2}")
            print(f"This is Q21111........{cur_date_q3}")
            print(f"This is Q21111........{cur_date_q4}")

            q1_sample = is_between_(last_sample_date_mysql_result_for_cal, vls_q1_start_date, vls_q1_end_date)
            q2_sample = is_between_(last_sample_date_mysql_result_for_cal, vls_q2_start_date, vls_q2_end_date)
            q3_sample = is_between_(last_sample_date_mysql_result_for_cal, vls_q3_start_date, vls_q3_end_date)
            q4_sample = is_between_(last_sample_date_mysql_result_for_cal, vls_q4_start_date, vls_q4_end_date)

            pills_of_90 = 90
            pills_of_120 = 120
            pills_of_150 = 150
            pills_of_180 = 180

            if isinstance(last_vl_result_mysql_result1, int) or isinstance(last_vl_result_mysql_result1, float):
                changed_last_vl_result_to_int = last_vl_result_mysql_result1
            elif isinstance(last_vl_result_mysql_result1, str):
                changed_last_vl_result_to_int = -1
            print(f"nnnnnnnn....{last_vl_result_mysql_result1}")
            print(type(last_vl_result_mysql_result1))

            quick_calc = (next_vl_date_) - (current_date + timedelta(days=90))
            print(f"jjjjjjj: ----- {quick_calc}")

            if int(client_age_fetch_mysql_result) < 19:
                ped_label = "3.    Pediatrics Client!!! Ensure all pediatrics related interventions are factored in. (e.g OVC, OTZ)"

            elif int(client_age_fetch_mysql_result) == 19:
                ped_label = "3.    Pediatrics client/Assess for OTZ enrollment!!! Ensure all pediatrics related interventions are factored in."
            elif 19 < int(client_age_fetch_mysql_result) < 25:
                ped_label = "3.    Assess client for OTZ enrollment!!! Ensure all OTZ related interventions are factored in."
            else:
                ped_label = ""


            if 0 <= vls_bleed_alert_days <= 179 and art_start_date_days >= 180 and last_sample_date_mysql_result_for_cal > last_vl_date_raw_mysql_result:
                bleeding_alert = "Pending VL Result"  # Valid VL Sample
            elif 0 <= vls_bleed_alert_days <= 179 and art_start_date_days >= 180 and int(last_vl_result_mysql_result1) < 1000:
                bleeding_alert = "Pending VL Result"
            elif 120 < art_start_date_days <= 180 and vls_bleed_alert_days < 121 and bleed_alert_days is None:
                bleeding_alert = "BLEED NOW"
            elif 60 < bleed_alert_days <= 90 and (
                    (q1 == True and cur_date_q1 == True) or (q2 == True and cur_date_q2 == True) or (
                    q3 == True and cur_date_q3 == True) or (q4 == True and cur_date_q4 == True)):
                bleeding_alert = "BLEED NOW"
            elif bleed_alert_days <= 60 and art_start_date_days > 180:
                bleeding_alert = "BLEED NOW"
            elif bleed_alert_days is None and art_start_date_days > 180:
                bleeding_alert = "BLEED NOW"

            elif 120 < art_start_date_days <= 180 and vls_bleed_alert_days < 121 and (last_sample_date_mysql_result_for_cal >= last_vl_date_raw_mysql_result) and 60 < bleed_alert_days <= 365:
                bleeding_alert = "VALID VL Result"

            elif 60 < bleed_alert_days <= 365:
                bleeding_alert = "VALID VL Result"

                print(f"bleeding_alert.....{bleeding_alert}")

            else:
                bleeding_alert = "Confirm VL Result"
                print(f"bleeding_alert.....{bleeding_alert}")

            if bleeding_alert == (-365 > pill_balance_cal1) and (
                    bleeding_alert == "BLEED NOW" or bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and art_start_date_days > 180:
                new_next_appt = current_date + timedelta(pills_of_90)  # Force MMD3 for IIT for 1 year and above
            elif (
                    bleeding_alert == "BLEED NOW" or bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and changed_last_vl_result_to_int >= 1000:
                new_next_appt = current_date + timedelta(days=30)
            # new_next_appt = current_date + timedelta(days=30)
            elif (
                    bleeding_alert == "BLEED NOW" or bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and changed_last_vl_result_to_int < 0 and 120 < art_start_date_days <= 180:
                new_next_appt = current_date + timedelta(days=90)
            elif (
                    bleeding_alert == "BLEED NOW" or bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 0 < changed_last_vl_result_to_int < 1000 and art_start_date_days > 180 and (
                    current_date + timedelta(days=pills_of_180)) <= (next_vl_date_):
                new_next_appt = current_date + timedelta(days=180)
            elif (
                    bleeding_alert == "BLEED NOW" or bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and -365 > pill_balance_cal1:
                new_next_appt = current_date + timedelta(days=90)
            elif (
                    bleeding_alert == "BLEED NOW" or bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 30 < art_start_date_days <= 120:
                new_next_appt = current_date + timedelta(days=90)
            elif bleeding_alert == "BLEED NOW":
                new_next_appt = current_date + timedelta(days=180)
            elif bleeding_alert == "BLEED NOW" and -365 < pill_balance_cal1:
                new_next_appt = current_date + timedelta(days=pills_of_180)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and bleed_alert_days <= 90 and (
                    (current_date + timedelta(days=90)) <= (next_vl_date_)) == True:
                new_next_appt = current_date + timedelta(days=pills_of_90)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and bleed_alert_days <= 90 and (
                    (current_date + timedelta(days=90)) <= (next_vl_date_)) == False and vls_bleed_alert_days >= 180:
                new_next_appt = current_date + timedelta(days=bleed_alert_days)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and bleed_alert_days <= 90 and (
                    (current_date + timedelta(days=90)) <= (
            next_vl_date_)) == False and 0 < vls_bleed_alert_days <= 179:
                new_next_appt = current_date + timedelta(days=90)

            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 90 < bleed_alert_days <= 100 and (
                    (current_date + timedelta(days=100)) <= (next_vl_date_)) == True:
                new_next_appt = current_date + timedelta(days=100)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 90 < bleed_alert_days <= 100 and (
                    (current_date + timedelta(days=100)) <= (next_vl_date_)) == False and vls_bleed_alert_days >= 180:
                new_next_appt = current_date + timedelta(days=bleed_alert_days)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 90 < bleed_alert_days <= 100 and (
                    (current_date + timedelta(days=100)) <= (
            next_vl_date_)) == False and 0 < vls_bleed_alert_days <= 179:
                new_next_appt = current_date + timedelta(days=100)

            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 100 < bleed_alert_days <= 110 and (
                    (current_date + timedelta(days=110)) <= (next_vl_date_)) == True:
                new_next_appt = current_date + timedelta(days=110)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 100 < bleed_alert_days <= 110 and (
                    (current_date + timedelta(days=110)) <= (next_vl_date_)) == False and vls_bleed_alert_days >= 180:
                new_next_appt = current_date + timedelta(days=bleed_alert_days)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 100 < bleed_alert_days <= 110 and (
                    (current_date + timedelta(days=110)) <= (
            next_vl_date_)) == False and 0 < vls_bleed_alert_days <= 179:
                new_next_appt = current_date + timedelta(days=110)

            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 110 < bleed_alert_days <= 115 and (
                    (current_date + timedelta(days=115)) <= (next_vl_date_)) == True:
                new_next_appt = current_date + timedelta(days=115)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 110 < bleed_alert_days <= 115 and (
                    (current_date + timedelta(days=115)) <= (next_vl_date_)) == False and vls_bleed_alert_days >= 180:
                new_next_appt = current_date + timedelta(days=bleed_alert_days)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 110 < bleed_alert_days <= 115 and (
                    (current_date + timedelta(days=115)) <= (
            next_vl_date_)) == False and 0 < vls_bleed_alert_days <= 179:
                new_next_appt = current_date + timedelta(days=115)

            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 115 < bleed_alert_days <= 120 and (
                    (current_date + timedelta(days=120)) <= (next_vl_date_)) == True:
                new_next_appt = current_date + timedelta(days=pills_of_120)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 115 < bleed_alert_days <= 120 and (
                    (current_date + timedelta(days=120)) <= (next_vl_date_)) == False and vls_bleed_alert_days >= 180:
                new_next_appt = current_date + timedelta(days=bleed_alert_days)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 115 < bleed_alert_days <= 120 and (
                    (current_date + timedelta(days=120)) <= (
            next_vl_date_)) == False and 0 < vls_bleed_alert_days <= 179:
                new_next_appt = current_date + timedelta(days=120)

            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 120 < bleed_alert_days <= 125 and (
                    (current_date + timedelta(days=135)) <= (next_vl_date_)) == True:
                new_next_appt = current_date + timedelta(days=125)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 120 < bleed_alert_days <= 125 and (
                    (current_date + timedelta(days=135)) <= (next_vl_date_)) == False and vls_bleed_alert_days >= 180:
                new_next_appt = current_date + timedelta(days=bleed_alert_days)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 120 < bleed_alert_days <= 125 and (
                    (current_date + timedelta(days=135)) <= (
            next_vl_date_)) == False and 0 < vls_bleed_alert_days <= 179:
                new_next_appt = current_date + timedelta(days=125)

            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 125 < bleed_alert_days <= 130 and (
                    (current_date + timedelta(days=130)) <= (next_vl_date_)) == True:
                new_next_appt = current_date + timedelta(days=130)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 125 < bleed_alert_days <= 130 and (
                    (current_date + timedelta(days=130)) <= (next_vl_date_)) == False and vls_bleed_alert_days >= 180:
                new_next_appt = current_date + timedelta(days=bleed_alert_days)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 125 < bleed_alert_days <= 130 and (
                    (current_date + timedelta(days=130)) <= (
            next_vl_date_)) == False and 0 < vls_bleed_alert_days <= 179:
                new_next_appt = current_date + timedelta(days=130)

            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 130 < bleed_alert_days <= 135 and (
                    (current_date + timedelta(days=135)) <= (next_vl_date_)) == True:
                new_next_appt = current_date + timedelta(days=135)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 130 < bleed_alert_days <= 135 and (
                    (current_date + timedelta(days=135)) <= (next_vl_date_)) == False and vls_bleed_alert_days >= 180:
                new_next_appt = current_date + timedelta(days=bleed_alert_days)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 130 < bleed_alert_days <= 135 and (
                    (current_date + timedelta(days=135)) <= (
            next_vl_date_)) == False and 0 < vls_bleed_alert_days <= 179:
                new_next_appt = current_date + timedelta(days=135)

            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 135 < bleed_alert_days <= 140 and (
                    (current_date + timedelta(days=140)) <= (next_vl_date_)) == True:
                new_next_appt = current_date + timedelta(days=140)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 135 < bleed_alert_days <= 140 and (
                    (current_date + timedelta(days=140)) <= (next_vl_date_)) == False and vls_bleed_alert_days >= 180:
                new_next_appt = current_date + timedelta(days=bleed_alert_days)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 135 < bleed_alert_days <= 140 and (
                    (current_date + timedelta(days=140)) <= (
            next_vl_date_)) == False and 0 < vls_bleed_alert_days <= 179:
                new_next_appt = current_date + timedelta(days=140)

            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 140 < bleed_alert_days <= 145 and (
                    (current_date + timedelta(days=145)) <= (next_vl_date_)) == True:
                new_next_appt = current_date + timedelta(days=145)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 140 < bleed_alert_days <= 145 and (
                    (current_date + timedelta(days=145)) <= (next_vl_date_)) == False and vls_bleed_alert_days >= 180:
                new_next_appt = current_date + timedelta(days=bleed_alert_days)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 140 < bleed_alert_days <= 145 and (
                    (current_date + timedelta(days=145)) <= (
            next_vl_date_)) == False and 0 < vls_bleed_alert_days <= 179:
                new_next_appt = current_date + timedelta(days=145)

            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 145 < bleed_alert_days <= 150 and (
                    (current_date + timedelta(days=150)) <= (next_vl_date_)) == True:
                new_next_appt = current_date + timedelta(days=pills_of_150)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 145 < bleed_alert_days <= 150 and (
                    (current_date + timedelta(days=150)) <= (next_vl_date_)) == False and vls_bleed_alert_days >= 180:
                new_next_appt = current_date + timedelta(days=bleed_alert_days)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 145 < bleed_alert_days <= 150 and (
                    (current_date + timedelta(days=150)) <= (
            next_vl_date_)) == False and 0 < vls_bleed_alert_days <= 179:
                new_next_appt = current_date + timedelta(days=150)

            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 150 < bleed_alert_days <= 155 and (
                    (current_date + timedelta(days=155)) <= (next_vl_date_)) == True:
                new_next_appt = current_date + timedelta(days=155)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 150 < bleed_alert_days <= 155 and (
                    (current_date + timedelta(days=155)) <= (next_vl_date_)) == False and vls_bleed_alert_days >= 180:
                new_next_appt = current_date + timedelta(days=bleed_alert_days)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 150 < bleed_alert_days <= 155 and (
                    (current_date + timedelta(days=155)) <= (
            next_vl_date_)) == False and 0 < vls_bleed_alert_days <= 179:
                new_next_appt = current_date + timedelta(days=155)

            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 155 < bleed_alert_days <= 160 and (
                    (current_date + timedelta(days=160)) <= (next_vl_date_)) == True:
                new_next_appt = current_date + timedelta(days=160)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 155 < bleed_alert_days <= 160 and (
                    (current_date + timedelta(days=160)) <= (next_vl_date_)) == False and vls_bleed_alert_days >= 180:
                new_next_appt = current_date + timedelta(days=bleed_alert_days)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 155 < bleed_alert_days <= 160 and (
                    (current_date + timedelta(days=160)) <= (
            next_vl_date_)) == False and 0 < vls_bleed_alert_days <= 179:
                new_next_appt = current_date + timedelta(days=160)

            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 160 < bleed_alert_days <= 165 and (
                    (current_date + timedelta(days=165)) <= (next_vl_date_)) == True:
                new_next_appt = current_date + timedelta(days=165)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 160 < bleed_alert_days <= 165 and (
                    (current_date + timedelta(days=165)) <= (next_vl_date_)) == False and vls_bleed_alert_days >= 180:
                new_next_appt = current_date + timedelta(days=bleed_alert_days)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 160 < bleed_alert_days <= 165 and (
                    (current_date + timedelta(days=165)) <= (
            next_vl_date_)) == False and 0 < vls_bleed_alert_days <= 179:
                new_next_appt = current_date + timedelta(days=165)

            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 165 < bleed_alert_days <= 170 and (
                    (current_date + timedelta(days=170)) <= (next_vl_date_)) == True:
                new_next_appt = current_date + timedelta(days=170)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 165 < bleed_alert_days <= 170 and (
                    (current_date + timedelta(days=170)) <= (next_vl_date_)) == False and vls_bleed_alert_days >= 180:
                new_next_appt = current_date + timedelta(days=bleed_alert_days)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 165 < bleed_alert_days <= 170 and (
                    (current_date + timedelta(days=170)) <= (
            next_vl_date_)) == False and 0 < vls_bleed_alert_days <= 179:
                new_next_appt = current_date + timedelta(days=170)

            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 170 < bleed_alert_days <= 175 and (
                    (current_date + timedelta(days=175)) <= (next_vl_date_)) == True:
                new_next_appt = current_date + timedelta(days=175)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 170 < bleed_alert_days <= 175 and (
                    (current_date + timedelta(days=175)) <= (next_vl_date_)) == False and vls_bleed_alert_days >= 180:
                new_next_appt = current_date + timedelta(days=bleed_alert_days)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 170 < bleed_alert_days <= 175 and (
                    (current_date + timedelta(days=175)) <= (
            next_vl_date_)) == False and 0 < vls_bleed_alert_days <= 179:
                new_next_appt = current_date + timedelta(days=175)

            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 175 < bleed_alert_days <= 180 and (
                    (current_date + timedelta(days=pills_of_180)) <= (next_vl_date_)) == True:
                new_next_appt = current_date + timedelta(days=pills_of_180)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 175 < bleed_alert_days <= 180 and (
                    (current_date + timedelta(days=pills_of_180)) <= (
            next_vl_date_)) == False and vls_bleed_alert_days >= 180:
                new_next_appt = current_date + timedelta(days=bleed_alert_days)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and 175 < bleed_alert_days <= 180 and (
                    (current_date + timedelta(days=pills_of_180)) <= (
            next_vl_date_)) == False and 0 < vls_bleed_alert_days <= 179:
                new_next_appt = current_date + timedelta(days=bleed_alert_days)


            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and bleed_alert_days > 180 and (
                    (current_date + timedelta(days=pills_of_180)) <= (next_vl_date_)) == True:
                new_next_appt = current_date + timedelta(days=pills_of_180)
            elif (
                    bleeding_alert == "Pending VL Result" or bleeding_alert == "VALID VL Result" or bleeding_alert == "Confirm VL Result") and bleed_alert_days > 180 and (
                    (current_date + timedelta(days=pills_of_180)) <= (next_vl_date_)) == False:
                new_next_appt = current_date + timedelta(days=pills_of_180)

            print(f"oooooooooooooopoooooooooooo - {new_next_appt}")

            '''           elif 60 < bleed_alert_days <= 90:
                new_next_appt = current_date + timedelta(days=pills_of_90)
            elif 90 < bleed_alert_days <= 120:
                new_next_appt = current_date + timedelta(days=pills_of_120)
            elif 120 < bleed_alert_days <= 150:
                new_next_appt = current_date + timedelta(days=pills_of_150)
            elif 120 < bleed_alert_days <= 180:
                new_next_appt = current_date + timedelta(days=pills_of_180)
            elif 180 < bleed_alert_days:
                new_next_appt = current_date + timedelta(days=pills_of_180)
            if bleed_alert_days <= 60:
                total_pills_dispense = 60
            elif 60 < bleed_alert_days <= 90:
                total_pills_dispense = 90
            elif 90 < bleed_alert_days <= 120:
                total_pills_dispense = 120
            elif 120 < bleed_alert_days <= 150:
                total_pills_dispense = 120
            elif 120 < bleed_alert_days <= 180:
                total_pills_dispense = 180
            elif 180 < bleed_alert_days:
                total_pills_dispense = 180
'''
            total_pills_dispense1 = new_next_appt - current_date
            total_pills_dispense = int(total_pills_dispense1.days)
            # Define the desired format string
            date_format_string = "%d-%m-%Y"
            date_format_string__ = "%Y-%m-%d"

            new_next_appt1 = new_next_appt.strftime(date_format_string)

            # Pill balance alternative in KEY NOTE
            if 1 > pill_balance_cal1:
                pill_balance_cal1_alt = 0
            else:
                pill_balance_cal1_alt = pill_balance_cal1

            # Convert date to 'Saturday, 2nd November 2024'
            def format_date_detailed(new_next_appt):
                """Formats a datetime object to include day of the week, ordinal suffix, and full month name."""
                # Get day of the week (0=Monday)
                day_of_week = new_next_appt.strftime("%A")  # Full day name (Monday-Sunday)
                day_number = new_next_appt.day

                # Define suffixes for dates (1st, 2nd, 3rd, etc.)
                suffixes = ["st", "nd", "rd", "th"]

                # Handle special cases for 11, 12, and 13
                if 11 <= day_number <= 13:
                    suffix = "th"
                else:
                    suffix = suffixes[day_number % 5 - 1]

                # Get full month name and formatted date
                month_name = new_next_appt.strftime("%B")  # Full month name (January-December)
                new_next_appt2 = f"{day_of_week} {month_name} {day_number}, {new_next_appt.year}"

                return new_next_appt2

            new_next_appt3 = format_date_detailed(new_next_appt)

            print(new_next_appt3)

            print(type(bleed_alert_days))

            # Combining selected clinic days
            combination = [self.checkboxmonday_var.get(), self.checkboxtuesday_var.get(),
                           self.checkboxwednesday_var.get(), self.checkboxthursday_var.get(),
                           self.checkboxfriday_var.get(), self.checkboxsaturday_var.get(),
                           self.checkboxsunday_var.get()]

            # Days of the week
            days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

            # Identify checked days
            checked_days = [day for day, state in zip(days_of_week, combination) if state == "on"]

            # Print the checked days
            print("Checked days:", checked_days)
            day_of_week = new_next_appt.strftime("%A")
            print(day_of_week)

            '''if day_of_week in checked_days:
                new_next_appt
                print(new_next_appt)
            else:
                new_next_appt - timedelta(days=1)'''

            # Define the initial date
            initial_date = new_next_appt  # Example initial date

            # Define the list of days of the week to check for
            days_to_check = checked_days

            # Define the initial day of the week for the initial date
            initial_day_of_week = initial_date.strftime('%A')

            # Initialize the result variable to store the final date
            result_date = initial_date

            # Loop until the resulting date falls on one of the specified days
            while result_date.strftime('%A') not in days_to_check:
                # Deduct one day from the current result date
                result_date -= timedelta(days=1)

            def is_between_2(check_date, start_date, end_date):
                print(check_date >= start_date <= end_date)

            yuletide_Start = date(year, 12, 15)
            yuletide_end = date(year2, 1, 15)

            print("kkkkkkkkkkkkkkkkkkkkkkkkkk")
            print(type(result_date))

            easter_period_start = date(year, 3, 20)
            easter_period_end = date(year, 4, 24)

            workers_day = date(year, 5, 1)
            democracy_day = date(year, 5, 29)
            Independence_day = date(year, 10, 1)

            # Print the final date
            print("Resulting Date:", result_date)
            clinic_days_based_date = result_date.strftime(date_format_string)

            yuletide_check = yuletide_Start <= result_date <= yuletide_end
            easter_day_check = easter_period_start <= result_date <= easter_period_end
            workers_day_check = workers_day = result_date
            democracy_day_check = democracy_day = result_date
            Independence_day_check = Independence_day = result_date

            print(yuletide_check)
            print(f"resulttttttttttttttttttttttttttttt: {yuletide_check}")

            # result_date__ = result_date.strftime(date_format_string__)
            # yuletide_Start__ = yuletide_Start.strftime(date_format_string__)
            # yuletide_end__ = yuletide_end.strftime(date_format_string__)

            '''result_date__1 = result_date[:4]
            result_date__2 = result_date[5:7]
            result_date__3 = result_date[-2:]

            result_date___ = date(result_date__1, result_date__2, result_date__3)

            yuletide_Start__ = str(yuletide_Start)
            yuletide_end__ = str(yuletide_end)

            #result_date___ = datetime.strptime(result_date__, '%Y-%m-%d').date()
            yuletide_Start___ = datetime.strptime(yuletide_Start__, '%Y-%m-%d').date()
            yuletide_end___ = datetime.strptime(yuletide_end__, '%Y-%m-%d').date()

            print((f"{result_date___}"))
            print(type(f"{yuletide_Start___}"))
            print(type(f"{yuletide_end___}"))'''

            def format_clinic_days_based_nxt_appt(result_date):
                """Formats a datetime object to include day of the week, ordinal suffix, and full month name."""
                # Get day of the week (0=Monday)
                day_of_week = result_date.strftime("%A")  # Full day name (Monday-Sunday)
                day_number = result_date.day

                # Define suffixes for dates (1st, 2nd, 3rd, etc.)
                suffixes = ["st", "nd", "rd", "th"]

                # Handle special cases for 11, 12, and 13
                if 11 <= day_number <= 13:
                    suffix = "th"
                else:
                    suffix = suffixes[day_number % 5 - 1]

                # Get full month name and formatted date
                month_name = result_date.strftime("%B")  # Full month name (January-December)
                result_date2 = f"{day_of_week} {month_name} {day_number}, {new_next_appt.year}"

                return result_date2

            result_date3 = format_clinic_days_based_nxt_appt(result_date)

            # Determine text color based on the condition
            if bleeding_alert == "VALID VL Result":
                text_color = "green"
            elif bleeding_alert == "Pending VL Result":
                text_color = "orange"
            else:
                text_color = "red"

            self.bleeding_action = customtkinter.CTkLabel(master=self.checkalert_frame, text="Bleeding action:",
                                                          font=customtkinter.CTkFont(size=14),
                                                          text_color="blue")
            self.bleeding_action.grid(row=0, column=1, padx=2, pady=(2, 1), sticky="w")

            self.bleeding_action1 = customtkinter.CTkLabel(master=self.checkalert_frame, text=f"{bleeding_alert}",
                                                           font=customtkinter.CTkFont(size=20, weight="bold"),
                                                           text_color=text_color)
            self.bleeding_action1.grid(row=1, column=1, padx=2, pady=(2, 1), sticky="w")

            self.appointment_sug = customtkinter.CTkLabel(master=self.checkalert_frame2,
                                                          text="Suggested Appointment Date:",
                                                          font=customtkinter.CTkFont(size=14, weight="bold"))
            self.appointment_sug.grid(row=0, column=2, padx=(2, 0), pady=(2, 1), sticky="w")

            self.appointment_sug_date = customtkinter.CTkLabel(master=self.checkalert_frame2,
                                                               text=f"{clinic_days_based_date} ({result_date3})",
                                                               font=customtkinter.CTkFont(size=20, weight="bold"))
            self.appointment_sug_date.grid(row=1, column=2, padx=(2, 0), pady=(2, 1), sticky="w")

            # create textbox
            total_pills_dispense__ = total_pills_dispense1
            total_pills_dispense__1 = total_pills_dispense__.total_seconds()

            # Convert total seconds to integer
            total_pills_dispense__2 = int(total_pills_dispense__1)
            total_pills_dispense__3 = total_pills_dispense__2 / 86400
            pill_balance_cal1__ = (pill_balance_cal1)

            dispense_quantity = total_pills_dispense - pill_balance_cal1_alt

            if last_vl_result_mysql_result1 is not None:
                try:
                    # Attempt conversion to integer
                    last_vl_result_int = int(last_vl_result_mysql_result1)
                    if last_vl_result_int >= 1000 and pill_balance_cal1 < 0:
                        dispense_quantity = 30
                except ValueError:
                    # Handle the case where conversion fails (e.g., print message)
                    print("Invalid value encountered for last_vl_result_mysql_result1")
            elif last_vl_result_mysql_result1 is not None:
                try:
                    # Attempt conversion to integer
                    last_vl_result_int = int(last_vl_result_mysql_result1)
                    if last_vl_result_int >= 1000 and 0 <= pill_balance_cal1 <= 20:
                        dispense_quantity = 30 - pill_balance_cal1
                except ValueError:
                    # Handle the case where conversion fails (e.g., print message)
                    print("Invalid value encountered for last_vl_result_mysql_result1")
            elif last_vl_result_mysql_result1 is not None:
                try:
                    # Attempt conversion to integer
                    last_vl_result_int = int(last_vl_result_mysql_result1)
                    if last_vl_result_int >= 1000 and pill_balance_cal1 > 20:
                        dispense_quantity = 0
                except ValueError:
                    # Handle the case where conversion fails (e.g., print message)
                    print("Invalid value encountered for last_vl_result_mysql_result1")
            elif pill_balance_cal1 > 0:
                dispense_quantity = total_pills_dispense - pill_balance_cal1_alt
            else:
                dispense_quantity = total_pills_dispense - pill_balance_cal1_alt

            print(type(total_pills_dispense1))
            print(type(pill_balance_cal1))
            print(total_pills_dispense1)
            print(pill_balance_cal1__)
            # print(dispense_quantity)

            print(type(last_vl_result_mysql_result1))

            if last_vl_result_mysql_result1 == "No VL Result.":
                eac_alert_text = ""
            elif int(last_vl_result_mysql_result1) >= 1000 and art_start_date_days > 180:
                eac_alert_text = "Assess Client for EAC"
            elif int(last_vl_result_mysql_result1) >= 1000 and art_start_date_days < 180:
                eac_alert_text = "Suspected Unpressed Baseline VL Result"
            elif int(last_vl_result_mysql_result1) >= 1000 and art_start_date_days > 180:
                eac_alert_text = "Assess Client for EAC"
            elif 50 <= int(last_vl_result_mysql_result1) <= 999 and art_start_date_days > 180:
                eac_alert_text = "Low-Level Viremia (LLV)"
            elif 50 >= int(last_vl_result_mysql_result1) <= 999 and art_start_date_days < 180:
                eac_alert_text = "Suspected LLV Baseline VL Result"
            else:
                eac_alert_text = ""

            # result_date__ = datetime.strftime(result_date, 'Y%-%m-%d').date()
            # yuletide_Start__ = datetime.strftime(yuletide_Start, 'Y%-%m-%d').date()
            # yuletide_end__ = datetime.strftime(yuletide_end, 'Y%-%m-%d').date()

            # result_date__ = (result_date)
            # yuletide_Start__ = (yuletide_Start)
            # yuletide_end__ = (yuletide_end)

            if yuletide_check == True:
                yuletide_alert_text = "YULETIDE PERIOD APPOINTMENT"
            elif easter_day_check == True:
                yuletide_alert_text = "Possible Easter Period Flag"
            elif workers_day_check == True:
                yuletide_alert_text = "Workers' Day Flag"
            elif democracy_day_check == True:
                yuletide_alert_text = "Democracy Day Flag"
            elif Independence_day_check == True:
                yuletide_alert_text = "Independence Day Flag"
            else:
                yuletide_alert_text = ""


            if int(client_age_fetch_mysql_result) < 19:
                client_age_text = "Pediatrics Client"
            elif int(client_age_fetch_mysql_result) == 19:
                client_age_text = "Pediatrics/Assess for OTZ"
            elif 19 < int(client_age_fetch_mysql_result) < 25:
                client_age_text = "Assess for OTZ"
            else:
                client_age_text = ""



            # Initialize a list to hold multiple notes for force_mmd3_for_iit_1_yr_above
            force_mmd3_notes = []

            # Evaluate each condition for force_mmd3_for_iit_1_yr_above and append the appropriate message
            if -366 > pill_balance_cal1 and not (
                    0 <= vls_bleed_alert_days <= 179 or last_vl_date_raw_mysql_result < last_sample_date_mysql_result_for_cal):
                force_mmd3_notes.append("Note: MMD3 is recommended for IIT client(s) for a year and above.")

            if changed_last_vl_result_to_int >= 1000:
                force_mmd3_notes.append("Note: One month refill is recommended for EAC clients.")

            if 0 <= vls_bleed_alert_days <= 179 and last_vl_date_raw_mysql_result < last_sample_date_mysql_result_for_cal:
                force_mmd3_notes.append(
                    f"Note: There is a pending VL result of a sample collected {vls_bleed_alert_days} days ago.")

            if 0 <= vls_bleed_alert_days <= 179 and -365 > pill_balance_cal1:
                force_mmd3_notes.append(
                    f"Note: 1. There is a pending VL result of a sample collected {vls_bleed_alert_days} days ago.\n"
                    f"2. MMD3 is recommended for IIT client(s) for a year and above.")

            if 0 <= vls_bleed_alert_days <= 179 and -365 > pill_balance_cal1 and last_vl_date_raw_mysql_result < last_sample_date_mysql_result_for_cal:
                force_mmd3_notes.append(
                    f"Note: 1. There is a pending VL result of a sample collected {vls_bleed_alert_days} days ago.\n"
                    f"2. MMD3 is recommended for IIT client(s) for a year and above.\n"
                    f"3. Pending VL result is yet to be updated in the system.")

            check_for_inh_start = my_cursor10.execute(Appointment_Alignment_Scripts.check_ihn_entry)
            check_for_inh_start1 = my_cursor10.fetchone()

            # Check the result and assign the appropriate value to start_client_on_inh
            if check_for_inh_start1 is not None:
                result = check_for_inh_start1[0]  # Assuming the result is in the first column
                if result == 2:
                    force_mmd3_notes.append("   **** Isoniazid is documented on the Pharmacy form, but not on the TPT form.")
                elif result == 3:
                    force_mmd3_notes.append("   **** TPT form documented, but not pharmacy.")

            # Combine all the notes into a single string, or set to an empty string if no notes were added
            force_mmd3_for_iit_1_yr_above = "\n".join(force_mmd3_notes) if force_mmd3_notes else ""

            # Print the final result
            print(f"Force MMD3 for IIT 1 year and above notes:\n{force_mmd3_for_iit_1_yr_above}")



            self.yuletide_alert_frame2 = customtkinter.CTkFrame(self.scrollable_frame, height=70, width=865, fg_color='#F3F3F3')
            self.yuletide_alert_frame2.grid(row=1, column=1, columnspan=4, padx=(2, 0), pady=2, sticky="w")
            #self.yuletide_alert_frame2.configure(background='black')
            self.yuletide_alert_frame2.grid_propagate(False)


            self.eac_alert_yuletide_alert = customtkinter.CTkLabel(master=self.yuletide_alert_frame2,
                                                                   text=f"- {eac_alert_text} - {yuletide_alert_text} - {client_age_text} - {start_client_on_inh}",
                                                                   width=250,
                                                                   font=customtkinter.CTkFont(size=21, weight="bold"),
                                                                   text_color="red", anchor="w", justify="center")
            self.eac_alert_yuletide_alert.grid(row=1, column=1, padx=10, pady=(20, 1), columnspan=3, sticky="w")

            # self.yuletide_alert = customtkinter.CTkLabel(self,
            #                                             text=f"{yuletide_alert_text}",
            #                                             width=250,
            #                                             font=customtkinter.CTkFont(size=20, weight="bold"),
            #                                             text_color="red")
            # self.yuletide_alert.grid(row=4, column=1, padx=(0, 10), pady=(1, 1), sticky="w")

            self.key_note_frame = customtkinter.CTkFrame(self.scrollable_frame, height=280, width=865)
            self.key_note_frame.grid(row=4, column=1, columnspan=4, padx=(5, 0), pady=2, sticky="w")
            # self.yuletide_alert_frame2.configure(background='black')
            self.key_note_frame.grid_propagate(False)


            self.suggestionbox_header = customtkinter.CTkLabel(master=self.key_note_frame,
                                                               text="KEY NOTES (Appointment suggestion considerations)",
                                                               width=250,
                                                               font=customtkinter.CTkFont(size=15, weight="bold"))
            self.suggestionbox_header.grid(row=1, column=1, columnspan=4, padx=(5, 0), pady=2, sticky="w")

            Total_pills = dispense_quantity + pill_balance_cal1_alt
            # suggestionbo_formatted_text = f"1.   Dispense {dispense_quantity} pill(s) - ({pill_balance_cal1_alt}
            # pill(s) still with client from previous refill. {Total_pills} in total).\n2.   The aligned next
            # appointment date is {new_next_appt1} ({new_next_appt3}) the suggested date is based on\n       the
            # clinic days specified.\n{ped_label}\n\n\n\n{force_mmd3_for_iit_1_yr_above} "
            suggestionbo_formatted_text = f"1.   Dispense for {dispense_quantity} day(s) to makeup {Total_pills} day" \
                                          f").\n2.   The aligned next appointment date is based on the clinic days " \
                                          f"specified.\n{ped_label}\n\n\n\n{force_mmd3_for_iit_1_yr_above} "
            suggestionbo_formatted_text2 = f"1.   Dispense for {dispense_quantity} day(s) to makeup {Total_pills} days refill)."

            self.suggestionbox = customtkinter.CTkLabel(master=self.key_note_frame, text=suggestionbo_formatted_text, width=250,
                                                        justify="left",
                                                        font=customtkinter.CTkFont(size=15))
            self.suggestionbox.grid(row=5, column=1, padx=(10, 10), pady=(1, 1), columnspan=2, sticky="w")

            # suggestionbo_formatted_text = f"3.   The aligned next appointment date is {new_next_appt1} ({new_next_appt3}) the suggested date is based on\n the clinic days specified."

            # suggestionbox_formatted_text = f"<span>{suggestionbo_formatted_text.replace(pill_balance_cal1, f'<b>{pill_balance_cal1}</b>')}</span>"
            # self.suggestionbox.insert("0.0",
            #                        "APPOINTMENT SUGGESTION\n\n" + f"1.   Discount the client's {pill_balance_cal1} left over pills from the {total_pills_dispense} days dispense as suggested.")

            def add_column_if_not_exists(cursor, table_name, column_name, column_definition):
                # Check if the column exists
                cursor.execute(f"""
                SELECT COUNT(*)
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_SCHEMA = 'appt_alignment_log'
                AND TABLE_NAME = '{table_name}'
                AND COLUMN_NAME = '{column_name}'
                """)

                if cursor.fetchone()[0] == 0:
                    # Column does not exist, so add it
                    try:
                        cursor.execute(f"""
                        ALTER TABLE `appt_alignment_log`.`{table_name}`
                        ADD COLUMN {column_name} {column_definition}
                        """)
                        print(f"Column {column_name} added successfully.")
                    except Exception as e:
                        print(f"Error adding column {column_name}: {e}")
                else:
                    print(f"Column {column_name} already exists.")



            ip = self.ip_entry.get()
            try:
                # Connection to create line-list db
                mydb2 = mysql.connector.connect(
                    host=ip,
                    user="root",
                    passwd="Admin123"
                )

                my_cursor2 = mydb2.cursor()

                # Create db
                my_cursor2.execute("CREATE DATABASE IF NOT EXISTS appt_alignment_log")
                my_cursor2.execute("CREATE TABLE IF NOT EXISTS appt_alignment_log.`appt_alignment_log_tab2` (\
                `State` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `SurgeCommand` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `LGA` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Datim_code` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Facility_name` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Pepid_Datim_code` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Patient_Id` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Pepid` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Client_Bio` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Last_Pickup_Date` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Duration_Last_Pickup` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Pill_Balance` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Last_VL_Date` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Last_VL_Result` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Additional_Service_Alert` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Bleeding_Alert` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL, \
                `Suggested_Next_Appt_Date` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Suggested_Next_Appt_Day` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Actual_Suggested_Next_Appt_Date` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Actual_Suggested_Next_Appt_Day` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Key_Note` LONGTEXT CHARACTER SET utf8 DEFAULT NULL,\
                `Search_Timestamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

                add_column_if_not_exists(my_cursor2, 'appt_alignment_log_tab2', 'Type_of_search',
                                         'VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL')

            except Exception as e:
                messagebox.showinfo('Info', "ERROR: {}".format(e))

            bulk_button_state = self.bulk_search_button.cget("state")
            print(f"sweedilido: {bulk_button_state}")


            # get yes/no answers
            if bulk_button_state == "normal":
                msg = CTkMessagebox(title="Attention!!!",
                                message="Is the client present on-site or service through DSD model?",
                                icon="question", option_1="Cancel", option_2="No", option_3="Yes")
            else:
                pass

            if bulk_button_state == "disabled":
                response = "Yes"
                search_type = "Bulk search"
            else:
                response = msg.get()
                search_type = "Single search"

            if response == "Yes":
                insert_searched_client = f"INSERT INTO `appt_alignment_log`.`appt_alignment_log_tab2` (`State`, " \
                                         f"`SurgeCommand`, `LGA`, `Datim_code`, `Facility_name`, `Pepid_Datim_code`, " \
                                         f"`Patient_Id`, `Pepid`, `Client_Bio`, `Last_Pickup_Date`, " \
                                         f"`Duration_Last_Pickup`, `Pill_Balance`, `Last_VL_Date`, " \
                                         f"`Last_VL_Result`, `Additional_Service_Alert`, `Bleeding_Alert`, `Suggested_Next_Appt_Date`, " \
                                         f"`Suggested_Next_Appt_Day`, `Actual_Suggested_Next_Appt_Date`, " \
                                         f"`Actual_Suggested_Next_Appt_Day`, `Key_Note`, `Type_of_search`) " \
                                         f"VALUES ((SELECT State FROM `openmrs`.CIHP_ListOfFacility WHERE Datim_Code = (" \
                                         f"SELECT `property_value` FROM `openmrs`.`global_property` WHERE `property`= " \
                                         f"'facility_datim_code')LIMIT 1), (SELECT SurgeCommand FROM " \
                                         f"`openmrs`.CIHP_ListOfFacility WHERE Datim_Code = (SELECT `property_value` FROM " \
                                         f"`openmrs`.`global_property` WHERE `property`= 'facility_datim_code') LIMIT 1), " \
                                         f"(SELECT LGA FROM `openmrs`.CIHP_ListOfFacility WHERE Datim_Code = (SELECT " \
                                         f"`property_value` FROM `openmrs`.`global_property` WHERE `property`= " \
                                         f"'facility_datim_code')LIMIT 1), (SELECT `property_value` FROM " \
                                         f"`openmrs`.`global_property` WHERE `property`= 'facility_datim_code' LIMIT 1), " \
                                         f"(SELECT `property_value` FROM `openmrs`.`global_property` WHERE `property`= " \
                                         f"'Facility_Name' LIMIT 1), CONCAT('{pepid}','_',(SELECT `property_value` FROM " \
                                         f"`openmrs`.`global_property` WHERE `property`= 'facility_datim_code' LIMIT 1)), " \
                                         f"'{result_patient_id}', '{pepid}', '{client_name_fetch_mysql_result}', '{last_refill_date_mysql_result1}', " \
                                         f"'{last_refill_days_mysql_result1}', '{pill_balance_cal1}', '{last_vl_date_mysql_result1}', " \
                                         f"'{last_vl_result_mysql_result1}', '- {eac_alert_text} - {yuletide_alert_text} - {client_age_text} - {start_client_on_inh}', '{bleeding_alert}', '{clinic_days_based_date}', '{result_date3}', " \
                                         f"'{new_next_appt1}', '{new_next_appt3}', '{suggestionbo_formatted_text2}', '{search_type}') "
                my_cursor2.execute(insert_searched_client)
                mydb2.commit()
            else:
                pass
            my_cursor2.close()
            mydb2.close()
        my_cursor1.close()
        mydb1.close()

        if my_cursor1:
            my_cursor1.close()
        if my_cursor2:
            my_cursor2.close()
        if my_cursor3:
            my_cursor3.close()
        if my_cursor4:
            my_cursor4.close()
        if my_cursor5:
            my_cursor5.close()
        if my_cursor6:
            my_cursor6.close()
        if my_cursor7:
            my_cursor7.close()
        if my_cursor8:
            my_cursor8.close()
        if my_cursor9:
            my_cursor9.close()
        if my_cursor10:
            my_cursor10.close()
        if my_cursor11:
            my_cursor11.close()
        if my_cursor12:
            my_cursor12.close()
        if my_cursor13:
            my_cursor13.close()
        if my_cursor14:
            my_cursor14.close()
        if my_cursor15:
            my_cursor15.close()
        if my_cursor16:
            my_cursor16.close()
        if my_cursor17:
            my_cursor17.close()
        if my_cursor18:
            my_cursor18.close()
        if my_cursor19:
            my_cursor19.close()
        if my_cursor20:
            my_cursor20.close()
        print(f"sergfrsdfgsdrgergsd-----{yuletide_alert_text}")
        print(f"sergfrsdfgsdrgergsd-----{yuletide_Start}")
        print(f"sergfrsdfgsdrgergsd-----{yuletide_end}")

    def combined_function(self):
        self.current_client_details()
        self.determinant()

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")



    def ip_get_destroy_top(self, event=None):
        ip_get = self.ip_entry.get()
        print(ip_get)
        self.topwindow.withdraw()
        #self.topwindow.destroy()
        # Enable the connect button again
        self.con_host_button.configure(state="normal")
        self.deiconify()

    def get_checked_days(self):
        if self.checkboxmonday_var.get() == "on" or self.checkboxtuesday_var.get() == "on" or self.checkboxwednesday_var.get() == "on" or self.checkboxthursday_var.get() == "on" or self.checkboxfriday_var.get() == "on" \
                or self.checkboxsaturday_var.get() == "on" or self.checkboxsunday_var.get() == "on":
            print([self.checkboxmonday_var.get(), self.checkboxtuesday_var.get(), self.checkboxwednesday_var.get(),
                   self.checkboxthursday_var.get(), self.checkboxfriday_var.get(), self.checkboxsaturday_var.get(),
                   self.checkboxsunday_var.get()])
            return ([self.checkboxmonday_var.get(), self.checkboxtuesday_var.get(), self.checkboxwednesday_var.get(),
                     self.checkboxthursday_var.get(), self.checkboxfriday_var.get(), self.checkboxsaturday_var.get(),
                     self.checkboxsunday_var.get()])

    def bulk_search_destroy_top(self, event=None):
        self.deiconify()
        loop_is_on = "On"

        ids_get = self.ids_entry.get()
        print(ids_get)
        self.topwindow_bulk.withdraw()

        # Input names separated by comma
        ids_input = ids_get

        # Split names by comma and strip whitespace
        global bulk_ids_inputed
        bulk_ids_inputed = [name.strip() for name in ids_input.split(',')]
        # Split names by comma
        #bulk_ids_inputed = ids_input.split(',')

        # Loop through each name
        for name_id in bulk_ids_inputed:
            try:
                # Simulate auto typing by printing with a delay
                #print(f"Auto supplying id: {name_id}")
                ids_get_loop = f"{name_id}"
                time.sleep(0.1)
                self.pepid_entry.delete(0, customtkinter.END)  # Clear current contents if any
                time.sleep(0.1)
                self.pepid_entry.insert(0, name_id)
                time.sleep(0.1)
                # Simulate pressing Enter using keyboard module
                #print("Auto pressing Enter...")
                #keyboard.send("enter")  # Sends an Enter key press

                self.current_client_details()
                time.sleep(0.2)

                please_wait = CTkMessagebox(title="Info", message="Bulk search is completed.")

                time.sleep(0.1)

                please_wait.withdraw()

            except Exception as e:
                print(f"Error occurred for id {name_id}: {e}")
                continue  # Continue to the next iteration even if there is an error

        #loop_is_on = "Off"
        CTkMessagebox(title="Completed", message="Bulk search is completed.",
                      icon="check", option_1="Thanks")

        def fetch_and_save_data(ip_get, bulk_ids_inputed):
            # Ensure bulk_ids_inputed is a list of strings and escape each item
            formatted_ids = ', '.join(f"'{id}'" for id in bulk_ids_inputed)

            # Connect to the MySQL database
            mydb2 = mysql.connector.connect(
                host=ip_get,
                user="root",
                password="Admin123",
                database="appt_alignment_log"  # Replace with your actual database name
            )

            # Define the SQL query with properly formatted IDs
            query = f"""
            SELECT * FROM appt_alignment_log_tab2 
            WHERE `Pepid` IN ({formatted_ids}) 
            AND `Type_of_search` = 'Bulk search'
            """

            # Execute query and load into a DataFrame
            df = pd.read_sql_query(query, mydb2)

            # Close the database connection
            mydb2.close()

            # Define path to Downloads folder
            downloads_folder = os.path.expanduser('~/Downloads')

            now = datetime.now()
            formatted_now = now.strftime("%Y-%m-%d %H.%M.%S")
            file_path = os.path.join(downloads_folder, f'Service Integrator Bulk Search_{formatted_now}.xlsx')

            # Save DataFrame to Excel
            df.to_excel(file_path, index=False, engine='openpyxl')

            print(f"Data saved to {file_path}")

        # Example usage
        ip_get = self.ip_entry.get()
        fetch_and_save_data(ip_get, bulk_ids_inputed)



            # Enable the connect button again
        self.bulk_search_button.configure(state="normal")
        self.deiconify()

        self.grid_rowconfigure(0, weight=1)  # Make the top row resizable
        self.grid_rowconfigure(1, weight=1)  # Make the bottom row resizable
        self.grid_rowconfigure(2, weight=1)  # Make the bottom row resizable
        self.grid_rowconfigure(3, weight=1)  # Make the bottom row resizable
        self.grid_rowconfigure(4, weight=1)  # Make the bottom row resizable
        self.grid_rowconfigure(5, weight=1)  # Make the bottom row resizable
        self.grid_rowconfigure(6, weight=1)  # Make the bottom row resizable
        self.grid_rowconfigure(7, weight=1)  # Make the bottom row resizable
        self.grid_rowconfigure(8, weight=1)  # Make the bottom row resizable
        self.grid_rowconfigure(9, weight=1)  # Make the bottom row resizable
        self.grid_rowconfigure(10, weight=1)  # Make the bottom row resizable
        self.grid_rowconfigure(11, weight=1)  # Make the bottom row resizable
        self.grid_columnconfigure(0, weight=1)  # Make the column resizable
        self.grid_columnconfigure(1, weight=1)  # Make the column resizable
        self.grid_columnconfigure(2, weight=1)  # Make the column resizable
        self.grid_columnconfigure(3, weight=1)  # Make the column resizable
        self.grid_columnconfigure(4, weight=1)  # Make the column resizable
        self.grid_columnconfigure(5, weight=1)  # Make the column resizable
        self.grid_columnconfigure(6, weight=1)  # Make the column resizable

        self.scrollable_frame.grid_rowconfigure(0, weight=1)  # Make the top row resizable
        self.scrollable_frame.grid_rowconfigure(1, weight=1)  # Make the bottom row resizable
        self.scrollable_frame.grid_rowconfigure(2, weight=1)  # Make the bottom row resizable
        self.scrollable_frame.grid_rowconfigure(3, weight=1)  # Make the bottom row resizable
        self.scrollable_frame.grid_rowconfigure(4, weight=1)  # Make the bottom row resizable
        self.scrollable_frame.grid_rowconfigure(5, weight=1)  # Make the bottom row resizable
        self.scrollable_frame.grid_rowconfigure(6, weight=1)  # Make the bottom row resizable
        self.scrollable_frame.grid_rowconfigure(7, weight=1)  # Make the bottom row resizable
        self.scrollable_frame.grid_rowconfigure(8, weight=1)  # Make the bottom row resizable
        self.scrollable_frame.grid_rowconfigure(9, weight=1)  # Make the bottom row resizable
        self.scrollable_frame.grid_rowconfigure(10, weight=1)  # Make the bottom row resizable
        self.scrollable_frame.grid_rowconfigure(11, weight=1)  # Make the bottom row resizable
        self.scrollable_frame.grid_columnconfigure(0, weight=1)  # Make the column resizable
        self.scrollable_frame.grid_columnconfigure(1, weight=1)  # Make the column resizable
        self.scrollable_frame.grid_columnconfigure(2, weight=1)  # Make the column resizable
        self.scrollable_frame.grid_columnconfigure(3, weight=1)  # Make the column resizable
        self.scrollable_frame.grid_columnconfigure(4, weight=1)  # Make the column resizable
        self.scrollable_frame.grid_columnconfigure(5, weight=1)  # Make the column resizable
        self.scrollable_frame.grid_columnconfigure(6, weight=1)  # Make the column resizable

        self.scrollable_frame1.grid_rowconfigure(0, weight=1)  # Make the top row resizable
        self.scrollable_frame1.grid_rowconfigure(1, weight=1)  # Make the bottom row resizable
        self.scrollable_frame1.grid_rowconfigure(2, weight=1)  # Make the bottom row resizable
        self.scrollable_frame1.grid_rowconfigure(3, weight=1)  # Make the bottom row resizable
        self.scrollable_frame1.grid_rowconfigure(4, weight=1)  # Make the bottom row resizable
        self.scrollable_frame1.grid_rowconfigure(5, weight=1)  # Make the bottom row resizable
        self.scrollable_frame1.grid_rowconfigure(6, weight=1)  # Make the bottom row resizable
        self.scrollable_frame1.grid_rowconfigure(7, weight=1)  # Make the bottom row resizable
        self.scrollable_frame1.grid_rowconfigure(8, weight=1)  # Make the bottom row resizable
        self.scrollable_frame1.grid_rowconfigure(9, weight=1)  # Make the bottom row resizable
        self.scrollable_frame1.grid_rowconfigure(10, weight=1)  # Make the bottom row resizable
        self.scrollable_frame1.grid_rowconfigure(11, weight=1)  # Make the bottom row resizable
        self.scrollable_frame1.grid_columnconfigure(0, weight=1)  # Make the column resizable
        self.scrollable_frame1.grid_columnconfigure(1, weight=1)  # Make the column resizable
        self.scrollable_frame1.grid_columnconfigure(2, weight=1)  # Make the column resizable
        self.scrollable_frame1.grid_columnconfigure(3, weight=1)  # Make the column resizable
        self.scrollable_frame1.grid_columnconfigure(4, weight=1)  # Make the column resizable
        self.scrollable_frame1.grid_columnconfigure(5, weight=1)  # Make the column resizable
        self.scrollable_frame1.grid_columnconfigure(6, weight=1)  # Make the column resizable

        self.clinicdays_frame.grid_rowconfigure(0, weight=1)  # Make the top row resizable
        self.clinicdays_frame.grid_rowconfigure(1, weight=1)  # Make the bottom row resizable
        self.clinicdays_frame.grid_rowconfigure(2, weight=1)  # Make the bottom row resizable
        self.clinicdays_frame.grid_rowconfigure(3, weight=1)  # Make the bottom row resizable
        self.clinicdays_frame.grid_rowconfigure(4, weight=1)  # Make the bottom row resizable
        self.clinicdays_frame.grid_rowconfigure(5, weight=1)  # Make the bottom row resizable
        self.clinicdays_frame.grid_rowconfigure(6, weight=1)  # Make the bottom row resizable
        self.clinicdays_frame.grid_rowconfigure(7, weight=1)  # Make the bottom row resizable
        self.clinicdays_frame.grid_rowconfigure(8, weight=1)  # Make the bottom row resizable
        self.clinicdays_frame.grid_rowconfigure(9, weight=1)  # Make the bottom row resizable
        self.clinicdays_frame.grid_rowconfigure(10, weight=1)  # Make the bottom row resizable
        self.clinicdays_frame.grid_rowconfigure(11, weight=1)  # Make the bottom row resizable
        self.clinicdays_frame.grid_columnconfigure(0, weight=1)  # Make the column resizable
        self.clinicdays_frame.grid_columnconfigure(1, weight=1)  # Make the column resizable
        self.clinicdays_frame.grid_columnconfigure(2, weight=1)  # Make the column resizable
        self.clinicdays_frame.grid_columnconfigure(3, weight=1)  # Make the column resizable
        self.clinicdays_frame.grid_columnconfigure(4, weight=1)  # Make the column resizable
        self.clinicdays_frame.grid_columnconfigure(5, weight=1)  # Make the column resizable
        self.clinicdays_frame.grid_columnconfigure(6, weight=1)  # Make the column resizable

        self.checkalert_frame.grid_rowconfigure(0, weight=1)  # Make the top row resizable
        self.checkalert_frame.grid_rowconfigure(1, weight=1)  # Make the bottom row resizable
        self.checkalert_frame.grid_rowconfigure(2, weight=1)  # Make the bottom row resizable
        self.checkalert_frame.grid_rowconfigure(3, weight=1)  # Make the bottom row resizable
        self.checkalert_frame.grid_rowconfigure(4, weight=1)  # Make the bottom row resizable
        self.checkalert_frame.grid_rowconfigure(5, weight=1)  # Make the bottom row resizable
        self.checkalert_frame.grid_rowconfigure(6, weight=1)  # Make the bottom row resizable
        self.checkalert_frame.grid_rowconfigure(7, weight=1)  # Make the bottom row resizable
        self.checkalert_frame.grid_rowconfigure(8, weight=1)  # Make the bottom row resizable
        self.checkalert_frame.grid_rowconfigure(9, weight=1)  # Make the bottom row resizable
        self.checkalert_frame.grid_rowconfigure(10, weight=1)  # Make the bottom row resizable
        self.checkalert_frame.grid_rowconfigure(11, weight=1)  # Make the bottom row resizable
        self.checkalert_frame.grid_columnconfigure(0, weight=1)  # Make the column resizable
        self.checkalert_frame.grid_columnconfigure(1, weight=1)  # Make the column resizable
        self.checkalert_frame.grid_columnconfigure(2, weight=1)  # Make the column resizable
        self.checkalert_frame.grid_columnconfigure(3, weight=1)  # Make the column resizable
        self.checkalert_frame.grid_columnconfigure(4, weight=1)  # Make the column resizable
        self.checkalert_frame.grid_columnconfigure(5, weight=1)  # Make the column resizable
        self.checkalert_frame.grid_columnconfigure(6, weight=1)  # Make the column resizable

        self.checkalert_frame2.grid_rowconfigure(0, weight=1)  # Make the top row resizable
        self.checkalert_frame2.grid_rowconfigure(1, weight=1)  # Make the bottom row resizable
        self.checkalert_frame2.grid_rowconfigure(2, weight=1)  # Make the bottom row resizable
        self.checkalert_frame2.grid_rowconfigure(3, weight=1)  # Make the bottom row resizable
        self.checkalert_frame2.grid_rowconfigure(4, weight=1)  # Make the bottom row resizable
        self.checkalert_frame2.grid_rowconfigure(5, weight=1)  # Make the bottom row resizable
        self.checkalert_frame2.grid_rowconfigure(6, weight=1)  # Make the bottom row resizable
        self.checkalert_frame2.grid_rowconfigure(7, weight=1)  # Make the bottom row resizable
        self.checkalert_frame2.grid_rowconfigure(8, weight=1)  # Make the bottom row resizable
        self.checkalert_frame2.grid_rowconfigure(9, weight=1)  # Make the bottom row resizable
        self.checkalert_frame2.grid_rowconfigure(10, weight=1)  # Make the bottom row resizable
        self.checkalert_frame2.grid_rowconfigure(11, weight=1)  # Make the bottom row resizable
        self.checkalert_frame2.grid_columnconfigure(0, weight=1)  # Make the column resizable
        self.checkalert_frame2.grid_columnconfigure(1, weight=1)  # Make the column resizable
        self.checkalert_frame2.grid_columnconfigure(2, weight=1)  # Make the column resizable
        self.checkalert_frame2.grid_columnconfigure(3, weight=1)  # Make the column resizable
        self.checkalert_frame2.grid_columnconfigure(4, weight=1)  # Make the column resizable
        self.checkalert_frame2.grid_columnconfigure(5, weight=1)  # Make the column resizable
        self.checkalert_frame2.grid_columnconfigure(6, weight=1)  # Make the column resizable

        # Configure the grid layout for the root window to resize correctly
        app.grid_rowconfigure(0, weight=1)
        app.grid_columnconfigure(0, weight=1)

'''
    def main_determinant(self):
        ip = self.ip_entry.get()
        try:
            mydb1 = mysql.connector.connect(
                host=ip,
                user="root",
                passwd="Admin123",
                database='openmrs'
            )
            my_cursor1 = mydb1.cursor()
            # my_cursor1.close()
            # mydb1.close()
        except Exception as e:
            messagebox.showinfo('Info', "ERROR: {}".format(e))
        pepid = self.pepid_entry.get()
        get_patient_id = f"SELECT `patient_id` FROM `patient_identifier` WHERE `identifier` = '{pepid}' AND `voided`=0;"
        run_set_patient_id = my_cursor1.execute(get_patient_id)
        result_patient_id1 = my_cursor1.fetchone()
        print(result_patient_id1)

        last_vl_date1 = my_cursor1.execute(Appointment_Alignment_Scripts.last_vl_date)
        last_vl_date1_mysql_result = my_cursor1.fetchone()

        last_vl_result1 = my_cursor1.execute(Appointment_Alignment_Scripts.last_vl_result)
        last_vl_result1_mysql_result = my_cursor1.fetchone()

        last_sample_date1 = my_cursor1.execute(Appointment_Alignment_Scripts.last_sample_date)
        last_sample_date1_mysql_result = my_cursor1.fetchone()

        last_refill_days = my_cursor1.execute(Appointment_Alignment_Scripts.last_refill_days)
        last_refill_days_mysql_result1 = my_cursor1.fetchone()

        # Calculate next appointment date
        last_pickup_date = my_cursor1.execute(Appointment_Alignment_Scripts.last_refill_date_raw)
        last_refill_date_raw_mysql_result = my_cursor1.fetchone()[0]
        print(f"Fetched data: {last_refill_date_raw_mysql_result},{last_refill_days_mysql_result1}")

        # Getting Drug refill date
        if last_refill_date_raw_mysql_result:  # Check if data is not None
            year, month, day = last_refill_date_raw_mysql_result.year, last_refill_date_raw_mysql_result.month, last_refill_date_raw_mysql_result.day  # Assuming date is the first element (index 0)
            last_pickup_date_convert = date(year, month, day)

        else:
            print("No data found.")
        next_appt = (last_pickup_date_convert) + timedelta(days=last_refill_days_mysql_result1)
        print(f"This is next appointment date {next_appt}")

        # Getting VL date
        last_vl_date = my_cursor1.execute(Appointment_Alignment_Scripts.last_vl_date_raw)
        last_vl_date_raw_mysql_result = my_cursor1.fetchone()[0]
        next_vl_date_ = last_vl_date_raw_mysql_result + timedelta(days=365.25)
        print(f"Fectched VL due date is: {next_vl_date_}")

        current_date = date.today()
        print(f"This is today's date {current_date}")

        pill_balance_cal = next_appt - current_date
        print(pill_balance_cal)
        pill_balance_cal1 = pill_balance_cal.days
        print(pill_balance_cal1)

        bleed_due_days = current_date - last_vl_date_raw_mysql_result
        bleed_alert_days = bleed_due_days.days
        print(f"Bleeding alerto - {bleed_alert_days}")

        range_0_60 = range(0, 61)  # Meaning 0-60

        return next_appt, next_vl_date_, current_date, pill_balance_cal1, bleed_alert_days

    def next_appointment_date(self):
        next_appt, next_vl_date_, current_date, pill_balance_cal1, bleed_alert_days = self.main_determinant()
        print(f"sdsdfsdfsdf {next_appt}")
        print(next_vl_date_)
        print(current_date)
        print(pill_balance_cal1) '''

if __name__ == "__main__":
    app = App()
    app.mainloop()
