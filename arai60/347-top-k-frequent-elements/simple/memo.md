# 347. Top K Frequent Elements

## Link

https://leetcode.com/problems/top-k-frequent-elements/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/9

## Comments

### Step 1

5 分以内に解けなかった。Kth Largest Element in a Stream のように heapq を使えば解けそうなことはわかるが、頻度をどう記録するかについて富豪プログラミング的な方法しか思い浮かばなかった。

### Step 3

入力配列の数字を key にした頻度を格納する object を作って、sorted (https://docs.python.org/3/library/functions.html#sorted) を使って頻度順に sort した配列を k 個まで返せば解ける。
あるいは、sorted を使わずに、頻度順に heapq を使って降順で並び替えて、k 個まで pop して返す方法もある。
