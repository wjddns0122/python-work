ss = 'I AM A STUDENT OF INDUK UNIVERSITY IN SEOUL KOREA.'

def count_words(string):
    words = string.split()
    return len(words)

def calculate_length(string):
    length = 0
    for _ in string:
        length += 1
    return length

def word_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1])
    for char, count in sorted_frequency:
        print(char, ":", count)

def main():
    word_count = count_words(ss)
    print("단어 수:", word_count)

    string_length = calculate_length(ss)
    print("문자열 길이:", string_length)

    string_frequency = word_frequency(ss)
    print("문자 발생 빈도:", string_frequency)


main()
