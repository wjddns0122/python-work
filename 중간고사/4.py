INDUK = {'university' : '대학교',
         'studen': '학생',
         'information': '정보',
         'communication' : '통신',
         'department' : '학과',
         'study': '공부',
         'program': '프로그램',
         'python': '파이썬'}


def create_induk_dictionary():
    induk_dictionary = dict(sorted(INDUK.items()))
    return induk_dictionary


def english_korean_dictionary(dictionary):
    print("영한 사전")
    for word, meaning in dictionary.items():
        print(word, ":", meaning)


def korean_english_dictionary(dictionary):
    print("한영 사전")
    for word, meaning in dictionary.items():
        print(meaning, ":", word)

def select_menu():
    print("메뉴를 선택하세요:")
    print("1. INDUK 사전 생성")
    print("2. 영한 사전")
    print("3. 한영 사전")
    menu = int(input("메뉴 번호를 입력하세요: "))
    return menu


def search_english_korean_dictionary(dictionary):
    print("영어 단어를 입력하세요:")
    word = input()
    if word in dictionary:
        print(dictionary[word])
    else:
        print("그런 영어 단어가 사전에 없습니다!")


def search_korean_english_dictionary(dictionary):
    print("한글 단어를 입력하세요:")
    word = input()
    found = False
    for korean, english in dictionary.items():
        if korean == word:
            print(english)
            found = True
            break
    if not found:
        print("그런 한글 단어가 사전에 없습니다!")

## 메인 함수 부분 ##
def main():
    induk_dictionary = {}
    while True:
        menu = select_menu()

        if menu == 1:
            induk_dictionary = create_induk_dictionary()
            print("INDUK 사전이 생성되었습니다.")

        elif menu == 2:
            english_korean_dictionary(induk_dictionary)
            search_english_korean_dictionary(induk_dictionary)

        elif menu == 3:
            korean_english_dictionary(induk_dictionary)
            search_korean_english_dictionary(induk_dictionary)

        else:
            print("잘못된 메뉴 번호입니다. 다시 입력해주세요.")
        
        print()

main()
