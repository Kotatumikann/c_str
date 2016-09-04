#!/bin/python
#-*-coding:utf-8-*-

"""
ただ、文字を連結するだけ
"""
def strcat(moji1,moji2):
	moji3=moji1+moji2
	return moji3
"""
lensに文字数を指定することによって
その分を引数1に連結する
"""	
def strncat(moji1,moji2,lens):
	moji_list=list(moji2)
	moji3=""
	for j in xrange(lens):
		moji3+=moji_list[j]
	mojicat=moji1+moji3
	return mojicat
	
def strncpy(moji1,n):
	moji_list=list(moji1)
	moji3=""
	for j in xrange(n):
		moji3+=moji_list[j]
	cp=moji3
	return cp
"""	
文字から特定の文字があるかを判断する
引数1に文字列,引数2に検索対象の文字
あれば,1を返す0ならない
"""
def strsearch(c_string,Searched):
	#検索対象の文字をリスト化する
	moji3=list(c_string)
	#検索対象の文字の長さを取る
	m_moji=len(moji3)
	#検索文字
	k_moji=len(Searched)
	#文字の回数を得る
	kaisu=m_moji/k_moji
	#あまりを計算
	judege=0
	sd=m_moji-k_moji
	dd=kaisu+sd
	#文字を判断する
	for i in xrange(dd):
		smoji=moji3[i:i+k_moji]
		ssmoji="".join(smoji)
		if ssmoji==Searched:
			judege=1
	return judege