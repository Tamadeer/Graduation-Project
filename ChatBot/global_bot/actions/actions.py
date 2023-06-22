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
 

class connectWithDatabase():
    def __init__(self) -> None:
        self.user ="postgres"
        self.password = "123456789"
        self.host = "localhost"
        self.port = "5432"
        self.database="school_final"
        
    def submit(self,query):
        record = ""           
        try:
            self.connection = psycopg2.connect(user=self.user,password=self.password,host=self.host,
                                            port=self.port,database=self.database)
 
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
# أوراق التسجيل 
class ActionPaperRej(Action):
   
    def name(self) -> Text:
        return "action_paper_Rej"
 

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query = (""" SELECT "paper_Register"
	                            FROM public.student_management_app_registerinschool
                                ORDER BY ID DESC LIMIT 1;""")

        
        info = cennect.submit(query)
        for i in info:
            dispatcher.utter_message(text=i)
     
        return []


# ألية  التسجيل 
class ActionRoadRej(Action):
   
    def name(self) -> Text:
        return "action_Road_Rej"
 

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query = (""" SELECT "road_Register"
	                            FROM public.student_management_app_registerinschool
                                ORDER BY ID DESC LIMIT 1;""")

        
        info = cennect.submit(query)
        for i in info:
            dispatcher.utter_message(text=i)
     
        return []

# وقت بدء التسجيل 
class ActionstarttimeRej(Action):
   
    def name(self) -> Text:
        return "action_start_time_Rej"
 

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query = (""" SELECT "start_at"
	                            FROM public.student_management_app_registerinschool
                                ORDER BY ID DESC LIMIT 1;""")

        
        info = cennect.submit(query)
        for i in info:
            dispatcher.utter_message(text=str(i))
        return []

# وقت انتهاء التسجيل 
class ActionendtimeRej(Action):
   
    def name(self) -> Text:
        return "action_end_time_Rej"
 

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        query = (""" SELECT "finish_at"
	                            FROM public.student_management_app_registerinschool
                                ORDER BY ID DESC LIMIT 1;""")

        
        info = cennect.submit(query)
        for i in info:
            dispatcher.utter_message(text=str(i))
        return []

# معلومات عامة للتسجيل
class ActionInfoRej(Action):
   
    def name(self) -> Text:
        return "action_info_rej"
 
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query = (""" SELECT gobol_info 
	                            FROM public.student_management_app_registerinschool
                                ORDER BY ID DESC LIMIT 1;""")

        
        info = cennect.submit(query)
        for i in info:
            dispatcher.utter_message(text=i)
        return []


# قسط التسجيل بالمدرسة 
class ActionSchoolregistrationpremium(Action):
   
    def name(self) -> Text:
        return "action_School_registration_premium"
 

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        query = (""" SELECT "maney_Register"
	                            FROM public.student_management_app_registerinschool
                                ORDER BY ID DESC LIMIT 1;""")

        
        info = cennect.submit(query)
        for i in info:
            dispatcher.utter_message(text=i)
        return []



# تكلفة التسجيل بالباصات 
class ActionBusregistrationcost(Action):
   
    def name(self) -> Text:
        return "action_Bus_registration_cost"
 

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        query = (""" SELECT "cost_Bus"
	                    FROM public.student_management_app_registerinbus
                        ORDER BY ID DESC LIMIT 1;""")

        
        info = cennect.submit(query)
        for i in info:
            dispatcher.utter_message(text=i)
        return []



# المناطق التي تخدمها الباصات 
class ActionBusserviceareas(Action):
   
    def name(self) -> Text:
        return "action_Bus_service_areas"
 

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            query = (""" SELECT area_server
	                    FROM public.student_management_app_registerinbus
                        ORDER BY ID DESC LIMIT 1;""")

        
            info = cennect.submit(query)
            for i in info:
                dispatcher.utter_message(text=i)
            return []


# تفاصيل التسجيل بالباصات 
class ActionBusregistrationdetails(Action):
   
    def name(self) -> Text:
        return "action_Bus_registration_details"
 
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            query = (""" SELECT "details_Register_Bus"
	                    FROM public.student_management_app_registerinbus
                        ORDER BY ID DESC LIMIT 1;""")

        
            info = cennect.submit(query)
            for i in info:
                dispatcher.utter_message(text=i)
            return []



# موعد انطلاق الباصات 
class ActionBusdeparturetime(Action):
   
    def name(self) -> Text:
        return "action_Bus_departure_time"
 

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
            query = (""" SELECT start_at
	                    FROM public.student_management_app_registerinbus
                        ORDER BY ID DESC LIMIT 1;""")

        
            info = cennect.submit(query)
            for i in info:
                dispatcher.utter_message(text=str(i))
            return []


   