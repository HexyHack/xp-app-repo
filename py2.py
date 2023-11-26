import urllib.request

def download_application(app_name, url):
    print(f"Downloading {app_name}...")
    urllib.request.urlretrieve(url, f"{app_name}.zip")
    print(f"{app_name} downloaded successfully!\n")

def main_menu():
    print("Simple Application Downloader")
    print("1. Download App 1")
    print("2. Download App 2")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        download_application("App 1", "https://example.com/app1.zip")
    elif choice == '2':
        download_application("App 2", "https://example.com/app2.zip")
    elif choice == '3':
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        main_menu()

if __name__ == "__main__":
    main_menu()