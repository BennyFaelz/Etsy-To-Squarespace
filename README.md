# Etsy-To-Squarespace
Turns your Etsy Sale Listing CSV into a usable Squarespace Products CSV

This is the first project I ever wrote in Python so it's probably not the best coding, but it works.

I created this project because the import button for Etsy on Squarespaces website does not work. I emailed them to make them aware of of this problem, however they have still not fixed it after about 6 months.

## How ToUe
- [Download your shops Etsy Sale Listing CSV.](https://help.etsy.com/hc/en-us/articles/360000343508-How-to-Download-Your-Listing-Information?segment=selling)
- Place you Etsy Sale Listing CSV into the folder with the EtsyToSquarespace.py file and rename it to "etsy.csv".
- Run the Python script and a new file, "new_squarespace.csv", will be created
- You can upload the file to Squarespace by going to Home -> Settings -> Advanced -> Import/Export -> Import -> Products via .csv and then uploading your new file

## Important Nots
- ~~THIS PROJECT DOES NOT WORK WITH IMAGES!! At this time I have not figured out a way to make images to work~~ I'm dumb just tried this again and now it works
- YOU CAN ONLY IMPORT UP TO 200 LISTINGS AT A TIME INTO SQUARESPACE. The program will automatically stop at 200 so Squarespace can accept the new CSV.
- Support not guaranteed

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
