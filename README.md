# ABTester
ABTester is a comparative tool designed for evaluating sets of images by allowing users to select their favorites through a straightforward interface. This utility is especially useful for subjective analysis of image sets, including but not limited to assessing the output of different epochs or versions of an AI model. By facilitating an unbiased preference selection process, ABTester helps identify the most appealing images within a dataset according to the user's perspective.

# Installation
It is always recommended to set up a [Virtual Environment](https://github.com/MNeMoNiCuZ/venv_create) first. Follow the instructions there, or create one yourself.

Install the requirements from `requirements.txt` using `pip install -r requirements.txt`.

# Launching
Run `launcher.bat`, or `py app.py`.

If successful, it should launch the flask server, and the website, and it should ask you the number of images in each set. To test it out, enter `4` here.

![image](https://github.com/MNeMoNiCuZ/ABTester/assets/60541708/388538c3-8b7b-43d7-92fa-88adbc722676)


# Image Setup
To prepare your images for testing, place them in the `/static/IMAGES/` directory. The tool supports both PNG and JPG formats. Image loading is sequential; thus, the naming convention of the files is significant for the testing sequence. Here is the expected naming format to organize image sets:

- `01.jpg` for Set 1
- `02.jpg` for Set 2
- `03.jpg` for Set 3
- `04.jpg` for Set 4
- `05.jpg` returns to Set 1
- `06.jpg` for Set 2, and so forth, following the pattern: 1, 2, 3, 4, 1, 2, 3, 4, etc.

This naming scheme ensures that images are grouped and presented in sets for comparison.

![image](https://github.com/MNeMoNiCuZ/ABTester/assets/60541708/60663171-a86b-4416-af4b-b8f94abd945e)

# Usage
To initiate the comparison tool:

1. Execute the `launcher.py` script. This action starts a Flask server and opens the tool in your web browser.
2. Upon reaching the landing page, input the total number of image sets you're comparing. This number should correspond to the grouping sequence established in your image setup.
3. Utilize the interface buttons to navigate through the testing process. Options include restarting the test, toggling set number visibility, and revealing the aggregated results of your selections.

![image](https://github.com/MNeMoNiCuZ/ABTester/assets/60541708/e8a91261-1746-4610-af2b-ffda5d1708c8)

The tool's design ensures a user-friendly experience for efficiently conducting image preference tests.

![image](https://github.com/MNeMoNiCuZ/ABTester/assets/60541708/1a3661ac-e022-4467-879f-cc6b3fc00151)

# Example Uses
![image](https://github.com/MNeMoNiCuZ/ABTester/assets/60541708/847b3b08-f723-49e6-a036-eab9c18d4d7b)
![image](https://github.com/MNeMoNiCuZ/ABTester/assets/60541708/2bb9eb42-e0f8-426e-87dd-13cf50a8c0a4)
![image](https://github.com/MNeMoNiCuZ/ABTester/assets/60541708/2e7842ab-6e56-40c4-8934-7c1825814d9b)
![image](https://github.com/MNeMoNiCuZ/ABTester/assets/60541708/fdf86ed3-c551-4b53-93b7-43d24c45a2be)
