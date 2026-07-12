# 49. Group Anagrams

## Link

https://leetcode.com/problems/group-anagrams/description/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

### 解法1

- strs を探索しつつ、`alphebetical order で sort した word: ヒットした配列`という形の hashmap を作っていって、最後にその values() を返す形で実装できそう。
- あら、`alphebetical order で sort した word` を key に使おうとすると、TypeError: cannot use 'list' as a dict key (unhashable type: 'list') というエラーが出るな。なんでだろう。
  - ああ、`Return a new sorted list from the items in iterable.` ということで、sorted()を使うと、list が返ってしまうからか。
  - https://docs.python.org/3/library/functions.html#sorted
- `TypeError: dict_values([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]) is not valid value for the expected return type list<list<string>>` というエラーに遭遇。そうか、sorted_str_to_anagrams.values() は view object を返すので list に変換しないといけない。
  - https://docs.python.org/3/library/stdtypes.html#dict-views
- 調べながら AC。
- Time Complexity: O(k log k n) (k は str の maximum length として、k log k は sortにかかる時間), Space Complexity: O(n)

```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_to_anagrams = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in sorted_str_to_anagrams:
                sorted_str_to_anagrams[sorted_s].append(s)
                continue
            sorted_str_to_anagrams[sorted_s] = [ s ]
        return list(sorted_str_to_anagrams.values())
```

## Step 2

- `小文字アルファベット以外が来ると何が起きるか考えておきましょう。どうでなくてはいけないというよりは、その帰結としてありうるシナリオの幅を広く考えておきたい、くらいの意図です。`
  - 帰結としてありうるシナリオをどれくらい想定できるか。
  - ord() を使った解法でアルファベットの小文字のみを想定していると、それ以外の入力をしたときに挙動がおかしくなる。
    - https://docs.python.org/3/library/functions.html#ord
  - 今回の例だと、step 1の解法だと大文字でも数字でも記号でも対応はできる感じではある。そういう観点での解法の選び方もあるのか。
  - https://github.com/Fuminiton/LeetCode/pull/12#discussion_r1971612972
- `「どれくらいの幅で可能性と対策が見えているか」`
  - https://github.com/quinn-sasha/leetcode/pull/15#discussion_r1970861088
- unicode の code point
  - ざっくり、記号、数字、記号、アルファベット大文字、記号、アルファベット小文字、記号という順になっているのか。なかなかにトリッキー。code point を比較するロジックを書くときはこの順番を念頭に入れておかないと挙動がおかしくなる。
    - https://en.wikipedia.org/wiki/List_of_Unicode_characters
  - https://github.com/azriel1rf/leetcode-prep/pull/4#discussion_r1973077272 
- Run Length Encoding (連長圧縮) とは、ある連続したデータを、そのデータ一つ分と連続した長さで表現することで圧縮する手法
  - https://ja.wikipedia.org/wiki/%E9%80%A3%E9%95%B7%E5%9C%A7%E7%B8%AE
  - なので、今回のように「ソートした上で文字とその出現頻度を文字列で表すだけ」だと、元の文字列にデコードできないので RLE とは言えない。
    - https://github.com/ichika0615/arai60/pull/11/changes#r1978511189

### 解法1: hashmap の key を tuple にする

- tuple は immutable なのでハッシュ可能。frozenset とかも同様にハッシュ可能。
- "".join() を使うよりも若干シンプルに書ける。
- Time Complexity: O(k log k n) (k は str の maximum length として、k log k は sortにかかる時間), Space Complexity: O(n)

```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        return list(groups.values())
```

#### 参考にした回答

- https://github.com/hayashi-ay/leetcode/pull/19/changes の 3rd
- https://github.com/olsen-blue/Arai60/pull/12/changes の 3rd

### 解法2: lowercase の alphabet をカウントする

- ord() を用いて入力に含まれる lowercase の alphabet のそれぞれの頻度を list に格納し、tuple 化、それを key にとり、value に strs の要素を挿入していき、その values を答えとして返すというもの。
- 基本参考回答に則りつつ、lowercase alphabet 以外が来たときも想定して ValueError を返すようにしてみた。
- count_alphabet を count_lowercase_alphabet に命名するか迷ったが、問題がそもそも lowercase 前提なので、あえて命名には含めなかった。好みの問題とは思う。
- Time Complexity: O(n k), Space Complexity: O(n k)
  - k は str の maximum length として、k は count_alphabet 内のループにかかる

```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def count_alphabet(s: str) -> Tuple[int, ...]:
            counts = [0] * 26
            for c in s:
                alphabet_index = ord(c) - ord("a")
                if not 0 <= alphabet_index < 26:
                    raise ValueError("Invalid character is contained. Only lowercase English letters are allowed.")
                counts[alphabet_index] += 1
            return tuple(counts)

        groups = defaultdict(list)
        for s in strs:
            groups[count_alphabet(s)].append(s)
        return list(groups.values())
```

#### 参考にした回答

- https://github.com/hayashi-ay/leetcode/pull/19/changes の 2nd

## Step 3

- Step 2の解法1で解いた。
- 実装がシンプルで分かりやすいのと、"".join(sorted(s)) を使うよりもワンライナーで書いた時の認知負荷が若干こっちの方が低い気がしたのでこちらが好み。
  - "".join()の方が記述量が多いのはもちろん、list を tuple よりも list を str に変える方が、色んなことに転用される可能性が多くてノイズに感じるからかなと思っている。

```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        return list(groups.values())
```

## Step 4


