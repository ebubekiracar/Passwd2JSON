import json
import os

passwd_file = open("/etc/passwd")
passwd_keys =['Username','Password','UID','GID','GECOS','Home','Shell']
data = {}
for f in passwd_file:
  line = f.strip().split(":")
  passwd_values = {}
  for j in range(len(passwd_keys)):
    passwd_values[passwd_keys[j]] = line[j]
    data[line[0]] = passwd_values
passwd_file.close()
json_data = json.dumps(data, indent=4)
print(json_data)
jsonfile = open("etcpasswd.json", "w+")
jsonfile.write(json_data)
jsonfile.close()
json_file_path = os.path.abspath("etcpasswd.json")
print("\033[32mProcess completed!\033[0m\n\033[33mFile path:\033[0m", json_file_path)
