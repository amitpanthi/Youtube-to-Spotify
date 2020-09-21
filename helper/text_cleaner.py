import re

def clean(string_list):
	for i in range(0, len(string_list)):
		string_list[i] = re.sub(r"[\(].*|[\|].*|\[.*\]", " ", string_list[i])
		string_list[i] = string_list[i].strip()

	return string_list