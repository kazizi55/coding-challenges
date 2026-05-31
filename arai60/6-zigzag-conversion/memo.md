# 6. Zigzag Conversion

## Link

https://leetcode.com/problems/zigzag-conversion/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/61

## Comments

### Step 1

- 左から右に並んでいる入力をジグザグの形に変換して返すというもの。どうやるんだこれ。
- numRowsの数ぶん縦に並べたのを列挙していって折り返す？
- adejacent matrixを使う？
- うーん解法が浮かばない。答えを見る。

### Step 3

- [[] for _ in range(numRows)]でnumRows分の配列を作ることができる。忘れていた。
- なるほどー、sをfor loopで探索しつつ、is_going_downをフラグとして持って参照するとジグザグに配列に追加していくことができるのか
  - 上端 (row = 0)までいったらis_going_downをTrueに、下端まで行ったら逆にFalseにする。
  - rowは上端だろうが下端だろうがその間だろうが、is_going_downのTrue/Falseに応じて+1/-1していく