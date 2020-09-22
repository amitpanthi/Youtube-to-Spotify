import re

def clean(string_list):
	for i in range(0, len(string_list)):
		string_list[i] = re.sub(r"[\(].*|[\|].*|\[.*\]", " ", string_list[i])
		string_list[i] = string_list[i].strip()

	return string_list

def clean_link(link):
	link = re.sub(r"https.*\&list=|https.*\?list=", '', link)
	return link

print(clean_link("https://www.youtube.com/playlist?list=PL7q6nAW6-CMsgIpYt9hwRycy6lShNf6wP"))