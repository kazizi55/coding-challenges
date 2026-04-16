# 283. Move Zeroes

## Link

https://leetcode.com/problems/move-zeroes/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/55

## Comments

### Step 1

- うーんこんな感じで0だったらin placeでpopとappendしていく感じがいいかなと思ったけど上手くいかず
```
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
```
- pop&appendした時にindexが1つ前にズレるからかー。うーんどう解決するか考えているところで時間切れになってしまった。geminiに聞く。
- あー、checked_countを持っておけばいいだけの話だった。悔しい。


### Step 3

#### Solution 1

- Revised Solution とは違い、0でない時用のindexを持っておいて、それを移動させた後に、そこから0をlen(nums)まで挿入していく感じ。直感的でわかりやすい
- 空間計算量が1になるが、loopは2個になってしまう

#### Solution 2

- 面白い。non_zero_putting_indexとindexで0を挟み込んで、その塊の左に0以外の数字を逃していくイメージ
- 空間計算量が1でloopも1つ。
