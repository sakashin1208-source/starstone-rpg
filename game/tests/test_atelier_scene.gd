extends SceneTree

func _initialize() -> void:
	print("--- Starting Atelier Scene & Emma NPC Verification Test ---")
	
	# Autoloads are automatically loaded by Godot under root
	var quest_manager = root.get_node_or_null("QuestManager")
	if not quest_manager:
		var QuestManagerScript = load("res://scripts/quest/quest_manager.gd")
		quest_manager = QuestManagerScript.new()
		quest_manager.name = "QuestManager"
		root.add_child(quest_manager)
	
	# 1. Load Atelier scene
	print("Step 1: Loading res://scenes/maps/atelier.tscn...")
	var atelier_res = load("res://scenes/maps/atelier.tscn")
	assert(atelier_res != null, "Failed to load atelier.tscn")
	
	var atelier_instance = atelier_res.instantiate()
	assert(atelier_instance != null, "Failed to instantiate atelier scene")
	root.add_child(atelier_instance)
	
	# Wait for nodes to enter tree and call _ready
	await process_frame
	
	# 2. Check essential nodes
	print("Step 2: Checking scene node hierarchy...")
	var emma = atelier_instance.get_node_or_null("EmmaNPC")
	assert(emma != null, "EmmaNPC node not found")
	assert(emma.npc_name == "職人の少女エマ", "Unexpected Emma NPC name: " + emma.npc_name)
	
	var workbench = atelier_instance.get_node_or_null("Furniture/Workbench")
	assert(workbench != null, "Furniture/Workbench node not found")
	
	var fox = atelier_instance.get_node_or_null("Furniture/CarvedFox")
	assert(fox != null, "Furniture/CarvedFox node not found")
	
	var door_exit = atelier_instance.get_node_or_null("DoorExit")
	assert(door_exit != null, "DoorExit node not found")
	assert(door_exit.target_scene_path == "res://scenes/maps/village.tscn", "DoorExit target scene mismatch")
	
	# 3. Check Emma NPC interaction logic without starstone
	print("Step 3: Verifying Emma dialogue without Starstone Shard...")
	quest_manager.has_starstone_shard = false
	var path_before = emma.get_current_dialogue_path()
	assert(path_before == "res://data/dialogues/craftsman_talk.json", "Dialogue path should be craftsman_talk.json, got: " + path_before)
	
	# 4. Check Emma NPC interaction logic with starstone
	print("Step 4: Verifying Emma dialogue WITH Starstone Shard...")
	quest_manager.has_starstone_shard = true
	var path_after = emma.get_current_dialogue_path()
	assert(path_after == "res://data/dialogues/craftsman_starstone.json", "Dialogue path should be craftsman_starstone.json, got: " + path_after)
	
	# 5. Check Village entrance teleporter
	print("Step 5: Verifying Village entrance teleporter...")
	var village_res = load("res://scenes/maps/village.tscn")
	assert(village_res != null, "Failed to load village.tscn")
	var village_instance = village_res.instantiate()
	root.add_child(village_instance)
	await process_frame
	
	var atelier_entrance = village_instance.get_node_or_null("AtelierEntrance")
	assert(atelier_entrance != null, "AtelierEntrance not found in village.tscn")
	assert(atelier_entrance.target_scene_path == "res://scenes/maps/atelier.tscn", "AtelierEntrance target mismatch")
	
	print("[TEST PASSED] Atelier scene and craftsman interaction verified successfully with 0 errors.")
	quit(0)
