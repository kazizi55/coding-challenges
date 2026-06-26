# 0. Template

## Link

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

## Comments

### Step 1

10 分ほど考えたが解けなかった。具体的には、`l1 = [9,9,9,9,9,9,9]`、`l2 = [9,9,9,9]`、`output = [8,9,9,9]`になる場合で NA になり、l1 is not None と l2 is not None を前提とする解法をガラッと変えないといけなくなりそうだったので一旦諦めて答えを見た。問題の Example3 に l1 と l2 の length が違うケースが載っていたことを見逃していたのが考慮不足の要因だ。反省。また、空行が多いことは迷いの現れという話をよく協会内で見るが、見返してみると確かに空行が多い。迷っていたことがはっきりわかる、、

#### 参考にした回答

- https://github.com/hayashi-ay/leetcode/pull/24/files

### Step 2

- 共通
  - sum という変数名にすることもできるが、Python の built-in 関数に sum が存在するため、避けたほうが良さそう
  - https://docs.python.org/3/library/functions.html#sum
  - 10 は magic number だが、他の基数への対応を考えるならば定数に切り出しておくのはあり。そういう要件があるなら切り出す。
  - 参照先が閉じているなら、inner function として書いてしまっても構わない
    - `Nested local functions or classes are fine when used to close over a local variable. Inner classes are fine.`
    - https://google.github.io/styleguide/pyguide.html#26-nestedlocalinner-classes-and-functions
  - コード領域、データ領域、スタック領域、ヒープ領域
    - コード領域: コンパイルされた機械語の命令（実行コード）が格納される。読み取り専用。
    - データ領域:
      - 初期化済みのデータ領域: プログラムの実行開始前に初期値が設定されているグローバル変数や静的変数などが格納される。
      - 初期化なしデータ領域: 初期値が設定されていないグローバル変数や静的変数などが格納される。プログラムの実行開始時にゼロで初期化される。
    - スタック領域: 関数呼び出しに伴うローカル変数（自動変数）、関数の引数、関数の戻りアドレスなどが格納される。
    - ヒープ領域: プログラムの実行中にプログラマが明示的に確保・解放を指示する動的メモリ（C 言語の malloc や C++の new など）が格納される。Python では、数値、文字列、リスト、辞書、関数、クラスのインスタンスなど、ほぼ全てのものがオブジェクトとして扱われ、これらは全てヒープ領域に動的に確保される。
    - https://discord.com/channels/1084280443945353267/1237649827240742942/1252085859096723558
- 再帰 (RecursiveSolution)
  - 再帰で書くと Output 用の LinkedList の管理が不要になるのでコード量を減らせる。特に sentinel を使わなくても良くなる
  - stack size の肥大化 やデバッグのしづらさなどの観点から再帰を書くことは少し躊躇したほうがいい
    - https://github.com/Yoshiki-Iwasa/Arai60/pull/4#discussion_r1644191582
  - 参考にした回答との差分
    - if not (l1 or l2 or carry) と書かれていたが、それぞれ具体的にどの値が来た場合を想定しているかを明示したかったので、 if l1 is None and l2 is None and carry == 0 と変更した
    - \_add_two_numbers と定義されていたが、この問題を解く上で private/public を気にするのは冗長に感じたので、add_two_numbers とリネームした
- Number の List を作って None を事前に取り除く (SolutionUsingNumberList)
  - None チェックを減らせるのでコード量を減らせる
  - 参考にした回答との差分
    - 番兵として head を用いているので、 sentinel にリネームした
    - carry を total としても扱っていたのが不自然に感じたので 別途 total として for 文の中に定義した
    - ListNode の list が list_of_numbers と定義されていたが、それだと int の list に見えると思ったので、nodes とリネームした
      - 代わりに sentinel から始まる node を current と命名した

#### 参考にした回答

- 共通
  - https://github.com/olsen-blue/Arai60/pull/5/files
  - https://github.com/ryosuketc/leetcode_arai60/pull/5/files
- RecursiveSolution
  - https://github.com/hayashi-ay/leetcode/pull/24/files
  - https://github.com/Yoshiki-Iwasa/Arai60/pull/4#discussion_r1644191582
- SolutionUsingNumberList
  - https://github.com/tokuhirat/LeetCode/pull/5/files#r2068222030

### Step 3

step 1 で解いた解法で 3 回とも解くことにした。sentinel を使いつつ、while ループで最初から順番に見ていき、output の list にひとつずつ ListNode を格納していくのが処理が追いやすいと思ったためだ。

### Step 4

以下、いただいたフィードバック:

- 共通
  - inner function の後には空行を入れ、区切りであることを視覚的に表現した方が見やすい
- divmod 関数を使う version
  - (divmod 関数)[https://docs.python.org/ja/3/library/functions.html#divmod]を使えば商と剰余をタプルで得られる
- 番兵を使わず、代わりに while ループ内に条件分岐を作る version
- SolutionUsingNumberList を while nodes or carry != 0 で書き直した version
  - while True の無限ループで書いているのに break が出てこないと若干困惑するので、通常の loop で条件を明示して、読み手の負荷を下げる
  - inner function の prefix として \_ をつけることで外側の関数と同じ名前になることを避ける
- val の total への加算と next へ進めることをまとめる version
