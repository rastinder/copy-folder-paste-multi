import shutil, os

# Set the source and destination directories
src_dir = r"C:\Users\Administrator\Desktop\coc\MBR_xbebenkMod\Profiles\MyVillage"
dst_dir = r"C:\Users\Administrator\Desktop\coc\MBR_xbebenkMod\Profiles"

# Loop through the range 1 to 32
for i in range(1, 33):
  # Set the new folder name
  new_folder_name = "my" + str(i)

  # Set the full path to the new folder
  new_folder_path = os.path.join(dst_dir, new_folder_name)

  # Copy the "myvillage" folder to the new location
  shutil.copytree(src_dir, new_folder_path)
