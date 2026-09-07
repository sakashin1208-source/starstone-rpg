# Starstone Hero 3D — AI Agent Operating Rules

This file defines repository-wide rules for AI agents.

All agents MUST read this file before changing the repository.

Priority:

1. Explicit current user instruction
2. AGENTS.md
3. Project architecture documents
4. Existing implementation conventions

Never interpret these rules as permission to destroy user work.

---

## 1. PROJECT

Name:
Starstone Hero 3D
星石の勇者 3D

Genre:
3D RPG

Visual Identity:
Doll × Diorama

Current Milestone:
Vertical Slice v0.1

Target:
Approximately 10 minutes of polished gameplay.

---

## 2. LONG-TERM VISION

The repository should gradually support:

Natural Language Request
↓
AI Director
↓
Task Decomposition
↓
Godot / Blender / Scenario / UI Agents
↓
Integration
↓
QA
↓
Build

Do not attempt to automate the entire vision before the basic development workflow works manually and reliably.

Rule:
Make it work → make it repeatable → automate it.

---

## 3. ENVIRONMENT POLICY

Do not assume installed versions.
Detect the actual environment.
Prefer compatible existing stable installations.
Do not upgrade Godot, Blender, Python, Node.js or major dependencies unless required and justified.
Record actual development versions in:
"docs/DEVELOPMENT.md"

---

## 4. WORKSPACE SAFETY

Do not create the repository inside real-time cloud-sync directories.
Avoid:
- OneDrive
- iCloud Drive
- Dropbox
- Google Drive sync
- similar sync roots
unless explicitly requested.

Preferred default locations:
macOS/Linux: "~/dev/starstone-rpg"
Windows: "%USERPROFILE%\dev\starstone-rpg"

Always inspect the actual environment first.

---

## 5. ENGINE

Use:
Godot 4.x stable

Primary language:
GDScript

Do not introduce C# without explicit justification or user instruction.

---

## 6. BLENDER

Use a compatible stable Blender release.
Prefer current LTS for a new environment.
Existing compatible stable installations may be retained.
Use Blender Python / "bpy" for automation when it improves repeatability.

---

## 7. CORE PRINCIPLES

Priority:
1. Preserve existing work.
2. Keep the project runnable.
3. Keep changes testable.
4. Prefer simple solutions.
5. Keep changes reversible.
6. Separate responsibilities.
7. Avoid unnecessary dependencies.
8. Maintain human readability.
9. Maintain AI readability.
10. Optimize only when necessary.

---

## 8. NEVER DO

Agents MUST NOT:
- delete features without instruction
- silently alter game design
- overwrite unrelated user changes
- perform destructive Git operations casually
- create giant all-purpose managers
- hardcode large content databases into gameplay scripts
- mix editable source and generated output
- overwrite ".blend" source with generated GLB
- claim unexecuted tests passed
- ignore parser/runtime errors
- generate huge amounts of content before core systems stabilize
- introduce major dependencies for trivial problems
- perform unrelated broad refactors during small fixes
- mark unverified work as fully DONE

---

## 9. PROJECT STRUCTURE

Primary structure:
game/
blender/
pipeline/
figma/
hyperframes/
docs/

Godot project: "game/"
Editable Blender sources: "blender/"
Automation: "pipeline/"
Design documentation: "figma/"
Video projects: "hyperframes/"
Architecture / game documentation: "docs/"

---

## 10. GODOT ARCHITECTURE

General principle:
1 Scene = 1 Responsibility

Prefer component-oriented architecture.
Use signals for appropriate decoupling.
Avoid excessive hardcoded NodePaths.
Avoid assumptions about deeply nested Scene Tree paths.
Use Autoload only for genuinely global responsibilities.

---

## 11. MANAGERS / SERVICES

Do not build a giant:
"GameManager.gd"
containing every game system.

Separate responsibilities when justified.
Possible examples:
- SaveService
- QuestService
- SceneTransitionService
- AudioService

Do not create services speculatively.

---

## 12. GAME DATA

Separate content from gameplay logic.
Prefer Resources or another structured data layer.
Potential types:
- CharacterData
- EnemyData
- ItemData
- SkillData
- QuestData

Gameplay systems consume data.
Content should not require modification of core systems whenever avoidable.

---

## 13. DATA-DRIVEN GOAL

Long-term requests such as:
"Add 30 enemies."
"Add 50 weapons."
"Add 20 quests."
should primarily create new data/assets rather than rewrite core gameplay code.

---

## 14. PLAYER

Possible responsibilities:
- Movement
- Interaction
- Stats
- Animation
- Combat

Split responsibilities when useful.
Do not fragment a tiny prototype into unnecessary micro-components.

---

## 15. STATE MACHINES

Consider State Machines where behavior has meaningful states.

Player example:
Idle, Move, Interact, Combat, Disabled

Enemy example:
Idle, Patrol, Chase, Attack, Dead

Do not introduce a State Machine when straightforward logic is clearer.

---

## 16. INPUT

Use Godot InputMap.
Prefer semantic actions:
- move_left
- move_right
- move_forward
- move_backward
- interact
- confirm
- cancel
- attack

Do not scatter physical keyboard key checks throughout gameplay code.

---

## 17. ASSET SOURCE SEPARATION

Editable source: "blender/"
Runtime 3D assets: "game/assets/models/"

Preferred pipeline:
.blend → Validation → Optimization if needed → GLB → Godot

Never overwrite ".blend" source during generation.

---

## 18. BLENDER AUTOMATION

Good automation candidates:
- buildings, props, trees, rocks
- procedural variations
- material assignment
- transforms, naming, validation
- GLB export
- repetitive operations
- collision preparation
- LOD generation

Do not force procedural generation for detailed artistic assets where handcrafted or external asset workflows are more appropriate.

---

## 19. BLENDER PIPELINE FILES

Primary scripts:
"pipeline/blender/export_glb.py"
"pipeline/blender/validate_asset.py"
"pipeline/blender/optimize_mesh.py"
"pipeline/blender/generate_lod.py"

Additional scripts require a clear responsibility.

---

## 20. BLENDER VALIDATION

Validate where relevant:
- Object names, Scale, Rotation, Origin
- Mesh integrity, Material, Texture references
- Polygon count, Animation references

Errors should be actionable.
Bad: "Export failed"
Better: "weapon_shop.blend: object Roof has unapplied scale."

---

## 21. ART DIRECTION

Before creating final visual assets, read:
"docs/ART_DIRECTION.md"

Primary style:
Doll × Diorama

Maintain consistency across agents.

---

## 22. GEOMETRY

Prefer:
- slightly softened edges
- subtle bevel
- readable silhouette
- handcrafted miniature impression
- deliberate simplification

Avoid arbitrary visual inconsistency.

---

## 23. MATERIALS

Priority materials:
- Wood, Stone, Cloth, Ceramic, Paper, Leather, Metal

World should feel tactile and crafted.
Avoid making every surface perfectly glossy or photorealistic.

---

## 24. CHARACTERS

General target:
High-quality doll-like character.
Approximate proportions: 5–6 heads tall.

Avoid accidental mixing of:
- photoreal human, anime, mascot cartoon, arbitrary low-poly

---

## 25. LIGHTING

Preferred:
- warm, soft, lantern light, sunset, morning light, gentle shadow

Gameplay readability takes priority over cinematic appearance.

---

## 26. CAMERA

Support the Diorama feeling through:
- controlled angles
- miniature composition
- moderate depth of field
- subtle tilt-shift impression

Do not sacrifice gameplay readability.

---

## 27. FIGMA

Figma is a design source, not a runtime dependency.
Translate design into:
- dimensions, spacing, typography, colors, components, design tokens, exported image assets

Runtime UI belongs in Godot.

---

## 28. UI COMPONENTS

Reuse UI components where appropriate:
- PrimaryButton, DialoguePanel, StatusBar, InventorySlot, QuestPanel

Avoid recreating the same UI component independently.

---

## 29. HYPERFRAMES

Use HyperFrames for promotional media:
- Trailer, Teaser, SNS video, Title animation, Character introduction

Do not make HyperFrames part of game runtime.
Do not prioritize it before the Vertical Slice is playable.

---

## 30. PLACEHOLDER POLICY

Missing final art must not stop gameplay development.
Use placeholders for:
- Hero, NPC, Enemy, Houses, Trees, Chests, Props

Clearly identify Placeholder assets.
Final visual replacement should require minimal or no gameplay-code change.

---

## 31. CURRENT VERTICAL SLICE

Required flow:
Title → New Game → Village → NPC Conversation → Elder → Quest Accept → Forest → Enemy → Battle → Victory → Treasure Chest → Return → Quest Complete → Save → Quit → Restart → Load

Do not expand into a large world before this works.

---

## 32. REQUIRED SYSTEMS

Minimum:
- Player Controller, Camera, NPC Interaction, Dialogue, Quest, Battle, Enemy, HP/MP, Item, Inventory, Scene Transition, Save, Load, Basic UI

---

## 33. QUEST SYSTEM

Separate:
Quest Definition, Quest Runtime State, Objectives, Rewards, UI Presentation

Avoid embedding long one-off quest logic directly in NPC scripts.

---

## 34. DIALOGUE

Dialogue content should generally remain separate from interaction logic.
NPC interaction triggers Dialogue.
NPC gameplay scripts should not become large dialogue databases.

---

## 35. BATTLE

Initial Vertical Slice battle:
Simple command-based battle.
Commands: Attack, Skill, Item, Defend
Start with 1–2 enemy types.
Prioritize a complete playable battle loop over framework complexity.

---

## 36. SAVE / LOAD

Save stable game state.
Vertical Slice minimum: Player state, Quest state, Inventory, relevant world progress.

Mandatory scenario:
Save → Quit → Restart → Load → State restored

---

## 37. CLI VALIDATION — GODOT

Determine the actual Godot executable first.
Possible names include: "godot", "godot4", or an absolute executable path.

Version: godot --version
Project load/import smoke check: godot --headless --path game --editor --quit
Script parse check example: godot --headless --path game --script res://tests/test_runner.gd --check-only

Important:
"--check-only" should be treated as a parse check used with "--script", not as a magical whole-project test command.
Scene smoke test where appropriate: godot --headless --path game res://scenes/example.tscn --quit-after 60

Headless validation does NOT replace visual QA. Use normal game execution when visual verification matters.

---

## 38. CLI VALIDATION — BLENDER

Determine the actual Blender executable first.
Version: blender --version
Background Python: blender --background --python pipeline/blender/script.py
Blend + Python: blender --background blender/file.blend --python pipeline/blender/export_glb.py

Check: exit status, stdout, stderr, generated file existence, output path.
Do not report export success merely because the Python script was generated.

---

## 39. TEST RESULT INTEGRITY

Never confuse expected result with observed result.
Bad: "The project works."
Good: "Executed Godot headless project-load check and received exit code 0."
If a test was not run: state that it was not run.

---

## 40. TESTING

Writing code is not completion.
After relevant changes:
1. Validate syntax.
2. Load the project.
3. Run the affected scene.
4. Test the changed feature.
5. Test closely related behavior.
6. Update documentation if needed.

---

## 41. REGRESSION

Example: When modifying battle rewards, also check battle completion, reward receipt, inventory, exit from battle, related quest update.
Test consequences, not only the changed line.

---

## 42. QA ROLE

Implementation and QA should be logically separate whenever practical.
QA should actively search for failures. Attempt to execute code.

---

## 43. E2E TARGET

Highest-priority integration test:
Launch → New Game → Move → Talk → Accept Quest → Travel → Battle → Win → Chest → Return → Complete Quest → Save → Restart → Load

---

## 44. DEFINITION OF DONE

A task is DONE only when:
Implementation exists AND Relevant validation passed AND No known critical regression remains AND Required documentation is updated.
If execution is impossible: use "Implemented — Not Fully Verified" or "BLOCKED".

---

## 45. GIT WORKFLOW

Use Git when available.
1 Logical Task = 1 Logical Commit
Do not create commit spam. Create checkpoints before risky changes.

---

## 46. GIT SAFETY

Do not use destructive operations without explicit need and authorization:
- git reset --hard
- git clean -fd
- forced checkout
- force push

Never discard user work.

---

## 47. DEPENDENCIES

Before introducing a dependency:
1. Determine if native tooling solves it.
2. Identify clear value.
3. Check maintenance status.
4. Prefer lightweight options.
5. Document rationale.

---

## 48. REFACTORING

Do not perform broad refactors to solve a local problem unless necessary.
If necessary: explain why, preserve behavior, test before/after.

---

## 49. DOCUMENTATION

Maintain:
"docs/GAME_DESIGN.md"
"docs/ART_DIRECTION.md"
"docs/ARCHITECTURE.md"
"docs/WORLD.md"
"docs/VERTICAL_SLICE.md"
"docs/DEVELOPMENT.md"
"docs/TODO.md"
"docs/CHANGELOG.md"

---

## 50. TODO

Recommended states:
BACKLOG, READY, IN_PROGRESS, BLOCKED, REVIEW, DONE.
Tasks must be actionable.

---

## 51. CHANGELOG

Record meaningful changes: gameplay systems, architecture, pipeline, schemas, major fixes.

---

## 52. AI-GENERATED CONTENT

AI may autonomously generate drafts of code, tests, data, scripts, assets, docs.
AI must not silently finalize major changes to story, philosophy, or art direction without user approval.

---

## 53. NAMING

Technical identifiers: English (e.g., player_controller.gd, quest_service.gd).
Japanese is acceptable for display text, dialogue, docs.
Avoid mixed-language code identifiers.

---

## 54. COMMENTS

Comments explain why, not obvious what.

---

## 55. ERROR MESSAGES

Make failures actionable. Include relevant context.

---

## 56. SECURITY

Never commit secrets, tokens, API keys. Use environment configs and .gitignore.

---

## 57. BLOCKED WORK

If blocked, state BLOCKED: Why, What is needed, What work can continue independently. Do not fake completion.

---

## 58. CONTINUE WHEN POSSIBLE

One blocked area should not freeze unrelated development (e.g., no Blender → use Godot primitives).

---

## 59. PHASE GATES

Do not execute every project phase in one session. Major phases end with a checkpoint.
Current first-run gate: Phase 1 ends after Minimum 3D Scene.

---

## 60. BEFORE CHANGING FILES

Inspect repository, read related docs, check Git status, determine affected systems, preserve unrelated changes.

---

## 61. AFTER CHANGING FILES

Validate, run code, check affected/related behavior, update documentation, update TODO, report actual results.

---

## 62. REPORT FORMAT

Format: Completed, Verified, Files Changed, Remaining, Blocked, Recommended Next.

---

## 63. PERFORMANCE

Do not prematurely optimize. Profile before significant optimization.

---

## 64. MOBILE / INPUT FUTURE

Do not hardwire exclusively to desktop. Keep InputMap extensible toward touch/controller.

---

## 65. AUTOMATION

Order: Manual → Repeatable → Validate → Automate → Optimize automation.

---

## 66. DEVELOPMENT PRIORITY

1. Stability → 2. Core gameplay → 3. Save/Load → 4. Integration → 5. Usable UI → 6. Art replacement → 7. Polish → 8. Optimization → 9. Promotion video.

---

## 67. CURRENT SUCCESS CRITERIA

Vertical Slice succeeds when a player can play the full loop without developer intervention.

---

## 68. FINAL DECISION RULE

When uncertain: safer → simpler → testable → reversible → understandable → extensible.

---

## 69. FINAL PRINCIPLE

Build the game first. Automate what works. Expand only after the Vertical Slice is stable.
