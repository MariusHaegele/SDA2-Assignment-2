Text Processing Tool Setup Guide
-------------------------

This document explains how to run the text processing tool in the terminal. Please follow the instructions carefully to ensure the tool runs successfully.


Requirements
------------
Python 3.6 or higher must be installed on the computer in order to run the tool. 

Check if Python is already installed:
Open a terminal (or the command prompt on Windows).
Enter the command "python --version" or "python3 --version".
If a version is displayed (e.g. Python 3.9.5), Python is already installed.

If Python is not installed:
Visit the official Python website: https://www.python.org.
Download and install the latest stable version.

Check the installation:
Repeat step 1 to ensure that Python has been installed correctly.


Instructions
------------
1. Open a terminal of your choice.

2. Navigate to the text_tool folder:
   cd path/to/text_tool

3. Inside the folder, you’ll find two text documents:
   input.txt
   output.txt

You can either use the example text provided in input.txt or enter your own text. Make sure to save your changes.

3. Run the following command in the terminal:
   python main.py

4. Once the text tool starts, you will be prompted to select both an input and an output file. When prompted to confirm the selection of the output file, choose "yes."

5. The text from the input file will then be displayed in the terminal under "Loaded text." Below this, you will see the various processing options offered by the tool.

6. Choose a processing option by entering its corresponding number. If you want to apply multiple processing options at once, separate the numbers with a comma.

7. The tool will process the selected options sequentially. For certain options, you may be prompted to make additional selections. Follow the instructions and provide the required input when prompted.

8. Once all selected processes are completed, the individual results will be displayed directly in the terminal. The results will also be saved in the chosen output file.

9. At the end, the tool will ask if you want to process another file. Respond with "yes" to use the tool again. If you type "no," the tool will exit with a goodbye message.


