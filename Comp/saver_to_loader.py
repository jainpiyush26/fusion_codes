# Saver To Loader 
"""
Converts the savers to the loaders

Author: Piyush Jain
"""
import os
import re

def get_paths(saver):
	saver_path = saver.Clip[0]
	saver_folder = os.path.dirname(saver_path)
	saver_name = os.path.split(saver_path)[-1]
	saver_name_pattern = saver_name.split(".")[0]
	if os.path.exists(saver_folder):
		saver_folder_list = os.listdir(saver_folder)
		if len(saver_folder_list) > 0:
			for items in sorted(saver_folder_list):
				if re.search(saver_name_pattern, items):
					return os.path.join(saver_folder, items)
		else:
			return None
	else:
		return None


def main():
	saver_list = comp.GetToolList(True, "Saver")
	comp_pos_obj = comp.CurrentFrame.FlowView
	comp.Lock()
	for saver_items in saver_list.values():
		saver_position_x, saver_position_y = comp_pos_obj.GetPosTable(saver_items).values()
		loader_path = get_paths(saver_items)
		if loader_path:
			loader_obj = comp.AddTool("Loader")
			comp_pos_obj.SetPos(loader_obj, saver_position_x+2.0, saver_position_y)
			loader_obj.Clip[0] = loader_path
		else:
			print ("For {} there is no valid render available!".format(saver_items.Name))

	comp.Unlock()


if __name__ == "__main__":
	main()