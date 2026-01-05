def words(book_text):
		split_text = book_text.split()
		num_words = len(split_text)
		return num_words

def num_characters(book_text):
    book_text = book_text.lower()
    num = {}
    for x in book_text:
        if x not in num:
            num[x] = 1
        else:
            num[x] += 1
    return num

def helper(item):
    return item["num"]

def final_list(book_text):
    counts = num_characters(book_text)
    results = []
    for letter, count in counts.items():
        empty_list = {"char": letter, "num": count}
        results.append(empty_list)
    results.sort(key=helper, reverse=True)
    return results 