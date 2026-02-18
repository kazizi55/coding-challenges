# 121. Best Time to Buy and Sell Stock

## Link

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/37

## Comments

### Step 1

DPを使ってmax profitを保持しつつ、loopを回す中でそれよりも大きい値だったらmax_profitを更新する、という形で解けた。
シンプルには書けたがもう少し他の解法が浮かぶようになりたい。再帰では解けそう。とりあえず答えを見てみる。

### Step 3

#### Solution 1

Step1と同じ解法だが、-math.infを使って初期化している点(最小値であり、上書きされることを明示)とmin_priceの更新をmax_profits[i]の代入の後に行っている点が違った。こっちの方がわかりやすい。
あと、i日まででのmax profitにしているか、i日単体でのmax profitにしているかという点で違った。個人的には前者の方がしっくりきたのでそれで実装。後者は厳密にいうとDPでない気がする。

#### Solution 2

左側からその日時点での最小値を、右側からその日時点での最大値を計算していき、その二つをみてmax_profitを計算する解法。関数型っぽいのは変数がimmutableなところ、宣言的なデータフロー、フローごとで状態の分離がされているところがあるため。

#### Solution 3

Solution 2を見て、Solution1の空間計算量を1にできるなと思ったのでそれで実装。合わせてコードもシンプルになった。
