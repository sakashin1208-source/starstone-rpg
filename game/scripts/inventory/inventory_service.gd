extends Node

signal inventory_changed
signal currency_changed(gold: int, exp_points: int)

var items: Dictionary = {
	"herb": 2,
	"starstone_shard": 0
}
var gold: int = 50
var exp_points: int = 0

func add_item(item_id: String, count: int = 1) -> void:
	if items.has(item_id):
		items[item_id] += count
	else:
		items[item_id] = count
	inventory_changed.emit()

func remove_item(item_id: String, count: int = 1) -> bool:
	if items.get(item_id, 0) >= count:
		items[item_id] -= count
		inventory_changed.emit()
		return true
	return false

func get_item_count(item_id: String) -> int:
	return items.get(item_id, 0)

func add_gold(amount: int) -> void:
	gold = max(0, gold + amount)
	currency_changed.emit(gold, exp_points)

func add_exp(amount: int) -> void:
	exp_points = max(0, exp_points + amount)
	currency_changed.emit(gold, exp_points)

func get_save_dict() -> Dictionary:
	return {
		"items": items.duplicate(),
		"gold": gold,
		"exp_points": exp_points
	}

func load_save_dict(data: Dictionary) -> void:
	if data.has("items"):
		items = data["items"].duplicate()
	if data.has("gold"):
		gold = int(data["gold"])
	if data.has("exp_points"):
		exp_points = int(data["exp_points"])
	inventory_changed.emit()
	currency_changed.emit(gold, exp_points)
