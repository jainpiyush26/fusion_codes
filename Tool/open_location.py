import os
import sys
import subprocess

def main():
    tools_selected = comp.GetToolList(True)
    object_validation = ["Saver", "Loader"]
    for item_index, tool_obj in tools_selected.items():
        if tool_obj.GetAttrs()['TOOLS_RegID'] in object_validation:
            clip_path = tool_obj.Clip[0]
            clip_folder_path = os.path.dirname(clip_path)
            if os.path.exists(clip_folder_path):
                if sys.platform == "win32":
                    subprocess.Popen('explorer /select,"{0}"'.format(clip_folder_path), shell=True)
                elif sys.platform == "linux2":
                    subprocess.Popen('xdg-open "{0}"'.format(clip_folder_path), shell=True)
                elif sys.platform == "darwin":
                    subprocess.Popen('open "{0}"'.format(clip_folder_path), shell=True)
            else:
                print("The clip folder path does not exist!")

if __name__ == "__main__":
    main()