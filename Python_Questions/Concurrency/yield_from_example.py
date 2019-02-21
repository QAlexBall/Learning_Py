def gen_func():
    a = yield 1
    print("a: ", a)
    b = yield 2
    print("b: ", b)
    c = yield 3
    print("c: ", c)
    return "finish"

def gen_func2():
    for i in range(4, 10):
        d = yield i
        print("d: ", d)
    return "finish2"

def middle():
    gen = gen_func()
    gen2 = gen_func2()
    ret = yield from gen # 会接收send()传递过来的参数并传给gen的yield
    print("ret: ", ret)
    ret2 = yield from gen2
    print("ret2: ", ret2)
    return "middel Exception"

def main():
    mid = middle()
    for i in range(10, 20):
        if i == 10:
            print(mid.send(None))   # send()需要先传入一个None初始化 
        else:
            try:
                print(mid.send(i))  # send()接收一个来自yield的参数
            except StopIteration as e:
                print("e: ", e)

if __name__ == '__main__':
    main()