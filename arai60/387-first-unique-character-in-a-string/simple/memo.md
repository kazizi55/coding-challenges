# 387. First Unique Character in a String

## Link

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/15

## Comments

### Step 1

文字と index の dict とダブった文字を格納する set を作り、入力文字列を for 文で操作していく解法。Time Complexity: O(n), Space Complexity: O(n)
これしか解法が浮かばなかったので、もっと浮かぶようにしたい。

### Step 3

#### Solution 1

入力文字列を for 文で回して文字と頻度の dict を作成し、再度入力文字列で for 文を回して頻度が 1 のものを見つけ次第 index を返す。Space Complexity が Step1 のものよりも少ないが、Time Complexity は 2O(n)になる。

#### Solution 2

collections.Counter を使う解法。Solution 1 と同じだが、ライブラリを使ってより記述量少なく表現できる。
