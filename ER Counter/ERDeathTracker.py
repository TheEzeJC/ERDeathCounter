import keyboard

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
manualCounter = 0 # Program Counter
# 1 for Eze, 2 for Carlos
# 2 for Carlos
userID = 2 # Switch User

# Functions
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

def loadCounter(filePath):
    global manualCounter
    try:
        with open(filePath, 'r') as file:
            content = file.read()  # Read the entire file content
            manualCounter = int(content[8:].strip()) # Gather Only Deaths and convert to int
            #print("Tracked Deaths: " + str(manualCounter))
    except FileNotFoundError:
        print(f"File not found: {filePath}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Creates new death file
def create_new_death_file(death_count, additional_deaths, selectedUser, filePath):
    try:
        # Calculate the total death count
        total_deaths = death_count + additional_deaths
        #print("Total deaths: " + str(total_deaths))
        tracker_file_name = "Modified_Deaths.txt"
        counter_file_name = "counter.txt"
        file_path_with_name = filePath + "\\" + tracker_file_name
        file2_path_with_name = filePath + "\\" + counter_file_name

        # Create and write to the file
        with open(file_path_with_name, 'w') as file:
            if (selectedUser == 1):
                file.write(f"Deaths: {total_deaths} ({carlosDeaths})\n")
                print(f"Deaths: {total_deaths} ({carlosDeaths})")
            elif (selectedUser == 2):
                file.write(f"Deaths: {total_deaths} ({ezeDeaths})\n")
                print(f"Deaths: {total_deaths} ({ezeDeaths})")
            else:
                print("Invalid selectedUser value")  # Handle invalid user
                return  # Return to exit the function or handle the error as needed   
        with open(file2_path_with_name, 'w') as file:
            file.write(f"Deaths: {additional_deaths}\n")
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
    global manualCounter
    manualCounter += 1

    # Refresh Deaths
    loadDeathFile(deathFile_path1, 1) # Eze
    loadDeathFile(deathFile_path2, 2) # Carlos

    if (userID == 1):
        saveCounter(manualCounter, newDeathFile1)
        create_new_death_file(ezeDeaths, manualCounter, userID, newDeathFile1)
    elif (userID == 2):
        create_new_death_file(carlosDeaths, manualCounter, userID, newDeathFile2)
        saveCounter(manualCounter, newDeathFile2)
    else:
        print("Invalid selectedUser value")  # Handle invalid user
        return  # Return to exit the function or handle the error as needed

# Decreases death counter total
def decrease_counter():
    global manualCounter
    manualCounter -= 1

    # Refresh Deaths
    loadDeathFile(deathFile_path1, 1) # Eze
    loadDeathFile(deathFile_path2, 2) # Carlos

    if (userID == 1):
        saveCounter(manualCounter, newDeathFile1)
        create_new_death_file(ezeDeaths, manualCounter, userID, newDeathFile1)
    elif (userID == 2):
        create_new_death_file(carlosDeaths, manualCounter, userID, newDeathFile2)
        saveCounter(manualCounter, newDeathFile2)
    else:
        print("Invalid selectedUser value")  # Handle invalid user
        return  # Return to exit the function or handle the error as needed

# Update Tracker without adding/removing deaths
def reset_tracker():
    # Refresh Deaths
    loadDeathFile(deathFile_path1, 1) # Eze
    loadDeathFile(deathFile_path2, 2) # Carlos

    if (userID == 1):
        saveCounter(manualCounter, newDeathFile1)
        create_new_death_file(ezeDeaths, manualCounter, userID, newDeathFile1)
    elif (userID == 2):
        create_new_death_file(carlosDeaths, manualCounter, userID, newDeathFile2)
        saveCounter(manualCounter, newDeathFile2)
    else:
        print("Invalid selectedUser value")  # Handle invalid user
        return  # Return to exit the function or handle the error as needed

# Start of program
# Gather information to fill variables
loadDeathFile(deathFile_path1, 1) # Eze
loadDeathFile(deathFile_path2, 2) # Carlos

# Create death files based on previously saved counter and current variables
if (userID == 1):
    loadCounter(counter_path1)
    create_new_death_file(ezeDeaths, manualCounter, userID, newDeathFile1)
elif(userID == 2):
    loadCounter(counter_path2)
    create_new_death_file(carlosDeaths, manualCounter, userID, newDeathFile2)
else:
    print("Invalid selectedUser value")  # Handle invalid user

# Register the hotkey
keyboard.add_hotkey('alt+6+7', increase_counter)
keyboard.add_hotkey('alt+4+5', decrease_counter)
keyboard.add_hotkey('alt+4+7', reset_tracker)
print("")
print("Press 'Alt + 6 + 7' to INCREASE the counter (even in the background).")
print("Press 'Alt + 4 + 5' to DECREASE the counter (even in the background).")
print("Press 'Alt + 4 + 7' to REFRESH the counter (even in the background).")
print("Press 'Esc + 4' to exit.")
# Wait until 'esc+4' is pressed to exit the program4
keyboard.wait('esc+4')
