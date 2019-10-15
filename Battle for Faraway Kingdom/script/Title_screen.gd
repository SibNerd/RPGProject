extends TextureRect

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.



func _on_StartButton_pressed():
	get_tree().change_scene('res://scenes/GroundScene.tscn')



func _on_SettingsButton_pressed():
	get_tree().change_scene('res://scenes/SettingsMenu.tscn')


