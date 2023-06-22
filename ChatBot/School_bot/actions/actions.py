# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
 


from typing import Any, Text, Dict, List
import random
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import psycopg2
from psycopg2 import Error
import sqlite3
 



class ActionGetEmailPassword(Action):
   
    def name(self) -> Text:
        return "action_get_email_password"
 
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
 
        # play rock paper scissors
        user_email = tracker.get_slot("email")
        # user_password = tracker.get_slot("password")

        dispatcher.utter_message(text=f"Your email {user_email}")
        # dispatcher.utter_message(text=f"Your password {user_password}")

 
        return []


class connectWithDatabase():
    def __init__(self) -> None:

        self.connection = sqlite3.connect(database="db.sqlite3")
        # self.user ="postgres"
        # self.password = "123456789"
        # self.host = "localhost"
        # self.port = "5432"
        # self.database="school_stu"
        # self.connection = psycopg2.connect(user=self.user,password=self.password,host=self.host,
        #                                     port=self.port,database=self.database)
    def submit(self,query):
        record = ""           
        try:
            cursor = self.connection.cursor()
            print("PostgreSQL server information")
            cursor.execute(query)
            record = cursor.fetchone()
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("PostgreSQL connection is closed")
        print("Record inserted successfully into table")
        return record
 
cennect = connectWithDatabase()  

class ActionSubmitPlaint(Action):
   
    def name(self) -> Text:
        return "action_submit_plaint"
 
 
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # get plaint (problem for user)
        plaint = tracker.get_slot("text_of_plaint")
        dispatcher.utter_message(text=f"Your plaint is: {plaint}")

       
        return []

    def submit(self):

        # dispatcher.utter_message(template="utter_submit")

        # d = DataUpdate()
        # dispatcher.utter_message("Your response has been loaded.")
        # dispatcher.utter_message(d)
        
                       
                        
        try:
            connection = psycopg2.connect(user="tecmint",
                                  password="securep@wd",
                                  host="localhost",
                                  port="5432",
                                  database="tecmintdb")

        #     # Create a cursor to perform database operations
            cursor = connection.cursor()
            # Print PostgreSQL details
            print("PostgreSQL server information")
            # print(connection.get_dsn_parameters(), "\n")
            # Executing a SQL query
            cursor.execute(" SELECT * from Classs")
            # Fetch result
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
                
        
        # print("Record inserted successfully into table")
       
       

        
        return []
 
class ActionPay(Action):
   
    def name(self) -> Text:
        return "action_pay"
 
 
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # get plaint (problem for user)
        # plaint = tracker.get_slot("text_of_plaint")
        # dispatcher.utter_message(text=f"Your plaint is: {plaint}")
        submit()
       
        return []

    def submit(self):

        # dispatcher.utter_message(template="utter_submit")

        # d = DataUpdate()
        # dispatcher.utter_message("Your response has been loaded.")
        # dispatcher.utter_message(d)
        
                       
                        
        try:
            connection = psycopg2.connect(user="tecmint",
                                  password="securep@wd",
                                  host="localhost",
                                  port="5432",
                                  database="tecmintdb")

        #     # Create a cursor to perform database operations
            cursor = connection.cursor()
            # Print PostgreSQL details
            print("PostgreSQL server information")
            # print(connection.get_dsn_parameters(), "\n")
            # Executing a SQL query
            cursor.execute(" SELECT * from Classs")
            # Fetch result
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
                
        
        # print("Record inserted successfully into table")
       
       

        
        return []

class ActionGetDays(Action):
   
    def name(self) -> Text:
        return "action_get_days"
 
 
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # get plaint (problem for user)
        # plaint = tracker.get_slot("text_of_plaint")
        # dispatcher.utter_message(text=f"Your plaint is: {plaint}")
 
       
        return []

    def submit(self):

        # # dispatcher.utter_message(template="utter_submit")

        # # d = DataUpdate()
        # # dispatcher.utter_message("Your response has been loaded.")
        # # dispatcher.utter_message(d)
        
                       
                        
        # try:
        #     connection = psycopg2.connect(user="tecmint",
        #                           password="securep@wd",
        #                           host="localhost",
        #                           port="5432",
        #                           database="tecmintdb")

        # #     # Create a cursor to perform database operations
        #     cursor = connection.cursor()
        #     # Print PostgreSQL details
        #     print("PostgreSQL server information")
        #     # print(connection.get_dsn_parameters(), "\n")
        #     # Executing a SQL query
        #     cursor.execute(" SELECT * from Classs")
        #     # Fetch result
        #     record = cursor.fetchone()
        #     print("You are connected to - ", record, "\n")

        # except (Exception, Error) as error:
        #     print("Error while connecting to PostgreSQL", error)
        # finally:
        #     if (connection):
        #         cursor.close()
        #         connection.close()
        #         print("PostgreSQL connection is closed")
                
        
        # # print("Record inserted successfully into table")
       
       

        
        return []


class ActionGetMark(Action):
    def name(self) -> Text:
        return "action_get_mark"
 
 
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # get plaint (problem for user)
        # plaint = tracker.get_slot("text_of_plaint")
        dispatcher.utter_message(text=f"العلامات المتوفرة: رياضيات 500 ")
 
       
        return []

   
