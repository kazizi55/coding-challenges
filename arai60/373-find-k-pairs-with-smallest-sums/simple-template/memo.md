# 373. Find K Pairs with Smallest Sums

## Link

https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/hayashi-ay/leetcode/pull/66/files

## Comments

### Step 1

解けなかった。347. Top K Frequent Elements の要領で、sum を key, pair の配列を value にしてそれを sum で昇順に並び替えて k 番目まで配列を返すということをやろうとしたが時間が足りず。

### Step 3

Solution1 は Gemini に聞きながら解いたもの。nums1 と nums2 を 2 次元のグリッドとして捉えて、nums2 を固定して nums1 の組み合わせを最初に網羅し、続いて nums2 の組み合わせも網羅するというものだ。このように「最初の列だけ heap に入れて、右にしかいかない」とすることによって重複を避けることができる。
Solution2 はダイクストラ法と DP 法を組み合わせたような解法。上と左が visited に格納されている時のみ candidates に追加する。
