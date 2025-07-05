# CLAUDE.md

このファイルは、Claude Code (claude.ai/code) がこのリポジトリで作業する際のガイダンスを提供します。

**重要**: `CLAUDE_PERSONAL.md` ファイルが存在する場合は、そちらも必ず読み込んでコミュニケーション設定を確認してください。

## プロジェクト概要

このリポジトリは、Flask-Freezeを使用した静的サイトジェネレータです。GitHub Pagesにデプロイされ、葉っぱが風で揺れるアニメーションを表示します。

## リポジトリ構造

### メインファイル
- `app.py` - Flaskアプリケーション（現在時刻を提供）
- `build.py` - Flask-Freezeを使用して静的サイトを生成
- `update_site.py` - HTMLの timestamp を更新するスクリプト
- `templates/index.html` - メインテンプレート（50本のバランの葉っぱアニメーション）
- `requirements.txt` - Python依存関係

### 設定ファイル
- `.gitignore` - Python関連ファイルとbuildディレクトリを除外
- `README.md` - プロジェクト説明

## Git情報

- メインブランチ: `main`
- Gitリポジトリとして初期化済み
- 開発コンテナサポート用の`.devcontainer/`ディレクトリを含んでいます（未追跡）
- 簡潔なコミットメッセージ形式で統一
- コミットメッセージにCo-Authored-Byを含めない
