
'''

First Install the Library by running the following command in your terminal:

pip install yt-dlp


'''

import yt_dlp as yt

print("Welcome to the Youtube VIdeo Downloader App!! \n")


def DownloadVideo(url):

    ydl_opts = {}

    with yt.YoutubeDL(ydl_opts) as yld:
        yld.download([url])


    print("Video Downloaded Successfully!!!")


#Menu Drive:

while (True):


    getPerm = input("Want to Download the Youtube Video(y/n):")
    print()

    if (getPerm.isdigit()):

        print("Invalid Entry!!!, Try Again\n")

    elif (getPerm.isalpha()):

        if (getPerm.lower() == "y") or (getPerm.lower() == "yes"):

            print()

            try:

                getUrl = input("Enter the URL of the Youtube Video:")

                DownloadVideo(getUrl)
            
            except:

                print("Invalid URL, Try Again\n")
        

        if (getPerm.lower() == "n") or (getPerm.lower() == "no"):
            
            print("Program Closed Successfully!")
            break


