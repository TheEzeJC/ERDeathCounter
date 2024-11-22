# ERDeathCounter
Program used to keep track of deaths through Elden Ring Co-Op playthrough This program was created in an attempt to keep track of the deaths by two players in Elden Ring. The [Death Counter for OBS](https://www.nexusmods.com/eldenring/mods/2989) does a great job, but does not have the ability to keep track of summon deaths. After getting donowalled after asking for help to modify the program to include the ability to keep track of summon deaths, I made my own version implementing the program.

This program runs off Python and a program created by Kam1k4dze named [Death Counter for OBS](https://www.nexusmods.com/eldenring/mods/2989)
To install you need:
1.Elden Ring + A Friend To Play With
2. Some IDE to run Python. I choose Visual Studio Code IDE
3. The "keyboard" library installed using "pip install keyboard" in Windows CMD
4. [Death Counter for OBS](https://www.nexusmods.com/eldenring/mods/2989)
5. An online file host. In my case I utilized DropBox.
6. The files in this repo

Before moving on, let's quickly explain how this program works. Initially the program was developed using Java, but due to the limitations of using keybinds and the previous [Pokemon Program Made](https://github.com/TheEzeJC/ShinyPokemonAutomation) it made more sense to use Python to update the counter. When using the [Death Counter for OBS](https://www.nexusmods.com/eldenring/mods/2989) program, the program creates a "deaths.txt" file to keep track and display the deaths on OBS. We utilize this file to keep track of the deaths outside of summoning. Using this file, the death amount was extracted and a program was created in Python to add/remove deaths manually using keyboard inputs. This allows us to add the summon deaths manualy. By using the cloud service, our friend is able to upload their correspoding death file. This allows us to display their deaths alongside ours in a file named "Deaths_Modified.txt" This file is used on OBS to display user and friend deaths in the format: Deaths: (Your Deaths) (Friend Deaths)

Some design notes:
- The files have to manually be refreshed. There probably is a method to do it automatically, but I worked around this issue by making the counter update every time we input a new value or when we use the "Refresh Bind" which only reloads the death counter files.
- The program is desined for only 2 players but can possibly be expanded for more.
- Each person has to run the program in a different folder to avoid counter conflict. The only thing shared betwen both is the "death.txt" file generated through the program.
- The program utlizes functions to redcue the file size and increase readability.
- Program functions great with a Stream Deck to simplify inputs.

Future Redesigns:
- Automatically update in realtime everytime a file updates. Ex: Friend dies and the program automatically updates the output file.
- idk lol
