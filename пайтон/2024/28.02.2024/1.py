import threading

def compute_average(sub_list, results, index):
    results[index] = sum(sub_list) / len(sub_list)

numbers = list(range(0, 10000))

length = len(numbers)
step = length // 4
sub_lists = [numbers[i:i+step] for i in range(0, length, step)]

results = [0] * 4

threads = []

for i in range(4):
    thread = threading.Thread(target=compute_average, args=(sub_lists[i], results, i))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()

average_of_averages = sum(results) / len(results)

print(f"Среднее значение списка: {average_of_averages}")