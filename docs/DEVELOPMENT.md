# Development Environment & Setup

## 1. 検出・インストール環境情報
- **OS**: macOS (Darwin 25.6.0 arm64 / Apple Silicon)
- **Git**: 2.50.1 (Apple Git-155)
- **Python**: Python 3.9.6 (System Python)
- **Godot**: **v4.3.stable.official.77dcf97d8** (インストール済み: `~/Applications/Godot.app`, CLI: `~/.local/bin/godot`)
- **Blender**: CLI未検出 (必要に応じて手動またはスクリプトで導入可能)

## 2. CLI検証実績 (2026-09-07)
- **バージョン確認**:
  `~/.local/bin/godot --version` -> `4.3.stable.official.77dcf97d8` (Exit Code 0)
- **プロジェクト読み込み・初期インポート検証**:
  `~/.local/bin/godot --headless --path game --editor --quit` (Exit Code 0)
- **メインシーンスモークテスト**:
  `~/.local/bin/godot --headless --path game res://scenes/main.tscn --quit-after 10` (Exit Code 0)

## 3. Blender 4.x LTS 導入ガイド (macOS)
- 公式サイト (https://www.blender.org/) より macOS 用 Blender をダウンロードして `/Applications/Blender.app` に配置
- または必要時に自動セットアップ可能
