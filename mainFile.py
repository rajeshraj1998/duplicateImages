#put ur source folder path
source=r"C:\Users\Rajesh\Desktop\miniProjectPython\Images"
all_images  = [_ for _ in os.listdir(source)]

#put ur destination folder path
destination = r'C:\Users\Rajesh\Desktop\miniProjectPython\duplicate'
duplicates = []
for file_org in all_images:
    if not file_org in duplicates:
        image_org = Image.open(os.path.join(source, file_org))
        imghash = imagehash.average_hash(image_org)
        
        for file_check in all_images:
            if file_check!=file_org:
                img_check = Image.open(os.path.join(source, file_check))
                imghash1 = imagehash.average_hash(img_check)
 
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
                
