# 703. Kth Largest Element in a Stream

## Link

https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/kazizi55/coding-challenges/pull/8

## Comments

### Step 1

- heapやsortを使うのはわかっていたが、概念を忘れているのもあり時間内に解けず、、
- 凡ミスに気づいてsortedで解き直したがheapを完全に忘れているので復習する。
- 過去の自分めっちゃまとめているなー。一方でそれをほぼ忘れていたので記憶の仕方に一考の価値ありということだろう。
- heapqはデフォルトだと最小ヒープになる。k番目に大きな値を求めたければ、k個の最小ヒープの一番最初の値がそれに当たる。
- largest_numsの要素数調整をinitでやるかaddでやるかという感じ。個人的にはinitでやる方が内部要素に一貫性がある感じがして好み。例えばaddと同じようにk番目に大きい要素を返すメソッドを別で作りたいとなった時にaddで調整していると二重実装になってしまう。
- bisect.insortを使って実装もできる。k個以上の要素を常に保持しながらk番目の値も返したいという要件があったとしたらこれを使うのも良いかも。

### Step 3

- heapqを使ってinitでaddするで解いた。これが書き方もシンプルだし、init後の内部要素に一貫性がある感じがして好み