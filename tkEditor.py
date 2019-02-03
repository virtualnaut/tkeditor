# Main File
import data_management as data
import ui, threading

widget_manager = data.data_manager("tk", "root")


b=ui.base()
#selection_manager = data.selection_manager(select)
select = ui.selection_ui(widget_manager)
disp = ui.display_window(widget_manager, select)
add = ui.add_ui(widget_manager, disp)
b.begin()
