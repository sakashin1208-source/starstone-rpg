class_name DioramaCamera
extends Camera3D

@export var target_node_path: NodePath
@export var offset: Vector3 = Vector3(0.0, 7.5, 9.0)
@export var follow_speed: float = 5.0
@export var look_at_height_offset: float = 1.0

var target_node: Node3D = null

func _ready() -> void:
	if not target_node_path.is_empty():
		target_node = get_node_or_null(target_node_path) as Node3D
	
	# Fallback: search for player group
	if target_node == null:
		var players = get_tree().get_nodes_in_group("player")
		if players.size() > 0:
			target_node = players[0] as Node3D

func _process(delta: float) -> void:
	if target_node == null:
		var players = get_tree().get_nodes_in_group("player")
		if players.size() > 0:
			target_node = players[0] as Node3D
		return

	var desired_position: Vector3 = target_node.global_position + offset
	global_position = global_position.lerp(desired_position, follow_speed * delta)
	
	var look_target: Vector3 = target_node.global_position + Vector3(0.0, look_at_height_offset, 0.0)
	look_at(look_target, Vector3.UP)
