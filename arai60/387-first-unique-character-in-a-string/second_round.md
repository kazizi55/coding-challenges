# 387. First Unique Character in a String

## Link

https://leetcode.com/problems/first-unique-character-in-a-string/description/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

### 解法1: set() と dict() の両方を使う

- 考えたこと
  - 重複していない文字のうち一番最初の index を返すという問題。
  - パッと思い浮かぶのは、set() の seen と character:index の hashmap の unique_charcter_to_index を作成しておいて、s を for loop で探査しながら seen と unique_character_to_index に値を入れていき、重複する値があったら unique_character_to_index から値を除く、最終的に sorted(unique_character_to_index.values())[0] を返す解法。とりあえず書いてみる。
  - 思った通りに書いて AC はしたが、seen と unique_character_to_index を両方保持するのが若干冗長な感じもある。for loop 1回で終わるのは良さではある。
  - 想定ユースケース
    - 公開 web サイトとかでユーザーが自由に値を入力して遊べるようなミニアプリ。
    - なので、LeetCode にあるような小文字のアルファベットでなくても処理が通るようにロジックを実装した。
    - UX を考えたら、s.length を 10^7 を超えると1秒以上時間がかかるようになってしまうので、10^7 以上のlength の入力は弾くとしても実際のアプリだといいかもしれない。
  - 計算量
    - 時間計算量: O(N)
      - Python の実行可能 step 数を 10^7 とし、LeetCode の constraints に基づき、最大 s.length として 10^5 が入力されると仮定すると、最悪時間計算量は、10^5/10^7 = 0.01 = 10ms ほどになる。
    - 空間計算量: O(k) (k は s に含まれる文字列の種類の数)
      - 1文字を 8 Byte とし、最大 s.length として 10^5 が入力されると仮定し、含まれる文字がすべて unique とする。小文字のアルファベットだけだと26種類だけなので、最悪空間計算量は、8 * 3 (seen, unique_character_to_index, unique_character_indexes) * 26 = 624B ほどになる。

```py
class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        unique_character_to_index = dict()
        for index, c in enumerate(s):
            if c in seen:
                if c in unique_character_to_index:
                    unique_character_to_index.pop(c)
                continue
            seen.add(c)
            unique_character_to_index[c] = index
        unique_character_indexes = list(unique_character_to_index.values())
        if len(unique_character_indexes) == 0:
            return -1
        return sorted(unique_character_indexes)[0]
```

## Step 2

- `LRU という名前は Least Recently Used という意味で、使わないやつから削除するということなので、現在の実装である同じものが2つ以上入ると Remove で linked list だけから削除されるというのは、ちょっと誤解を生む気がします。`
  - 認識同じ。LRU をある程度改造した時点で LRU 以上の何かになっているのだから命名も変えるべき。
  - https://github.com/colorbox/leetcode/pull/29#discussion_r1861030810  
- `LinkedHashMapやPythonのOrderDict、3.7以降のdictは要素の挿入順番を覚えているので、1回登場した文字のインデックスを保持するハッシュテーブルに最後まで残った要素の先頭が求める答えるなります`
  - なるほど、挿入順番を頼りにするとしたら unique first character の index を value として保持する必要もないな。この視点はなかった。
  - https://discord.com/channels/1084280443945353267/1233603535862628432/1237973490796072991
  - `Changed in version 3.7: Dictionary order is guaranteed to be insertion order. This behavior was an implementation detail of CPython from 3.6.`
    - ちなみに OrderedDict でなくとも通常の dict でも挿入順に並ぶことは3.7以降保証されているとのことだった。
    - https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
- `個人的には特段パフォーマンス要件などなければハッシュテーブルでいいかなと思います`
  - 上の discord コメントより。
  - list の index access は memory direct access だが、dict の retrieval は hash key の計算をしたりする都合上、やや遅くなる。ともに O(1) ではあるので millisecond レベルの最適化をしたい場合に list を選ぶとかがいいんだろうか。基本は hash table の方が key で検索ができたりと使い回しが良いので。
    - https://stackoverflow.com/questions/39192442/which-is-faster-a-dictionary-retrieve-or-a-list-indexing
- `川があって、毎日文字が1文字ずつ流れてきます。川の側に小屋があって、そこから流れてくる文字を監視しています。それで、文字が流れ終わったあとに、最初に流れてきた1回しか流れてこない文字を報告します。で、毎日、仕事を一人でやっていると辛いので、(労働基準法上、連続勤務は12日までです。)シフトを決めて仕事の引き継ぎをしたいのです。`
  - oda さんの例えはいつも興味深い。
  - 自分は割と解法を考える時は pseudo code くらい具体的な処理の流れを先に考えてしまうが、このような物語形式的な方がイメージがしやすく忘れづらそうなのと人に説明しやすそう。普段コードを書く時からこういうもっと物語的なイメージをする癖をつけるようにする。
  - https://discord.com/channels/1084280443945353267/1233603535862628432/1238208008182562927
- Java に LinkedHashMap というものがあるらしい。挿入順を保持する hashmap ということで実質 Python 3.7以降の dict と同じような動きをするということだろうか
  - https://docs.oracle.com/javase/8/docs/api/java/util/LinkedHashMap.html
- `実際に、何が最善かは状況によるのですが、ここで問題になっているのは、「どれくらいの幅で可能性と対策が見えているか」です。 ... 一方で、二分探索の入力がソートされているかを確認していたら何をしているか分かりませんね。そういう具合でいろいろな事情で変わるわけですが、そこまで考えて行動しましょうということです。`
  - 参照先の discussion では呼び出し側に例外処理をさせる前提で考えていた旨の記載があり、それに対するコメント。
  - 例示されている二分探索の入力はソートされている前提なので、確かに呼び出し先で確認するのは責務範囲外という感じがする。
  - 銀の弾丸はない。やはり想定ユースケースを解法ごとで考えてそれに適しているかどうかで考えるのが良いのだろう。
  - https://github.com/quinn-sasha/leetcode/pull/15#discussion_r1970861088
- str.encode() はデフォルトで utf8 でエンコードする
 - https://github.com/ichika0615/arai60/pull/12#discussion_r1986042349
- `if s.find(character) == s.rfind(character)` を使うと一発で first unique character を返せるのか。
  - 計算量的には O(N^2) だが、内部でネイティブコードが動いているので早い
  - https://github.com/t0hsumi/leetcode/pull/15/changes#r1930362913
- collections.Counter を使っても実装できる。
  - https://docs.python.org/3/library/collections.html#collections.Counter
  - https://github.com/olsen-blue/Arai60/pull/15/changes

### 解法1: dict の挿入順が保存されていることを利用する

- 参考にした回答
  - https://github.com/hayashi-ay/leetcode/pull/28/changes の 4th
- 考えたこと
  - step 1 と基本的に考え方が同じだが、最後の return の仕方が違う。`next(iter(unique_charater_to_index.values()))` の方が iterator の一番最初の値を返すだけなので早い。O(1)で済む。sorted()を使うと sort してから最初の値を返すので、O(k log k) かかる。(k は len(unique_character_to_index.values()))
  - step1 では pop() を使っていたが、返り値を使わないのに、pop() を使うのは冗長だなと思ったので、参考回答通り del を使うで良さそう。pop() の方が key が存在しなかった時に error ではなく default で返す値を設定できるのが違いか。
    - https://docs.python.org/3/library/stdtypes.html#dict.pop
    - https://docs.python.org/3/library/stdtypes.html#dict
  - 参考回答、seen が暗黙的に重複しているものだけを add するようになっているのが引っかかる。個人的には1度しか出てきていないものも含めて add した方が seen という言葉の意味により近いと思う。
  - `if len(unique_character_to_index) == 0` か `if not unique_character_to_index` でいうと、PEP8 的には `For sequences, (strings, lists, tuples), use the fact that empty sequences are false` とあるので、後者のが準拠しているのか。
    - https://peps.python.org/pep-0008/#programming-recommendations
  - 想定ユースケース
    - step1 と同様、ユーザーに公開しているミニアプリ。
  - 計算量も step1 と同様。sorted() ではなく、next(iter()) を使って O(k log k) から O(1) にしているのでわずかに早くはなる。

```py
class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        unique_character_to_index = dict()
        for i, c in enumerate(s):
            if c in unique_character_to_index:
                del unique_character_to_index[c]
                continue
            if c in seen:
                continue
            seen.add(c)
            unique_character_to_index[c] = i
        if not unique_character_to_index:
            return -1
        return next(iter(unique_character_to_index.values()))
```

### 解法2: list の direct index access を利用する

- 参考にした回答
  - https://github.com/hayashi-ay/leetcode/pull/28/changes の 1st
  - https://github.com/quinn-sasha/leetcode/pull/15/changes の 3rd
- 考えたこと
  - lowercase English letters の数に関しては PEP8 に則り uppercase の定数にして module レベルで定義。`ord("z") - ord("a") + 1`とかの定義もできるが厳密には定数ではなくなってしまうので26のベタ書きとした。
    - https://peps.python.org/pep-0008/#constants
  - `return -1` を最後ではなく途中に配置するような流れにしようとすると、以下のようにalphabet_frequencies のうち value が1のものだけ index を順番に取り出して別の list に格納するみたいなことをして複雑になってしまう。
    - `target_index = next((i for i, c in enumerate(s) if alphabet_frequencies[ord(c) - ord("a")] == 1), -1)`
  - 普段は自分はreturn - 1などの happy path 以外のロジックは途中に入れたい派なのだが、ロジックの簡潔さを犠牲にしてまで`return -1`を途中に持ってこようとは思わないので途中においた。
  - 想定ユースケース
    - 入力できる文字の種類が英字小文字だけとかなり限られているので、ライブラリの1関数として提供するというユースケースが良さそう。
    - 英字小文字以外が渡されたらエラーを raise するのが呼び出し側としては扱いやすいはず。
      - 2度目のループで c は lowercase English letter であることが確定しているのに、またチェックするのが若干冗長に感じるが、`ord(c) - ord("a")`を関数に切り出したかったのと、その処理とエラー処理はセットにして関数化したかったので許容とした。
  - 計算量
    - 時間計算量: O(N)
      - step1、step2 の解法1と同じ時間計算量だが、loop が2回走るので、10ms * 2= 20msほどかかる見込み。
      - が、hash table を使う 1 pass よりも direct index access を使う 2 pass の方が実際は早いかもしれない。
    - 空間計算量: O(1)
      - 1文字を 8 Byte とし、8 * 26 = 208B。

```py
class Solution:
    ALPHABET_SIZE = 26
    def firstUniqChar(self, s: str) -> int:
        def to_alphabet_index(c: str) -> bool:
            alphabet_index = ord(c) - ord("a")
            if not 0 <= alphabet_index < Solution.ALPHABET_SIZE:
                raise ValueError(
                    "Input character is not a lowercase English letter",
                    f"character: {c}"
                )
            return alphabet_index

        alphabet_frequencies = [0] * Solution.ALPHABET_SIZE
        for c in s:
            alphabet_frequencies[to_alphabet_index(c)] += 1
        for i, c in enumerate(s):
            if alphabet_frequencies[to_alphabet_index(c)] == 1:
                return i
        return -1
```

## Step 3

- 考えたこと
  - step2 の解法1が好みだが、より慣れていない解法2を練習する。
  - alphabet_frequencies という命名が若干不親切だなと思ったが、何回か解きながら考えうる中で最善ではないかと思い直した。
    - `lowercase English letter 内の順番を index に当てはめた上で value を頻度としたもの` という実態が名前を見てパッとわからないのではと思ったが、これ以上わかりやすくしようとすると、`alphabet_offset_frequencies`といった感じでどういうデータ構造かを明示する必要がある。
    - リファクタを今後していくとしてデータの保持の仕方が変わったときに命名も変えなくてはいけないのはメンテナンス性が悪いかなという気持ち。
    - Google Style Guide の `names that needlessly include the type of the variable (for example: id_to_name_dict)` というルールもこの考え方が背後にあると思っている。
      - https://google.github.io/styleguide/pyguide.html#3161-names-to-avoid

```py
class Solution:
    ALPHABET_SIZE = 26
    def firstUniqChar(self, s: str) -> int:
        def to_alphabet_index(c: str) -> int:
            alphabet_index = ord(c) - ord("a")
            if not 0 <= alphabet_index < Solution.ALPHABET_SIZE:
                raise ValueError(
                    "Input character is not a lowercase English letter",
                    f"character: {c}"
                )
            return alphabet_index
        
        alphabet_frequencies = [0] * Solution.ALPHABET_SIZE
        for c in s:
            alphabet_frequencies[to_alphabet_index(c)] += 1
        for i, c in enumerate(s):
            if alphabet_frequencies[to_alphabet_index(c)] == 1:
                return i
        return -1
```

## Step 4


