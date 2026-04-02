# 3. Longest Substring Without Repeating Characters

## Link

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/49

## Comments

### Step 1
- うーん、直前と同じかどうかを見るだけだと不十分だから、配列とかで値を保持しつつ、インクリメントしていく必要がありそう。

> s consists of English letters, digits, symbols and spaces.

とあるので、spaceも考慮しないと行けなさそうだなー。

- setにしてfind効率を上げつつ、ダブってなかったら and スペースでなかったらaddする、最後にlen(set)を返せばOKかも。
- いや、これだと連続している文字が複数あるときに対応できない (abcccderとか)
- うーんmax_lenを持っておいて、max()で比較していくのが良さそうだなー。
- あー時間切れだー。答えを見る。

### Step 3
- sliding window と言うアルゴリズムがあるのか。連続していて単調性がある対象に対して使える。
  - 単調性とは？右を広げると「条件に近づく/離れる」が一定と言うこと。
  - 一次配列や文字列に対して使えるが、負の数を含む配列だと使えない。単調性がないので。
    - 窓を広げても、負の数を足すと合計が減るかもしれない。
    - 窓を縮めても、負の数を引くと合計が増えるかもしれない。

#### Solution 1
- set()を使う解き方
- windowが伸び縮みしているのがわかりやすい。seen_charにs[right]があったら、ダブりがなくなるまでwhile loopを回し続けるため処理が見やすいからだろう。

#### Solution 2
- dict()を使う解き方
- last_char_to_index.get(s[right], -1) を使うのめちゃスマートだな
  - s[right]とダブっていないところまでleftを一気にワープさせられる
  - 初期値で-1を持っておくことで + 1して0から始められるようにもできる
