# 2. Add Two Numbers

## Link

https://leetcode.com/problems/add-two-numbers/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/kazizi55/coding-challenges/pull/5

## Comments

### Step 1

- 内容を整理して解いていったがWA。loop 後のcarry overの考慮をしていなかったので直してAC。
  - while loopにcarry != 0を含めておくとこれいらないのかー。
- while loopが結構長くなってしまっているので、functionに切り分けても良いなー。
- あと、is_carried_overというbool値じゃなくてcarryという数字を持たせた方がいいなと思い直した。切り上げがあるという情報だけを持たせるのではなくてどれくらい持っているかを併せ持てる方が良いかなという次第。
- divmod(a, b)という a//b, a%b を返してくれるbuit-in functionがある。使わない手はないが覚えてたら書いてもよさそう
  - https://docs.python.org/3/library/functions.html#divmod
- sentinelを使わないで書くと確かにif文が増える。
- l1とl2のvalを足すのとnextに進めるのを同じタイミングでやるの好みかも。

### Step 3

- l1とl2のvalを足すのとnextに進めるのを同じタイミングでやる解法で解いた
- 各ループでtotalにcarryを入れた状態で初期化して、l1とl2のNone checkで足し上げていくのが、実際の手計算と流れが同じように思えてイメージしやすかった