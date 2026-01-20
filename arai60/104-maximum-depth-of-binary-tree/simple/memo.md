# 104. Maximum Depth of Binary Tree

## Link

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/21

## Comments

### Step 1

再帰で左と右の node が none かどうか見ていって none じゃなかったら max depth を increment して max を取ればいけるなーと思ったが時間が来てしまったので解ききれず、、

### Step 3

#### Solution 1

なるほどー。与えられた関数自体を再帰として使用すればめちゃコード量少なく書けるなー。。

#### Solution 2

127. Word Ladder とコードの構造が似ている。BFS だとかなり同じようなコードになるんだなーと。
