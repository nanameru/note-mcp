# agent-skills Issue #27 連携ログ

GitHub fork `nanameru/note-mcp` はIssue機能が無効なため、`agent-skills#27` に紐づく補助変更として記録する。

## 目的

既存API層にある `get_preview_access_token` と `build_preview_url` をMCPツールとして公開し、note公開後の非公開複製プレビューをDiscord配信処理へ渡せるようにする。

## 制約

- note公開やDiscord送信は行わない。
- プレビューURLをテストログ、Issue、コミット本文へ実値で保存しない。
- 既存API実装を再利用し、トークン生成ロジックを重複させない。
