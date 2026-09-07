class_name TitleScreen
extends Control

@export var start_scene_path: String = "res://scenes/maps/village.tscn"

@onready var continue_btn: Button = $CenterContainer/VBoxContainer/ButtonsContainer/ContinueBtn
@onready var new_game_btn: Button = $CenterContainer/VBoxContainer/ButtonsContainer/NewGameBtn
@onready var quit_btn: Button = $CenterContainer/VBoxContainer/ButtonsContainer/QuitBtn

func _ready() -> void:
	var save_service = _get_save_service()
	if save_service and not save_service.has_save_file():
		continue_btn.disabled = true
		continue_btn.modulate = Color(0.6, 0.6, 0.6, 0.6)

func on_new_game_pressed() -> void:
	# Reset state
	var qm = _get_quest_manager()
	if qm:
		qm.current_state = QuestManager.QuestState.NOT_STARTED
		qm.current_objective = "長老から話を聞く"
		qm.has_starstone_shard = false
	
	var inv = _get_inventory_service()
	if inv:
		inv.items = {"herb": 2, "starstone_shard": 0}
		inv.gold = 50
		inv.exp_points = 0
		
	get_tree().change_scene_to_file(start_scene_path)

func on_continue_pressed() -> void:
	var save_service = _get_save_service()
	if save_service and save_service.has_save_file():
		save_service.load_game()

func on_quit_pressed() -> void:
	get_tree().quit()

func _get_save_service() -> Node:
	if has_node("/root/SaveService"):
		return get_node("/root/SaveService")
	return null

func _get_quest_manager() -> Node:
	if has_node("/root/QuestManager"):
		return get_node("/root/QuestManager")
	return null

func _get_inventory_service() -> Node:
	if has_node("/root/InventoryService"):
		return get_node("/root/InventoryService")
	return null
