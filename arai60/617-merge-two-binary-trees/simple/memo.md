# 617. Merge Two Binary Trees

## Link

https://leetcode.com/problems/merge-two-binary-trees/description/

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。

[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考にした。まずはコードを書く部分にフォーカスして 60 問解き切った後に Step 1-4 をもう一度行う。レビュー依頼は行わない。

## Referenced PR

https://github.com/olsen-blue/Arai60/pull/23

## Comments

### Step 1

途中までしか解けず。ループの中で node をどう left と right に繋げていくかのロジックが思い浮かばなかった、、

### Step 3

#### Solution 1

DFS の入力非破壊 version。call stack で回す。
シンプルで頭に入ってきやすい流れだった。

#### Solution 2

DFS の入力非破壊で値渡しする version。こちらの方がより副作用を考慮しないでいい。

#### Solution 3

DFS の入力破壊 version。
Space Complexity が少ないのはわかるが、やはり root1 を丸っと書き換えるのは抵抗があるな、、
実務ではまず使わないかなとは思う。

#### Solution 4

DFS の list の stack を使う version。
call stack に比べて記述量は増えるが、その分処理はより追いやすいかも。入力を破壊してしまっているが、、
非破壊にするには`stack = [(new_root, root1, root2)]`みたいな感じで new_root も stack に積むようにするとできる。

#### Solution 5

BFS の deque の queue を使う version。
確かに Solution 4 のデータ構造を stack から queue に変えるだけで BFS になるのは驚き。
