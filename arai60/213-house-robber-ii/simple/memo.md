# 213. House Robber II

## Link

https://leetcode.com/problems/house-robber-ii/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

## Comments

### Step 1

うーん、やはり198. House Robberとほぼ同じようなアプローチだとうまくいかないかー。エッジをどう処理するかが思い浮かばなかったので答えを見る。

### Step 3

#### Solution 1

最初の家と最後の家をそれぞれ除いたmax_amountsを作成して最後にそれらのmax_amounts[-1]を比べて大きい方を答えとする解法。最初と最後をそれぞれ除くことで円環を一つの線として扱うことができる。
素直に全て記述するので若干記述量が多い印象。

#### Solution 2

Solution1がボトムアップだったのに対し、こちらはトップダウン。house robber iと同じだが再帰を二つ並べるかどうかの違いだけ。

#### Solution 3

Solution2の関数を共通化したもの。すっきりしてみやすい。
@cacheを適用するにはhashableなものを引数として渡さないといけないのでtupleにして渡す。

#### Solution 4

ボトムアップにしつつ、二つのパラレルワールドの範囲を関数に渡すようにしたversion。numsを保持しなくて良くなるので空間計算量が節約できるし、intを渡すのでtupleを使う必要もない。
