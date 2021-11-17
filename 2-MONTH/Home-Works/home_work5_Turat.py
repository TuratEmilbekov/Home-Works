import re 

file_path = "MOCK_DATA.txt"
result_file_path = "result1.txt"
file_r = open(file_path, mode="r", encoding="Latin-1")
results_file = open(result_file_path, mode="w", encoding="Latin_1")
my_text = file_r.read()

searching = r"[A-Z][a-z]+\W+\w+\s[A-Z]\w+|[A-Z]+\w+\s[A-Z]+\w+|[A-Za-z][A-Za-z]+\s[A-Za-z][']?[A-Z]\w+"
results_all = re.findall(searching, my_text)

for item in results_all:
    print(item)
    results_file.write(item + "\n")

print(f"Total: {str(len(results_all))}")





file_path = 'MOCK_DATA.txt'
result_file_path = 'result2.txt'
file_r = open(file_path, mode="r", encoding='Latin-1')
result_file = open(result_file_path, mode="w", encoding='Latin_1')
my_text = file_r.read()

searching = r"[\w+_-]@[\w+_-]+.[\w.]+"
result_all = re.findall(searching, my_text)

for item in result_all:
    print(item)
    result_file.write(item + "\n")

print(f'Total: {str(len(result_all))}')





file_path = "MOCK_DATA.txt"
result_file_path = "result3.txt"
file_r = open(file_path, mode="r", encoding="Latin-1")
results_file = open(result_file_path, mode="w", encoding="Latin_1")
my_text = file_r.read()

searching = r"[A-Z]+[a-z]+\w+[.]+[a-z]+[0-9]|" \
            r"[A-Z]+[a-z]+\w+[.]+[a-z]+|" \
            r"[A-Z]+[a-z]+[.]+[a-z]+[0-9]|" \
            r"[A-Z]+[a-z]+[.]+[a-z]+|" \
            r"[A-Z]+[.]+[a-z]+|" \
            r"[A-Z]+[.]+[a-z]+[0-9]"
results_all = re.findall(searching, my_text)

for item in results_all:
    print(item)
    results_file.write(item + "\n")

print(f"Total: {str(len(results_all))}")





file_path = "MOCK_DATA.txt"
result_file_path = "result4.txt"
file_r = open(file_path, mode="r", encoding="Latin-1")
results_file = open(result_file_path, mode="w", encoding="Latin_1")
my_text = file_r.read()

searching = r"#\w+"
results_all = re.findall(searching, my_text)

for item in results_all:
    print(item)
    results_file.write(item + "\n")

print(f"Total: {str(len(results_all))}")
