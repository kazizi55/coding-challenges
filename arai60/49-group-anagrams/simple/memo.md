# 0. Template

## Link

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

## Comments

### Step 1

dict 型を使って sort された str を key にして、それと他の str を sort して比較していくという手法で解けた。
後から見ると、camelCase と snake_case がごっちゃになっている、、反省。

なお、defaultdict だと key が存在しなければ勝手に [] が作られ、そこに append されるようだった([doc](https://docs.python.org/3/library/collections.html#collections.defaultdict))ので、`if len(anagram_keys) == 0 or not(sortedStr in anagram_keys)`という条件はいらないようだった。

### Step 3

Step 1 と同じ方針で解いたが、変数の命名を改善したのと、Tuple を key にする方法でも試してみた。好みの問題か。
