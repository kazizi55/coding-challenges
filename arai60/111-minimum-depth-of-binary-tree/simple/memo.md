# 111. Minimum Depth of Binary Tree

## Link

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/22

## Comments

### Step 1

最短経路なので BFS で行くことはわかり、28 / 53 testcases passed まで行ったが時間切れで解けず、、
あー if node.left is None and node.right is None の and を or で定義していたためだった。`Note: A leaf is a node with no children.`。これが抜けていた、、気をつける。

### Step 3

#### Solution 1

DFS の解法。BFS よりもシンプルに書ける印象。

#### Solution 2

BFS の解法で、depth += 1 を for 文の最後に持ってきて nodes_in_depth の更新タイミングと合わせてみた。こっちの方が自然な感じがする。
