# 323. Number of Connected Components in an Undirected Graph

## Link

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/19

## Comments

### Step 1

解けず。edges が[[0,1],[1,2],[0,2],[3,4]]の[0,1]と[0,2]みたくただ一つ前の edge を見るだけじゃ判定できないケースもあることがわかり、時間切れ。やはり DFS か BFS を使うのがよさそう。答えを見る。

### Step 3

#### Solution 1

DFS と Adjacency list を使う解法。
adjacency list は知っていたがこういう形で定義・利用できるのかと勉強になった。

#### Solution 2

BFS と Adjacency list を使う解法。
再帰を使わないで書けるから DFS と比べてこっちの方がそういう制約がある時には有用かと思ったが、DFS も stack を使うことで再帰を使わないでかける。2 周目で試す。
