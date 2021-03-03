#モジュールのインポート
import re
#リストの作成
colon_loc = []
n_loc = []
t_loc = []
#tsvの読み込み
input_tsv = input('tsvを入力してください')
with open(input_tsv) as f:
    text = f.read()
#最初と最後を\nの状態にする
if text[:1] != "\n":
    text = "\n"+text
if text[-1:] != "\n":
    text = text+"\n"
def find_loc():
    #":","\n","\t"の位置情報の取得
    colon_find = re.finditer(":",text)
    n_find = re.finditer("\n",text)
    t_find = re.finditer("\t",text)
    #それぞれのリストに代入
    for match in colon_find:
        colon_loc.append(match.start())
    for match in n_find:
        n_loc.append(match.start())
    for match in t_find:
        t_loc.append(match.start())
#":"の変換
def replace_word():
    global text
    #":"の数だけループ
    for i in range(len(colon_loc)):
        ndifs = []
        tdifs = []
        #":"から手前の"/n","/t"までの距離を測る
        for loc in n_loc:
            if colon_loc[i]-loc>0:
                dif = colon_loc[i]-loc
                ndifs.append(dif)
        for loc in t_loc:
            if colon_loc[i]-loc>0:
                dif = colon_loc[i]-loc
                tdifs.append(dif)
        #":"の位置がtextの変換によって変わるので改めて位置情報を取得
        re_colon_loc = []
        re_colon_find = re.finditer(":",text)
        for match in re_colon_find:
            re_colon_loc.append(match.start())
        #"/n"と"/t"どちらが近いかによって場合分け
        if min(ndifs, tdifs, key=min) == tdifs:
            #変換するwordの作成
            text1 = text[:re_colon_loc[0]]
            #後ろのwordを引っ張る
            search = re.findall("\n.*?\t", text1)[-1]
            #":"の変換
            text = text.replace(":", search, 1)
        if min(ndifs, tdifs, key=min) == ndifs:
            #変換するwordの作成
            text2 = text[re_colon_loc[0]:]
            search = re.search("\t.*?\n",text2).group()
            #":"の変換
            text = text.replace(":", search, 1)
    #output.tsvというファイルを作リ書き込んでいく
    text_file = open("output1.tsv","wt")
    text_file.write(text)
    print(text)
#main()関数を定義
def main():
    find_loc()
    replace_word()
#実行
if __name__ == '__main__':
    main()
