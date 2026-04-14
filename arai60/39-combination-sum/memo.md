# 39. Combination Sum

## Link

https://leetcode.com/problems/combination-sum/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/53

## Comments

### Step 1

- candidatesの中から合計がtargetになる組み合わせを返すというもの。前問のbacktrackingを使えば解けそうな感じがする
- candidatesから同じ数字を何個でも取っていいので、ビット全探索は使えないかも
- 前問から子供を1つ増やす形 (同じ数字を探索する子供)でいけるか？いやーどう表現すればいいんだろう、、
- TLEで時間切れ。Geminiに聞いてみる。
- なるほどー、sum()を毎回使うとcombinationの数(k)だけ毎回o(k)かかるからcurrent_sumで持っておけばo(1)になるな
- index == len(candidates)のガードを入れ忘れていた。
- あと、再帰関数の中で最初に同じ数字を入れるようにすれば[2,2,2]みたいな同じ数字を使うパターンにも対応できるのかー。
- [2,3,3]と[3,2,3]みたいな同じ内容の組み合わせがどうして発生しないんだろうと思ったが、一方向で探索されるので、一度探索された数字はもう使われないからということだった

### Step 3

#### Solution 1

- Step 1のRevised solutionと同じ解法
- 再帰関数の引数の順番と命名を変えた
  - current_sumのcurrentは冗長なのでtotalに
  - 同じデータ型で並べたほうが綺麗かも？と思いindex, total, combinationに
- 元回答はtraverse_combination(index + 1, total, combination)の後にraverse_combination(index, total + candidates[index], combination)と書いていたが、個人的には足踏みしてから次に進める方がbacktrackingのイメージに合っているかなと思ったので逆にした
- ちなみにappendとpopを使わなくてもcombination + [candidates[index]]みたいな感じにすれば書けるが空間計算量がその分増えるし処理時間もo(n)にはなるのでappendとpopを使う方がいいかも

#### Solution 2

- Solution 1のstackバージョン
- 同様に足踏みしてから次に進める感じにした
