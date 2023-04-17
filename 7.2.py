import os


def find_file(filename, search_path):
    for root, dir, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None


result = find_file('1.txt', '/Users/username/Document')
print(result)
