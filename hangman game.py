# 여기에 코드를 작성해주세요
def hangman(answer):
    life = 8
    letters = []
    aplha = 'qwertyuioplkjhgfdsazxcvbnm'
    
    
    while 1:
        print(f'life : {life}')
        out_letters=' '.join(letters)
        print(f'letters = {out_letters}')
        status_text = status(answer,letters)
        out_status_text=' '.join(status_text)
        print(f'status : {out_status_text}')

        if ''.join(status_text)==answer:
            print('----------------------------')
            print('you win!')
            print('----------------------------')
            return 0
        if life==0:
            print('you lose!')
            print(f'answer : {answer}')
            return 0
        
        c = input('알파벳을 넣으세요 : ')
        if len(c)!=1:
            print("1글자 만 넣으세요")
        elif c in letters:
            print("이미 있는 알파벳입니다.")
        elif c not in aplha:
            print("알파벳 만 넣으세요.")
        else :
            letters.append(c)
            letters.sort()
            if c not in answer:
                life-=1
        print('----------------------------')
        
def status(answer,letters):
    out = []
    for i in range(len(answer)):
        if answer[i] in letters:
            out.append(answer[i])
        else:
            out.append('_')
    return out
    
#------------------------------------------------
if __name__=='__main__':
    hangman('apple')