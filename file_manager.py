import os

# שאלה 1
files = os.getcwd()
print(files)

# שאלה 2
files = os.listdir()
print(files)


# שאלה 3
def list_and_return(target_path):
    original_path = os.getcwd()
    print(f"נתיב התחלתי: {original_path}")
    os.chdir(target_path)
    print(f"עברנו לתיקייה: {os.getcwd()}")
    print("--- תוכן התיקייה ---")
    contents = os.listdir()
    print(*contents)
    os.chdir(original_path)
    print(f"---חוזרים לתיקייה המקורית ---\n{os.getcwd()}")


#
target_dir = ("C:\\Users\\User\\Desktop\\kodkod\\python")
list_and_return(target_dir)


# שאלה 4
def print_all_files_recursive(target_path):
    for root, dirs, files in os.walk(target_path):
        for filename in files:
            print(filename)


print_all_files_recursive(target_dir)


# שאלה 5
def print_all_files_recursive(target_path):
    list_of_py = []
    for root, dirs, files in os.walk(target_path):
        for filename in files:
            if filename.endswith(".py"):
                list_of_py.append(filename)
    return list_of_py


print(print_all_files_recursive(target_dir))


# שאלה 6
def print_all_files_recursive(target_path):
    dict_files = {}
    counter_py = 0
    counter_txt = 0
    counter_pdf = 0
    for root, dirs, files in os.walk(target_path):
        for filename in files:
            if filename.endswith(".py"):
                counter_py += 1
            elif filename.endswith(".txt"):
                counter_txt += 1
            elif filename.endswith(".pdf"):
                counter_pdf += 1
    dict_files["files of python"] = counter_py
    dict_files["files of pdf"] = counter_pdf
    dict_files["files of txt"] = counter_txt
    return dict_files


print(print_all_files_recursive(target_dir))


# שאלה 7
def find_large_files(target_path, size):
    list_big = []
    files = os.listdir(target_path)
    for file in files:
        full_path = os.path.join(target_path, file)
        if os.path.isfile(full_path):
            if os.path.getsize(full_path) > size:
                list_big.append(file)
    return list_big


print(find_large_files(target_dir, 5))


# שאלה 8
def find_duplicates(path):
    files_dict = {}
    for root, dirs, files in os.walk(path):
        for filename in files:
            full_path = os.path.join(root, filename)
            if filename in files_dict:
                files_dict[filename].append(full_path)
            else:
                files_dict[filename] = [full_path]
    duplicate_dict = {}
    for names, pates in files_dict.items():
        if len(pates) > 1:
            duplicate_dict[names] = pates

    return duplicate_dict


print(find_duplicates(target_dir))
