def palindrome_index (q: int, s: str):
    for cases in range(q):
        if s == s[::-1]:
            print(-1)
        else:
            found = False
            index = 0
            while not found and index < len(s):
                compair_s = s[:index] + s[index+1:]
                if compair_s == compair_s[::-1]:
                    found = True
                    print(index)
                    break
                else:
                    index += 1
            if not found:
                print(-1)
            

palindrome_index(int(input()), input())




