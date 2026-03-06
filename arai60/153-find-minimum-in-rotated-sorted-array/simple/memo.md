# 153. Find Minimum in Rotated Sorted Array

## Link

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

## Comments

### Step 1

これはleftとmidの数字を比べてleftの方が小さくなるまで続けて行って残ったleftを返せばいけるのでは。いや、全然ダメだな、、
Geminiに聞いてみる。なるほどー、nums[left]ではなくnums[right]を基準にすべきなのかー。

> 二分探索で「最小値」を探すときの絶対的なルールは「未探索の範囲内に必ず最小値を閉じ込めておくこと」
> nums[left] を基準にすると、**「左側が整列していること」は分かっても、「その外側（右側）に、もっと小さい値があるかどうか」**が判断できない

右半開区間で解こうとすると末尾の値との比較をするから境界線を考えるのが若干大変になりそうだなー。

### Step 3

あー、sortedとかminを使っても解けたな。コーディング試験ではまず使わないとは思うが。

#### Solution 1

再帰を使った解法。考え方は同じ。
if nums[mid] < nums[right]でもif nums[mid] <= nums[right]でも通るのなんでだろうと思っていたら、

> All the integers of nums are unique.

だから、nums[mid] == nums[right]にはなり得ないってことかー。

ちなみにif nums[mid] < nums[right]:をif nums[mid] < nums[-1]:にしても通る。

> この問題の目的は、mid が「回転して持ち上げられた大きな数字のグループ（左側）」(グループA)にいるのか、「回転の影響を受けていない本来の小さい数字のグループ（右側）」(グループB)にいるのかを判定することです。ここで、nums[-1]は、必ずグループBの最大の数字になります。

#### Solution 2

while loopを使う右半開区間を使った解法。
if nums[middle] < nums[-1]ではなく、if nums[middle] <= nums[-1]としないといけないのなんでと思ったが、探索の最後に mid が末尾に追いついて重なる瞬間があるから、その時に追い越さないためのストッパーとして = が必要という感じかー。rightの最後の数字が空っぽだかたらleft + rightを2で割るとはみ出しちゃってleft < rightなのにnums[mid] == nums[right]になることがあるってことかー。逆に閉区間だといらない。
