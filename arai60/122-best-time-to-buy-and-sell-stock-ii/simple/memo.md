# 122. Best Time to Buy and Sell Stock II

## Link

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/38

## Comments

### Step 1

解けず。うーん、どうやってその時点より過去のmax profitと今のmax profitを積み上げていくのか、そしてmin_priceを更新していくのかがわからず時間を使ってしまったので答えを見る。

### Step 3

#### Solution 1

DPの中でさらに2つに分岐させて保持させればいけるのか、勉強になる。
株を買う・買わない場合で場合わけしてDPテーブルを保持しておき、日毎でそれぞれの最大値を更新し続けて、最終日にその2つの大きい方を取れば最大利益がわかるという次第。

#### Solution 2

貪欲法で解いてみた。めちゃシンプルだが、売買後は一日休まないといけないとか売買に手数料が発生するとかの他に条件が加わるとこれでは解けなくなる。

#### Solution 3

Peak Valley Approachという手法らしい。確かに標高の差分を比較するように解けるので直感的でわかりやすい。
