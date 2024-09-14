char_map = { " ":" " ,"a":"1" ,"b":"3" ,"c":"+", "d":"0" , "e":"9" , "f":"7" , "g":"!", "h":"5", "i":"@", "j":">","k":"-", "l":"?" ,"m":"#", "n":"$", "o":"^", "p":"%", "q":"2", "r":"&", "s":"*", "t":"4", "u":"8", "v":"=", "w": "6" , "x":"<", "y":"/", "z":"_" }
input_string = str(input("암호화 할 내용 입력>>" ))

output_string = "".join([char_map[char] for char in input_string])
print(output_string)  
