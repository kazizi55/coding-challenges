# 300. Longest Increasing Subsequence

## Link

https://leetcode.com/problems/longest-increasing-subsequence/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/31

## Comments

### Step 1

dynamic programming を適用するなら、「連続している数を index として保存して 1 つ前の index を参照する」と言う形で解けそう。
うーん、時間かけすぎているので一旦答えを見る。難しく考えすぎていたようだ、、

### Step 3

#### Solution 1

なるほど、ここまで簡潔に書けるのか。
最初から最後まで積み上げていかないといけないと思い込んでいたが、こんな感じで 1 つ前よりも大きい時だけ最大値かどうかをチェックして、最後に一番大きい値を max()で求めればグッとシンプルになる。

#### Solution 2

めちゃ興味深い。binary search を使って解くことができるのか。
lis と命名されていた変数は min_ends と名付けるのが良さそう。
それぞれの index に格納されている値が nums の中で見たときに長さが n の階段を作れる最小の最後尾なので。

```
min_ends[0] : 長さ 1 の階段を作れる、最小の最後尾
min_ends[1] : 長さ 2 の階段を作れる、最小の最後尾
min_ends[2] : 長さ 3 の階段を作れる、最小の最後尾
```

このアルゴリズムは patience sort を利用したものらしい。

#### Solution 3

bisect_left を自前実装した version。
