ss = input("문자열 입력 : ")

if ss.isalpha():
    print("글자입니다.")
else:
    if ss.isdigit():
        print("숫자입니다")
    else:
        if ss.isalnum:
            print("글자 + 숫자입니다.")