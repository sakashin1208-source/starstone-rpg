class_name Interactable
extends Area3D

signal interacted(interactor: Node3D)

@export var prompt_message: String = "[E] はなす"
@export var prompt_offset: Vector3 = Vector3(0.0, 1.8, 0.0)

var is_player_nearby: bool = false
var current_interactor: Node3D = null
var prompt_label: Label3D = null

func _ready() -> void:
	collision_layer = 4 # Interaction layer
	collision_mask = 2  # Player layer
	
	body_entered.connect(_on_body_entered)
	body_exited.connect(_on_body_exited)
	
	_create_prompt_label()

func _create_prompt_label() -> void:
	prompt_label = Label3D.new()
	prompt_label.text = prompt_message
	prompt_label.position = prompt_offset
	prompt_label.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	prompt_label.no_depth_test = true
	prompt_label.font_size = 32
	prompt_label.outline_size = 8
	prompt_label.outline_modulate = Color(0.1, 0.1, 0.1, 0.8)
	prompt_label.visible = false
	add_child(prompt_label)

func _on_body_entered(body: Node3D) -> void:
	if body.is_in_group("player"):
		is_player_nearby = true
		current_interactor = body
		if prompt_label:
			prompt_label.visible = true

func _on_body_exited(body: Node3D) -> void:
	if body == current_interactor:
		is_player_nearby = false
		current_interactor = null
		if prompt_label:
			prompt_label.visible = false

func _unhandled_input(event: InputEvent) -> void:
	if is_player_nearby and event.is_action_pressed("interact"):
		interacted.emit(current_interactor)
		get_viewport().set_input_as_handled()
