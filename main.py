import zxcvbn
import speedtest
import random
import string
import os
import psutil
import platform

# Banner
def show_banner():
    print("""
    ╔══════════════════════════════════════════════╗
    ║             MULTI-UTILITY TOOL               ║
    ║ Password | Generator | Network Speed | Games ║
    ║             Fast. Simple. Reliable.          ║
    ╚══════════════════════════════════════════════╝
              Created by Alankrita Singh Chauhan
              
    """)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_menu():
    print("""
    ------------------- MENU -------------------
    1. Password Strength Checker
    2. Password Generator
    3. Network Speed Tester
    4. System Information Viewer
    5. Number Guessing Game
    6. Exit
    --------------------------------------------
    """)

def analyze_password_strength():
    print("\nPassword Strength Checker - Powered by Alankrita")
    password = input("Enter the password to analyze: ").strip()
    if not password:
        print("Please enter a valid password.")
        return
    result = zxcvbn.zxcvbn(password)
    score = result['score'] * 25
    feedback = result['feedback']['suggestions']
    print(f"\nStrength Score: {score}/100")
    print(f"Suggestions: {' '.join(feedback) if feedback else 'Password is acceptable, but adding more complexity is recommended.'}\n")

def create_password():
    print("\nPassword Generator - Powered by Alankrita")
    try:
        length = int(input("Enter desired password length (e.g., 12): "))
        if length < 4:
            print("Password length should be at least 4 characters.")
            return
        include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        include_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        characters = string.ascii_letters
        if include_numbers:
            characters += string.digits
        if include_special:
            characters += string.punctuation
        
        password = "".join(random.choice(characters) for _ in range(length))
        print(f"\nGenerated Password: {password}\n")
    except ValueError:
        print("Please enter a valid number for the length.")

def measure_network_speed():
    print("\nNetwork Speed Tester - Powered by Alankrita")
    try:
        print("Performing speed test, please wait...")
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1024 / 1024
        upload_speed = st.upload() / 1024 / 1024
        ping_time = st.results.ping
        print(f"\nDownload Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")
        print(f"Ping: {ping_time:.2f} ms\n")
    except Exception as e:
        print(f"An error occurred: {e}. Please check your internet connection and try again.")

def system_info():
    print("\nSystem Information Viewer - Powered by Alankrita")
    try:
        # OS Details
        print(f"Operating System: {platform.system()} {platform.release()}")
        print(f"Processor: {platform.processor() or 'N/A'}")
        # CPU Usage (with permission handling)
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"CPU Usage: {cpu_usage}%")
        except PermissionError:
            print("CPU Usage: N/A (Permission denied for CPU stats)")
        except Exception as e:
            print(f"CPU Usage: N/A (Error: {e})")
        # RAM Usage
        try:
            ram = psutil.virtual_memory()
            print(f"RAM Usage: {ram.percent}% ({ram.used / 1024 / 1024:.2f} MB used of {ram.total / 1024 / 1024:.2f} MB)")
        except Exception as e:
            print(f"RAM Usage: N/A (Error: {e})")
        # Disk Usage
        try:
            disk = psutil.disk_usage('/')
            print(f"Disk Usage: {disk.percent}% ({disk.used / 1024 / 1024 / 1024:.2f} GB used of {disk.total / 1024 / 1024 / 1024:.2f} GB)")
        except Exception as e:
            print(f"Disk Usage: N/A (Error: {e})")
    except Exception as e:
        print(f"An error occurred: {e}. Some system information may be unavailable.")

def number_guessing_game():
    print("\nNumber Guessing Game - Powered by Alankrita")
    print("Guess the number between 1 and 100! You have 7 attempts.")
    secret_number = random.randint(1, 100)
    attempts = 7
    try:
        while attempts > 0:
            guess = input(f"\nEnter your guess (1-100, {attempts} attempts left): ").strip()
            try:
                guess = int(guess)
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue
                attempts -= 1
                if guess == secret_number:
                    print(f"\nCongratulations! You guessed the number {secret_number} correctly!")
                    print("Alankrita says: You're a legend! 🎉")
                    return
                elif guess < secret_number:
                    print("Too low! Try a higher number.")
                else:
                    print("Too high! Try a lower number.")
                if attempts == 0:
                    print(f"\nGame Over! The number was {secret_number}.")
                    print("Alankrita says: Better luck next time! 😎")
            except ValueError:
                print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")

def main():
    clear_screen()
    show_banner()
    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()
        
        if choice == "1":
            analyze_password_strength()
        elif choice == "2":
            create_password()
        elif choice == "3":
            measure_network_speed()
        elif choice == "4":
            system_info()
        elif choice == "5":
            number_guessing_game()
        elif choice == "6":
            print("\nExiting the Multi-Utility Tool. Goodbye from Alankrita!")
            break
        else:
            print("\nInvalid option. Please select a number from 1 to 6.")
        
        input("Press Enter to return to the menu... ")
        clear_screen()
        show_banner()

if __name__ == "__main__":
    try:
        main()
    except ImportError as e:
        print(f"Dependency error: {e}")
        print("Please install the required libraries by running:")
        print("pip install zxcvbn speedtest-cli psutil")
