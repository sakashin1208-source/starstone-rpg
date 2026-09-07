class_name DialogueBox
extends CanvasLayer

signal dialogue_started
signal dialogue_ended

@onready var panel_container: PanelContainer = $Control/PanelContainer
@onready var speaker_label: Label = $Control/PanelContainer/MarginContainer/VBoxContainer/SpeakerLabel
@onready var content_label: Label = $Control/PanelContainer/MarginContainer/VBoxContainer/ContentLabel
@onready var next_indicator: Label = $Control/PanelContainer/MarginContainer/VBoxContainer/NextIndicator

var dialogue_lines: Array = []
var current_line_index: int = 0
var is_active: bool = false

func _ready() -> void:
	add_to_group("dialogue_box")
	panel_container.visible = false

func start_dialogue_from_file(file_path: String, fallback_speaker: String = "") -> void:
	if not FileAccess.file_exists(file_path):
		start_dialogue(fallback_speaker, ["(会話データが見つかりませんでした)"])
		return

	var file = FileAccess.open(file_path, FileAccess.READ)
	var json_text = file.get_as_text()
	var json = JSON.new()
	var parse_err = json.parse(json_text)
	if parse_err != OK:
		start_dialogue(fallback_speaker, ["(会話データの解析に失敗しました)"])
		return

	var data = json.data
	var speaker = data.get("speaker", fallback_speaker)
	var lines = data.get("lines", [])
	start_dialogue(speaker, lines)

func start_dialogue(speaker: String, lines: Array) -> void:
	if lines.is_empty():
		return

	dialogue_lines = lines
	current_line_index = 0
	is_active = true
	speaker_label.text = speaker
	
	panel_container.visible = true
	_lock_player(true)
	_display_current_line()
	dialogue_started.emit()

func _display_current_line() -> void:
	content_label.text = str(dialogue_lines[current_line_index])
	if current_line_index >= dialogue_lines.size() - 1:
		next_indicator.text = "▼ 完了 [E]"
	else:
		next_indicator.text = "▼ つぎへ [E]"

func advance_dialogue() -> void:
	current_line_index += 1
	if current_line_index < dialogue_lines.size():
		_display_current_line()
	else:
		end_dialogue()

func end_dialogue() -> void:
	is_active = false
	panel_container.visible = false
	_lock_player(false)
	dialogue_ended.emit()

func _lock_player(locked: bool) -> void:
	var players = get_tree().get_nodes_in_group("player")
	for p in players:
		if p.has_method("set_control_locked"):
			p.set_control_locked(locked)

func _unhandled_input(event: InputEvent) -> void:
	if is_active and (event.is_action_pressed("interact") or event.is_action_pressed("ui_accept")):
		advance_dialogue()
		get_viewport().set_input_as_handled()
