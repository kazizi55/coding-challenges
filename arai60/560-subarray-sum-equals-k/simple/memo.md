# 560. Subarray Sum Equals K

## Link

https://leetcode.com/problems/subarray-sum-equals-k/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/16

## Comments

### Step 1

解けず、、累積をどう表現するのかに悩み、結局答えを見た。

### Step 3

#### Solution 1

Time complexity O(n^2)の解法だと Time exceeded になってしまうので、O(n)で解けるようなものでないといけない。

[1,2,3,4,5] という配列を考えた時に、2,3,4 の合計は 1+2+3+4 - 1 で算出できるので、現在の合計 - 過去の合計 = その区間の合計と言える。今回は、その区間の合計 = k。なので逆算して、**現在の合計 - k = 過去の合計とも言える**ので、過去の合計を格納する dict を作成して、現在の合計 - k と一致する値があれば、その区間の合計で k であるということになる。
