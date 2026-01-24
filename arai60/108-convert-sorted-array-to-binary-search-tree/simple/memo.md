# 108. Convert Sorted Array to Binary Search Tree

## Link

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/24

## Comments

### Step 1

解けなかった、、答えを見て難しく考えすぎていたことを知った。再帰を使えばよかったのか、、

### Step 3

#### Solution 1

Referenced PR の師匠と弟子の metaphor がわかりやすかった。今後はどう解けるかを metaphor を使って考えると良さそう。

#### Solution 2

右半開区間 (left-closed, right-open interval)、閉区間 (closed interval)という言葉、ちゃんと調べたことがなかったので調べた。
これは Solution1 を右半開区間で書き直したもの。Gemini によると Python や C#のライブラリなどではこちらの書き方の方がよく書かれているらしい。
