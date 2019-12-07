# FindDupImage.py
 
import os, glob
import Image
import hashlib
import shutil
 
def Imge_md5hash(im_file):
    im = Image.open(im_file)
    return hashlib.md5(im.tostring()).hexdigest()
 
def findDupImgMd5(data_path):
    hashdict={}
    deletionList=[]
 
    for infile in glob.glob(data_path + os.sep +"*.jpg"):
        fileNP, ext = os.path.splitext(infile)
        ids = fileNP.split(os.sep)
        hash_result = Imge_md5hash(infile)
        if hashdict.has_key(hash_result):
            deletionList.append(infile)
            hashdict.setdefault(hash_result, []).append(ids)
    return deletionList, hashdict
 
if __name__=="__main__":
 
    folderPath = r"your-image-data-folder"
    deletionList, hashdict = findDupImgMd5(folderPath)
 
    print("Start to save the data")
 
    with open("dupImageList.txt", 'wb') as ofile:
        _=[ofile.write(item+"\n") for item in deletionList]
 
    with open("hashDupImageDict.txt",'wb') as ofile:
        _=[ofile.write(k+"\t"+ "\t".join(v)+"\n") for (k,v) in hashdict.items()]
 
    """Copy the duplicated image to Dup-folder, renamed with
    hash-code and original id"""
  DesFolder = os.path.join(folderPath, "DupImg")
 
    if not os.path.exist(DesFolder):
        os.madir(DesFolder)
 
    for k,v in hashdict.items():
        if len(v)>1:
            for vi in v:
                srcP = os.path.join(folderPath, vi+".jpg")
                dstP = os.path.join(DesFolder, k+"_"+vi+".jpg")
                shutil.copyfile(srcP,dstP)