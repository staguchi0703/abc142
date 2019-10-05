# 
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\D\D_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# 
# 以下ペースト可
# start 21:14
a, b = [int(item) for item in input().split()]

# 素因数リスト
import math
def factor(num):
    divisor_list = [1]
    divisor = 2
    max_prime = int(math.sqrt(num))
    while max_prime >= divisor:
        if num % divisor == 0:
            divisor_list.append(divisor)
            num //= divisor

        else:
            divisor += 1
    divisor_list.append(num)
    return divisor_list

# 最大公約数
def gcd(a, b):
    while b > 1:
        a, b = b, a & b
    return a

cd_list = set(factor(gcd(a, b)))

print(len(cd_list))

