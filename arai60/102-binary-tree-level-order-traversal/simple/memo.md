# 102. Binary Tree Level Order Traversal

## Link

https://leetcode.com/problems/binary-tree-level-order-traversal/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/26

## Comments

### Step 1

階層ごとで node の数を入れていく必要があるから BFS がしっくりきた。
その階層の node.val の配列を答えの配列に追加して、次の人に引き継ぎするイメージ。
うーん、queue の中の同じ階層の node を tuple でまとめたいんだけど、1 か 2 の時があってそれをどう分ければいいのかという感じだ、、
時間切れになってしまったので答えを見る。あー while の中で range を使って階層ごとの node の数を判断すればいいのか。あと root node 無視していた、、

### Step 3

#### Solution1

同じく BFS だが、nodes_in_next_depth を nodes_in_depth に代入する手法。この方が現在の階層と次の階層を明示できる。

#### Solution2

Solution1 を元に deque を使う解法で変数に意味を持たせるようにしてみた。
この方が処理がより直感的に感じる。
