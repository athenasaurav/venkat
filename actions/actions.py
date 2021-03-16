# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Form, AllSlotsReset, Restarted
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hi human, I'm sure you want something   😃 I'm sure you are gonna ask me something")

        return []


class ActionPostAccommodationServicesHotel(Action):

    def name(self) -> Text:
        return "action_post_Accommodation_Services_Hotel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hotel")

        return []


class ActionPostCityAttractionSpa(Action):

    def name(self) -> Text:
        return "action_post_city_attraction_spa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Spa")

        return []

class ActionPostEducationalSuppliesDealers(Action):

    def name(self) -> Text:
        return "action_post_Educational_Supplies_Dealers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Education supplies dealers")

        return []


class ActionPostEducationalSuppliesDealersBookShop(Action):

    def name(self) -> Text:
        return "action_post_Educational_Supplies_Dealers_book_shop"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Book Services")

        return []

class ActionPostAccountant(Action):

    def name(self) -> Text:
        return "action_post_Accountant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Accountant")

        return []

class ActionPostInsurance(Action):

    def name(self) -> Text:
        return "action_post_Insurance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Insurance")

        return []

class ActionPostATM(Action):

    def name(self) -> Text:
        return "action_post_ATM"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="ATM")

        return []

class ActionPostGovernmentOffices(Action):

    def name(self) -> Text:
        return "action_post_Government_Offices"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="GOVT OFFICE")

        return []
class ActionPostNightlife(Action):

    def name(self) -> Text:
        return "action_post_Nightlife"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Nightlife")

        return []

class ActionPostNightlifeHookah(Action):

    def name(self) -> Text:
        return "action_post_Nightlife_Hookah"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Nightlife Hookah")

        return []

class ActionPostSchools(Action):

    def name(self) -> Text:
        return "action_post_Schools"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Schools")

        return []

class ActionPostSchoolsRetakers(Action):

    def name(self) -> Text:
        return "action_post_Schools_Retakers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Schools Retakers")

        return []

class ActionPostGamesCenters(Action):

    def name(self) -> Text:
        return "action_post_Games_Centers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Game Centers")

        return []


class ActionPostFoodandDininglocation(Action):

    def name(self) -> Text:
        return "action_post_Food_and_Dining_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Food_and_Dining_location")

        return []

class ActionPostFoodandDiningFoodProductSuppliers(Action):

    def name(self) -> Text:
        return "action_post_Food_and_Dining_Food_Product_Suppliers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Food_and_Dining_Food_Product_Suppliers")

        return []

class ActionPostFoodandDiningRestaurant(Action):

    def name(self) -> Text:
        return "action_post_Food_and_Dining_Restaurant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Food_and_Dining_Restaurant")

        return []

class ActionPostFoodandDiningSeafood(Action):

    def name(self) -> Text:
        return "action_post_Food_and_Dining_Seafood"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Food_and_Dining_Seafood")

        return []

class ActionPostFoodandDiningSweet(Action):

    def name(self) -> Text:
        return "action_post_Food_and_Dining_Sweet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Food_and_Dining_Sweet")

        return []

class ActionPostGrocery(Action):

    def name(self) -> Text:
        return "action_post_Grocery"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Grocery")

        return []

class ActionPostClinicsAndDoctorsType(Action):

    def name(self) -> Text:
        return "action_post_Clinics_and_Doctors_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="action_post_Clinics_and_Doctors_type")

        return []

class ActionPostClinicsandDoctorstypeChiropractors(Action):

    def name(self) -> Text:
        return "action_post_Clinics_and_Doctors_type_Chiropractors"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="action_post_Clinics_and_Doctors_type_Chiropractors")

        return []

class ActionPostClinicsandDoctorstypeDentists(Action):

    def name(self) -> Text:
        return "action_post_Clinics_and_Doctors_type_Dentists"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="action_post_Clinics_and_Doctors_type_Dentists")

        return []

class ActionPostEmergencyServices(Action):

    def name(self) -> Text:
        return "action_post_Emergency_Services"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="action_post_Emergency_Services")

        return []

class ActionPostLegalService(Action):

    def name(self) -> Text:
        return "action_post_Legal_Service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="action_post_Legal_Service")

        return []

class ActionPostLegalServiceAdvocates(Action):

    def name(self) -> Text:
        return "action_post_Legal_Service_Advocates"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="action_post_Legal_Service_Advocates")

        return []

class ActionPostLegalServiceImmigration(Action):

    def name(self) -> Text:
        return "action_post_Legal_Service_Immigration"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="action_post_Legal_Service_Immigration")

        return []

class ActionPostLegalServicePassport(Action):

    def name(self) -> Text:
        return "action_post_Legal_Service_Passport"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="action_post_Legal_Service_Passport")

        return []

class ActionPostFuneralsandMemorials(Action):

    def name(self) -> Text:
        return "action_post_Funerals_and_Memorials"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="action_post_Funerals_and_Memorials")

        return []

class ActionPostGardenandLawn(Action):

    def name(self) -> Text:
        return "action_post_Garden_and_Lawn"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="action_post_Garden_and_Lawn")

        return []

class ActionPostGardenandLawnGarden(Action):

    def name(self) -> Text:
        return "action_post_Garden_and_Lawn_Garden"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="action_post_Garden_and_Lawn_Garden")

        return []

class ActionPostGardenandLawnIrrigation(Action):

    def name(self) -> Text:
        return "action_post_Garden_and_Lawn_Irrigation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="action_post_Garden_and_Lawn_Irrigation")

        return []



class ActionRestarted(Action):
    def name(self):
        return "action_restart"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_reset_full", tracker)
        return [Form(None), AllSlotsReset(None), Restarted(None)]
