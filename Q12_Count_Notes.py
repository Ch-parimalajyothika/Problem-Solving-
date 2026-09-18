def count_notes(amount):
    notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    result = {}
    for note in notes:
        count = amount // note
        if count:
            result[note] = count
            amount %= note
    return result

amount = int(input("Enter amount: "))
for note, count in count_notes(amount).items():
    print(note, ":", count)
