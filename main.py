import sys
from stats import words, num_characters, final_list

def get_book_text(filepath):
	with open(filepath, "r") as f:
		file_contents = f.read()  
		return file_contents

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	book_text = get_book_text(book_path)
	num_words = words(book_text)
	sorted_chars = final_list(book_text)
	print("============ BOOKBOT ============")
	print("Analyzing book found at /home/ziga/workspace/github.com/ZigaSL/bookbot/main.py...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for item in sorted_chars:
		char = item["char"]
		count = item["num"]
		if not char.isalpha():
			continue
		print(f"{char}: {count}")
	print("============= END ===============")
print(sys.argv)
main()