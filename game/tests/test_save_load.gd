extends SceneTree

func _init() -> void:
	print("--- Starting Save & Load E2E Verification Test ---")
	
	# Instantiate services directly for isolated CLI test
	var SaveServiceScript = load("res://scripts/save/save_service.gd")
	var QuestManagerScript = load("res://scripts/quest/quest_manager.gd")
	var InventoryServiceScript = load("res://scripts/inventory/inventory_service.gd")
	
	var save_service = SaveServiceScript.new()
	var quest_manager = QuestManagerScript.new()
	var inventory = InventoryServiceScript.new()
	
	root.add_child(quest_manager)
	quest_manager.name = "QuestManager"
	
	root.add_child(inventory)
	inventory.name = "InventoryService"
	
	root.add_child(save_service)
	save_service.name = "SaveService"
	
	# 1. Setup mock test state
	print("Step 1: Setting up mock game state...")
	quest_manager.current_quest_id = "quest_001"
	quest_manager.current_state = 2 # READY_TO_REPORT
	quest_manager.current_objective = "長老に報告する"
	quest_manager.has_starstone_shard = true
	
	inventory.items = {"herb": 5, "starstone_shard": 1}
	inventory.gold = 150
	inventory.exp_points = 60
	
	var test_scene = "res://scenes/maps/forest.tscn"
	var test_pos = Vector3(2.5, 0.0, -8.0)
	
	# 2. Save game
	print("Step 2: Saving game to user://savegame.json...")
	var save_ok = save_service.save_game(test_scene, test_pos)
	if not save_ok:
		printerr("[FAIL] save_game returned false")
		quit(1)
		return
	
	# 3. Mutate/Reset current state
	print("Step 3: Mutating/Resetting current in-memory state...")
	quest_manager.current_state = 0 # NOT_STARTED
	quest_manager.current_objective = "長老から話を聞く"
	quest_manager.has_starstone_shard = false
	inventory.items = {}
	inventory.gold = 0
	inventory.exp_points = 0
	save_service.has_pending_load_pos = false
	
	# 4. Load game
	print("Step 4: Loading game from user://savegame.json...")
	var load_ok = save_service.load_game(false)
	if not load_ok:
		printerr("[FAIL] load_game returned false")
		quit(1)
		return
		
	# 5. Verify restored state
	print("Step 5: Verifying restored game state...")
	var errors = []
	
	if quest_manager.current_state != 2:
		errors.append("Quest state mismatch: expected 2, got %s" % quest_manager.current_state)
	if not quest_manager.has_starstone_shard:
		errors.append("Quest starstone flag mismatch: expected true")
	if quest_manager.current_objective != "長老に報告する":
		errors.append("Quest objective mismatch: %s" % quest_manager.current_objective)
		
	if inventory.get_item_count("herb") != 5:
		errors.append("Herb count mismatch: expected 5, got %d" % inventory.get_item_count("herb"))
	if inventory.get_item_count("starstone_shard") != 1:
		errors.append("Starstone shard mismatch: expected 1, got %d" % inventory.get_item_count("starstone_shard"))
	if inventory.gold != 150:
		errors.append("Gold mismatch: expected 150, got %d" % inventory.gold)
	if inventory.exp_points != 60:
		errors.append("EXP mismatch: expected 60, got %d" % inventory.exp_points)
		
	if not save_service.has_pending_load_pos:
		errors.append("Pending load pos flag was not set")
	if save_service.pending_load_position.distance_to(test_pos) > 0.001:
		errors.append("Player position mismatch: expected %s, got %s" % [test_pos, save_service.pending_load_position])

	if errors.size() > 0:
		printerr("[TEST FAILED]")
		for e in errors:
			printerr("  - ", e)
		quit(1)
	else:
		print("[TEST PASSED] Save/Load E2E persistence verified successfully with 0 errors.")
		quit(0)
