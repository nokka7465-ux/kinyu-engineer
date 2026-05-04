# 金融マンがエンジニアになった話

金融機関から未経験で IT エンジニアに転身した実体験ブログの静的サイトです。
転職の流れ・SES の実態・年収変化・使った転職エージェントを正直に公開しています。

- 公開URL（想定）: https://kinyu-engineer.github.io/
- 運営者: tamal（たまる）

## 構成

すべてルート直下に配置されたフラットな静的 HTML サイトです。CSS は各 HTML 内にインラインで記述しています。ビルド工程はありません。

```
.
├── index.html          トップページ（ヒーロー / 記事一覧 / 転職エージェント / プロフィール）
├── privacy.html        プライバシーポリシー
├── article1.html       体験談: 金融機関からエンジニアに転職した正直な話
├── article2.html       体験談: 未経験でSESに入社して1年半経った正直な感想
├── article3.html       ノウハウ: 異業種からエンジニア転職する具体的な手順
├── article4.html       比較: 未経験エンジニア転職エージェントおすすめ3選
├── article5.html       データ: 金融→エンジニア転職で年収はどう変わったか
├── article6.html       体験談: エンジニア転職前に知っておきたかった10のこと
├── article7.html       ノウハウ: 未経験エンジニア転職の面接で聞かれること
├── article8.html       体験談: SESエンジニアの1日のスケジュール
├── article9.html       ノウハウ: Pythonを3ヶ月独学してエンジニア転職した方法
├── article10.html      体験談: エンジニア転職して後悔したこと・よかったこと
├── article11.html      体験談: 金融知識はエンジニア転職で武器になるか
├── article12.html      比較: プログラミングスクール vs 独学 どっちが転職に有利か
├── article13.html      ノウハウ: 未経験エンジニアのポートフォリオは何を作るべきか
├── article14.html      ノウハウ: SESから自社開発に転職する方法
├── article15.html      データ: 30代未経験でもエンジニア転職できるか
├── article16.html      体験談: エンジニア1年目に買ってよかったもの10選
├── article17.html      比較: SES vs SIer vs 自社開発 徹底比較
├── article18.html      ノウハウ: 業務外で勉強を続けるコツ【1年半続けた7つの方法】
├── article19.html      データ: エンジニア転職に効く資格3選
├── article20.html      体験談: SES配属ガチャの実態と対処法
├── article21.html      体験談: SESエンジニアのリモートワーク実態
├── article22.html      ノウハウ: 技術ブログの始め方と継続のコツ
├── article23.html      比較: 文系出身 vs 理系出身 エンジニア転職での差は？
├── article24.html      体験談: コードレビューで言われた指摘TOP10
├── article25.html      データ: フリーランスエンジニアの年収シミュレーション
├── article26.html      比較: 転職サイト・エージェント・リファラル違い
├── article27.html      体験談: 客先常駐エンジニアの人間関係
├── article28.html      ノウハウ: エンジニアの副業の始め方【月3万円】
├── article29.html      データ: 未経験エンジニアの月間労働時間【1年10ヶ月分】
├── article30.html      体験談: エンジニア1年目で身についた最も役立つスキル7選
├── article31.html      ノウハウ: エンジニアの退職交渉と引き継ぎ完全マニュアル
├── article32.html      比較: ITパスポート vs 基本情報技術者
├── article33.html      データ: 未経験エンジニアにスカウトメールは来るのか
├── article34.html      ノウハウ: 未経験エンジニアの英語学習法
└── article35.html      ノウハウ: エンジニアがChatGPTを業務で使い倒した方法
```

## カテゴリとタグ色

| カテゴリ | 該当記事 | 件数 | タグ色 |
|---|---|---|---|
| 体験談 | article1, 2, 6, 8, 10, 11, 16, 20, 21, 24, 27, 30 | 12 | オレンジ (`--accent2` #C4572A) |
| ノウハウ | article3, 7, 9, 13, 14, 18, 22, 28, 31, 34, 35 | 11 | 深緑 (`--accent` #1A3A2A) |
| 比較 | article4, 12, 17, 23, 26, 32 | 6 | ゴールド (`--accent3` #8B6914) |
| データ | article5, 15, 19, 25, 29, 33 | 6 | グレー (`--text2`) |
| **合計** | | **35** | |

## デザイン

- フォント: Noto Serif JP（本文）+ DM Mono（数字・ラベル）
- 配色: ベージュ背景 (#F5F0E8) + 深緑アクセント (#1A3A2A) + オレンジ (#C4572A)
- 演出: SVG ノイズテクスチャ、fadeUp アニメーション、sticky ナビ
- レスポンシブ: 600px 以下でナビリンク非表示・プロフィール 1 カラム

## 計測・収益化

- Google Analytics: `G-QPKSYX94QP`（全ページに同一スニペット）
- アフィリエイト: レバテックキャリア / マイナビ IT AGENT を `index.html` および各記事内 `affiliate-box` で紹介
  - 現在 `href="#"` のままのリンクは **申請完了後に成果リンクへ差し替え**

## ローカルでの確認方法

ビルド不要のため、ローカル HTTP サーバーを立てて `index.html` を開くだけです。

```bash
# Python 3 が入っている場合
python -m http.server 8000
# → http://localhost:8000 をブラウザで開く
```

または `index.html` をブラウザにドラッグ＆ドロップ。

## デプロイ

GitHub Pages 想定。`main` ブランチをそのまま公開すれば動作します。

## 編集時の注意

- 各記事の `<style>` ブロックは独立しているため、共通スタイルを変更する場合は **全 37 ファイル**（index + privacy + article1〜35）に反映が必要です。
- `scripts/gen_article.py` と `scripts/new_articles_data.py` を使えば新規記事をテンプレートから一括生成できます（`python scripts/run_gen.py`）。
- 記事を追加した際は `index.html` の該当カテゴリブロックにカード（`.article-item`）を追加してください。
- フッターの `© 2025-2026` 表記は新年に更新を忘れないこと。

## 残タスク（外部情報が必要）

### 1. アフィリエイトリンクの差し替え

`href="#"` の affiliate-btn が30箇所あります（`grep -n 'href="#" class="affiliate-btn"' *.html` で一覧取得可）。
ASP（A8.net・もしもアフィリエイト 等）から発行された成果リンクを取得後、
`href="#"` を実 URL に置換してください。`rel="sponsored noopener"` と `target="_blank"` は既に付与済みです。

### 2. カスタムドメイン化

GitHub Pages にカスタムドメインを設定する場合、リポジトリ直下に `CNAME` ファイル
（中身：`example.com` など独自ドメイン）を作成し、`main` ブランチに push します。
DNS 側で `CNAME` レコード（`www`）または `A` レコード（apex）を GitHub Pages の
IP（`185.199.108.153` 〜 `185.199.111.153`）に向ける設定も必要です。
`og:url` / `og:image` / `canonical` / `sitemap.xml` / `robots.txt` 内の
`https://kinyu-engineer.github.io` を新ドメインに一括置換してください。

### 3. Google Search Console / Bing Webmaster Tools への登録

サイトマップを検索エンジンに認識させるための登録手順：

- **Google Search Console**: https://search.google.com/search-console
  プロパティ追加 → URL プレフィックス → `https://kinyu-engineer.github.io/`
  → 所有権確認（HTML タグ法のメタを `index.html` の `<head>` に貼る）
  → サイトマップ → `sitemap.xml` を送信
- **Bing Webmaster Tools**: https://www.bing.com/webmasters
  Search Console から自動インポート可能。

メタタグでの所有権確認をする場合、`<meta name="google-site-verification" content="...">`
を `index.html` の `<head>` 内（`<title>` の前後）に追加すれば OK です。

## 外部リンク

- 統計検定 学習帳: https://toukei-app-eight.vercel.app
- たまるツール工房: https://nokka7465-ux.github.io
