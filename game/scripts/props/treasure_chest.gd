class_name TreasureChest
extends StaticBody3D

@export var item_name: String = "星石のかけら"
@export var is_opened: bool = false

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
	
	# Visual open feedback (rotation or scale pop)
	if has_node("Lid"):
		get_node("Lid").rotation_degrees.x = -60.0
	elif has_node("ChestModel"):
		var model = get_node("ChestModel")
		var tween = create_tween()
		tween.tween_property(model, "scale", Vector3(1.15, 1.15, 1.15), 0.15)
		tween.tween_property(model, "scale", Vector3(1.0, 1.0, 1.0), 0.15)
	
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
	if is_inside_tree() and has_node("/root/QuestManager"):
		return get_node("/root/QuestManager")
	var nodes = get_tree().get_nodes_in_group("quest_manager")
	return nodes[0] if nodes.size() > 0 else null
