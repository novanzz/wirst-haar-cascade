import urllib.request
import cv2
import numpy as np
import os

# neg1
def store_raw_images():
    # link kumpulan url untuk download image di image-net.com
    
    # family room http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03319745
    # tv room http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04406239
    # conference room http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03089879
    
   
  
    neg_images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04107743' 
    # room light 
    # orang http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n09618957
    # reading room http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04058096
    # waiting room http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03691817
    # room http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04105893

    # download dari link diatas lalu di decode karena hasil yang di ambil datanya masih berupa bit
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 2733  
    
    #jika tidak ada path dengan nama neg maka kita buat folder neg nya untuk mengkumpulkan image negatif
    if not os.path.exists('neg'):
        os.makedirs('neg')
    
    #iterasi jika image selesai di download maka akan langsung download lagi image selanjutnya
    for i in neg_image_urls.split('\n'):
        try:
            # print link
            print(i)
            #ambil gambar dan di jadi kan jpg
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            #ubah gambar ke grayscale
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # sampel harus punya ukuran yang sama jadi kita reize jadi 100*100
            resized_image = cv2.resize(img, (200, 200))
            # cetak gambar
            cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e)) 

# neg2
def store_raw_images2():
    # link kumpulan url untuk download image di image-net.com
    
    # family room http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03319745
    # tv room http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04406239
    # conference room http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03089879
    
   
  
    neg_images_link = '' 
    # room light http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04107743
    # orang http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n09618957
    # reading room http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04058096
    # waiting room http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03691817
    # room http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04105893

    # download dari link diatas lalu di decode karena hasil yang di ambil datanya masih berupa bit
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 4171
    
    #jika tidak ada path dengan nama neg maka kita buat folder neg nya untuk mengkumpulkan image negatif
    if not os.path.exists('neg2'):
        os.makedirs('neg2')
    
    #iterasi jika image selesai di download maka akan langsung download lagi image selanjutnya
    for i in neg_image_urls.split('\n'):
        try:
            # print link
            print(i)
            #ambil gambar dan di jadi kan jpg
            urllib.request.urlretrieve(i, "neg2/"+str(pic_num)+".jpg")
            #ubah gambar ke grayscale
            img = cv2.imread("neg2/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # sampel harus punya ukuran yang sama jadi kita reize jadi 100*100
            resized_image = cv2.resize(img, (200, 200))
            # cetak gambar
            cv2.imwrite("neg2/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))   


# sort gambar dummy
def find_badPict():
    match = False
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('badPict'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('badPict/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('Delete pict')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))

# untuk buat deskriptor gambar negatif dan positiv 1
def create_pos_n_neg():
    for file_type in ['neg']:
        
        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)

# untuk buat deskriptor gambar negatif dan positiv 2
def create_pos_n_neg2():
    for file_type in ['neg2']:
        
        for img in os.listdir(file_type):

            if file_type == 'pos2':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info2.dat','a') as f:
                    f.write(line)
            elif file_type == 'neg2':
                line = file_type+'/'+img+'\n'
                with open('bg2.txt','a') as f:
                    f.write(line)


def store_raw_imagesWatchPos():
    # link kumpulan url untuk download image di image-net.com
    neg_images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03323096'   
    # download dari link diatas lalu di decode karena hasil yang di ambil datanya masih berupa bit
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 1
    
    #jika tidak ada path dengan nama neg maka kita buat folder neg nya untuk mengkumpulkan image negatif
    if not os.path.exists('info'):
        os.makedirs('info')
    
    #iterasi jika image selesai di download maka akan langsung download lagi image selanjutnya
    for i in neg_image_urls.split('\n'):
        try:
            # print link
            print(i)
            #ambil gambar dan di jadi kan jpg
            urllib.request.urlretrieve(i, "info/"+str(pic_num)+".jpg")
            #ubah gambar ke grayscale
            img = cv2.imread("info/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # sampel harus punya ukuran yang sama jadi kita reize jadi 100*100
            resized_image = cv2.resize(img, (100, 100))
            # cetak gambar
            cv2.imwrite("info/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))  


# store_raw_images()
# find_badPict()
# create_pos_n_neg()
store_raw_images2()
