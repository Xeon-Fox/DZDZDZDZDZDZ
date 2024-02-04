def get_emoji_from_user(num_emoji):
    if num_emoji:
        return '😭' * num_emoji

def get_max_non_decreasing_sequence_length(numbers: list):
    max_length = 0
    current_length = 1
    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[i-1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
    return max(max_length, current_length)

def find_same_surnames(employees: list):
    surnames = {}
    for employee in employees:
        name, surname = employee.split()
        if surname not in surnames:
            surnames[surname] = []
        surnames[surname].append(name)
    return {surname: names for surname, names in surnames.items() if len(names) > 1}

def find_local_extremes(temperatures):
    extremes = []
    for i in range(1, len(temperatures)-1):
        if temperatures[i-1] < temperatures[i] > temperatures[i+1] or temperatures[i-1] > temperatures[i] < temperatures[i+1]:
            extremes.append((i+1, temperatures[i]))#первое это день а второе температура
    return extremes

def test_all_that():
    assert get_emoji_from_user(5) == "😭😭😭😭😭"
    assert get_emoji_from_user(0) == None
    
    assert get_max_non_decreasing_sequence_length([2,6,5,3,1,2,3,4,5,7]) == 6
    assert get_max_non_decreasing_sequence_length([2,3,4,1]) == 3

    assert find_same_surnames(["Алексей Шевцов", "Ктото Шевцов", "Игорь линк"]) == {'Шевцов': ['Алексей', 'Ктото']}
    assert find_same_surnames(["Алексей Шевцов", "Ктото Шевцов", "Игорь Шевцов", "Шевцов Шевцов"]) == {'Шевцов': ['Алексей', 'Ктото', 'Игорь', 'Шевцов']}

    assert find_local_extremes([16,23,30,21,19]) == [(3,30)]
    print("Все ок")

test_all_that()