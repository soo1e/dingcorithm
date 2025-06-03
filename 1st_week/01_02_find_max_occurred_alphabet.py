"""
Q. 다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오.
(단 최빈값을 가진 알파벳이 여러개일 경우 알파벳 순서가 가장 앞에 위치한 알파벳을 출력하시오)
"""

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26  # 알파벳 개수(26개)만큼 리스트 초기화

    for char in string:
        char = char.lower()  # 대소문자 구분 없이 소문자로 변환
        if 'a' <= char <= 'z':  # 알파벳인 경우만 처리
            alphabet_occurrence_array[ord(char) - ord('a')] += 1  # 등장 횟수 증가

    return alphabet_occurrence_array


print("정답 = [3, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2, 2, 1, 1, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("Hello my name is sparta"))
print("정답 = [2, 1, 2, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("Sparta coding club"))
print("정답 = [2, 2, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 3, 3, 0, 0, 0, 0, 0, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("best of best sparta"))