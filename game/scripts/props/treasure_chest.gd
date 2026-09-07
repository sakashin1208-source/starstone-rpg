class_name TreasureChest
extends StaticBody3D

@export var item_name: String = "星石のかけら"
@export var is_opened: bool = false

@onready var lid: Node3D = $Lid
@onready var interactable: Interactable = $Interactable

func _ready() -> void:
	if interactable:
		interactable.interacted.connect(_on_interacted)

func _on_interacted(_interactor: Node3D) -> void:
	if is_opened:
		var dialogue_boxes = get_tree().get_nodes_in_group("dialogue_box")
		if dialogue_boxes.size() > 0:
			dialogue_boxes[0].start_dialogue("宝箱", ["宝箱はからっぽだ。"])
		return

	open_chest()

func open_chest() -> void:
	is_opened = true
	if lid:
		lid.rotation_degrees.x = -60.0 # Open lid
	
	var qm = _get_quest_manager()
	if qm and qm.has_method("mark_ready_to_report"):
		qm.mark_ready_to_report()
	
	var dialogue_boxes = get_tree().get_nodes_in_group("dialogue_box")
	if dialogue_boxes.size() > 0:
		dialogue_boxes[0].start_dialogue("宝箱", [
			"宝箱を開けた！",
			"『%s』を手に入れた！" % item_name,
			"温かな光を放っている…… 長老に報告しに行こう。"
		])

func _get_quest_manager() -> Node:
	if has_node("/root/QuestManager"):
		return get_node("/root/QuestManager")
	var nodes = get_tree().get_nodes_in_group("quest_manager")
	return nodes[0] if nodes.size() > 0 else null
