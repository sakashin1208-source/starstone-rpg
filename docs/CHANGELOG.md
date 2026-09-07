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

## [0.3.0-game-loop] - 2026-09-07
- Phase 3 Game Loop実装完了
- クエスト管理サービス (`quest_manager.gd`) をAutoload登録し、HUD表示 (`quest_hud.tscn`) を追加
- 双方向マップ移動トリガー (`map_teleporter.gd`) を作成し、村と森を接続
- ささやきの森マップ (`forest.tscn`) 構築（深緑の草地、樹木群、古代の祠）
- スライム敵エンティティ (`slime.tscn`) およびターン制コマンドバトル画面 (`battle_scene.tscn`, `battle_system.gd`) 実装（攻撃/スキル/道具/防御）
- 宝箱ギミック (`treasure_chest.tscn`) 実装（開錠アニメーション、星石のかけら入手、クエスト進捗連動）
- 長老NPCのクエスト進行連動ダイアログ分岐（未受注 → 探索中 → 報告達成 → 完了後）実装
- 全スクリプト（11本）および全シーン（村・森・戦闘）のCLI検証完了 (Exit Code 0)
