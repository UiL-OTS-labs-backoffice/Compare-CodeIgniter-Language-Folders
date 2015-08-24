# Compare-CodeIgniter-Language-Folders
Compares files in the different language folders that follow the code igniter markup. Gives, per language and then per file, an indication of which keys are missing in any of the other languages.

The script is not flawless, but it makes checking the differences easier than having to go by the entries one by one. 

# How to use
* Go to the project folder of your CodeIgniter website. Go to `applications` --> `language`. 
* Copy all the folders in that directory that you want to compare (for example: `english` and `dutch`), with all the files they contain, into the folder where you placed your `compare.py` script, or place the `compare.py` script into the language folder in your project.
* Run `python compare.py` in a terminal from the directory where your `compare.py` script is located.

# Read the output
The program makes a list of all the languages that were found (equal to the name of the folders). It then creates a list of files, for each of the languages. If any of the files that is present in any of the language folders is not present in any of the other folders, this will be printed to the terminal. 
For each of the files that are present in more than one folder, each of the language keys present in any of the files is checked. If any of the files with the same name in a different language folder lacks that key, the key, the language string, the containing file and all languages which lack the key are printed to the console. 
This is quite a litteral process, so comments that are spelled differently in all the language files will be printed as well.
