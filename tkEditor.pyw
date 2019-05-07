# Main File
import data_management as data
import ui

widget_manager = data.data_mana+ger("tk.Tk", "root")

select = ui.selection_ui(widget_manager)
disp = ui.display_window(widget_manager)

select.ui_supply(disp)
disp.ui_supply(select)

add = ui.add_ui(widget_manager, disp)
menu = ui.menu_ui(widget_manager, disp, select)

select.start()

