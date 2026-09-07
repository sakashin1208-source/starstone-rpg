# Development Environment & Setup

## 1. 検出環境情報 (STEP 0 結果)
- **OS**: macOS (Darwin 25.6.0 arm64 / Apple Silicon)
- **Git**: 2.50.1 (Apple Git-155)
- **Python**: Python 3.9.6 (System Python)
- **Node.js**: 未検出 (Vertical Slice初期では必須ではない)
- **Godot**: CLI未検出 (手動インストール推奨)
- **Blender**: CLI未検出 (手動インストール推奨)

## 2. ツール導入ガイド (macOS)
### Godot 4.x (Standard Edition)
- 公式サイト (https://godotengine.org/) より macOS 用 Godot 4.x をダウンロード
- `/Applications/Godot.app` に配置
- CLIで動作させる場合、パスを通すか alias を設定:
  ```bash
  alias godot="/Applications/Godot.app/Contents/MacOS/Godot"
  ```

### Blender 4.x LTS
- 公式サイト (https://www.blender.org/) より macOS 用 Blender をダウンロード
- `/Applications/Blender.app` に配置
- CLIエイリアス設定:
  ```bash
  alias blender="/Applications/Blender.app/Contents/MacOS/Blender"
  ```

## 3. 検証用コマンド
- プロジェクト構文・読み込み確認:
  `godot --headless --path game --editor --quit`
- メインシーン実行確認:
  `godot --headless --path game res://scenes/main.tscn --quit-after 60`
