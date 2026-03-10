# 1011. Capacity To Ship Packages Within D Days

## Link

https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/44

## Comments

### Step 1

うーん、日毎の総重量を変数で持っておいて、日毎にmaxで比較して行って、大きい方を格納して行って最後にその値を返すのが良さそう？が、どうやって日毎の重量を計算するのがいいのだろう。あと、これにbinary searchをどうやって適用するのだろう、、
わからないな。答えを見る。

### Step 3

#### Solution 1

なるほど、重量の最小・最大を定義してそれを二分探索するのかー。

- 最小: 一番重い荷物の重量
- 最大: 荷物の重量の和

is_loadable_capacityという関数を定義して、そこで全ての荷物を引数のcapacity内で積み切れるかをみている。
今回は境界を探しているので、while low <= highではなく、low < highとする。
highを暫定チャンピオンとしてmiddleが正解の場合も考慮するので、high = middle - 1ではなく、high = middleとする。
highの初期値がsum(weights) + 1なのはwhile low < highという右半開区間で比較しているため、+1をしないとsum(weights)自体が含まれなくなってしまうから。

#### Solution 2

Solution 1の考え方をそのままにbisect_leftをフルに使った解法。keyとか探索対象を変えるだけでこんな感じで使えるのかー。
