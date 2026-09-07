extends Node

enum QuestState {
	NOT_STARTED,
	IN_PROGRESS,
	READY_TO_REPORT,
	COMPLETED
}

signal quest_state_changed(quest_id: String, state: QuestState, objective: String)

var current_quest_id: String = "quest_001"
var current_state: QuestState = QuestState.NOT_STARTED
var current_objective: String = "長老から話を聞く"
var has_starstone_shard: bool = false
var quest_data: Dictionary = {}

func _ready() -> void:
	_load_quest_data("res://data/quests/quest_001_forest.json")

func _load_quest_data(path: String) -> void:
	if FileAccess.file_exists(path):
		var file = FileAccess.open(path, FileAccess.READ)
		var json = JSON.new()
		if json.parse(file.get_as_text()) == OK:
			quest_data = json.data

func start_quest(quest_id: String = "quest_001") -> void:
	if current_state == QuestState.NOT_STARTED:
		current_quest_id = quest_id
		current_state = QuestState.IN_PROGRESS
		current_objective = quest_data.get("objectives", {}).get("in_progress", "森の奥を調査する")
		quest_state_changed.emit(current_quest_id, current_state, current_objective)

func mark_ready_to_report() -> void:
	if current_state == QuestState.IN_PROGRESS:
		has_starstone_shard = true
		current_state = QuestState.READY_TO_REPORT
		current_objective = quest_data.get("objectives", {}).get("ready_to_report", "長老に報告する")
		quest_state_changed.emit(current_quest_id, current_state, current_objective)

func complete_quest() -> void:
	if current_state == QuestState.READY_TO_REPORT:
		current_state = QuestState.COMPLETED
		current_objective = quest_data.get("objectives", {}).get("completed", "調査完了！")
		quest_state_changed.emit(current_quest_id, current_state, current_objective)

func get_objective_text() -> String:
	return current_objective
