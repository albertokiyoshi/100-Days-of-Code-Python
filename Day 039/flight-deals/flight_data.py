import time
import pandas


class FlightData:
    def __init__(self):
        self.all_flights = {}

    def add_data(self, flights_info, iata_code):
        flights_list = []
        for flight in flights_info["data"]:
            flight_info = {
                "id": flight["id"],
                "iata_from": flight["flyFrom"],
                "iata_to": flight["flyTo"],
                "city_from": flight["cityFrom"],
                "city_to": flight["cityTo"],
                "price": flight["price"],
                "outbound": time.strftime("%Y-%m-%d", time.localtime(flight["dTime"])),
                "inbound": time.strftime("%Y-%m-%d", time.localtime(flight["aTime"])),
            }
            flights_list.append(flight_info)
        flights_list_df = pandas.DataFrame(flights_list)
        self.all_flights[iata_code] = flights_list_df

    def lowest_prices(self, iata_code_destination):
        sorted_flights = self.all_flights[iata_code_destination].sort_values(by="price", ascending=1)
        return sorted_flights.iloc[0]
