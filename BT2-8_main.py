import csv       # for Create CSV File
import sys       # System
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from BT28UI import Ui_MainWindow
from datetime import datetime
import os
import time
import sqlite3

house_list = []
edge_list  = []
component_list  = []
date_list = []
qt_limit = 5    # Limit Quantity of House for printing
#======================================================
# Parth to Connect to SQL Lite
db_path = "Databases/BartendeerDB.db"
ap_csv_path = 'Databases/existing_data.csv'
#======================================================
class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    # My Design Button ===================================================================================
        self.ui.pushButton_9.clicked.connect(lambda :self.add_data())    # add database 
        self.ui.pushButton_10.clicked.connect(lambda :self.del_data())   # del note list for mdata base
        self.ui.pushButton_8.clicked.connect(lambda :self.print_label()) # trigger BT to printing process
        self.ui.pushButton_7.clicked.connect(lambda :self.clear_tab())   # Clear Data
    # Add Data ===========================================================================================
    def add_data(self) :
        # Selection Process ==========================
        global house_list
        global edge_list
        global component_list
        # Edge ID ====================================
        Edge_ID = self.ui.lineEdit.text()
        # House ID ===================================
        House_ID = self.ui.lineEdit_2.text()
        # Select Component List ======================
        Comp_Sel = self.ui.comboBox.currentText()
        if Comp_Sel == "None" :
           Comp_Sel = self.ui.comboBox_2.currentText()
           if Comp_Sel == "None" :
              Comp_Sel = ""
        #=============================================
        # Save Data List
        if House_ID != "" and Comp_Sel != ""  :
            house_list.append(House_ID)
            edge_list.append(Edge_ID)
            component_list.append(Comp_Sel)
        else :  # IF IMPORTANT DATA NOT FILL
            self.ui.label_2.setText("Error To Regist")
            self.ui.label_2.setStyleSheet("color : red ;")
        #=============================================
        # Display Data on WT  ================================================================
        if  Comp_Sel != "" and House_ID != ""  : # if data has full filled
            de_col = len(house_list)-1
            self.ui.tableWidget_3.setItem(de_col,0,QtWidgets.QTableWidgetItem(Edge_ID)) 
            self.ui.tableWidget_3.setItem(de_col,1,QtWidgets.QTableWidgetItem(House_ID)) 
            self.ui.tableWidget_3.setItem(de_col,2,QtWidgets.QTableWidgetItem(Comp_Sel))
            print("Add Data :")
            self.ui.label_2.setText("QT: " + str(len(house_list)))
            self.ui.label_2.setStyleSheet("color : green ;")
            self.sql_DB() ## tEST DB
            self.ap_database() # Append Data
        elif Edge_ID == "" and Comp_Sel == "" and House_ID == "" :  # if data dosnt full fill
            self.ui.label_2.setText("No Data to Display")
            self.ui.label_2.setStyleSheet("color : red ;")
        #=====================================================================================
        # Automation Print Trigger - Define By QT_LIMIT
        if len(house_list) == qt_limit:  
            self.print_label()
            self.clear_tab()
        self.clear_ui()
        print(house_list)
        print(edge_list)
        print(component_list)
    # End ================================================================================================
    # Delete Data ========================================================================================
    def del_data(self) :
        print("Delete Data :") 
        # Set Variable ===============================
        House_ID = self.ui.lineEdit_2.text()
        if House_ID != "" :
            data_num = int(House_ID) ## Numeric Comparetor Input  (Pointer of ARRAY)
            if data_num > len(house_list) :
                self.ui.label_2.setText("Numeric Error")
                self.ui.label_2.setStyleSheet("color : red ;")
            elif data_num <= len(house_list) : ## Number of Data in All Data Range (up to 1 untill n )
                self.ui.label_2.setText(House_ID + " Has Been Deleted")
                self.ui.label_2.setStyleSheet("color : orange ;")
                # claer Data ======================== ## Ref form House ID (integer) to Remove Data in Array
                house_list[int(House_ID)-1] = ""
                edge_list[int(House_ID)-1] = ""
                component_list[int(House_ID)-1] = ""
                # ===================================
                # Blank Data ======================== ## Prepare for something
                Col_New = int(House_ID) -1 # Set Column
                Emty = "" # Blank Data 
                # Replace old data with Blank Data =========================================
                self.ui.tableWidget_3.setItem(Col_New,0,QtWidgets.QTableWidgetItem(Emty)) 
                self.ui.tableWidget_3.setItem(Col_New,1,QtWidgets.QTableWidgetItem(Emty)) 
                self.ui.tableWidget_3.setItem(Col_New,2,QtWidgets.QTableWidgetItem(Emty))
        else : # IF Input is STRING or SOMTHING ELSE
            self.ui.label_2.setText("Invalid Data Type")
            self.ui.label_2.setStyleSheet("color : red ;")
        self.clear_ui()
    # End ================================================================================================
    # Print Label=========================================================================================
    def print_label(self) :
      if len(house_list) >= 1 :
        # Create CSV Trigger =======================================
        # Combine the data into rows
        data_rows = zip(house_list,edge_list,component_list)
        # Specify the CSV file path
        csv_file_path = 'DataBases/DataOutput.csv'
        # Write the data to the CSV file
        with open(csv_file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Write the header (optional)
            csv_writer.writerow(['HouseID', 'EdgeID', 'Component'])
            # Write the data rows
            csv_writer.writerows(data_rows)
        print(f"CSV file '{csv_file_path}' has been created.")     
        self.ui.label_2.setText("Printing") 
        self.ui.label_2.setStyleSheet("color : green ;")                     
        #===========================================================
        #===========================================================
        self.date_time()
        self.clear_ui()
        self.clear_tab()
      else : 
        self.ui.label_2.setText("Input Not Found") 
        self.ui.label_2.setStyleSheet("color : RED ;")
    # End ================================================================================================
    # Clear ==============================================================================================
    def clear_ui(self) : 
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox_2.setCurrentIndex(0)
     # End ===============================================================================================
    def clear_tab(self) :
        # CLEAR DATA IN ARRAY =====================================
        global house_list
        global edge_list
        global component_list
        house_list = [] 
        edge_list  = []
        component_list  = []
        # Clear WT ================================================
        for row in range(self.ui.tableWidget_3.rowCount()):
            for col in range(self.ui.tableWidget_3.columnCount()):
                item = QtWidgets.QTableWidgetItem("")
                self.ui.tableWidget_3.setItem(row, col, item)
    # DateTime ===========================================================================================
    def date_time(self) :
        date = datetime.now()
        print("Print Date: " + str(date))
        self.clear_tab()
    #=====================================================================================================
    def ap_database(self) :
        # Edge ID ====================================
        Edge_ID = self.ui.lineEdit.text()
        # House ID ===================================
        House_ID = self.ui.lineEdit_2.text()
        # Select Component List ======================
        Comp_Sel = self.ui.comboBox.currentText()
        # Time =======================================
        add_date = datetime.now()
        #=============================================
        ap_insert = [[Edge_ID,House_ID,Comp_Sel,add_date]]
        # Append new data to the CSV file
        with open(ap_csv_path, 'a', newline='') as csvfile :
            csv_writer = csv.writer(csvfile)
        # Write the new data rows
            csv_writer.writerows(ap_insert)
    print(f"New data has been appended to the CSV file '{ap_csv_path}'.")     
    # Create SQL DataBases ===============================================================================
    def sql_DB(self) :
        # Edge ID ====================================
        Edge_ID = self.ui.lineEdit.text()
        # House ID ===================================
        House_ID = self.ui.lineEdit_2.text()
        # Select Component List ======================
        Comp_Sel = self.ui.comboBox.currentText()
        # Time =======================================
        add_date = datetime.now()
        # Print_stat =================================
        print_stat = 'Test'
        #=============================================
        bt28_insert = [add_date,Edge_ID,House_ID,Comp_Sel,print_stat]
        print(len(bt28_insert))
        conn = sqlite3.connect(db_path)
        my_insert_sql = '''INSERT INTO test_sql(date_time,house_id,edge_id,component,print_status) VALUES(?,?,?,?,?)'''
        try:
            conn = sqlite3.connect(db_path)
            cur = conn.cursor()
            cur.execute(my_insert_sql,bt28_insert)
            conn.commit()
            return 1
        except sqlite3.Error as e:
             print("SQLite error:", e)
        finally:
            if conn:
                conn.close()
            return 0
    # Update SQL DataBases ==============================================================================
    def up_print_stat(House_ID) :
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("UPDATE test_sql SET print_status = 'Printed' WHERE house_id = ?", (House_ID))
            conn.commit()
            return 1
        except sqlite3.Error as e:
            print("SQLite error:", e)
        finally:
            if conn:
                conn.close()
            return 0
    pass
    # End ===============================================================================================      
def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())
        
if __name__ == "__main__":
    # del_file()
    main()
# exit -------------------------------------//