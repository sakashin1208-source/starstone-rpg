extends Node

signal save_completed(success: bool)
signal load_completed(success: bool)

const SAVE_PATH: String = "user://savegame.json"

var pending_load_position: Vector3 = Vector3.ZERO
var has_pending_load_pos: bool = false

func has_save_file() -> bool:
	return FileAccess.file_exists(SAVE_PATH)

func save_game(scene_path: String = "", player_position: Vector3 = Vector3.ZERO) -> bool:
	var qm = _get_quest_manager()
	var inv = _get_inventory_service()
	
	if scene_path.is_empty():
		if get_tree() and get_tree().current_scene:
			scene_path = get_tree().current_scene.scene_file_path
		else:
			scene_path = "res://scenes/maps/village.tscn"

	var save_dict: Dictionary = {
		"version": "0.1.0",
		"timestamp": Time.get_datetime_string_from_system(),
		"scene": scene_path,
		"player": {
			"x": player_position.x,
			"y": player_position.y,
			"z": player_position.z
		},
		"quest": {
			"id": qm.current_quest_id if qm else "quest_001",
			"state": int(qm.current_state) if qm else 0,
			"objective": qm.current_objective if qm else "",
			"has_starstone": qm.has_starstone_shard if qm else false
		},
		"inventory": inv.get_save_dict() if inv else {}
	}

	var file = FileAccess.open(SAVE_PATH, FileAccess.WRITE)
	if not file:
		save_completed.emit(false)
		return false

	var json_string = JSON.stringify(save_dict, "\t")
	file.store_string(json_string)
	file.close()

	save_completed.emit(true)
	return true

func load_game(change_scene: bool = true) -> bool:
	if not has_save_file():
		load_completed.emit(false)
		return false

	var file = FileAccess.open(SAVE_PATH, FileAccess.READ)
	if not file:
		load_completed.emit(false)
		return false

	var json = JSON.new()
	var parse_err = json.parse(file.get_as_text())
	file.close()
	if parse_err != OK:
		load_completed.emit(false)
		return false

	var data: Dictionary = json.data
	var qm = _get_quest_manager()
	var inv = _get_inventory_service()

	# Restore Quest State
	if qm and data.has("quest"):
		var q_data = data["quest"]
		qm.current_quest_id = q_data.get("id", "quest_001")
		qm.current_state = int(q_data.get("state", 0))
		qm.current_objective = q_data.get("objective", "")
		qm.has_starstone_shard = q_data.get("has_starstone", false)
		qm.quest_state_changed.emit(qm.current_quest_id, qm.current_state, qm.current_objective)

	# Restore Inventory
	if inv and data.has("inventory"):
		inv.load_save_dict(data["inventory"])

	# Restore Player position and transition scene
	if data.has("player"):
		var p = data["player"]
		pending_load_position = Vector3(p.get("x", 0.0), p.get("y", 0.0), p.get("z", 0.0))
		has_pending_load_pos = true

	if change_scene and get_tree():
		var target_scene = data.get("scene", "res://scenes/maps/village.tscn")
		get_tree().change_scene_to_file(target_scene)

	load_completed.emit(true)
	return true

func _get_quest_manager() -> Node:
	if is_inside_tree() and has_node("/root/QuestManager"):
		return get_node("/root/QuestManager")
	if get_parent() and get_parent().has_node("QuestManager"):
		return get_parent().get_node("QuestManager")
	if get_tree():
		var nodes = get_tree().get_nodes_in_group("quest_manager")
		if nodes.size() > 0:
			return nodes[0]
	return null

func _get_inventory_service() -> Node:
	if is_inside_tree() and has_node("/root/InventoryService"):
		return get_node("/root/InventoryService")
	if get_parent() and get_parent().has_node("InventoryService"):
		return get_parent().get_node("InventoryService")
	return null
