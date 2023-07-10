import shutil, os
 
formats = {
    "video" : [".mp4", ".wmv" ".webm", ".avi", ".flv", ".mov", ".mvk"],
    "image" : [".png", ".jpg", ".jpeg", ".gif", ".psd", ".tiff"],
    "documents" : [".txt", ".doc", ".docx", ".pdf", ".xls", ".xlsx", ".ppt", ".pps", ".odp", ".pptx", ".ods", ".odt", ".txt"]
}
 
src_folder = os.path.join(os.path.expandvars("%userprofile%"), "Downloads")
base_folder_count = 4
 
folders = ["Videos", "Images", "Documents", "Misc"]
 
for folder in folders:
    if(os.path.exists(os.path.join(src_folder, folder)) == False):
        os.makedirs(os.path.join(src_folder, folder))
 
files = os.listdir(src_folder)
 
for file in files:
    current_file_path = os.path.join(src_folder, file)
    file_split = os.path.splitext(file)
    if(formats["video"].count(file_split[1].lower()) > 0):
        shutil.move(current_file_path, os.path.join(src_folder, folders[0]))
        continue
    elif(formats["image"].count(file_split[1].lower()) > 0):
        shutil.move(current_file_path, os.path.join(src_folder, folders[1]))
        continue
    elif(formats["documents"].count(file_split[1].lower()) > 0):
        shutil.move(current_file_path, os.path.join(src_folder, folders[2]))
        continue
    elif(os.path.isfile(os.path.join(src_folder, file))):
        shutil.move(current_file_path, os.path.join(src_folder, folders[3]))
        continue