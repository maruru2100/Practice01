#cording= UTF-8

#pythonでFizzBuzzやってみた
#FizzBuzzの概要：3の倍数で"Fizz"、5の倍数で"Buzz"、3と5の公倍数で"FizzBuzz"を表示し、それ以外は数字を表示する。
#作成日：2018/08/06

print ("FizzBuzz Start")
print ("\r")

#1～49までfor文を回す。考え方は、Javaでいう拡張for文
for x in range(1,50):
	#ブール演算子というらしい。Javaで言う比較の「&&」がpythonだと「and」らしい。
	#これ回りくどく、3と5の余りが"0"の時にしてるけど計算できるなら15の余りが"0"の時とかにしたほうがいいかも
	if x%3 == 0 and x%5 == 0:
		print ("FizzBuzz")
	elif x%5 == 0:
		print ("Buzz")
	elif x%3 == 0:
		print ("Fizz")
	else:
		#xを出力するところだけど、python3の場合()で囲わなきゃならないので注意
		print (x)

print ("\r")
print ("FizzBuzz End")
print ("To be Continue")