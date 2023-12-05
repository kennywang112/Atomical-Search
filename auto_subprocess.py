import subprocess
import json
import random
import re

lst = []
verified = []

name = "capybaras"
Json_path = ""
satsbyte = "20"

random_order = random.sample(range(10), 10)

for index in random_order:

    first_template = 'yarn cli get-container-item "#{}" "{}"'
    first = first_template.format(name, index)
    
    first_res = subprocess.run(first, shell = True, stdout = subprocess.PIPE, text = True)

    match = re.search(r'\{.*\}', first_res.stdout, re.DOTALL)

    if match:
        # find json part
        json_string = match.group()
        json_object = json.loads(json_string)

    else:

        print("No valid JSON found in the string.")

    if json_object['data']['status'] == "null":

        second_template = 'yarn cli mint-item "#{}" "{}" "{}" item-{}.json --satsbyte={}'
        second = second_template.format(name, index, Json_path, index, satsbyte)

        second_res = subprocess.run(str(second), shell=True, stdout=subprocess.PIPE, text=True)

        # lst.append(index)
        print("unverify id :", index)

    else:

        print("verified id:", index)
        # verified.append(index)
        # continue



# print(lst)
# print(verified)


