# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answers = []
    words = s.split(" ")
    tmp = False

    for i in range(len(words)):
        if words[i] == "":
          answers.append("")
          continue
        else:
          a = ""
          for j in range(len(words[i])):
            if j == 0:
              if tmp == True:
                a += words[i][j].lower() 
              else:
                a += words[i][j].upper()
            else:
              a += words[i][j].lower()
          answers.append(a)
    return ' '.join(answers)
