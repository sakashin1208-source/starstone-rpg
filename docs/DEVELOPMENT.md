# Development Environment & Setup

## 1. 検出・インストール環境情報
- **OS**: macOS (Darwin 25.6.0 arm64 / Apple Silicon)
- **Git**: 2.50.1 (Apple Git-155)
- **Python**: Python 3.9.6 (System Python)
- **Godot**: **v4.7.2.stable.official.ed1daf0bf** (インストール済み: `~/Applications/Godot.app`, CLI: `~/.local/bin/godot`)
- **Blender**: **v4.2.23 LTS (arm64)** (インストール済み: `~/Applications/Blender.app`, CLI: `~/.local/bin/blender`)

## 2. CLI検証実績 (2026-09-08)
- **Godot バージョン確認**:
  `~/.local/bin/godot --version` -> `4.7.2.stable.official.ed1daf0bf` (Exit Code 0)
- **Godot プロジェクト読み込み・インポート検証**:
  `~/.local/bin/godot --headless --path game --editor --quit` (Exit Code 0)
- **Godot E2E自動テスト**:
  `~/.local/bin/godot --headless --path game -s res://tests/test_save_load.gd` (Exit Code 0, 0 errors)
  `~/.local/bin/godot --headless --path game -s res://tests/test_atelier_scene.gd` (Exit Code 0, 0 errors)
- **Blender バージョン確認**:
  `~/.local/bin/blender --version` -> `Blender 4.2.23 LTS` (Exit Code 0)
- **Blender Python パイプライン実証**:
  ヘッドレススクリプトから `wooden_crate.blend` 原本保存および `wooden_crate.glb` 生成・Godot自動インポート成功 (Exit Code 0)
