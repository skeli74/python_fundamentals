strings = input().split(" ")
palindrome = input()
palindrome_list = []

for word in strings:
    if word == word[::-1]:
        palindrome_list.append(word)

counter_palindrome = palindrome_list.count(palindrome)
print(palindrome_list)
print(f"Found palindrome {counter_palindrome} times")
