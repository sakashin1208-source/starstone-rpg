class_name NPC
extends CharacterBody3D

@export var npc_name: String = "長老"
@export var dialogue_file_path: String = "res://data/dialogues/elder_intro.json"

@onready var interactable: Interactable = $Interactable

func _ready() -> void:
	if interactable:
		interactable.interacted.connect(_on_interacted)

func _on_interacted(interactor: Node3D) -> void:
	var dialogue_boxes = get_tree().get_nodes_in_group("dialogue_box")
	if dialogue_boxes.size() > 0:
		var dialogue_box = dialogue_boxes[0]
		dialogue_box.start_dialogue_from_file(dialogue_file_path, npc_name)
		
		# Turn NPC towards player
		if interactor:
			var look_dir = interactor.global_position - global_position
			look_dir.y = 0.0
			if look_dir.length_squared() > 0.01:
				rotation.y = atan2(look_dir.x, look_dir.z)
