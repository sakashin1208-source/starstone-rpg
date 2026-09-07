# Changelog

## [0.1.0-bootstrap] - 2026-09-07
- Phase 1 Bootstrap完了
- ディレクトリ構造スケルトン構築
- AGENTS.md (全69条) 配備
- docs一式 (DEVELOPMENT, ARCHITECTURE, VERTICAL_SLICE, ART_DIRECTION, TODO, GAME_DESIGN, WORLD) 作成

## [0.2.0-core-playground] - 2026-09-07
- Phase 2 Core Playground実装完了
- プレイヤー操作 (`player_controller.gd`) 実装（WASD/矢印キー、回転補間、重力）
- ジオラマ俯瞰追従カメラ (`diorama_camera.gd`) 実装
- シルヴァ村マップ (`village.tscn`) 構築（長老の家、武器屋、宿屋、木、道、ランタン）
- 汎用インタラクションコンポーネント (`interactable.gd`) およびNPCシーン (`npc.tscn`) 実装
- 会話ウィンドウUI (`dialogue_box.tscn`, `dialogue_box.gd`) および会話データJSON作成
- 全スクリプトのCLIパースチェックおよび村シーンのCLI実行検証 (Exit Code 0)
