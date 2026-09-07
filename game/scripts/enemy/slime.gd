class_name SlimeEnemy
extends CharacterBody3D

@export var enemy_data_path: String = "res://data/enemies/slime.json"
@export var battle_scene_path: String = "res://scenes/battle/battle_scene.tscn"

@onready var visual: Node3D = $Visual

var time_passed: float = 0.0

func _physics_process(delta: float) -> void:
	# Idle squishy animation
	time_passed += delta * 3.0
	if visual:
		visual.scale.y = 1.0 + sin(time_passed) * 0.1
		visual.scale.x = 1.0 - sin(time_passed) * 0.05
		visual.scale.z = 1.0 - sin(time_passed) * 0.05

func _on_encounter_area_body_entered(body: Node3D) -> void:
	if body.is_in_group("player"):
		# Trigger battle
		get_tree().change_scene_to_file(battle_scene_path)
