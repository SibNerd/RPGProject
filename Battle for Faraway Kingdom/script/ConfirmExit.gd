extends Control



func _on_No_pressed():
	get_tree().change_scene("res://scenes/GroundScene.tscn")


func _on_Yes_pressed():
	get_tree().change_scene("res://scenes/Title_screen.tscn")
