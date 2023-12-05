import subprocess

def get_all_wifi_passwords():
    try:
        # Run the command to get all Wi-Fi profiles
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], shell=True, universal_newlines=True)
        
        # Extract profile names
        profiles = [line.split(":")[1].strip() for line in result.split('\n') if "All User Profile" in line]

        # Get and display passwords for each profile
        for profile in profiles:
            password = get_wifi_password(profile)
            print(f"Wi-Fi Password for '{profile}': {password}")

    except subprocess.CalledProcessError:
        print("Error retrieving Wi-Fi passwords.")

def get_wifi_password(profile_name):
    try:
        # Run the command to get Wi-Fi password
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', 'name=' + profile_name, 'key=clear'], shell=True, universal_newlines=True)
        
        # Search for the Key Content line in the result
        key_content_line = [line.strip() for line in result.split('\n') if 'Key Content' in line]
        
        # If Key Content line is found, extract and return the password
        if key_content_line:
            password = key_content_line[0].split(':')[-1].strip()
            return password
        else:
            return "Password not found."

    except subprocess.CalledProcessError:
        return "Error retrieving password."

if __name__ == "__main__":
    get_all_wifi_passwords()

    # Wait for user input before exiting
    input("Press Enter to exit...")
