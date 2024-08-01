from data_manager import *  # Importing data management functions
from flight_search import *  # Importing flight search functions
from flight_data import *  # Importing flight data classes
from datetime import *  # Importing date and time functions
from notification_manager import *  # Importing notification functions
import time  # For adding delays

# Initialize instances for flight search, data management, and notifications
flightSearch = FlightSearch()
dataManager = DataManager()
notificationManager = NotificationManager()

# Retrieve main data and customer emails
sheet_data = dataManager.get_data()  # Main data from the sheet
customer_data = dataManager.get_customer_emails()  # Customer email list
customer_email_list = [row["whatIsYourEmail?"] for row in customer_data]  # Extract emails

# Update sheet data with real IATA codes
for city in sheet_data:
    cityName = city['city']
    id = city['id']
    data = {
        'price': {  
            'iataCode': flightSearch.fetch_iata_code(cityName)  # Fetch IATA code
        }
    }
    dataManager.put_data(data=data, id=id)  # Update sheet with new IATA code

# Refresh data with updated IATA codes
sheet_data = dataManager.get_data()

# Set origin city and date range for flight search
ORIGIN_CITY_IATA = "IAD"
tomorrow = datetime.now() + timedelta(days=1)  # Date for tomorrow
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))  # Date for six months from today

# Search for flights and notify if cheaper flights are found
for destination in sheet_data:
    print(f"Getting direct flights for {destination['city']}...")
    flights = flightSearch.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)  # Find the cheapest flight
    print(f"{destination['city']}: £{cheapest_flight.price}")
    
    time.sleep(2)  # Delay to avoid rate limit

    # If a cheaper flight is found, send notifications
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        if cheapest_flight.stops == 0:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly direct "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                      f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                      f"with {cheapest_flight.stops} stop(s) "\
                      f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."

        print(f"Check your email. Lower price flight found to {destination['city']}!")
        notificationManager.send_whatsapp(message_body=message)  # Send WhatsApp notification
        notificationManager.send_emails(email_list=customer_email_list, email_body=message)  # Send email notifications
