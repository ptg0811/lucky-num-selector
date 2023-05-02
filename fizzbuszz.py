for k in range(1,16+1):
    if k%3==0 or k%5==0:
        print('fizz'*(k%3==0)+'buzz'*(k%5==0))
    else:
        print(f'{k}')
