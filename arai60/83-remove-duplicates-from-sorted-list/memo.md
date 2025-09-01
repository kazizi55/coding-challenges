# 0. Template

## Link

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

## Comments

### Step 1

途中まで Set()を返そうとしてしまっており、5 分以内に解くことができなかった。焦らず問題文を読むことが大切だなと改めて痛感したのと、移動の隙間時間でやるものではないと思い直した。また、前回の問題を解いてから 1 週間以上時間が空いてしまったのも関係していると感じたので今後は問題を解く間隔を狭めていく。

hayashi-ay さんが行っていた 5 ステップ目も今後はやってみる。

https://hayapenguin.com/notes/Posts/2024/04/24/how-to-practice-coding-effectively#%E5%85%B7%E4%BD%93%E7%9A%84%E3%81%AA%E7%B7%B4%E7%BF%92%E6%96%B9%E6%B3%95

> 3 ステップ目と同じルールで一度解けた問題について、3 日後に挑戦します。OK なら 7 日後に挑戦します。OK なら 30 日後に挑戦して、3 連続で OK ならクリアとします。一度でも失敗したら最初からやり直します。

答えを見て、while と if-else で既存の LinkedList を書き換えるパターンで解き直した。

- 時間計算量: O(N)
- 空間計算量: O(1)

#### 参考にした回答

https://github.com/t-ooka/leetcode/pull/10

### Step 2

while と if-else で既存の LinkedList を書き換えるパターンのほかにもざっくり以下があることがわかった。

1. 二重 while で既存の LinkedList を書き換えるパターン
2. 新しい LinkedList を作成するパターン

#### 1. 二重 while で既存の LinkedList を書き換えるパターン

while と if-else を使うパターンとほぼ同じだが、while node is not None を最初の while に持ってくることで条件分岐がわかりやすくなる印象。

- 時間計算量: O(N)
- 空間計算量: O(1)

#### 2. 新しい LinkedList を作成するパターン

記述量も空間計算量も増えた。既存の LinkedList に変更を加えないで実装したい時に使う。

- 時間計算量: O(N)
- 空間計算量: O(N)

#### 参考にした回答

https://github.com/hayashi-ay/leetcode/pull/20/files
https://github.com/skypenguins/coding-practice/pull/13/files
https://github.com/tokuhirat/LeetCode/pull/3/files

#### 参考にしたコメント

変数が素直に状況を説明しおらず、巧妙に動いてしまっていると、直感的でない。例えば head という変数なのに中身が移り変わっていく場合は名実が異なっているので iterative など別の変数を使った方がわかりやすい。
https://discord.com/channels/1084280443945353267/1192736784354918470/1199759433543200819
https://discord.com/channels/1084280443945353267/1228896007279083653/1231823840355815475
https://discord.com/channels/1084280443945353267/1200089668901937312/1206180274442993694

if node だと 0 や[]の時は true になるので、それらも false として判定してほしいときは if node is not None を使うのが良さそう。
https://github.com/olsen-blue/Arai60/pull/3/files#r1930423910

#### 個人的な好み

- 他の回答で、冒頭に if head is None と書いて早期 return しているものがあったが、その後で while node is not None と書くので、早期 return は冗長なのではと思った。新しい LinkedList を作る場合は head を使って new head を初期化する必要があるので必要ではある。
- 他の回答で、node.next を next_node という変数に入れているものがあったが、next node なのは自明なのでやはり冗長なのではと思った。

### Step 3

3 回書いてみて、while node is not None を最初に括り出して、二重 while で書くのが直感的だと感じた。

### Step 4

以下、いただいたフィードバック:
