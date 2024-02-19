# Roblox Account Generator

The Roblox Account Generator is a Python script that automates the process of creating multiple Roblox accounts. It utilizes the Selenium framework for browser automation to simulate user actions on the Roblox website.

The Chrome Browser Version this was tested on is '121.0.6167.185 (Official Build) (64-bit)'.

## Purpose

The purpose of this project is to simplify the creation of multiple Roblox accounts, which can be useful for various purposes. Instead of manually creating each account, this script allows users to specify the number of accounts they want to create and provides options for customizing account details such as usernames and passwords.

## Features

- **Automated Account Creation**: The script automates the process of creating Roblox accounts by programmatically interacting with the Roblox website using the Selenium framework.
- **Customizable Account Details**: Users can specify the number of accounts to create and customize details such as usernames and passwords for each account.
- **Headless Browser Support**: Users have the option to run the script in headless mode, which means the browser window is not displayed during execution, making it suitable for running in the background.
- **Bypass FunCAPCHA**: Users will not have to worry about FunCapchas ruining the automation of accounts.
- **Stored Accounts**: All made accounts will be stored in a file called "accounts.txt". This will contain the username, password and roblosecurity cookie for ease of access.

## Demo

[![Thumbnail](https://github.com/I0re/RobloxAccountGenerator/assets/95900417/46d3061b-8312-4387-b5f0-b5be7adcf7fb)](https://player.vimeo.com/video/914589420)

<iframe src="https://player.vimeo.com/video/914589420" width="640" height="360" frameborder="0" allowfullscreen></iframe>

## Installation

1. Clone the repository to your local machine:

 ```bash
   git clone https://github.com/I0re/RobloxAccountGenerator.git
 ```

2. Install the required dependencies using pip:

 ```bash
   pip install -r requirements.txt
 ```

## Usage

1. Run the `main.py` script:

```bash
   python main.py
 ```

2. The GUI (Graphical User Interface) will open, allowing you to specify the number of accounts to create, set a password for the accounts, and choose whether to enable headless mode.

3. Click the "Submit" button to start the account creation process. The script will launch a browser window (or run in headless mode) and begin creating the specified number of Roblox accounts.

4. In order to make use of NopeCHA service to bypass FunCapcha the user must register for a plan in NopeCHA to utilize their service.
****
## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
