#coding= UTF-8

#pythonでCSVファイルを読み込んで表示してみた。
#作成日：2018/08/07

#csvのpython標準のライブラリとのこと
import csv

#pythonのメソッドで「def」を使って定義してあげれる。
def readCSV(fldir, headerflg):

	#CSVファイルを開くやつで、引数1=ファイルの場所、引数2=「r」or「w」で読み書き切り替え、後はencoding=開くときの形式、errors=良くわからん、
	#newline=universal newlinesモードの動作を制御します。None, '', '\n', '\r', '\r\n' の指定が可能。
	csv_file = open(fldir, "r", encoding="shift_jis", errors="", newline="" )

	'''
	リスト形式で読み込む
	delimiter フィールド間を分割するのに使用する文字。 
	doublequote フィールド内のquotecharがその文字自身である場合どのようにクオートするか。True の場合、この文字は二重化。 False の場合、 escapechar は quotechar の前に置かれます。 
	escapechar エスケープ用の文字列をしてします。読み込み時、escapechar はそれに引き続く文字の特別な意味を取り除きます。 
	lineterminator writerを使用する際に、各行の終端を表すのに使用する文字。readerでは、'\r' または '\n' を終端とするようにハードコードされているので関係ない。 
	quotechar delimiter や quotechar といった特殊文字を含むか、改行文字を含むフィールドをクオートする際に用いられる 1 文字からなる文字 
	skipinitialspace True の場合、 delimiter の直後に続く空白は無視されます。 
	'''
	f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

	#↓これいらなくね？？
	#hedderflgがあればheaderを読み込んで表示してする
	if headerflg:
		header = next(f)
		print(header)


	#for文で一行ずつ読み込んで表示する。
	for row in f:
		print(row)

	#辞書形式
	#f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

ROUTE_DELIMITER = "\\"
root_driver = "D:"
file_path = "01なんかもらったもの\\201808月\\20180807\\ふるさと"
file_name = "05210F050219920180807H_00000030000011.csv"

#CSVファイルの場所設定
fldir= root_driver + ROUTE_DELIMITER + file_path + ROUTE_DELIMITER + file_name
headerflg = True

#CSVファイルの場所を引数としてreadCSVを呼び出す。
readCSV(fldir, headerflg)


