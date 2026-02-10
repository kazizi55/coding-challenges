# 198. House Robber

## Link

https://leetcode.com/problems/house-robber/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/35

## Comments

### Step 1

解けず。今のループの数字とそれ以降の全ての数字の大小を比較することにならないか？それをどうsum upしていくのかがイメージできなかったので答えを見る。なるほど、index2から始めて2つ前の合計と今回の数字を足したものと1つ前の合計を比較して大きい方をとる、とすればDPで溶けるのかー。

### Step 3

#### Solution 1

ボトムアップの解法。メインのロジックさえわかればシンプル。

#### Solution 2

トップダウンの解法。内容はSolution 1と変わらない。cacheがないと時間切れになる。
