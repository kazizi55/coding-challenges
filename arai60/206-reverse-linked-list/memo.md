# 206. Reverse Linked List

## Link

https://leetcode.com/problems/reverse-linked-list/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/kazizi55/coding-challenges/pull/7

## Comments

### Step 1

- うーん愚直にstackにnode.valを一個ずつ格納していってまたそれを詰め直す感じだろうか。
- とりあえずACしたが (time complexity: O(N), space complexity: O(N))、後半の命名が冗長で納得いっていなさもある。
- new_headとかnew_nodeとあえてしなくてもいいのかもと思い始めてきた。入力値を上書きしているのではないし、private variableを上書きするのはあまり問題がないように思えてきた
- while len(stack) > 0 のほかにfor num in reversed(stack)という選択肢があることを思い出したが、stackの特性であるFILOに忠実である方が好みだなと思うので、元々の前者を選択。
- 再帰で帰りがけでreversedを完成させる解法、確かに書かなくていいならtailなしの方がいいかもしれない。実際に呼び出し側の視点に立った時にtailは使わない (tailは内部の再帰都合で仕方なく露呈させているだけなのだから)
- tailなしで再帰を書くことでより再帰の処理の流れがわかった気がする。今見ているnodeを軸に次のnodeを見て、次のnodeの次に今のnodeが来るようにして、循環参照にならないように、今のnodeの次をNoneにする。そのnodeの次は一個上で代入される。
- あー、sentinel入れてもいけるのか。
- restとnext_nodeを使って行きがけでreversed_listを作るのも好みだなー。実際に目の前で入れ替えるとしたら同じ順で入れ替えるだろうし、記述量も少ない。1個前のrestをreversed_headとしてrest.next.nextに代入するのを繰り返していっている感じかー。

### Step 3

- 結局最初の解法で命名だけ調整する形で書いた。(new_node -> node)
- 一番流れが直感的で好みだったので書いてみた。stackを目に見える形で積み上げてから1個ずつpopしていくのが分かりやすい。