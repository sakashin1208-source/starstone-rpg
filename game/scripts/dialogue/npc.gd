class_name NPC
extends CharacterBody3D

@export var npc_name: String = "長老"
@export var dialogue_file_path: String = "res://data/dialogues/elder_intro.json"

@onready var interactable: Interactable = $Interactable

func _ready() -> void:
	if interactable:
		interactable.interacted.connect(_on_interacted)

func _on_interacted(interactor: Node3D) -> void:
	var qm = _get_quest_manager()
	var current_dialogue_path = dialogue_file_path
	
	# Quest-specific branch for Elder
	if npc_name == "村の長老" and qm:
		var state = qm.current_state
		if state == QuestManager.QuestState.NOT_STARTED:
			current_dialogue_path = "res://data/dialogues/elder_intro.json"
		elif state == QuestManager.QuestState.IN_PROGRESS:
			current_dialogue_path = "res://data/dialogues/elder_in_progress.json"
		elif state == QuestManager.QuestState.READY_TO_REPORT:
			current_dialogue_path = "res://data/dialogues/elder_complete.json"
		elif state == QuestManager.QuestState.COMPLETED:
			current_dialogue_path = "res://data/dialogues/elder_after.json"

	var dialogue_boxes = get_tree().get_nodes_in_group("dialogue_box")
	if dialogue_boxes.size() > 0:
		var dialogue_box = dialogue_boxes[0]
		dialogue_box.start_dialogue_from_file(current_dialogue_path, npc_name)
		
		# Hook for dialogue completion
		if npc_name == "村の長老" and qm:
			var callable = Callable(self, "_on_elder_dialogue_ended")
			if not dialogue_box.dialogue_ended.is_connected(callable):
				dialogue_box.dialogue_ended.connect(callable, CONNECT_ONE_SHOT)

		# Turn NPC towards player
		if interactor:
			var look_dir = interactor.global_position - global_position
			look_dir.y = 0.0
			if look_dir.length_squared() > 0.01:
				rotation.y = atan2(look_dir.x, look_dir.z)

func _on_elder_dialogue_ended() -> void:
	var qm = _get_quest_manager()
	if not qm:
		return
	if qm.current_state == QuestManager.QuestState.NOT_STARTED:
		qm.start_quest("quest_001")
	elif qm.current_state == QuestManager.QuestState.READY_TO_REPORT:
		qm.complete_quest()

func _get_quest_manager() -> Node:
	if has_node("/root/QuestManager"):
		return get_node("/root/QuestManager")
	var nodes = get_tree().get_nodes_in_group("quest_manager")
	return nodes[0] if nodes.size() > 0 else null
