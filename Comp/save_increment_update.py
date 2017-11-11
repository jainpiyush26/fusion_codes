# Save Increment and Update
"""
Save and increments the version as well as any savers present in the comps

"""
import os
import re

def get_updated_version(comp_name):
	version_pattern_search = re.search("(v{0,1}\d*)$", os.path.splitext(comp_name)[0], re.I)
	if not version_pattern_search:
		return None, None
	else:
		orig_version_string = version_pattern_search.group(0)
		if re.match("v", orig_version_string, re.I):
			version_string = orig_version_string[1:]
		else:
			version_string = orig_version_string
			
		padding = len(version_string)
		current_version = int(version_string)
		new_version = current_version + 1
		new_version_padding = "{0:0" + str(padding) + "d}"
		new_version_final = new_version_padding.format(new_version)

		return new_version_final, version_string

def update_savers(saver, new_version, old_version_string):
	saver_path = saver.Clip[0]
	new_saver_path = re.sub(old_version_string, new_version, saver_path)
	if not os.path.exists(os.path.dirname(new_saver_path)):
		try:
			os.makedirs(os.path.dirname(new_saver_path))
		except:
			print ("You do not have rights to create folders there!")

	saver.Clip[0] = new_saver_path


def main():
	comp_name = comp.GetAttrs()['COMPS_Name']
	comp_file_location = os.path.dirname(comp.GetAttrs()['COMPS_FileName'])

	new_version, current_version_pattern = get_updated_version(comp_name)

	if not new_version:
		print ("Bad version string in the comp!")
		return

	comp.Lock()
	new_comp_name = re.sub(current_version_pattern + ".comp", new_version + ".comp", comp_name + ".comp")
	new_comp_location = os.path.join(comp_file_location, new_comp_name)
	comp.Save(new_comp_location)
	saver_list = comp.GetToolList(False, "Saver")
	if len(saver_list.values()) > 0:
		for items in saver_list.values():
			update_savers(items, new_version, current_version_pattern) 
	comp.Unlock()


if __name__ == "__main__":
	main()