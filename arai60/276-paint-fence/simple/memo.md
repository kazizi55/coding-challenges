# 276. Paint Fence

## Link

https://leetcode.com/problems/paint-fence/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

## Comments

### Step 1

dynamic programming の問題は初めて解くが、一瞥して数 A の場合分けみたいな印象を抱いた。
再帰を使って解くのがシンプルにできていいのかな。確か dynamic programming って小さい結果を積み上げて大きなものにしていくみたいな概念だったと思うし。
うーん、時間切れになってしまったので答えを見る。

### Step 3

#### Solution 1

なるほど、動的計画法ってこうやって書くのかー。

```
i が直前と違う色 = i - 1 番目までの全パターン x (k - 1)
i が直前と同じ色 = i - 2 番目までの全パターン x (k - 1)
```

これを n まで積み上げていくことで ways_at_index[n]がわかる。

#### Solution 2

事前の結果を記録しないで再帰で積み上げていく解法。@cache を使わないと TLE になる。class の下に cache を定義しているので instance ごとの cache になる。

#### Solution 3

配列ではなく dict を使う version。
問題によってはこっちしか使えないとかもあるのかもしれない。
