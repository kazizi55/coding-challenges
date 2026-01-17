# 0. Template

## Link

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/18

## Comments

### Step 1

200 Number Of Islands を応用して、DFS で解こうと思ったが動かず、、時間が来たので答えを見る。ああ、考え方はあっていて、定数を前の問題に引っ張られて string にしていてダメだった。WATER が string でも一部通る理由は、Python の比較演算において 1 != "0" が True になり、陸地（1）以外の判定が正しく機能してしまうため。一部 test case が pass していたのでアルゴリズム自体の問題だと思ってしまった、、

### Step 3

#### Solution 1

DFS で grid に変更を加える version。
x,y を c,r (column, row)に変えることでより縦横がわかりやすくなった感がある。

#### Solution 2

BFS で grid に変更を加える version。
DFS でも BFS でも Time Complexity は O(R ^ C)。
deque を使うことで、末尾の追加と先頭の pop を O(1)で実行できる。

#### Solution 3

DFS で grid に変更を加えない version。
space complexity こそ多いものの、実務では他への影響を加味してこっちの version の方が使うことが多いかもしれない。

#### Solution 4

BFS で grid に変更を加えない version。
DFS よりもなんか直感的な感じがしないので行ったり来たりしてしまう。とりあえず Arai60 を一周してみて様子を見る。
