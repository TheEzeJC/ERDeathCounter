import keyboard
import threading

# File Paths
deathFile_path1 = r"E:\Dropbox\Coding\VisualStudio\ER Counter\Eze\deaths.txt"
deathFile_path2 = r"E:\Dropbox\Coding\VisualStudio\ER Counter\Carlos\deaths.txt"
newDeathFile1 = r"E:\Dropbox\Coding\VisualStudio\ER Counter\Eze"
newDeathFile2 = r"E:\Dropbox\Coding\VisualStudio\ER Counter\Carlos"
counter_path1 = r"E:\Dropbox\Coding\VisualStudio\ER Counter\Eze\counter.txt"
counter_path2 = r"E:\Dropbox\Coding\VisualStudio\ER Counter\Carlos\counter.txt"

# Variables
ezeDeaths = 0 # Eze Deaths
carlosDeaths = 0 # Carlos Deaths
manualCounter1 = 0 # Program Counter Eze
manualCounter2 = 0 # Program Counter Carlos
spinAmount = 10
# 1 for Eze, 2 for Carlos
# 2 for Carlos
userID = 1 # Switch User

# Functions
# schedule refresh
def schedule_auto_refresh(interval):
    refresh_tracker()
    threading.Timer(interval, schedule_auto_refresh, [interval]).start()

# Open the original "deaths.txt" files in read mode
def loadDeathFile(filePath, selectedUser):
    global ezeDeaths
    global carlosDeaths
    try:
        with open(filePath, 'r') as file:
            content = file.read()  # Read the entire file content
            if (selectedUser == 1):
                ezeDeaths = int(content[8:].strip()) # Gather Only Deaths and convert to int
                #print("Eze Deaths: " + str(ezeDeaths))
            elif (selectedUser == 2):
                carlosDeaths = int(content[8:].strip()) # Gather Only Deaths and convert to int
                #print("Carlos Deaths: " + str(carlosDeaths))
            else:
                print("Invalid selectedUser value")  # Handle invalid user
                return  # Return to exit the function or handle the error as needed
    except FileNotFoundError:
        print(f"File not found: {filePath}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Loads manually counted deaths from both players
def loadCounter():
    global manualCounter1
    global manualCounter2
    
    # Load Eze
    try:
        with open(counter_path1, 'r') as file:
            content = file.read()  # Read the entire file content
            manualCounter1 = int(content[8:].strip()) # Gather Only Deaths and convert to int
    except FileNotFoundError:
        print(f"File not found: {counter_path1}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Load Carlos
    try:
        with open(counter_path2, 'r') as file:
            content = file.read()  # Read the entire file content
            manualCounter2 = int(content[8:].strip()) # Gather Only Deaths and convert to int
    except FileNotFoundError:
        print(f"File not found: {counter_path2}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Creates Death and Counter files
def create_new_death_file(selectedUser, filePath):
    try:
        tracker_file_name = "Modified_Deaths.txt"
        file1_path_with_name = filePath + "\\" + tracker_file_name # Deaths
        eze_total_deaths = ezeDeaths + manualCounter1 # Automatic + Counnted Deaths
        carlos_total_deaths = carlosDeaths + manualCounter2 # Other players TOTAL deaths

        # Create and write to file that will be used on OBS
        if (selectedUser == 1):
            # Stores the manually stored deaths
            with open(file1_path_with_name, 'w') as file:
                file.write(f"Deaths: {eze_total_deaths} ({carlos_total_deaths})\n")
                if ((eze_total_deaths + carlos_total_deaths)%10 == 0):
                    if(eze_total_deaths + carlos_total_deaths != 0):
                        file.write(f"SPIN!\n")
                        print(f"SPIN!\n")
                print(f"Deaths: {eze_total_deaths} ({carlos_total_deaths})")

        elif (selectedUser == 2):
            # Stores the manually stored deaths
            with open(file1_path_with_name, 'w') as file:
                file.write(f"Deaths: {carlos_total_deaths} ({eze_total_deaths})\n")
                if ((eze_total_deaths + carlos_total_deaths)%10 == 0):
                    if(eze_total_deaths + carlos_total_deaths != 0):
                        file.write(f"SPIN!\n")
                        print(f"SPIN!\n")
                print(f"Deaths: {carlos_total_deaths} ({eze_total_deaths})")
        else:
            print("Invalid selectedUser value")  # Handle invalid user
            return  # Return to exit the function or handle the error as needed   

    except Exception as e:
        print(f"An error occurred: {e}")

# Saves manual count to file to be restored
def saveCounter(count, filePath):
    try:
        file_name = "counter.txt"
        file_path_with_name = filePath + "\\" + file_name

        # Create and write to the file
        with open(file_path_with_name, 'w') as file:
            file.write(f"Deaths: {count}\n")
    except Exception as e:
        print(f"An error occurred: {e}")

# Increases death counter total
def increase_counter():
    global manualCounter1
    global manualCounter2

    # Refresh Deaths
    loadDeathFile(deathFile_path1, 1) # Eze
    loadDeathFile(deathFile_path2, 2) # Carlos
    loadCounter() # Gets up to date counter

    if (userID == 1):
        manualCounter1 += 1
        saveCounter(manualCounter1, newDeathFile1)
        create_new_death_file(userID, newDeathFile1)
    elif (userID == 2):
        manualCounter2 += 1
        saveCounter(manualCounter2, newDeathFile2)
        create_new_death_file(userID, newDeathFile2)
    else:
        print("Invalid selectedUser value")  # Handle invalid user
        return  # Return to exit the function or handle the error as needed

# Decreases death counter total
def decrease_counter():
    global manualCounter1
    global manualCounter2

    # Refresh Deaths
    loadDeathFile(deathFile_path1, 1) # Eze
    loadDeathFile(deathFile_path2, 2) # Carlos
    loadCounter() # Gets up to date counter

    if (userID == 1):
        manualCounter1 -= 1
        saveCounter(manualCounter1, newDeathFile1)
        create_new_death_file(userID, newDeathFile1)
    elif (userID == 2):
        manualCounter2 -= 1
        saveCounter(manualCounter2, newDeathFile2)
        create_new_death_file(userID, newDeathFile2)
    else:
        print("Invalid selectedUser value")  # Handle invalid user
        return  # Return to exit the function or handle the error as needed

# Update Tracker without adding/removing deaths
def refresh_tracker():
    # Refresh Deaths
    loadDeathFile(deathFile_path1, 1) # Eze
    loadDeathFile(deathFile_path2, 2) # Carlos
    loadCounter() # Gets up to date counter

    if (userID == 1):
        create_new_death_file(userID, newDeathFile1)
    elif (userID == 2):
        create_new_death_file(userID, newDeathFile2)
    else:
        print("Invalid selectedUser value")  # Handle invalid user
        return  # Return to exit the function or handle the error as needed

# Start of program
# Gather information to fill variables
loadDeathFile(deathFile_path1, 1) # Eze
loadDeathFile(deathFile_path2, 2) # Carlos
loadCounter() # Load counters with existing information

# Create files based on previously saved counter, current variables, and user
if (userID == 1):
    create_new_death_file(userID, newDeathFile1)
elif(userID == 2):
    create_new_death_file(userID, newDeathFile2)
else:
    print("Invalid selectedUser value")  # Handle invalid user

# Refresh tracker every 30 seconds
schedule_auto_refresh(60)

# Register the hotkey
keyboard.add_hotkey('ctrl+9', increase_counter)
keyboard.add_hotkey('ctrl+8', refresh_tracker)
keyboard.add_hotkey('ctrl+7', decrease_counter)
print("")
print("Press 'Ctrl + 9' to INCREASE the counter (even in the background).")
print("Press 'Ctrl + 8' to REFRESH the counter (even in the background).")
print("Press 'Ctrl + 7' to DECREASE the counter (even in the background).")
print("Press 'Esc + 4' to exit.")
# Wait until 'esc+4' is pressed to exit the program4
keyboard.wait('esc+4')
