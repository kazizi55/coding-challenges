# 929.

## Link

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/14

## Comments

### Step 1

+以降と@の前までを strip した文字列が今まで探索した文字列に存在するかをチェックすればいけるなーと思ったが、時間切れ。

### Step 3

#### Solution 1

Time Complexity が O(n^2)の解法。与えられた email の配列を for 文で、それぞれの email の character をさらに for 文で見ていくやり方で straightforward。
解答がもし思いつかなくてもこういう O(n^2)の解法を捻り出すくらいの気持ちで今後の問題は臨みたい。

#### Solution 2

Time Complexity が O(n)の解法。元々自分が解こうとしていたやり方に近い。与えられた email の配列を for 文で回して、その中で email を local と domain にわけ、local を unique な形に整形して set に add していく。ロジックがシンプルで計算量も比較的少なめで好み。

#### Solution 3

Solution2 とほぼ同じだが、正規表現を使うやり方。いろんな問題に応用が効きそう。
