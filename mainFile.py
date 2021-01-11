#replace with  your source folder path
source=r"C:\Users\Rajesh\Desktop\miniProjectPython\Images"
all_images  = [_ for _ in os.listdir(source)]

#replace with your destination folder path
destination = r'C:\Users\Rajesh\Desktop\miniProjectPython\duplicate'
duplicates = []
for file_org in all_images:
    if not file_org in duplicates:
        image_org = Image.open(os.path.join(source, file_org))
        imghash = imagehash.phash(image_org)
        
        for file_check in all_images:
            if file_check!=file_org:
                img_check = Image.open(os.path.join(source, file_check))
                imghash1 = imagehash.phash(img_check)
 
                if(imghash==imghash1):
                    duplicates.append(file_org)
                    duplicates.append(file_check)
print(duplicates)        

count=0
for dup in duplicates:
    for file_org in all_images:
        if(dup==file_org):
            try:
                shutil.move(os.path.join(source, file_org),os.path.join(destination, file_org))
                os.rename(os.path.join(destination, file_org),os.path.join(destination, str(count)+file_org))
                count=count+1
            except:
                print("")
                
