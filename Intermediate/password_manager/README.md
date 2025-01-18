# Password Manager
![Password Manager](https://github.com/MogharedWahid/PythonPlayground/blob/main/Intermediate/password_manager/logo.png)

A simple Python-based password manager built using Tkinter for the graphical user interface (GUI). This application allows users to securely store their passwords and associated details, generate strong passwords, and copy them to the clipboard.

## Features
- **Random Password Generator:** Generate strong passwords containing a mix of letters, numbers, and symbols.
- **Secure Storage:** Save website names, associated emails, and passwords in a text file for later use.
- **Clipboard Copy:** Automatically copies the generated password to your clipboard for easy use.
- **Error Handling:** Alerts the user if any required fields are left empty and requests confirmation before saving data.
- **Intuitive GUI:** Built using Tkinter, the interface is simple and user-friendly.

## How to Use

1. **Generate a Password**: 
   - Click on the **"Generate Password"** button to create a random password. 
   - The password will contain a combination of letters, numbers, and symbols.
   - The generated password will automatically be copied to your clipboard.

2. **Enter Website and Email**:
   - Fill in the **Website** and **Email/Username** fields with the appropriate details for the account you wish to save.

3. **Save Data**: 
   - After entering the details, click on the **"Add"** button.
   - You will be prompted to confirm whether you want to save the website, email, and password.
   - The information will be saved to a `data.txt` file.

4. **View Saved Data**: 
   - The saved website, email, and password entries will be stored in the `data.txt` file in the following format:
     ```website_name | email | password```


## Example of `data.txt` File
```
  example.com | user@example.com | A1b2@x3Y
  another-site.com | anotheruser@example.com | F4g5#z6K
```


## Code Overview

### Password Generation
The `generate_pass()` function randomly selects letters, symbols, and numbers to create a secure password. The length of each type is randomized, and the components are shuffled before being joined to form the final password.

### Saving Password
The `add_pass()` function retrieves the website, email, and password entered by the user. It checks if any fields are empty and prompts the user for confirmation before saving the data to a `data.txt` file.

### User Interface
The GUI is created using Tkinter:
- A logo is displayed at the top of the window.
- Fields to input website names, emails, and passwords.
- Buttons to generate passwords and save data.


---

### Happy Password Managing! 🚀
