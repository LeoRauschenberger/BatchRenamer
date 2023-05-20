import os

# --- Add Folder path here. Make sure to use /and not\   ----
folder_path = 'C:/Users/.../Folder'  # Replace with the path to your folder

# --- Prefix and suffix Operations --------------------------
rm_prefix = "LS"
addprefix = "DS"
rm_suffix = "_A"
addsuffix = ""
# Example given would rename "LS_2023_A" to "DS_2023" etc.

# --- Iterate over all files in the folder ------------------
for filename in os.listdir(folder_path):
    # Check if the item is a file
    if os.path.isfile(os.path.join(folder_path, filename)):
        name = os.path.splitext(filename)[0]
        name = name.lstrip(rm_prefix)
        name = name.rstrip(rm_suffix)
        new_filename = addprefix+name+addsuffix+os.path.splitext(filename)[1]
        # Rename the file
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        print(f"Renamed {filename} to {new_filename}")
