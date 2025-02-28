# ISS Overhead Notifier
![ISS Overhead Notifier](https://github.com/MogharedWahid/PythonPlayground/blob/main/Intermediate/iss_overhead_notifier/ISS_Egypt.jpg)

This Python script sends you an email notification whenever the International Space Station (ISS) is overhead and it's dark outside. 

## How it Works

The script uses the following APIs and libraries:

* **Open Notify API:** Fetches the current location of the ISS.
* **Sunrise-Sunset API:** Determines sunrise and sunset times for your location.
* **`requests` library:** Makes HTTP requests to the APIs.
* **`datetime` library:** Handles time calculations.
* **`smtplib` library:** Sends emails using your Gmail account.
* **`time` library:** Pauses the script execution for a specified time.

**Logic:**

1.  **Check ISS proximity:** The script checks if the ISS is within 5 degrees of your latitude and longitude.
2.  **Check for darkness:** It determines if it's currently dark outside based on your location's sunrise and sunset times.
3.  **Send email notification:** If both conditions are met, it sends an email to your specified address.
4.  **Repeat:** The script runs continuously, checking every 60 seconds.

## Tools and Lessons Applied

* **API integration:** The project demonstrates how to interact with external APIs to retrieve data.
* **Data processing:** It involves parsing JSON responses and extracting relevant information.
* **Time management:** The script uses `datetime` to work with time data and `time` to control the execution frequency.
* **Email automation:** It shows how to automate email sending using `smtplib`.
* **Conditional logic:** The script's behavior is based on conditions like ISS proximity and darkness.

## Setup and Usage

1.  **Install required libraries:**
    ```bash
    pip install requests
    ```

2.  **Replace placeholders:**
    * Update `MY_LAT` and `MY_LONG` with your actual latitude and longitude.
    * Replace `EMAIL` and `PASSWORD` with your Gmail credentials.

3.  **Run the script:**
    ```bash
    python main.py 
    ```

**Note:** You might need to enable "Less secure app access" in your Gmail account settings for the email sending to work.

This project is a great example of how to combine different Python libraries and APIs to create a useful and fun application. It can be further extended with features like:

* **Customizable notification radius:** Allow users to define the proximity range for ISS notifications.
* **GUI interface:** Create a user-friendly interface for easier configuration.
* **Different notification methods:** Explore other notification options like SMS or push notifications.
