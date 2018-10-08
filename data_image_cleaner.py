import re
import urllib
import os
import random


dir_path = os.path.dirname(os.path.realpath(__file__))

images_path = dir_path + '/latina/'

# Define the list from links list in autoswiper only right!
c = []

clean = filter(None,c)

link_list = []
final_list = []

for i in clean:
	link = re.search("(?P<url>https?://[^\s]+)", i).group("url")
	clean_link = re.sub(r'"\);','',link)
	link_list.append(clean_link)
	for num in link_list:
		if num not in final_list:
			final_list.append(num)

for i in final_list:
	name_of_file = str(random.randint(1,123912931)) + '.jpeg'
	complete_name = images_path + name_of_file
	print(complete_name)
	urllib.urlretrieve(i,complete_name)

print(len(final_list))
print(len(c))