import time
#モジュールインポート

def input_username():#ユーザーの名前を取得する関数
    name = input("your name: ")#inputがCUIから値を取ってくる
    return name#returnは返り値, この関数を呼ぶとnameの値を取得可能

def input_numarr():#配列取得のための関数
    num_arr = []#空配列の用意,(pythonだとlist)
    while True:#なにもない限りずっと処理を回す無限ループ
        num = input("please input number: ")#数字をinputする
        if num == "q":#押されたkeyがqだったら
            break#ループを抜ける
        try:#エラー処理,tryの中にはしたいことを書く
            num = int(num)#とってきた要素をint型にキャスト
            num_arr.append(num)#配列の中に入れる
        except ValueError:#キャストしようとしてできなかった(number以外の要素が入ってきた)
            print("please input number,don't use others type.")#この文章を表示して
            continue#loopを続ける
        print("if you stop this script, please input q.")#処理を終わらせるための指示メッセージ
    return num_arr#数列を返り値として渡す

def call_element(name,arr):
    print("Hello,{}.your input:{}".format(name,arr))#呼び出すための関数, 普通にprintしても全然OK

def add_func(arr):#足し入れの関数
    sum = 0#からの値
    for i in range(len(arr)):#配列の要素分処理をする
        sum = sum +arr.pop()#popしてそれぞれの値足し入れ
    return sum,arr#合計値と使い終わった, arrをリターン

def timemanager(t):#時間管理の関数, 時間を引数としてとる
    e_time = int(time.time()-t)#開始時間と, 今の時間を引き算して差分の計算
    print("elapsed time:{}s".format(e_time))#経過時間を出力


if __name__ == '__main__':
    start_time = time.time()
    name = input_username()#それぞれの返り値は変数にいれることが可能
    num_arr = input_numarr()
    call_element(name,num_arr)#他の関数で作った値を引数として指定
    sum,empty_arr = add_func(num_arr)
    print("{},total sum is {}, and arr is {}.".format(name,sum,empty_arr))
    #pythonのデバッグはprintだけじゃなくて,formatprintをするとわかりやすいのでオヌヌメ
    timemanager(start_time)
    print("finished.")
