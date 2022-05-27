from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()

sheet_data = data_manager.get_data()

for row in sheet_data:

    city = flight_search.get_iata(row["city"].lower())
    row["iataCode"] = city["locations"][0]["code"]
    data_manager.update_data(str(row["id"]), "iataCode", city["locations"][0]["code"])

    flights_info = flight_search.get_flight_info(row["iataCode"])

    flight_data.add_data(flights_info, row["iataCode"])
    lowest_price_flight = flight_data.lowest_prices(row["iataCode"])

    if lowest_price_flight.price < row["lowestPrice"]:
        notification_manager.send_message(lowest_price_flight)
