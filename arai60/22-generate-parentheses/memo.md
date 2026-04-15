# 22. Generate Parentheses

## Link

https://leetcode.com/problems/generate-parentheses/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/54

## Comments

### Step 1

- 与えられたnの個数分の括弧の閉じ方の組み合わせを返す問題。
- 前問と同じように解けるか？足踏みもするし先に進みもするし。括弧をどう閉じるかが鍵だなー。
- うーん、どうやって括弧をcombinationに入れるかとベースケースをどう定義するかで詰まってしまった。geminiに聞いてみる。
- あー、分岐を(と)でそれぞれ作るのかー。
- カッコの種類は一つだけなのでopen_countとclose_countで持っておきさえすればOK。
- n未満しか左括弧を使っていないときに左括弧を追加、使った左括弧の数よりも右括弧の方が少ない時に右括弧を追加できる

### Step 3

#### Solution 1
- なるほどーindexなしでも書けるのか
- combinationは再帰関数の引数に持たせなくても外に変数定義しておけば事足りる
  - 今までのbacktrackで引数に持たせていたのもこんな感じで外に切り出せるのでは。結局引数を破壊していたわけだし

#### Solution 2
- (A)Bと分けてresultを構築していく解法。面白い
- AもBも最大ペア数はnになるので、for num_pairs_A in range(n)で回しつつ、括弧の実体をA,Bともにself.generateParenthesisから得る形になる
- Bのself.generateParenthesisに渡すn - 1 - num_pairs_Aは全体のペア数から据え置きの()のぶんの1とAのペア数を引いたもの
