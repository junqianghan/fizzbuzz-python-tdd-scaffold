
def transform(num):
    ret=''
    if num % 3 == 0:
        ret+='Fizz'
    if num % 5 == 0:
        ret += 'Buzz'
    if ret:
        return ret
    else:
        return str(num)