import time

def input_username():
    name = input("your name: ")

    return name

def input_numarr():
    num_arr = []
    while True:
        num = input("please input number: ")
        if num == "q":
            break
        try:
            num = int(num)
            num_arr.append(num)
        except ValueError:
            print("please input number,don't use others type.")
            continue
        print("if you stop this script, please input q.")
    return num_arr

def call_element(name,arr):
    print("Hello,{}.your input:{}".format(name,arr))

def add_func(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum +arr.pop()
    return sum,arr

def timemanager(t):
    e_time = int(time.time()-t)
    print("elapsed time:{}s".format(e_time))


if __name__ == '__main__':
    start_time = time.time()
    name = input_username()
    num_arr = input_numarr()
    call_element(name,num_arr)
    sum,empty_arr = add_func(num_arr)
    print("{},total sum is {}, and arr is {}.".format(name,sum,empty_arr))
    timemanager(start_time)
    print("finished.")
