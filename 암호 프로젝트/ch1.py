char_map = { " ":" " ,"a":"1" ,"b":"3" ,"c":"+", "d":"0" , "e":"9" , "f":"7" , "g":"!", "h":"5", "i":"@", "j":">","k":"-" ,"l":"?", "m":"#", "n":"$", "o":"^", "p":"%", "q":"2", "r":"&", "s":"*", "t":"4", "u":"8", "v":"=", "w": "6" , "x":"<", "y":"/", "z":"_" }

  
inverted_char_map = {v: k for k, v in char_map.items()}

# 변환할 문자열
encoded_string = str(input("복호화 할 내용을 입력>>"))

# 반전된 딕셔너리를 사용해 다시 변환
decoded_string = "".join([inverted_char_map[char] for char in encoded_string])

print(decoded_string)