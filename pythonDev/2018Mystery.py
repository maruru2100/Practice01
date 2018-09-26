#coding: utf-8

#TwitterだかQiitaだかで話題になっていたネタをpythonでやってみた。
#2018年の「2018」は7から始まる12連続整数の平方和であるらしい。
#実際にfor文の練習という事で検証してみた。
#作成日：2018/08/08

#あらかじめ、初期化した合計値入れる変数と、スタート時の平方根を入れておく
ans = 0
root_Namber = 7

#for文で12回回す。range()関数はこういう使い方をする。
for x in range(12):
	#演算子いっぱい使ってるけど、意味はなんとなく分かるっしょ
	ans += root_Namber ** 2
	root_Namber += 1
	#print(ans)

#表示が2018になるはず！！
print(ans)

