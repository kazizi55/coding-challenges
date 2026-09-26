# 127. Word Ladder

## Link

https://leetcode.com/problems/word-ladder/description/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

### 解法1

- 考えたこと
  - beginWord から1文字ずつ変えていって、endWord にたどり着くまでに何個 word を経たかを返す問題。
  - なんか前提条件が多いな。まとめて整理してみる。
    - なので beginWord と endWord もその数に含める。
    - beginWord は wordList に含まれている必要はない(含まれている可能性もある)。endWord は含まれていなければならない。
    - beginWord, endWord, wordList は全て小文字の alphabet で文字の長さも同じ。
    - beginWord と endWord は not equal
    - wordList はダブりなし
    - wordList も beginWord も必ず存在。
    - `Every adjacent pair of words differs by a single letter.`
      - ん、example1 だと dog と lot が横並びになっているぞ、、どっちが正しいんだ。
      - ああ、これは a transformation sequence のことを言っているのであって、wordList のことではないのか。
  - wordList を前から探索しながら、その単語を word_in_transformation と1文字ずつ比較していって、違いが2文字以上ある時点で skip、そうでない場合は word_in_transformation をその単語に置き換えて num_transformation も increment、endWord と1文字しか違いがなくなった時点でその num_transformation を返す、何もヒットしなかったら 0 を返す、というふうにすれば解けそう。
  - うーん、時間切れ。Gemini に聞いてみる。

```py
# 時間切れ
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        num_transformation = 0
        word_in_transformation = beginWord
        for word in wordList:
            for ch in word:
                for ch2 in word_in_transformation:
                    
        return num_transformation
```

- 考えたこと
  - 先に考えていた線形探索だと、word_in_transformation がリストの前方にあったときに対応できない。
  - BFS を用いて解き直した。
  - DFS だと最小の transformation の数ではなく、最初の一致する transformation の数を返すのでこの問題に対応できない。
    - 厳密には currentWord == endWord になったタイミングで都度 transformation の数を保持しておき、その条件がヒットするたびに、min() で比較して格納していけば理論上は解けるが、backtrack を実装しないといけない都合上、全経路探索になり、時間計算量としては、O(N! * M^2) になるため (N は len(wordList)、M は len(wordList[i]))、Python で実行すると、最悪 5000! * 10^2 / 10^7 秒かかる。5000! が 約 10^16310 年なので確実に TLE となる。(宇宙が誕生してから 10^10 年。)
    - アルゴリズムの違いだけで宇宙単位の違いが出るの面白いな。
    - https://www.numberempire.com/factorialcalculator.php?number=5000
  - 想定ユースケース
    - 不正な入力に対してエラーを返すとかもしていないので社内利用前提のスクリプトなどを想定。
    - グラフ全体の保持が不要なので、メモリ制約が厳しい場合に有用か。小文字アルファベット前提なので、数字や Unicode を扱う用途には不向き。
    - 単語長が2乗で増加していくので、ある程度短い前提。
  - 計算量
    - M は len(wordList[i]), N は len(wordList) とする
    - 時間計算量: O(M^2 * N)
      - wordList を word_list の set() に変換するのに O(M * N) かかる
      - word_and_num_sequence_to_visit の while ループは最悪 N + 1 回
        - beginWord と wordList 全て
      - while ループ内の外側の for ループは M 回、内側のループは 26 回
      - さらに next_word を作るのに、O(M) かかる。
      - next_word を word_list と visited で探索するのに hash(next_word) を実行する必要があり、それにも O(M) かかる。
      - なので、M * N + (N + 1) * M * 26 * (M + M) = M * N + 52 * M^2 * N + 52 M^2 がざっくりの計算量となる。
      - この問題の制約上の Python での推定実行時間は、最大で、(10 * 5000 + 52 * 10^2 * 5000 + 52 * 10^2) / 10^7 = 2.6 秒 程度。
    - 空間計算量: O(M * N)
      - word_list, word_and_num_sequence_to_visit, visited にそれぞれ長さ M の単語を N 個保持するため。
      - この問題の制約上の Python での推定最大メモリ使用量は、
        - 文字データ: 10 * 1 Byte * 5000 = 50 KB
        - ポインタ: 3 * 5000 * 8 Byte = 120 KB
        - 合計して 170 KB

```py
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_list = set(wordList)
        word_and_num_sequence_to_visit = deque([(beginWord, 1)])
        visited = set([beginWord])
        while word_and_num_sequence_to_visit:
            current_word, current_num_sequence = word_and_num_sequence_to_visit.popleft()
            if current_word == endWord:
                return current_num_sequence
            for i in range(len(current_word)):
                for c in string.ascii_lowercase:
                    next_word = current_word[:i] + c + current_word[i+1:]
                    if next_word not in word_list or next_word in visited:
                        continue
                    visited.add(next_word)
                    word_and_num_sequence_to_visit.append((next_word, current_num_sequence + 1))
        return 0
```

## Step 2

- `何かをしようとして、そのことを覚えておきながら別のことをしようとすると、覚えておかないといけないので混乱する`
  - 発想法。処理が長くなってきた時に、別関数に分けずに1つの関数だけで書こうとすると、一度に覚えていないといけないものが増える。分離することで自然言語で処理を表現できるようになり、また変数のスコープも関数ごとに狭まるので、処理の詳細を覚えておく必要がなくなる。発想をそのまま形にしやすくなる。
  - https://github.com/goto-untrapped/Arai60/pull/57#discussion_r1781365485
- `通らなかったらよくない解答である、通ったらよい解答である、というようには見ないほうがいい`
  - 同意。実際のユースケースを想定するのもこれを前提にしているからという理解。
  - https://github.com/t0hsumi/leetcode/pull/20#discussion_r1938166243

### 解法1: pattern と words を dict に格納する

- 参考にした回答
  - https://github.com/hayashi-ay/leetcode/pull/42/changes の 4th
  - https://github.com/tarinaihitori/leetcode/pull/20/changes の 3rd
- 考えたこと
  - 1 文字違いの pattern と words の dict を作成し、wordList を前から見ていき、pattern が一致した words を BFS で探索していく解法。
  - `make_patterns` で関数に切り出したことで見通しが良くなった。
  - `pattern_to_words[pattern] = []` を追加することで、wordList の複数単語で同じパターンを共有している場合にそれらを skip することができる。
  - 想定ユースケース
    - 小文字アルファベットに依存しないので、任意文字コードを含む文字列探索に使える。
    - step1 同様、単語長がある程度短い前提。
  - 計算量
    - M は len(wordList[i]), N は len(wordList) とする
    - 時間計算量: O(M^2 * N)
      - pattern_to_words に値を追加するのに M^2 * N
      - BFS で wordList を前からパターンを作成しながら探索していくのに M^2 * N
      - 問題の制約に基づいた Python での最大推定実行時間は、2 * 10^2 * 5000 / 10^7 = 100ms 程度
    - 空間計算量: O(M^2 * N)
      - pattern_to_words が M^2 * N
        - key が M^2 * N
        - value が M * N
      - visited, words_to_visit がそれぞれ N
      - 問題の制約に基づいたPython での最大推定メモリは、10^2 * 5000 + 10 * 5000 * 8 + 2 * 5000 * 8 = 980KB 程度

```py
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        def make_patterns(word: str) -> List[str]:
            patterns = []
            for i in range(len(word)):
                patterns.append(f"{word[:i]}*{word[i+1:]}")
            return patterns
        
        if endWord not in wordList:
            return 0
        pattern_to_words = defaultdict(list)
        for word in wordList:
            for pattern in make_patterns(word):
                pattern_to_words[pattern].append(word)
        visited = set([beginWord])
        words_to_visit = [beginWord]
        num_words = 1
        while words_to_visit:
            num_words += 1
            next_words = []
            for word in words_to_visit:
                for pattern in make_patterns(word):
                    for next_word in pattern_to_words[pattern]:
                        if next_word == endWord:
                            return num_words
                        if next_word in visited:
                            continue
                        visited.add(next_word)
                        next_words.append(next_word)
            words_to_visit = next_words
        return 0
```

### 解法2: 隣接リスト用の class を作成する

- 参考にした回答
  - https://discord.com/channels/1084280443945353267/1303605021597761649/1306631474065309728
- 考えたこと
  - 解法1と考えはそのままに関連する処理を WordNeighbor クラスにまとめた解法。
    - key を word 内の文字を一つ飛ばしにした tuple にしている点では少し違う。
  - クラスで表現すると自然言語で各処理を表現できるだけでなく、関数同士の凝集性も上がって一層見やすい感じがあって好み。
  - yield を使うと、値を返しつつ後続の処理を継続できる。iterator を返すので、for loop などで使うことできる。
    - https://www.w3schools.com/python/ref_keyword_yield.asp
  - 想定ユースケース
    - 解法1と基本的に同じ。
    - だが、WordNeighbor クラスを作成して隣接判定ロジックと BFS の責務を分離しているため、各ロジックの変更・拡張が容易になる。テストも書きやすい。
      - 実務だったらこのように書くと思う。
  - 計算量
    - 解法1と同じ。

```py
class WordNeighbors:
    def __init__(self):
        self.key_to_neighbors = defaultdict(list)
    
    def to_key(self, word):
        for i in range(len(word)):
            yield (word[:i], word[i + 1:])
    
    def add(self, word):
        for key in self.to_key(word):
            self.key_to_neighbors[key].append(word)
    
    def get_neighbors(self, word):
        for key in self.to_key(word):
            for neighbor in self.key_to_neighbors[key]:
                yield neighbor

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        neighbors = WordNeighbors()
        for word in wordList:
            neighbors.add(word)
        level = 1
        words = [beginWord]
        visited = set([beginWord])
        while words:
            next_words = []
            for word in words:
                if word == endWord:
                    return level
                for neighbor in neighbors.get_neighbors(word):
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    next_words.append(neighbor)
            words = next_words
            level += 1
        return 0
```

### 解法3: ハミング距離を利用

- 参考にした回答
  - https://github.com/hayashi-ay/leetcode/pull/42/changes の 4th
  - https://github.com/tarinaihitori/leetcode/pull/20/changes の 2nd
  - https://github.com/nanae772/leetcode-arai60/pull/20 の 4th
- 考えたこと
  - ハミング距離、初めて知った。「同じ長さを持つ2つのデータ（文字列、バイナリ列、ベクトルなど）において、対応する位置の値が異なっている箇所の総数」。まさにこの問題と合致する。
    - https://www.ibm.com/think/topics/hamming-distance
  - `「ハミング距離1かそうでないか」をチェックするのが目的で、距離の長さ自体は利用していないので、ハミング距離が1かどうかというメソッドを作れば良いと思いました。`
    - これは確かに。ロジックをより効率化できるメリットもある。
    - https://github.com/nanae772/leetcode-arai60/pull/20#discussion_r2378658187
  - ハミング距離は編集距離の一つ。ハミング距離は2つのデータの長さが一致していないといけない、操作が置き換え以外できないなどの制約がある。
    - https://www.geeksforgeeks.org/dsa/edit-distance-dp-5/
    - https://github.com/tarinaihitori/leetcode/pull/20/changes#r1853203044
  - 1文字違いの隣接リストを作成し、wordList を前から見ながら、BFS で探索していく解法。
  - 想定ユースケース
    - 単語数が少なく、単語長が長いデータで有効。
  - 計算量
    - M は len(wordList[i]), N は len(wordList) とする
    - 時間計算量: O(M * N^2)
      - 具体的には M * N + M * N * (N-1)/2 + M * N + M * N * 25 * M /2
        - BFS 部分は neighbor 同士は一文字ずつしか違わないので、各単語の neighbor は最大でも 25 * M 個となる
      - 問題の制約に基づいた Python での最大推定実行時間は、(10 * 5000 + 10 * 5000 * 4999 / 2 + 10 * 5000 + 10 * 5000 * 25 * 10 / 2) / 10^7 ≈ 13s
        - LeetCode 上の実行時間は 6s 前後。やはりあまり当てにするべきではない。
    - 空間計算量: O(M * N)
      - 具体的には M * N * 25 + 2 * N
        - M * N * 25: 各単語の最大 25 * M 個の隣接リストの合計ポインタ数
        - 2 * N: dict の key (N) + visited / queue (N) のポインタ数
      - 問題の制約に基づいたPython での最大推定メモリは、(10 * 5000 * 25 + 2 * 5000) * 8 ≈ 10MB

```py
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        def has_one_char_diff(word1, word2):
            num_diff = 0
            for ch1, ch2 in zip(word1, word2):
                if ch1 != ch2:
                    num_diff += 1
                if num_diff > 1:
                    return False
            return num_diff == 1
        
        if endWord not in wordList:
            return 0
        word_to_neighbors = defaultdict(list)
        for i in range(len(wordList) - 1):
            for j in range(i + 1, len(wordList)):
                word1, word2 = wordList[i], wordList[j]
                if not has_one_char_diff(word1, word2):
                    continue
                word_to_neighbors[word1].append(word2)
                word_to_neighbors[word2].append(word1)
        for word in wordList:
            if not has_one_char_diff(beginWord, word):
                continue
            word_to_neighbors[beginWord].append(word)
            word_to_neighbors[word].append(beginWord)
        words = [beginWord]
        visited = set([beginWord])
        num_words = 1
        while words:
            next_words = []
            for word in words:
                if word == endWord:
                    return num_words
                for neighbor in word_to_neighbors[word]:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    next_words.append(neighbor)
            words = next_words
            num_words += 1
        return 0
```

## Step 3

- 考えたこと
  - 可読性・拡張性、またこの問題に対する効率性を考慮し、step 2 の解法2が最も好み。

```py
class WordNeighbors:
    def __init__(self):
        self.key_to_neighbors = defaultdict(list)
    
    def to_key(self, word):
        for i in range(len(word)):
            yield (word[:i], word[i + 1:])
    
    def add(self, word):
        for key in self.to_key(word):
            self.key_to_neighbors[key].append(word)
    
    def get_neighbors(self, word):
        for key in self.to_key(word):
            for neighbor in self.key_to_neighbors[key]:
                yield neighbor

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if not endWord in wordList:
            return 0
        neighbors = WordNeighbors()
        for word in wordList:
            neighbors.add(word)
        words = [beginWord]
        visited = set([beginWord])
        level = 1
        while words:
            next_words = []
            for word in words:
                if word == endWord:
                    return level
                for neighbor in neighbors.get_neighbors(word):
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    next_words.append(neighbor)
            words = next_words
            level += 1
        return 0
```

## Step 4


