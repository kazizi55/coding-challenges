# 142. Linked List Cycle II

## Link

https://leetcode.com/problems/linked-list-cycle-ii/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

- https://github.com/kazizi55/coding-challenges/pull/2
  - 過去の自分の PR を参照して復習

## Comments

### Step 1

- 141とほぼ同じコードで解くことができる。True/Falseをnode/Noneに変えるだけ。
- これだけだと味気ないので他の解法も考える。
- set()を使いつつ、再帰を使って解くこともできる。流石に9ヶ月前だとほとんど忘れているな、、
- そうか、これもtortoise and hareを使って解くことができるのか。
  - 考え方を忘れているなー。
  - 開始点から分岐点の長さをX, 分岐点から合流点の長さをY、分岐点からの閉路一周の長さをLとした時、fastはslowの2倍のスピードで動くのとslowとfastは分岐点で会うので、2(X+Y) = X+Y+mLと置ける。展開するとX+Y = mL。よって合流点から分岐点の長さもXになるので、slowを開始点から、fastを合流点から同じスピード(1ずつ)でX走らせると、分岐点に行き着く。
  - https://github.com/ntanaka1984/leetcode/pull/2#issuecomment-3106759861
- is はobjectのアドレスを比較するbuilt-in function
  - https://docs.python.org/3/reference/expressions.html#is-not

### Step 3

- 結局set()・whileを使う解法が好みだった。なぜなら処理がシンプルであるし、上から下に読み解いていくだけで個人的には理解もしやすいから。