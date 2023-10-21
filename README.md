# ABTester
An A/B tester for sets of images.

This is a tool where you will have a bunch of images displayed, and you pick your favorite. Repeat this over and over with your image dataset, and see which ones were your favorites.

An example use case is when you have trained an AI model, and you want to get an un-biased test on which epoch/version you think looks better.

# Image Setup
Add your images in the /static/IMAGES/ folder. Supports PNG and JPG. At least.
The images will be loaded sequentially, so the file name matters.
The expected format is:
* 01.jpg (Set 1)
* 02.jpg (Set 2)
* 03.jpg (Set 3)
* 04.jpg (Set 4)
* 05.jpg (Set 1)
* 06.jpg (Set 2)
* 07.jpg (Set 3)
* 08.jpg (Set 4)
* 09.jpg (Set 1)
* 10.jpg (Set 2)
* 11.jpg (Set 3)
* 12.jpg (Set 4)

![image](https://github.com/MNeMoNiCuZ/ABTester/assets/60541708/60663171-a86b-4416-af4b-b8f94abd945e)


Just like when dividing up into teams/groups of people, 1.2.3.4.1.2.3.4.1.2.3.4.

# Usage
Run the launcher.py script to start a flask server and launch the website in your browser.

On the landing page, enter the number of sets you have.
This is the number of images you will compare each time.

![image](https://github.com/MNeMoNiCuZ/ABTester/assets/60541708/e8a91261-1746-4610-af2b-ffda5d1708c8)

Use the buttons below the images to restart, toggle set numbers, or show the results.
![image](https://github.com/MNeMoNiCuZ/ABTester/assets/60541708/1a3661ac-e022-4467-879f-cc6b3fc00151)
