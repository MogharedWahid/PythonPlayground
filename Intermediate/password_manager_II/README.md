# Password Manager  
![Password Manager](https://github.com/MogharedWahid/PythonPlayground/blob/main/Intermediate/password_manager/logo.png)

A Python-based password manager application built with Tkinter for a graphical user interface (GUI). It allows users to securely store and retrieve passwords for various websites, as well as generate strong passwords. This version has been updated to use a JSON file for storage, ensuring better data handling and retrieval.

## Features
- **Random Password Generator:** Generate strong passwords containing letters, numbers, and symbols.
- **Secure Storage:** Store website names, associated emails, and passwords in a `data.json` file for secure storage.
- **Clipboard Copy:** Automatically copies the generated password to your clipboard.
- **Search Function:** Quickly search for saved passwords by website name.
- **Error Handling:** Alerts the user if any required fields are left empty or if no data is found for a website.
- **Intuitive GUI:** Built using Tkinter, providing an easy-to-use interface.

## How to Use

1. **Generate a Password**  
   - Click on the **"Generate Password"** button to create a strong random password.  
   - The generated password will automatically be copied to your clipboard.

2. **Enter Website and Email**  
   - Fill in the **Website** and **Email/Username** fields with the appropriate details for the account you wish to save.

3. **Save Data**  
   - After entering the details, click on the **"Add"** button.  
   - If any required fields are empty, the app will alert you to complete them.  
   - The information will be saved to a `data.json` file.

4. **Search for Saved Data**  
   - Enter the **Website** name and click on the **"Search"** button to retrieve the saved email and password for that website.  
   - If no data is found, a notification will inform you.

## Example of `data.json` File
The passwords and account details are stored in a JSON format, which looks like this:
```json
{
  "example.com": {
    "email": "user@example.com",
    "password": "A1b2@x3Y"
  },
  "another-site.com": {
    "email": "anotheruser@example.com",
    "password": "F4g5#z6K"
  }
}
```

## Code Overview
### Password Generation
The `generate_password()` function generates a random password using letters, numbers, and symbols. It shuffles the components to ensure unpredictability and copies the password to the clipboard for easy use.
### Saving Password
The `save()` function collects the website, email, and password entered by the user. It checks if any fields are empty and updates the data.json file with the new information. If the file doesn’t exist, it creates one.
### Searching for Password
The `search()` function allows users to search for a website’s login details. It loads the saved data.json file and looks for the website. If found, it displays the corresponding email and password in a message box.
### User Interface
The GUI is created using Tkinter and includes:
  * A logo at the top of the window.
  * Input fields for the website, email/username, and password.
  * Buttons to generate passwords, add new entries, and search for existing entries.

---

### Happy Password Managing! 🚀
