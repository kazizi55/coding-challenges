# 209. Minimum Size Subarray Sum

## Link

https://leetcode.com/problems/minimum-size-subarray-sum/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/50

## Comments

### Step 1

- 合計がtargetかそれ以上の最小のsubarrayのlengthを配列の中で見つけると言うことは、leftとrightを動かしていってsliding windowで解けそうではある。
- currentのtotalを持っておいて、target以上になるまでたす、その度にmin_lengthとmin()で比較する、とすればいけるのではないか。
- 解けず。答えを見る。

### Step 3

#### Solution 1

- なるほど、前問がsliding windowのleftを狭め切った後に毎回max_lengthを確認していたのに対して、今回はsliding windowを狭めながらmin_lengthを更新していく感じになる。prefix_sub >= targetの最小値を探したいのだからそれはそうか。
- 当たり前だけどsliding windowがある中でどこで答えとなる値を更新するかは問題によることがわかった。sliding windowはそこにただあるのだ。

#### Solution 2
- 右のprefix_sums - 左のprefix_sums = 区間の合計だから、
- 右のprefix_sums - 左のprefix_sums >= targetが言えるので、右のprefix_sums >= target + 左のprefix_sumsも言える。
- なんでif target_index == len(prefix_sums)なんだろう、と思ったが、target_sum が最後の要素より大きければ、bisect_left は len(prefix_sums) を返すからか。
- prefix_sums[i] = prefix_sums[i-1] + nums[i-1]のnums[i-1]はnums[i]ではと思ったが、nums と prefix_sums のインデックスが 0-indexed vs 1-indexed とでずれているかかー。
- 差分が最小になり、その差分はtarget以上である右と左のindexを求めたい。prefix_sumsの中でprefix_sums[右のindex] - target以下で最大の値を持つindexを探している。
- なるほど、累積和と binary tree は相性がいいんだなー。
- 今回を通して基本概念が理解できていないと、解法のロジックの理解にも時間がかかるのだなと言うことが改めてわかった。
- bisect.bisect_leftの動き方も復習
  - 存在しない値 && 最小値より小さい: 0を返す
  - 存在しない値 && 範囲内: 大きくて一番近い値の左の値のindexを返す
  - 存在する値が1つだけ: 存在する値のindexを返す
  - 存在する値が2つ以上ある: 一番左の値のindexを返す (これがbisect_**left**であるゆえん)
  - 存在しない値 && 最大値より大きい: 全体のlen - 1の+ 1 の index を返す
- target_index - from_indexで+1がいらないのは番兵を入れているから
