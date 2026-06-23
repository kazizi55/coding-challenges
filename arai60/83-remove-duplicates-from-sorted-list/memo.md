# 83. Remove Duplicates from Sorted List

## Link

https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/kazizi55/coding-challenges/pull/3

## Comments

### Step 1

- ダブった数字がないようにすれば良いのでnodeの値を格納するset()を作ってloopの中でダブっていないかを都度確認する、ダブっていたら繋ぎ直すという感じにすれば解けそう。
- あら、なぜか解けず、、
- そもそもheadが削除されることはないのでsentinelは不要、かつ常にduplicatedなnodeは常に隣り合っているのでset()に保存する必要もなし。もっとシンプルに書ける。反省。
- 再帰でも実装。remove_duplicates(node)をそのまま返すとその親を返していかないのでnodeを返す必要がある。
- ああ、あと入力を破壊しない方法でも書けるな。duplicatedかどうかのguardを!=にしないとnode = node.nextを2回書かないといけないので!=の方が好み。
- 入力を破壊しない解法を参考にif節の内容を逆にした解法も追加。うーん個人的にはダブっているかどうかをvalidationするというイメージが強いので、逆にしないほうが好みかなー

### Step 3

- ダブっているかどうかをvalidationするシンプルなwhileループを選択