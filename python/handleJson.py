import json
filename='data.json'
try:
	with open(filename) as f_obj:
		data = json.load(f_obj)
		#print(data)
except FileNotFoundError:
	print('File not found')

handledJson = {}
def hJson(json_data):
	if(isinstance(json_data, dict)):
		kl = list(json_data.keys())
		for k in kl:
			if (k == 'currency' or k == 'name'):
				json_data.pop(k)
				print('=====================')
				continue
			elif (isinstance(json_data[k], dict)):
				print("%s : %s"%(k,json_data[k]))
				hJson(json_data[k])
			elif (isinstance(json_data[k], list)):
				for kk in json_data[k]:
					hJson(kk)
			else:
				print("%s : %s"%(k,json_data[k]))
	else:
		print("json1  is not josn object!")
        
hJson(data)

with open('output.json', 'w') as json_obj:
	json.dump(data, json_obj, indent=2)

