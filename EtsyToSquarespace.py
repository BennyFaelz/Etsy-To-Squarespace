#2019 BennyF
import csv

with open('etsy.csv', 'r') as csv_file: #you can change etsy.csv to whatever your file is called
	csv_reader = csv.reader(csv_file)

	next(csv_reader, None) #skips header row

	with open('new_squarespace.csv', 'w') as new_file: #you can change new_squarespace.csv to whatever you want the output file to be named
		csv_writer = csv.writer(new_file)

		#writes Squarespace header
		csv_writer.writerow(['Product URL', 'Title', 'Description', 'Product Type', 'Tags', 'Categories', 'Visible', 'Hosted Image URLs', 'SKU', 'Option Name 1', 'Option Value 1', 'Option Name 2', 'Option Value 2', 'Option Name 3', 'Option Value 3', 'Price', 'Sale Price', 'On Sale', 'Weight', 'Length', 'Width', 'Height', 'Stock'])

		n = 0

		for line in csv_reader:
			if n != 200:
				n = n + 1
				title = line[0]
				url = "python/" + title.replace(" ", "-") #You can change this to whatever you want it to be
				description = line[1]
				type = "Physical"
				tags = line[5]
				Categories = "python" #Etsy does not have categories but you can set all your imported ones to have the same category to easily search for them
				Visible = "FALSE"
				Images = line[7] + "\r" + line[8] + "\r" + line[9] + "\r" + line[10] + "\r" + line[11] + "\r" + line[12] + "\r" + line[13] + "\r" + line[14] + "\r" + line[15] + "\r" + line[16]
				SKUN = 60000 + n #I don't use SKU's on my shop so I set them to a random number.
				SKU = "SQ" + str(SKUN)
				Price = line[2]
				Stock = "Unlimited" #I like having everything set to unlimited, but you can get etsy stock by setting it to line[4]


				print(title)
				print(n)
			
				#This program does not work with options/variants
				csv_writer.writerow([url, title, description, type, tags, Categories, Visible, Images, SKU, '', '', '', '', '', '', Price, '', '', '', '', '', '', Stock])
			else:
				print("Max of 200 has been reached. There is still " + str(sum(1 for line in csv_reader)) + " remaining rows.")
input("Press Enter to exit...")