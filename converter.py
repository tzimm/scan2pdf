import Image
import ImageEnhance
import os

class Converter(): 
    """
    basic converting methods to create a sharp pdf out of scanned images
    """
    def Convert(self, prps, fileslist, general_output):
        """
        prps = properties
        properties = {"flip":flag, "contrast":integer, "brightness":integer, "sharpness":integer}

        fileslist: whole path of all jpgs to convert
        """
        #step1: create a pdf out of every single jpg
        for path in fileslist:
            self.Jpeg2Pdf(path, prps["contrast"], prps["brightness"], prps["sharpness"], prps["flipflag"])
        
        #step2: join the pdfs if necessary
        if len(general_output)>0:
            print "joining the created pdf files"
            #I use the raw path twice, hence create a new list for it
            fileslist_noextension=[]                
            argumentstring = ""            
            for i in fileslist:
                one_entry=i[:i.rfind(".")]
                fileslist_noextension.append(one_entry)
                argumentstring += one_entry
                argumentstring += ".pdf "
            argumentstring += "cat output "
            argumentstring += general_output

            os.system("pdftk "+argumentstring)
            
            for i in fileslist_noextension: #clean up
                i+=".pdf"
                print "deleting: " + i
                os.remove(i)    
   
    def Jpeg2Pdf(self, path, contrast, brightness, sharpness, flipflag):
        """
        takes path; creates a relatively small ".pdf" out of it
        """
        sourcepath = path
        destpath   = path[:path.rfind(".")] + ".pdf"
        new_scale = (1279,1772)
        DinA4     = (210,297)
        #image oeffnen
        im = Image.open(sourcepath)
        #kontrast verbessern
        enhancer = ImageEnhance.Contrast(im)
        im = enhancer.enhance(contrast)

        # heller machen
        enhancer = ImageEnhance.Brightness(im) 
        im = enhancer.enhance(brightness)

        # sharpness; experimentell
        enhancer = ImageEnhance.Sharpness(im)
        im = enhancer.enhance(sharpness)

        if(flipflag):
            #um 180 Grad drehen
            im = im.rotate(180)

        #skalieren
        im = im.resize(new_scale)

        #ausschneiden
        x_crop = (new_scale[1]*DinA4[0])/(DinA4[1])

        #box = 4 tuple

        new_scale[0]
        new_scale[1]

        x_crop_diff=new_scale[0]-x_crop

        box = (x_crop_diff,0,new_scale[0],new_scale[1])

        im = im.crop(box)

        #fp = open( destpath, 'w')
        im.save(destpath, "PDF", Quality = 100)

