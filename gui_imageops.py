import os

path = '/home/shrutheeshir/Desktop/ODLC-GUI/static/images'
path1 = '/home/shrutheeshir/Desktop/ODLC-GUI/static/images_moved/'
mainimg = '/home/shrutheeshir/Desktop/ODLC-GUI/static/images/MainImage.jpg'



class ImageVals:
    
    def __init__(self,imageArray,imageIndex):
        self.imageIndex = 0
        self.imageArray = []
        
    def val_set(self,imageArray,imageIndex):
        self.imageIndex = imageIndex
        self.imageArray = imageArray

    def getimg(self,imageArray,imageIndex):

        for subdir, dirs, files in os.walk(path):
            for file in files:
                print('++++++' + str(file) + '++++++')
                filepath = os.path.join(subdir, file)
                if filepath.endswith('.jpg') or filepath.endswith('.JPG'):
                    if filepath not in self.imageArray:
                        self.imageArray.append(filepath)
                        
        print(imageArray)
        #return self.imageArray,self.imageIndex;
        
        return None

    def previousimg(self,imageArray,imageIndex,myImage):
        if (self.imageIndex!=0):
            self.imageIndex=self.imageIndex-1
            print('*******' + str(self.imageIndex))
            myImage.setAttribute('src','images/'+self.imageArray[self.imageIndex])
            #myImage.src = (self.imageArray[self.imageIndex])
            #return self.imageArray,self.imageIndex;
            return None
    
    def nextimg(self,imageArray,imageIndex,myImage):
        print('*******' + str(self.imageIndex) + '*****')
        print(self.imageArray)

        if (self.imageIndex!=len(self.imageArray)-1):
            print('*******' + str(self.imageIndex) + '*****')

            self.imageIndex += 1
            print('-----------' + str(self.imageIndex) + '--------')

            #print("myImage.src",myImage.src)
            #myImage.src = (self.imageArray[self.imageIndex])
            myImage.setAttribute('src','images/'+self.imageArray[self.imageIndex])
            #print("Index",self.imageIndex)
            #return self.imageArray,self.imageIndex;
            return None
    
    def deleteimg(self,imageArray,imageIndex):
        #self.imageIndex = self.imageIndex-1
        os.unlink(self.imageArray[self.imageIndex])
        self.imageArray.remove(self.imageArray[self.imageIndex])

        if(self.imageIndex==len(self.imageArray)):
            self.imageIndex=0

        #self.imageIndex+=1
        #return self.imageArray,self.imageIndex;
        return None
        
    def moveimg(self,imageArray,imageIndex):
        #self.imageIndex = self.imageIndex-1
        os.rename(self.imageArray[self.imageIndex], path1+'img'+str(imageIndex)+'.jpg')
        self.imageArray.remove(self.imageArray[self.imageIndex])
        #self.imageIndex+=1
        #return self.imageArray,self.imageIndex;
        if(self.imageIndex==len(self.imageArray)):
            self.imageIndex=0
        
        return None
        
    def image_src(self,imageArray,imageIndex):
        return self.imageArray[self.imageIndex]
    