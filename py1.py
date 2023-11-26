import urllib.request

def download_application(app_name, url):
    print(f"Downloading {app_name}...")
    urllib.request.urlretrieve(url, f"{app_name}.zip")
    print(f"{app_name} downloaded successfully!\n")

def main_menu():
    while True:
        print("Simple Application Downloader")
        print("1. App 1")
        print("2. App 2")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            app_menu("App 1", "https://example.com/app1.zip")
        elif choice == '2':
            app_menu("App 2", "https://example.com/app2.zip")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def app_menu(app_name, app_url):
    while True:
        print(f"\n{app_name} Menu")
        print("1. Download")
        print("2. Back to Main Menu")

        app_choice = input("Enter your choice (1 or 2): ")

        if app_choice == '1':
            download_application(app_name, app_url)
        elif app_choice == '2':
            print(f"Returning to the main menu.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main_menu()