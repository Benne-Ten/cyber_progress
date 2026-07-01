import subprocess

result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
result = result.stdout
lst_result = result.split("\n")
nb_result = 0
for item in lst_result:
	nb_result += 1
print(nb_result)
