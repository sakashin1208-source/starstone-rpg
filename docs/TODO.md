# Project TODO

## PHASE 1: Bootstrap & Foundation [DONE]
- [x] STEP 0: Environment Discovery (macOS arm64, Git, Python detected, Godot 4.3 installed)
- [x] STEP 1: Workspace Initialization (`~/dev/starstone-rpg`)
- [x] STEP 2: Repository Skeleton & .gitignore
- [x] STEP 3: Project Governance (AGENTS.md, docs)
- [x] STEP 4: Godot Empty Project Setup (`project.godot`)
- [x] STEP 5: Minimum 3D Scene (`main.tscn`)
- [x] Phase 1 Checkpoint & Hard Stop Report

## PHASE 2: Core Playground [DONE]
- [x] STEP 6: Player Controller & Movement (InputMap, velocity, gravity, smooth rotation)
- [x] STEP 7: Diorama Camera (smooth target tracking, fixed tilt angle)
- [x] STEP 8: Village Placeholder (Elder house, Weapon shop, Inn, paths, trees, lanterns)
- [x] STEP 9: NPC Interaction (Reusable Interactable Area3D component, Elder & Villager)
- [x] STEP 10: Dialogue System (CanvasLayer DialogueBox UI, JSON data loading, page advance)
- [x] Phase 2 Checkpoint & Hard Stop Report

## PHASE 3: Game Loop [DONE]
- [x] STEP 11: Quest System & Elder Quest (QuestManager Autoload, QuestHUD UI)
- [x] STEP 12: Forest Map & Scene Transition (`forest.tscn`, `map_teleporter.gd`)
- [x] STEP 13: Enemy Encounter & Turn-based Battle (`slime.tscn`, `battle_scene.tscn`, `battle_system.gd`)
- [x] STEP 14: Treasure Chest (`treasure_chest.tscn`, Starstone Shard drop)
- [x] STEP 15: Return to Village & Quest Completion (Elder dialogue branching & complete loop)
- [x] Phase 3 Checkpoint & Hard Stop Report

## PHASE 4: Persistence [DONE]
- [x] STEP 16: Inventory & Item Management (`inventory_service.gd`)
- [x] STEP 17: Save & Load System (`save_service.gd` - `user://savegame.json`, Quick save F5/C)
- [x] STEP 18: Title Screen & State Restoration (`title_screen.tscn`, `title_screen.gd`)
- [x] E2E Save/Load Persistence Automated Test (`test_save_load.gd` - PASSED with 0 errors)
- [x] Phase 4 Checkpoint & Hard Stop Report

## PHASE 5: Craftsman Atelier Interior [DONE]
- [x] Blender 4.2 Python パイプラインで工房専用3Dアセット7種量産 (`generate_atelier_assets.py`)
- [x] 工房内装シーン (`atelier.tscn`) 構築（作業台、彫刻狐、和紙提灯、棚、籠、職人の少女エマ）
- [x] 村 (`village.tscn`) と工房 (`atelier.tscn`) の双方向移動テレポート扉設置
- [x] 職人の少女エマの会話分岐（通常／星石のかけら所持時）実装
- [x] 工房シーン自動検証テスト (`test_atelier_scene.gd` - PASSED with 0 errors)

## PHASE 6: Vertical Slice QA & Polish (Next)
- [ ] End-to-End Playable Loop Confirmation (GUI Run)
- [ ] Figma UI Specifications & Design Token Mapping
- [ ] HyperFrames Promotion Video Pipeline
