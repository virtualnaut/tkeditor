# Main File
import data_management as data
import ui
import threading

widget_manager = data.data_manager("tk", "root")

x=ui.display_window()
y=ui.add_ui(widget_manager)
