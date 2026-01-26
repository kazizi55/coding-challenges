# 103. Binary Tree Zigzag Level Order Traversal

## Link

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/27

## Comments

### Step 1

102 と同じく BFS が使えそう。うーん、14 / 33 testcases passed だったな、、
あーなるほど、node_values に各階層の val を入れるときに反転させるようにしないと、親子関係とかがチグハグになってしまうのか。

### Step 3

BFS を使うが、nodes_in_next_depth を使う & depth を変数に持ってそれで挿入の reversed かどうかの判定をする解法。
うーん、好みの問題だと思うが、個人的には is_left_to_right のトグル値を明示的に持っておく方がわかりやすいと感じた。
