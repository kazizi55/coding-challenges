# 252. Meeting Rooms

## Link

https://leetcode.com/problems/meeting-rooms/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/56

## Comments

### Step 1

- intervalの中の数字を見ていって、時間の重複がなければTrue、あればFalseを返すという感じ
- Constraints的に二重ループだとTLEになりそう
- max_startとmin_endを保持しつつ、for loopの中で各intervalがその中に収まっているかみていく方法がいいかも？
- max_startが現在のstart以上、あるいはmin_endが現在のend以下だったらだめ
- うーん15分経ってしまった。geminiに聞く
- なるほど、時間が進む順にソートした上で、直前の会議が終わった時間だけ保持しておけば解けるのか。

### Step 3

#### Solution 1

- RevisedSolutionと解き方は同じだけど、以下の点が違う
  - intervalsを破壊しない
  - sortのkeyにinterval endを使っている。デフォだとx[0]が使われるが、x[1]でも解ける。同時にどれだけのMTGに参加できるかとかをみる時にはそっちの方がいいのだろう
  - last_interval_endの初期値が-1になっていた。constraintsでstartとendは0以上という話だったからこれで十分か

#### Solution 2  

- startだったら+1、endだったら-1する配列を時間をindexにして作った上で、その累積和が2以上になる瞬間があるかをみる解法。面白い。
- どの大きさの入力であったとしても空間計算量が10 ** 6 + 1になるのはちょっと非効率なのではと思う
- 一方でsort不要なのは嬉しいな
- if prefix_sum == 2でも通りはしたが、全く同じ時刻に会議が始まることもあると思うのでそれを想定して >=とする方が良さそう
