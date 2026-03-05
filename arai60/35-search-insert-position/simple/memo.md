# 35. Search Insert Position

## Link

https://leetcode.com/problems/search-insert-position/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/41

## Comments

### Step 1

うーん、アルゴリズムは覚えているが書き方を忘れているな、、targetがある区間に向けて配列を半分にし続けていくイメージ。

> If not, return the index where it would be if it were inserted in order

これむずいな。どうやるんだろう。答えを見る。

なるほど、base caseがなかったのと、子に渡すときにmid - 1とmid +1を渡す必要があったのかー。より深く理解できて良かった。

### Step 3

#### Solution1

興味深い。ほぼ同じアルゴリズムだが、Step1は閉区間で、この解法は右半開区間で解いている。
あと、以下のように処理を書かなくてもif start == endで拾える。そのように処理をかくと、targetと同値の数字が連続していた場合に任意の(真ん中の)場所に挿入されることになるので、厳密にはbisect_leftとは違う挙動になる。

```py
  if nums[mid] == target:
      return mid
```

#### Solution2

Step1のRevisedSolutionと同じく閉区間だが、nums[mid] == targetの文を消してターゲットと同値が続いている場合に左端を返すように修正。

#### Solution3

右半開区間をwhile loopで実装。
この方がcall stackを考えなくていいから考えることが少し減るかもしれない。
