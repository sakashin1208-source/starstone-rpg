class_name MapTeleporter
extends Area3D

@export var target_scene_path: String = "res://scenes/maps/forest.tscn"
@export var prompt_text: String = "[E] 移動する"
@export var require_interact_key: bool = true

var player_nearby: bool = false

func _ready() -> void:
	collision_layer = 4
	collision_mask = 2
	body_entered.connect(_on_body_entered)
	body_exited.connect(_on_body_exited)

func _on_body_entered(body: Node3D) -> void:
	if body.is_in_group("player"):
		player_nearby = true
		if not require_interact_key:
			teleport()

func _on_body_exited(body: Node3D) -> void:
	if body.is_in_group("player"):
		player_nearby = false

func _unhandled_input(event: InputEvent) -> void:
	if player_nearby and require_interact_key and event.is_action_pressed("interact"):
		teleport()
		get_viewport().set_input_as_handled()

func teleport() -> void:
	if not target_scene_path.is_empty() and ResourceLoader.exists(target_scene_path):
		get_tree().change_scene_to_file(target_scene_path)
