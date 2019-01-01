# Main File
import data_management as data
import ui, threading

widget_manager = data.data_manager("tk", "root")

disp = ui.display_window(widget_manager)
add = ui.add_ui(widget_manager, disp)
