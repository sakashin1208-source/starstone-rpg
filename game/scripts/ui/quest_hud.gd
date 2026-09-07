class_name QuestHUD
extends CanvasLayer

@onready var objective_label: Label = $Control/MarginContainer/Panel/MarginContainer/VBoxContainer/ObjectiveLabel

func _ready() -> void:
	var qm = _get_quest_manager()
	if qm:
		qm.quest_state_changed.connect(_on_quest_state_changed)
		objective_label.text = qm.get_objective_text()

func _get_quest_manager() -> Node:
	if has_node("/root/QuestManager"):
		return get_node("/root/QuestManager")
	var nodes = get_tree().get_nodes_in_group("quest_manager")
	return nodes[0] if nodes.size() > 0 else null

func _on_quest_state_changed(_id: String, _state: int, objective: String) -> void:
	objective_label.text = objective
