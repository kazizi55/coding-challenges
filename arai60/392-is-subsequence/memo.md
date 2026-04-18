# 392. Is Subsequence

## Link

https://leetcode.com/problems/is-subsequence/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/58

## Comments

### Step 1

- sがtの元の順番を保持しながら0個を含む任意の文字数を削除した文字列かどうかを判別する感じだな。
- 当然だけど、s in tだと元の順番を保持しながらという条件に反するのでWA
- tをloopで回して、sと一致するかを順番に見ていくのが良さそう
- ACになったけど、if s_index == len(s)が二個あるのがredundantであまり美しくないな。ああ、if s == ''を入れるだけで1つにできた。

### Step 3

#### Solution 1

- if s_index == len(s)だったらTrue、if t_index == len(t)になったらFalseというの対称性があって好みだなー。
- 同様にif s[s_index] == t[t_index]ならindexを共に+1して、そうでなければt_indexだけ足すというのも対称性があっていい。

#### Solution 2

- 対称性という点ではこちらも負けてないなー
- が、他の問題でも感じたように、こちらの方が引き継ぎ感は少ないな。工場とかで作業している人たちがイメージしやすい再帰の方が好みかも。

#### Solution 3

- RevisedSolutionと同じ。
- if s == ''というガード節がいるのがぎこちなく感じてきた。
