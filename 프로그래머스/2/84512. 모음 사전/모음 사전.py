index = 0
found = False

def solution(word):
    # 사용할 모음 리스트
    words = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(current_word):
        global index, found
        

        if current_word == word:
            found = True
            return


        if len(current_word) < 5:
            for w in words:
                if found:
                    return
                index += 1
                dfs(current_word + w)

    dfs('')
    
    return index