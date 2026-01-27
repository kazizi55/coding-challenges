# 98. Validate Binary Search Tree

## Link

https://leetcode.com/problems/validate-binary-search-tree/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/28

## Comments

### Step 1

うーん、pre-order で一層ずつ見ていくからこれも BFS だろうか。
あれ、77 / 86 testcases passed だ。時間切れになってしまったので答えを見る。
なるほど、直近の親だけではなくて、先祖と比べても大きい・小さいを判断する必要があったのかー。そもそも BST の理解が甘かった、、
[5,4,6,null,null,3,7]の時とかは False になるということ。

### Step 3

#### Solution 1

DFS で再帰で解く version。コード量少なくかけてスッキリ。参照先 PR で書かれているように、binary search 的な感じで分岐してみていくことで先祖と比べることができている。MAX_VALUE と MIN_VALUE の定義の仕方は勉強になった。

#### Solution 2

DFS で stack を使う version。個人的にはこっちの方が再帰よりも処理を追いやすい。
node_stack という変数名に若干違和感あり(low と high も入っていることを明示したい)だが、一旦これでいく

#### Solution 3

BFS の version。同じく node_queue という変数名に若干違和感ありだが一旦これでいく。

#### Solution 4

DFS を再帰で in-order で行う version。nonlocal は初めて使った。nonlocal がないと、Python は min_node_val = node.val を「新しいローカル変数の作成」とみなしてしまう。
