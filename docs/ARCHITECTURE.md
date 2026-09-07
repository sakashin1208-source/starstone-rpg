# Architecture Document

## 1. 全体思想
- **Component-Oriented**: 1 Scene = 1 Responsibility。巨大なGodotノードを作らない。
- **Data-Driven Design**: ロジックとデータを分離。敵・アイテム・クエストはResource (`res://data/...`) として定義し、スクリプトにハードコードしない。
- **原本と実行用アセットの分離**:
  - 原本: `blender/` (.blend)
  - 実行用: `game/assets/models/` (.glb)
  - パイプラインスクリプト (`pipeline/blender/`) を経由して自動エクスポート。

## 2. サービス構成 (Autoload最小化)
- 必要に応じて疎結合なサービス群を定義:
  - `SaveService`: セーブ・ロード管理
  - `QuestService`: クエスト進行状態管理
  - `SceneTransitionService`: マップ・シーン遷移制御
