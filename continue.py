while True:
    s = input('type a word:')
    if s == 'quit':
        break
    elif len(s) < 3:
        print('Too small,type a longer word')
        continue
    print('Input is of sufficient length:', len(s))
