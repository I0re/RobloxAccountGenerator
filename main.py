import random
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import customtkinter as ctk
from customtkinter import *
from tkinter import messagebox

class RandomRobloxUser:
    def __init__(self, password) -> None:
        self.password = password
        self.generate_user()
        self.birth_day = random.randint(1, 30)
        self.birth_month = random.randint(1, 12)
        self.birth_year = str(random.randint(1970, 2009))

    def generate_user(self):
        while True:
            first_name, last_name = self.generate_names()
            random_number = random.randint(1, 99999)
            self.user_name = f"{first_name}{last_name}{random_number}"
            if len(self.user_name) <= 20:
                break

    def generate_names(self):
        with open("first_names.txt", 'r') as f:
            first_names = f.readlines()
        with open("last_names.txt", 'r') as f:
            last_names = f.readlines()
        first_name = random.choice(first_names).strip()
        last_name = random.choice(last_names).strip()
        return first_name, last_name

def create_accounts(num_accounts, password, headless_var):
    current_working_directory = os.path.dirname(__file__)
    chrome_driver_path = os.path.join(current_working_directory, "chromedriver.exe")
    chrome_service = Service(executable_path=chrome_driver_path)

    # Setup Nopecha extension
    nopecha_extension_path = os.path.join(current_working_directory, "NopeCHA.crx")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension(nopecha_extension_path)

    if headless_var:
        chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get("https://roblox.com")

    for _ in range(num_accounts):
        random_user = RandomRobloxUser(password)

        wait = WebDriverWait(driver, timeout=100)
        birth_month = Select(wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#MonthDropdown"))))
        birth_month.select_by_index(random_user.birth_month)
        birth_day = Select(driver.find_element(By.CSS_SELECTOR, "#DayDropdown"))
        birth_day.select_by_index(random_user.birth_day)
        birth_year = Select(driver.find_element(By.CSS_SELECTOR, "#YearDropdown"))
        birth_year.select_by_value(random_user.birth_year)
        username = driver.find_element(By.CSS_SELECTOR, "#signup-username")
        username.send_keys(random_user.user_name)
        password_input_field = driver.find_element(By.CSS_SELECTOR, "#signup-password")
        password_input_field.send_keys(random_user.password)
        gender = driver.find_element(By.CSS_SELECTOR, random.choice(["#FemaleButton", "#MaleButton"]))
        gender.click()
        time.sleep(6)
        signup_button = driver.find_element(By.CSS_SELECTOR, "#signup-button")
        wait.until(EC.element_to_be_clickable(signup_button))
        signup_button.click()
        wait.until(EC.url_changes(driver.current_url))

        roblox_cookie = driver.get_cookie(".ROBLOSECURITY")
        if roblox_cookie:
            roblox_cookie_value = roblox_cookie["value"]
        with open("accounts.txt", "a") as f:
            f.write(f"usr: {random_user.user_name}\n")
            f.write(f"pass: {random_user.password}\n")
            if roblox_cookie:
                roblox_cookie_value = roblox_cookie["value"]
                f.write(f"cookie: {roblox_cookie_value}\n\n")
            else:
                print("Failed to retrieve Roblox security cookie.")

        time.sleep(6)

        gear_icon = driver.find_element(By.CSS_SELECTOR, "#nav-settings")
        gear_icon.click()
        time.sleep(5)
        logout_button = driver.find_element(By.CSS_SELECTOR, "#settings-popover-menu > li:nth-child(5) > a")
        logout_button.click()
        time.sleep(5)
        selectors21 = [
            "#rbx-body > div:nth-child(164) > div.fade.verification-modal.in.modal > div > div > div.modal-footer > div > button.change-email-button",
            "#rbx-body > div:nth-child(165) > div.fade.verification-modal.in.modal > div > div > div.modal-footer > div > button.change-email-button"
        ]
        logout_step2_button = None
        for selector in selectors21:
            try:
                logout_step2_button = driver.find_element(By.CSS_SELECTOR, selector)
                break  # Exit the loop if the element is found
            except NoSuchElementException:
                continue  # Try the next selector if element not found

        if logout_step2_button:
            logout_step2_button.click()
        else:
            print("Logout step 2 button not found.")
        time.sleep(5)
        signup_button1 = driver.find_element(By.CSS_SELECTOR, "#sign-up-button")
        signup_button1.click()
        time.sleep(5)

    driver.quit()

def create_accounts_gui():
    def submit():
        try:
            num_accounts = int(num_accounts_entry.get())
            password = password_entry.get()
            enable_headless = headless_var.get() == 1
            create_accounts(num_accounts, password, enable_headless)
            messagebox.showinfo("Success", f"{num_accounts} accounts created successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    root = CTk()
    root.title("Roblox Account Creator")
    icon_path = os.path.join(os.path.dirname(__file__), "assets", "icon.ico")
    root.iconbitmap(icon_path)
    root.geometry("330x230")
    root.configure(bg="#333")  # Background color
    root.resizable(False, False)  # Make the window non-resizable

    set_appearance_mode("dark")  # Set dark theme

    frame = CTkFrame(master=root, width=200, height=200)
    frame.grid(row=0, column=0, sticky="nsew")

    num_accounts_label = CTkLabel(frame, text="Number of Accounts:")
    num_accounts_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    num_accounts_entry = CTkEntry(frame)
    num_accounts_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    password_label = CTkLabel(frame, text="Password for Accounts:")
    password_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    password_entry = CTkEntry(frame, show="")
    password_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    headless_label = CTkLabel(frame, text="Enable Headless Driver:")
    headless_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    headless_var = ctk.IntVar()
    headless_checkbox_yes = CTkCheckBox(frame, text="Yes", variable=headless_var, onvalue=1, offvalue=0)
    headless_checkbox_yes.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    submit_button = CTkButton(frame, text="Submit", command=submit)
    submit_button.grid(row=3, columnspan=2, padx=10, pady=10)

    frame.rowconfigure(0, weight=1)  # Make rows expandable
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.columnconfigure(0, weight=1)  # Make columns expandable
    frame.columnconfigure(1, weight=1)

    root.grid_rowconfigure(0, weight=1)  # Make root widget expandable
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()

if __name__ == "__main__":
    create_accounts_gui()