# def num_word():
#     '''Number to words . Create a python function that takes an integer number and
#     print the number in words
#     args: input number as int
#     return : number in words
#     '''
#     num=int(input("enter number :".title()))
#     word=str(num)
#     return(f"new words is {list(word)}")
# result=num_word()
# print(result)


from google_images_download import google_images_download  # importing the library

response = google_images_download.googleimagesdownload()  # class instantiation

arguments = ({"keywords": "cars , dogs in car , buaty baby , ",
             "limit": 15, "print_urls": True})  # creating list of arguments
paths = response.download(arguments)  # passing the arguments to the function
print(paths)  # printing absolute paths of the downloaded images
