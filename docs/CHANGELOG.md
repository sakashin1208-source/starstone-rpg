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

## [0.4.0-vertical-slice] - 2026-09-07
- Phase 4 Persistence実装完了により、**「約10分のVertical Slice」ゲーム全体ループが成立**
- インベントリ管理サービス (`inventory_service.gd`) 実装（やくそう、星石のかけら、Gold、EXP）
- セーブ＆ロードサービス (`save_service.gd`) 実装（`user://savegame.json` への永続化、座標・クエスト状態・所持品の完全復元）
- プレイヤーのクイックセーブ機能（[F5] / [C]キー）およびロード時座標復元処理を統合
- タイトル画面 (`title_screen.tscn`, `title_screen.gd`) 実装（はじめから／つづきから／おわる）
- セーブ＆ロード完全復元自動テスト (`test_save_load.gd`) を構築し、CLI検証で合格（Exit Code 0, 0 errors）を確認
- 全14本のスクリプトおよび全シーンのCLI構文・実行テストを完全通過

## [0.5.0-3d-asset-production] - 2026-09-07
- Blender 4.2 Python 自動化パイプラインによる **Doll × Diorama 3Dアセット12種類の量産完了**
- プロップ量産 (`generate_props.py`):
  - `diorama_tree` (2段リーフのジオラマ樹木)
  - `diorama_rock` (角丸の苔むした岩)
  - `wooden_fence` (木製横木柵)
  - `village_lantern` (真鍮×すりガラスの街灯)
  - `ancient_shrine` (古代石造りの階段台座・二本柱祠)
  - `starstone_chest` (真鍮帯金付き木製宝箱)
- 建物量産 (`generate_buildings.py`):
  - `doll_house_elder` (長老宅: 赤屋根・レンガ煙突・木製ドア・窓)
  - `doll_house_shop` (武器屋: 青屋根・板張り壁・庇・吊り看板)
  - `doll_house_inn` (宿屋: 緑屋根・石造り基部・木製テラス)
- キャラクター量産 (`generate_characters.py`):
  - `doll_slime` (半透明エメラルドグリーン・ハイライトアイ)
  - `doll_hero_leon` (5〜6頭身ドール調素体・マント・ベルト・ブーツ)
- 原本 `.blend` はすべて `blender/` 配下に保管、実行用 `.glb` は `game/assets/models/` にエクスポート
- 村シーン (`village.tscn`)、森シーン (`forest.tscn`)、プレイヤー (`player.tscn`)、スライム (`slime.tscn`)、宝箱 (`treasure_chest.tscn`) のプレースホルダーをすべて高品質本番モデルへ差し替え完了
- 全シーンおよびセーブ＆ロードテストのCLI自動検証を完全通過 (Exit Code 0)
