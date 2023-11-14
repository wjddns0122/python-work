inStr = '<<<파<<이>>썬>>>'
outStr = ""

for i in range(0, len(inStr)):
    if inStr[i] not in ['<', '>']:
        outStr += inStr[i]

print('원래 문자열 ==> ' + '[' + inStr + ']')
print('공백 삭제 문자열 ==> ' + '[' + outStr + ']')
