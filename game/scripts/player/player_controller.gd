class_name PlayerController
extends CharacterBody3D

@export var move_speed: float = 4.5
@export var rotation_speed: float = 10.0
@export var acceleration: float = 14.0

var gravity: float = ProjectSettings.get_setting("physics/3d/default_gravity", 9.8)
var is_control_locked: bool = false

@onready var visual_node: Node3D = $Visual if has_node("Visual") else self

func _ready() -> void:
	_ensure_input_actions()

func _ensure_input_actions() -> void:
	# Fallback auto-registration if actions are missing from project settings
	var default_actions = {
		"move_left": [KEY_A, KEY_LEFT],
		"move_right": [KEY_D, KEY_RIGHT],
		"move_forward": [KEY_W, KEY_UP],
		"move_backward": [KEY_S, KEY_DOWN],
		"interact": [KEY_E, KEY_SPACE]
	}
	for action_name in default_actions:
		if not InputMap.has_action(action_name):
			InputMap.add_action(action_name)
			for keycode in default_actions[action_name]:
				var ev = InputEventKey.new()
				ev.physical_keycode = keycode
				InputMap.action_add_event(action_name, ev)

func _physics_process(delta: float) -> void:
	# Apply gravity
	if not is_on_floor():
		velocity.y -= gravity * delta
	else:
		velocity.y = 0.0

	if is_control_locked:
		velocity.x = move_toward(velocity.x, 0.0, acceleration * delta)
		velocity.z = move_toward(velocity.z, 0.0, acceleration * delta)
		move_and_slide()
		return

	# Read InputMap actions
	var input_dir: Vector2 = Input.get_vector("move_left", "move_right", "move_forward", "move_backward")
	var target_velocity_xz: Vector3 = Vector3(input_dir.x, 0.0, input_dir.y).normalized() * move_speed

	# Smooth horizontal velocity
	velocity.x = move_toward(velocity.x, target_velocity_xz.x, acceleration * delta)
	velocity.z = move_toward(velocity.z, target_velocity_xz.z, acceleration * delta)

	# Rotate character towards movement direction
	if input_dir.length_squared() > 0.01:
		var target_angle: float = atan2(input_dir.x, input_dir.y)
		visual_node.rotation.y = lerp_angle(visual_node.rotation.y, target_angle, rotation_speed * delta)

	move_and_slide()

func set_control_locked(locked: bool) -> void:
	is_control_locked = locked
	if locked:
		velocity.x = 0.0
		velocity.z = 0.0
