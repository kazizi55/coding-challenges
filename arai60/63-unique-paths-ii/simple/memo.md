# 63. Unique Paths II

## Link

https://leetcode.com/problems/unique-paths-ii/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/34

## Comments

### Step 1

62 と基本同じ解き方で obstacleGrid[r][c]が 1 の時を skip すればいいのではと思い回答を書いてみたが、通らず、、時間切れになったので答えを見る。
なるほど、1 行目と 1 列目の考慮が足りていなかったかー。

### Step 3

#### Solution 1

先にエッジ初期化をする解法。なるほど、確かにこの方が一度に考えることが少なくなるので読みやすい・書きやすい。

#### Solution 2

二重ループの中で全てを処理する解法。step1よりは簡略化されていてわかりやすいがsolution 1と比べるとやはりちょっと大変。
