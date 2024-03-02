# это ужааас а не задача😭😭😭 зачем такое надо оно не работает

import os
import threading

def process_file(filename):
    new_filename = filename.replace('hi.txt', 'hi_modified.txt')
    with open(filename, 'r') as f:
        data = f.read()
    data = data.replace('старое', 'новое')
    with open(new_filename, 'w') as f:
        f.write(data)

def main():
    files = [f for f in os.listdir() if f.endswith('.txt')]
    threads = []
    for filename in files:
        thread = threading.Thread(target=process_file, args=(filename,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()