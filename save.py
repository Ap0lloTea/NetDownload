import urllib.request
try:
	f = open("img.txt","r+")
	img_url_list = []
	for i in f.readlines():
		img_url_list.append(i.strip("\n"))
except Exception as e1:
	print(e1)
	print("Readfile Error")

count = 0
try:
	for target_url in img_url_list:
		temp_name_list = target_url.split("/")
		filename = temp_name_list[len(temp_name_list)-1]
		with urllib.request.urlopen(target_url, timeout=15) as response, open("./"+filename, 'wb') as f_save:
			f_save.write(response.read())
			f_save.flush()
			f_save.close()
		count+=1
		if count %500 == 0:
			print("Save count: " + str(count))

except Exception as e2:
	print(e2)
	print("Save Error")
