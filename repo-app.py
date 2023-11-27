import urllib.request
import time
import sys

def download_application(app_name, url):
    print(f"Downloading {app_name}...")
    # file size
    with urllib.request.urlopen(url) as response:
        file_size = int(response.headers['Content-Length'])

    # download url
    with urllib.request.urlopen(url) as response, open(f"{app_name}.zip", 'wb') as out_file:
        chunk_size = 1024  
        bytes_read = 0

        while True:
            chunk = response.read(chunk_size)
            if not chunk:
                break
            out_file.write(chunk)
            bytes_read += len(chunk)

            print(f"Progress: {bytes_read / file_size * 100:.2f}% ({bytes_read / (1024 * 1024):.2f} MB / {file_size / (1024 * 1024):.2f} MB)", end='\r')

    print(f"\n{app_name} downloaded successfully!\n")

def main_menu():
    while True:
        print("----------------------------------------------------------")
        print("Windows XP Browser Downloader (x32 only!) Build 27.11.23")
        print("by HexyHack")
        print("------------------------------")
        print("1. Mypal 68")
        print("2. NewMoon")
        print("3. NewMoon (for non SSE2 PCs)")
        print("4. Kafan MiniBrowser")
        print("5. 360Chrome")
        print("------------------------------")
        print("6. Exit")
        print("------------------------------")

        choice = input("Enter your choice (number): ")

        if choice == '1':
            app_menu("Mypal 68", "https://github.com/Feodor2/Mypal68/releases/download/68.13.7b/mypal-68.13.7.en-US.win32.zip")
        elif choice == '2':
            app_menu("NewMoon", "https://o.rthost.win/palemoon/palemoon-28.10.7a1.win32-git-20231125-d849524bd-uxp-b47d46219f-xpmod.7z")
        elif choice == '3':
            app_menu("NewMoon (for non SSE2 PCs)", "https://o.rthost.win/palemoon/palemoon-28.10.7a1.win32-git-20231125-d849524bd-uxp-b47d46219f-xpmod-sse.7z")
        elif choice == '4':
            app_menu("Kafan MiniBrowser", "https://archive.org/download/360EE_Modified_Version/MiniBrowser_1.0.0.127_Modified.7z")  
        elif choice == '5':
            app_menu("360Chrome", "https://archive.org/download/360EE_Modified_Version/360EE_13.0.2310.0_Modified.7z")                     
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, etc..")

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