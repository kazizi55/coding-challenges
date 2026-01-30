# 53. Maximum Subarray

## Link

https://leetcode.com/problems/maximum-subarray/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/32

## Comments

### Step 1

nums のそれぞれの index での subarray の最大値を二重ループを回して解く形がいいかなと思ったが、時間をかけすぎていたので答えを見る。

### Step 3

#### Solution 1

なるほど、累積和を標高に例えて、最も小さかった時と現時点での差を見れば、自分がどれくらい高く登って行ったかがわかるということか。
prefix sum = 累積和という意味。

#### Solution 2

kadane のアルゴリズム(今の累積和と今の index の数字を比べて多い方を割り当てる)を DP に当てはめて解く方法。一つ前を見ながら辞書を塗りつぶしていって最後に max を返す手法はかなり DP っぽいなと思った。
ちなみに INITIAL_VAL に 0 ではなく-math.inf を使うのは出てくる値よりもかならず小さい値にするため。最大値を求めるときはそれを使うといい。

#### Solution 3

kadane のアルゴリズムを使いつつ、global sum の変数を用意して DP っぽくない形で解く方法。シンプルでわかりやすい。
