#モジュールのインポート
import re
import collections
#keyとvalueの要素を入れるlistの作成
rep_finds_key = []
rep_finds_value = []
#text = "\nfruit\tapple\nfruit\tbanana\nbeverage\t\nfruit\tbanana\nbeverage\tcoke\npet\tdog\n"
#tsvの読み込み
input_tsv = input('tsvを入力してください')
with open(input_tsv) as f:
    text = f.read()
#最初と最後を\nの状態にする
if text[:1] != "\n":
    text = "\n"+text
if text[-1:] != "\n":
    text = text+"\n"
#rep_finds_keyとrep_finds_valueに要素を入れる
def make_list():
    #findallで要素を引っ張る
    finds_key = re.findall("\n.*?\t", text)
    finds_value = re.findall("\t.*?\n",text)
    #keyとvalueそれぞれ整形してlistに入れる
    for find in finds_key:
        find = find.replace('\n',"")
        find = find.replace('\t',"")
        rep_finds_key.append(find)
    for find in finds_value:
        find = find.replace('\n',"")
        find = find.replace("\t","")
        rep_finds_value.append(find)
#keyのそれぞれの要素の数をcountしてkeysに入れる
def count():
    global keys
    counter = collections.Counter(rep_finds_key)
    keys = [k for k,v in counter.items()]
#正規化したtsvを作る
def make_tsv():
    #output.tsvというファイルを作リ書き込んでいく
    text_file = open("output2.tsv","wt")
    #keyのそれぞれの要素の数に対してループを回す
    for k in range(len(keys)):
        #keyのそれぞれの要素に対して最初のvalueには":"をつけないためroupeという変数を作り区別する
        roupe = 0
        #まずkeyを書き込む
        text_file.write("\n"+keys[k]+"\t")
        #keyの一つ一つの要素に対してループを回す
        for i in range(len(rep_finds_key)):
            #一つ目のループで焦点を置いている要素に対し一致する場合以下のコードを実行する
            if rep_finds_key[i] == keys[k]:
                key_set = keys[k]+str(i)
                #最初のvalueの場合":"はつけない
                if roupe == 0:
                    data_line = rep_finds_value[i]
                #それ以外は":"をつける
                else:
                    data_line = ":"+rep_finds_value[i]
                text_file.write(data_line)
                roupe += 1
#main()関数を定義
def main():
    make_list()
    count()
    make_tsv()
#実行
if __name__ == '__main__':
    main()
