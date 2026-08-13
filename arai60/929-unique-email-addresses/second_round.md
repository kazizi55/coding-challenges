# 929. Unique Email Addresses

## Link

https://leetcode.com/problems/unique-email-addresses/description/

## How to work on each step

- Step 1: 答えを見ずに 15 分以内に解く。
- Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。
- Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。
- Step 4: いただいたレビューをもとに、コードを整える。

なお、[oda さんの提案](https://discord.com/channels/1084280443945353267/1366778718705553520/1450943270799671337)を参考に、コードを書く部分にフォーカスして Arai60 を1周しています。今回は2周目に当たります。

## Step 1

- 改めて見ると条件が複雑に見えるな。書き出してみる。
  - @ で local name と domain name に分ける
  - . は local name に入っていたらあってもなくても同じものにカテゴライズ。domain name は別のものとしてカテゴライズ
  - + は local name に入っていたら最初の + 以降のものが全て無視される。domain name は特になし。
- loop で emails を探索しつつ、上記の条件で変形させたものを set() に格納していき、その len を返せばいけそう。
- 条件が多いので関数に分けたくなる。自然言語で説明してもややこしくなるレベルのものは関数に分けるべきだろう。

### 解法1: format_email 関数を作成してそこでまとめてフォーマットする

- `Wrong Answer 184 / 188 testcases passed`
- なんでだろう、、Gemini に聞いてみる。
- ああ、str.strip()は末端の値しか strip しないのか、、
  - https://docs.python.org/3/library/stdtypes.html#str.strip をみて仕様をわかった気になっていた。反省。

```py
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def format_email(email: str) -> str:
            local, domain = tuple(email.split("@"))
            stripped_local = local.strip(".")
            stripped_local = stripped_local.split("+")[0]
            return stripped_local + "@" + domain

        formatted_emails = set()
        for email in emails:
            formatted = format_email(email)
            formatted_emails.add(formatted)
        return len(formatted_emails)
```

- str.strip() を str.replace() に変えて AC。
- Time Complexity: O(N * L) (L は email の長さ)
  - for loop で emails を1個ずつ探索するのと、format_email 内でそれぞれの文字列の探索も行うため。
  - emails.length は最大100個、各 email の最大長も100なので、最悪でも大体 Python だと、100 * 100 / 10^7 = 0.001 = 1ms ほどで計算が終わる見込み。
- Space Complexity: O(k * L) (k は len(formatted_emails)、L は email の長さ)
  - formatted_emails に格納されている要素数 * それぞれの文字列の長さ。
  - emails.length が最悪 N になるとして最大100個、各 email の最大長も100として考えると、8 byte * 100 * 100 = 80 KB 程度になる

```py
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def format_email(email: str) -> str:
            local, domain = email.split("@")
            stripped_local = local.replace(".", "")
            stripped_local = stripped_local.split("+")[0]
            return stripped_local + "@" + domain

        formatted_emails = set()
        for email in emails:
            formatted = format_email(email)
            formatted_emails.add(formatted)
        return len(formatted_emails)
```

## Step 2

- `気にしているのは、オーダーが正しく動くか、ではなくて、半年後に読んだ別の同僚が不安にならないか、環境の変化に対して頑健か`
  - 常識に反することをするということはメンテナンス性や可読性を損なうことがあるということを認識しておく。
  - https://discord.com/channels/1084280443945353267/1200089668901937312/1210619083385479258
- str.split には maxsplit を渡すこともできる。また、右から分割する str.rsplit もある。
  - https://docs.python.org/3.12/library/stdtypes.html#str.split
  - `email.rsplit("@", maxsplit=1)で分割してあげれば@マークが最低1つ存在する場合については確実に有効なドメインが取得できそうです。`
    - なるほど、こういう使い方もできるな。
    - https://discord.com/channels/1084280443945353267/1200089668901937312/1209416153982697492
- `The labels must follow the rules for ARPANET host names.  They must start with a letter, end with a letter or digit, and have as interior characters only letters, digits, and hyphen.  There are also some restrictions on the length.  Labels must be 63 characters or less.`
  - email の始まりは文字でないといけないのか、知らなかった
  - https://www.ietf.org/rfc/rfc1034.txt#:~:text=The%20labels%20must%20follow%20the%20rules%20for%20ARPANET%20host%20names.%20%20They%20must%0Astart%20with%20a%20letter%2C%20end%20with%20a%20letter%20or%20digit%2C%20and%20have%20as%20interior%0Acharacters%20only%20letters%2C%20digits%2C%20and%20hyphen.%20%20There%20are%20also%20some%0Arestrictions%20on%20the%20length.%20%20Labels%20must%20be%2063%20characters%20or%20less
- ""って RFC には local name にも使えると定義されているのか。が、gmail とかだと受け入れていないらしい。確かに扱いに困りそうではある。
  - https://datatracker.ietf.org/doc/html/rfc5322#section-3.4.1
  - `"john@doe"@domain.com` みたいに @ を複数持つこともできてしまうのかー。
    - https://github.com/SuperHotDogCat/coding-interview/pull/30#discussion_r1646552062
- `とりあえず、ユースケースの想定ですね。これ、そもそもなんでこんなものを作りたいんだと思いますか。`
  - 銀の弾丸はない。これは面接だけではなくて普段の仕事でも重要な視点だと再認識した。
  - https://github.com/Yoshiki-Iwasa/Arai60/pull/13#discussion_r1649832719
- RFC は規格ではない。インターネット技術の標準的な仕様を記した文書。
  - https://github.com/rinost081/LeetCode/pull/13#discussion_r2099861018
- `最低限、「パレート最適」、つまり、何かを改善しようとすると、何かが悪くなる、くらいにはよいコードを書きたいです。その中では比較的、コードの複雑さ(code complexity) が優先される事が多いです。`
  - パレート最適、知らなかった。
  - https://github.com/Ryotaro25/leetcode_first60/pull/66#discussion_r2035896259

### 解法1: State Machine を実装した解法 (登録されているデータを利用する想定)

- 参考にした解法
  - https://github.com/hayashi-ay/leetcode/pull/25/changes の 6th
- 考えたこと
  - この canonicalize_email のように、状態を保持しつつ、入力に応じて状態を遷移させていくパターンを (Finite) State Machine という
    - https://discord.com/channels/1084280443945353267/1200089668901937312/1207996784211918899
    - https://en.wikipedia.org/wiki/Finite-state_machine
  - for loop で emails を探索しながら、それぞれの email の文字をさらに探索し、 State Machine を用いてドメイン名かどうか無視すべき箇所かどうかを判別しつつ、正規化した email を答えの set() に格納していく解法。
  - step1 でかいた format_email よりも canonicalize の方が関数により情報を与えられている感じで好み
    - numUniqueEmails の配下にあるので、_email はなくても email が対象であることは自明のように思えた
  - Python の文字列は immutable なので、canonicalized を文字列で保持すると + や += で結合されるたびに新しい文字列の作成とデータコピーが発生し、Time Complexity がO(L^2) に悪化してオーバーヘッドが大きくなる。一方で、配列で保持しておき最後にその配列を join して文字列として返すことで O(L) で行える。
  - Time Complexity と Space Complexity はともに Step1 と同じ。
  - 想定ユースケースとしては、マーケティングメールを送るための既存顧客のメアドのリストアップとした。一度既存顧客のメアドとして登録されているものなので、@が二つ含まれているなどの不正なメアドはその時に validation がかかってそもそも登録されていないとした。
  - 計算量は step1 と同じ
    - Time Complexity: O(N * L) (L は email の長さ)
    - Space Complexity: O(k * L) (k は len(canonicalized_emails)、L は email の長さ)

```py
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def canonicalize(email: str) -> str:
            canonicalized = []
            is_domain = False
            skip_alias = False
            for c in email:
                if is_domain:
                    canonicalized.append(c)
                    continue
                if c == "@":
                    is_domain = True
                    canonicalized.append(c)
                    continue
                if skip_alias:
                    continue
                if c == "+":
                    skip_alias = True
                    continue
                if c == ".":
                    continue
                canonicalized.append(c)
            return "".join(canonicalized)

        canonicalized_emails = set()
        for email in emails:
            canonicalized_emails.add(canonicalize(email))
        return len(canonicalized_emails)
```

### 解法2: 正規表現を利用した解法 (ユーザーから入力される想定)

- 参考にした解法
 - https://github.com/t0hsumi/leetcode/pull/14/changes の 4th
 - https://github.com/plushn/SWE-Arai60/pull/14/changes の 2nd
 - https://github.com/fhiyo/leetcode/pull/17/changes の 4th
- 考えたこと
  - 解法1の想定ユースケースとは違うユースケースで使えるようなものを探す。今回はメアドの一括登録とする。ユーザーからの入力を直接受け付けるため、不正な値かどうかをより厳密に見なくてはならない。LeetCode のconstraints を登録したい内容と仮定して処理を書く
  - あと、正規表現を使っても解けそうなのでそのような解法がないかも探す。
  - RFC 上だと email ば最大254文字とされている。LeetCode の constraints は RFC より厳しい制約なのか。より厳しい方を採用する。
    - https://github.com/plushn/SWE-Arai60/pull/14#discussion_r2052171339
  - 用語
    - normalize: 内部的な冗長性をなくすための正規化
      - なるほど、例えば DB の正規化はこっちなのか。
    - canonicalize: 比較のための（外部への表示としての）正規化
      - 今回はこちら。
  - re.match() は前方部分一致、re.fullmatch() は完全一致。今回は厳密に見たいケースなので後者。
    - https://docs.python.org/3/library/re.html#re.match
  - 正規表現を使うとやりたいことを凝縮して書けるが、可読性が低くなりやすいなと思ったので関数に分けたり、parse と replace の処理を分けたりするなどした。
  - LeetCode の シンプルな constraints に従っているかどうかの validation を実装するだけでもやや複雑だなと思ったので、実際の email の validation は結構大変なんだろうなと思った。もっと許容する幅を増やさないといけないので。
    - これを思い出した。RFC に則ると許容度がだいぶ広くなるので意図的に制約を厳しくした parse library の例。
      - https://github.com/colinhacks/zod/issues/3155
  - 計算量は step1 と同じ
    - Time Complexity: O(N * L) (L は email の長さ)
    - Space Complexity: O(k * L) (k は len(canonicalized_emails)、L は email の長さ)

```py
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def is_valid(email: str) -> bool:
            if not 1 <= len(email) <= 100:
                return False
            parsed_email = re.fullmatch(r"[a-z0-9][a-z0-9.\+]*@[a-z0-9.\+]+\.com$", email)
            return parsed_email is not None
            
        def canonicalize(email: str) -> str:
            parsed_email = re.match(r"^(.+)@(.+)$", email)
            local, domain = parsed_email.groups()
            local = re.sub(r"\+.*|\.", "", local)
            return f"{local}@{domain}"

        canonicalized_emails = set()
        for email in emails:
            if not is_valid(email):
                raise ValueError(
                    "numUniqueEmails(): Input email is invalid: ",
                    f"email = {email}"
                )
            canonicalized_emails.add(canonicalize(email))
        return len(canonicalized_emails)
```

## Step 3

- 考えたこと
  - 正規表現に慣れたいので step2 の解法2で練習
  - canonicalized() でも re.fullmatch() を使うように
  - re.fullmatch() 使用時の末尾の冗長な $、\ を削除

```py
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def is_valid(email: str) -> bool:
            if not 1 <= len(email) <= 100:
                return False
            parsed_email = re.fullmatch(r"[a-z0-9][a-z0-9.+]*@[a-z0-9.+]+.com", email)
            return parsed_email is not None
        
        def canonicalize(email: str) -> str:
            parsed_email = re.fullmatch(r"(.+)@(.+)", email)
            local, domain = parsed_email.groups()
            local = re.sub(r"\+.*|\.", "", local)
            return f"{local}@{domain}"
        
        canonicalized_emails = set()
        for email in emails:
            if not is_valid(email):
                raise ValueError(
                    "Input email is invalid.",
                    f"email: {email}"
                )
            canonicalized_emails.add(canonicalize(email))
        return len(canonicalized_emails)
```

## Step 4

### State Machine に振り切る解法

- 純粋な state で管理するようにしたら match 文だけで書けるようになった。状態遷移がよりはっきり見える形になってこれはこれで好み。
- if 文 で書くか match 文で書くか迷ったが、個人的には、左辺が同じものを続けて比較している場合には match 文の方が見やすいと思う。
- state を enum 管理するか迷ったが、1関数のためにやるのは若干やり過ぎ感があるかなと思ったので見送った。クラス全体で使うとか、複数 module で使われるとかなったら enum にすると思う。
  - https://docs.python.org/3/library/enum.html

```py
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def canonicalize(email: str) -> str:
            canonicalized = []
            state = "LOCAL"
            for c in email:
                match state:
                    case "LOCAL":
                        match c:
                            case "@":
                                state = "DOMAIN"
                                canonicalized.append(c)
                            case "+":
                                state = "ALIAS"
                            case ".":
                                continue
                            case _:
                                canonicalized.append(c)
                    case "ALIAS":
                        match c:
                            case "@":
                                state = "DOMAIN"
                                canonicalized.append(c)
                    case "DOMAIN":
                        canonicalized.append(c)
            return "".join(canonicalized)

        canonicalized_emails = set()
        for email in emails:
            canonicalized_emails.add(canonicalize(email))
        return len(canonicalized_emails)
```