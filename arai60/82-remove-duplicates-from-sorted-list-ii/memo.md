# 82. Remove Duplicates from Sorted List II

## Link

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/kazizi55/coding-challenges/pull/4

## Comments

### Step 1

- うーん15分かけたけど解けなかったなー。悔しい、、
- node.val == node.next.valだった時にnodeごと消したいのだけどどうやってその前のnodeのnextを書き換えるかで迷って時間を使ってしまった
- 前回解いた時はpreviousとcurrentを使っていたが改めてみると違和感あるな。実質previousが答えの先端で　currentは探査用のnodeなので、　tailとnodeとするのがスッキリするな
- node.next is not None and node.val == node.next.valの条件節はifではなくwhileにする方が一見すると良いと思う。ifとすると都度親のwhileを通ることになるので、重複が連続している時に余計な条件を毎回通るのが冗長に感じるため。が、その条件をifとwhileでダブってネストさせて書かないといけない (continueさせるため、およびダブりが連続しているときの最後のnodeもスキップするため)ので、冗長だなと思うので、やはりval_to_removeを使って解くのが好み。
- tail.next = Noneはwhileの外の最後に書くよりもnode.next is not None and node.val == node.next.valのたびに書く方が好み。明示的にダブっているものはtailに含めませんと表現する方が分かりやすいと思うため。

### Step 3

- val_to_removeを使った解法で解いた。やっぱりこれが直感的で好み。