# 0. Template

## Link

## How to work on each step

- Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

## Comments

### Step 1

5 分は過ぎてしまったが、Python の文法を調べながら他の方の回答を見ずに解いた。
同じ内容を繰り返し書いてしまっていて冗長なので、step を進めて洗練させてみる。

### Step 2

- 共通
  - プッシュダウンオートマトン: 「無限の容量を持つスタック（stack）」と「有限オートマトン 」を組み合わせた理論モデル
    - まさにこの問題のような対応関係のチェックができる。この理論モデルを強調する形でコードを書くと(stack という変数名にするなど)わかりやすくなる
  - 有限オートマトン: メモリを持たず、有限個の状態とルールだけで動く、最も単純な理論モデル
    - 自販機: 何枚のコインが入ったか（合計金額 = 状態）は覚えているが、今まで入れたコインの順番や 100 円を入れた回数などを細かく記録はしていない
  - オートマトン理論においては他にも以下のような階層的なモデルが存在している
    - 線形有界オートマトン: 使えるメモリが問題の長さに限られた理論モデル
    - チューリングマシン: 無限のメモリを持つ、あらゆる計算が可能な究極の理論モデル
  - チョムスキー階層: 形式言語学やコンピュータサイエンスにおいて、言語の文法（ルール）の複雑さを 4 つのレベルに分類した階層構造
    - 正規文法 (type 3): 繰り返しや直列など、パターンマッチングのような単純なルールで認識できる言語。有限オートマトンに対応
    - 文脈自由文法 (type 2): 括弧の対応や、入れ子構造（ネスト）など、過去の情報を一時的に覚えておく必要がある言語。プッシュダウンオートマトンに対応
    - 文脈依存文法 (type 1): ルールの適用が、その単語の「周りの文脈」に依存する言語。線形有界オートマトンに対応
    - 制限なし文法 (type 0): アルゴリズムで計算できるすべての問題を含む最も強力なクラス。チューリングマシンに対応
  - parentheses の単数形は parenthesis。ラテン語の第三変化名詞に由来する。
  - 異常な入力への対処に関して毎回何かする必要があるわけではないが、いくつか対応方法があるので毎回自問自答する癖をつける。今回は意図的に無視している。
  - 条件文では if bracket_pairs[open_brackets.pop()] などの副作用がある複雑な式は避ける
  - 関数の呼び出しを測るには timeit を import して使うといい
  - stack の命名に関しては、他の方のコードを見て、open_to_close_brackets など色んな命名が見られたが、プッシュダウンオートマトンであることを明示したいので stack とした
- SolutionWithBracketPairsAndSentinel
  - bracket pair を作ることでそれぞれのカッコごとに条件を作らなくて良くなる
  - {open: close}という形で pair を定義することで bracket_pairs[stack[-1]]と定義でき、仮に bracket 以外が入力されても例外を投げなくなる
  - さらに番兵を入れることで stack[-1]で参照エラーになることも防げる
- SolutionWithReversedBracketPairs
  - 参照した回答との差分
    - stack.pop()を条件文に入れて副作用を発生させたくなかったので、last_stack = stack.pop()を定義して、if last_stack != bracket_pairs[char]という条件文にした
- SolutionWithBracketWithoutSentinel
  - sentinel ありの時よりも if 文が増えて複雑になる

#### 参考にしたコメント

- 共通
  - https://discord.com/channels/1084280443945353267/1206101582861697046/1216945010189144085
  - https://discord.com/channels/1084280443945353267/1201211204547383386/1202541275115425822
  - https://github.com/konnysh/arai60/pull/6#discussion_r1843004273
  - https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.jdtk9v35bca4
  - https://github.com/saagchicken/coding_practice/pull/21#discussion_r2014536948
  - https://github.com/ryosuketc/leetcode_arai60/pull/6/files/f75fc4a3ac0f11cdefd086be95ec9a8b8661dd50#r2253408361
- SolutionWithBracketPairsAndSentinel
  - https://github.com/SanakoMeine/leetcode/pull/7#discussion_r1903352693
- SolutionWithReversedBracketPairs
  - https://github.com/ryosuketc/leetcode_arai60/pull/6/files

### Step 3

最終的に sentinel・reversed ではない bracket_pairs を使う解法に落ち着いた。処理の流れが追いやすい上にシンプルに書けるため。

### Step 4

以下、いただいたフィードバック:
