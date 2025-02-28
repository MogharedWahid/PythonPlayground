import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 30.045949
MY_LONG = 30.984135
EMAIL = "my_email@example.com"  # Replace with your email
PASSWORD = "my_password"  # Replace with your email password

def is_iss_nearby():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    # Check if the ISS is within ±5 degrees of my position
    return (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and \
           (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)

def is_it_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 2  # Adjust for timezone
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 2  # Adjust for timezone
    time_now = datetime.now()
    if sunrise < time_now.hour < sunset:
        return False
    return True

def send_email():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject:Look Up!\n\nThe ISS is above you in the sky!"
        )



while True:
    if is_iss_nearby() and is_it_dark():
        send_email()
    time.sleep(60)
  
