# 8. String to Integer (atoi)

## Link

https://leetcode.com/problems/string-to-integer-atoi/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/60

## Comments

### Step 1

- 2つ目以降は数字しか受け付けない
- 1つ目だけ+と-は許容
  - これを判定するのに2番目も合わせてチェックする必要がある
- whitespaceは無視
- 時間切れ。答えを見る。

### Step 3

- なるほど、orb()を使ってs[index]を比較することで、s[index]が数字の文字列かそうでないかを考慮せずに処理を書くことができる。
- また、indexをincrementさせる形をとることで、条件が色々分かれていてもokだったらindex += 1するのだなとわかりやすくていい。
- stringからintに変える部分、toInt的なものを使うとばかり思っていたので、それもorbを使ってincrementalにできるのは目から鱗だった