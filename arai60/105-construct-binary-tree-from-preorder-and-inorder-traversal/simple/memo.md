# 105. Construct Binary Tree from Preorder and Inorder Traversal

## Link

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/29

## Comments

### Step 1

基本的に preorder を見つつ、どの node の子かどうかを inorder を見て判定すればいいと理解。
が、10 分くらい経ってしまい埒があかないので答えを見る。

### Step 3

#### Solution 1

pre-order で親をきめつつ、in-order でその親の子が何に当たるかを left の index と right の index を絞り込みながら探索している。

#### Solution 2

Solution1 とほぼ同じだが、dict ではなく inorder.index()を使う version。
inorder の traverse が O(1)から O(n)になるので基本的には Solution1 で解きたいところ。
