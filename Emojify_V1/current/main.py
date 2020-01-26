import cv2
import find_emoji

if __name__=='__main__':
    def video_parse():
        cap = cv2.VideoCapture(0)

        frequency = 10     # higher freq, lower still image outputs
        i=0

        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break
            
            if (i%frequency==0):
                cv2.imwrite('CLASSIFY_ME.jpg',frame)
                find_emoji.find_emoji()
                print("Parsing emotion:\n")
            
            i+=1

        cap.release()
        cv2.destroyAllWindows()
    

    video_parse()
    
