# 문자열 데이터를 분석 하기전에 처리함수 만들기
# 1. 공백제거
# 2. 필요 없는 문자 부호 제거
# 3. 대소문자 정리 (Captalization)
import re

states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']

def clean_string(strings):
    results = []

    for string in strings:
        string = string.strip()
        string = re.sub('[!#?]', '',string)
        string = string.title()
        results.append(string)

    return results

states = clean_string(states)
print(states)

###############################################################################

states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']

def clean_strings(strings, *funcs):
    results = []
    for string in strings:
        for func in funcs:
            string = func(string)
        results.append(string)
    return results

def remove_special(s):
    return re.sub('[!#?]','', s)

states = clean_strings(states, str.strip, str.title, remove_special) # 함수를 가져다가 가변으로 놓겠다
print('람다로 바꿈')
states = clean_strings(states, str.strip, str.title, lambda s:re.sub('[!#?]','', s))


print(states)

print("  abc   ".strip())
print(str.strip("  abc  "))
