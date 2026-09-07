class_name BattleSystem
extends Node3D

enum BattleState {
	PLAYER_TURN,
	ENEMY_TURN,
	WON,
	LOST,
	BUSY
}

@export var return_scene_path: String = "res://scenes/maps/forest.tscn"

var player_hp: int = 40
var player_max_hp: int = 40
var player_mp: int = 15
var player_max_mp: int = 15

var enemy_name: String = "フォレストスライム"
var enemy_hp: int = 25
var enemy_max_hp: int = 25
var enemy_atk: int = 6

var is_defending: bool = false
var state: BattleState = BattleState.PLAYER_TURN

@onready var log_label: Label = $UI/PanelContainer/MarginContainer/VBoxContainer/LogLabel
@onready var player_hp_label: Label = $UI/StatusPanel/MarginContainer/HBoxContainer/HPLabel
@onready var player_mp_label: Label = $UI/StatusPanel/MarginContainer/HBoxContainer/MPLabel
@onready var enemy_hp_bar: ProgressBar = $UI/EnemyPanel/VBoxContainer/EnemyHPBar
@onready var enemy_name_label: Label = $UI/EnemyPanel/VBoxContainer/EnemyNameLabel
@onready var commands_container: HBoxContainer = $UI/CommandsPanel/MarginContainer/HBoxContainer
@onready var slime_visual: Node3D = $SlimeNode/Visual

func _ready() -> void:
	_update_ui()
	_set_log("スライムがあらわれた！ どうする？")

func _update_ui() -> void:
	player_hp_label.text = "HP: %d / %d" % [player_hp, player_max_hp]
	player_mp_label.text = "MP: %d / %d" % [player_mp, player_max_mp]
	enemy_hp_bar.max_value = enemy_max_hp
	enemy_hp_bar.value = enemy_hp
	enemy_name_label.text = enemy_name

func _set_log(text: String) -> void:
	log_label.text = text

func _set_commands_enabled(enabled: bool) -> void:
	for btn in commands_container.get_children():
		if btn is Button:
			btn.disabled = not enabled

func on_attack_pressed() -> void:
	if state != BattleState.PLAYER_TURN:
		return
	state = BattleState.BUSY
	_set_commands_enabled(false)
	is_defending = false
	
	var damage = randi_range(9, 13)
	enemy_hp = max(0, enemy_hp - damage)
	_update_ui()
	_set_log("レオンのこうげき！ %s に %d のダメージ！" % [enemy_name, damage])
	
	await get_tree().create_timer(1.2).timeout
	_check_battle_status()

func on_skill_pressed() -> void:
	if state != BattleState.PLAYER_TURN:
		return
	if player_mp < 5:
		_set_log("MPがたりない！")
		return
		
	state = BattleState.BUSY
	_set_commands_enabled(false)
	is_defending = false
	player_mp -= 5
	
	var damage = randi_range(18, 22)
	enemy_hp = max(0, enemy_hp - damage)
	_update_ui()
	_set_log("星光斬！ %s に %d の特大ダメージ！" % [enemy_name, damage])
	
	await get_tree().create_timer(1.2).timeout
	_check_battle_status()

func on_item_pressed() -> void:
	if state != BattleState.PLAYER_TURN:
		return
	state = BattleState.BUSY
	_set_commands_enabled(false)
	is_defending = false
	
	var heal = 20
	player_hp = min(player_max_hp, player_hp + heal)
	_update_ui()
	_set_log("やくそうを使った！ HPが %d 回復した！" % heal)
	
	await get_tree().create_timer(1.2).timeout
	_enemy_turn()

func on_defend_pressed() -> void:
	if state != BattleState.PLAYER_TURN:
		return
	state = BattleState.BUSY
	_set_commands_enabled(false)
	is_defending = true
	_set_log("レオンは身をかためている。受けるダメージが半減する！")
	
	await get_tree().create_timer(1.0).timeout
	_enemy_turn()

func _check_battle_status() -> void:
	if enemy_hp <= 0:
		_victory()
	else:
		_enemy_turn()

func _enemy_turn() -> void:
	state = BattleState.ENEMY_TURN
	_set_log("%s のたいあたり！" % enemy_name)
	await get_tree().create_timer(1.0).timeout
	
	var raw_damage = randi_range(4, 7)
	var final_damage = max(1, int(raw_damage / 2.0)) if is_defending else raw_damage
	player_hp = max(0, player_hp - final_damage)
	_update_ui()
	_set_log("レオンは %d のダメージを受けた！" % final_damage)
	
	await get_tree().create_timer(1.0).timeout
	if player_hp <= 0:
		_defeat()
	else:
		state = BattleState.PLAYER_TURN
		_set_commands_enabled(true)
		_set_log("どうする？")

func _victory() -> void:
	state = BattleState.WON
	_set_log("%s をたおした！ 20 EXP と 15 Gold を手に入れた！" % enemy_name)
	await get_tree().create_timer(1.8).timeout
	get_tree().change_scene_to_file(return_scene_path)

func _defeat() -> void:
	state = BattleState.LOST
	_set_log("レオンはたおれてしまった…… 村へ戻ります。")
	await get_tree().create_timer(2.0).timeout
	get_tree().change_scene_to_file("res://scenes/maps/village.tscn")
