def print_hello():
    print('hello world')

def print_hello_new(who):
    print('hello ' + who)

if __name__=='__main__':
    name = 'china'
    print_hello()
    print_hello_new(name)
