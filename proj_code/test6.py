# -------------------1. Create a dict for news_url and text to be appended to get feed url ------------------------

# news_web_rss = {
#     'https://timesofindia.indiatimes.com/': 'rss.cms',
#     'https://www.ndtv.com/': 'rss',
#     'https://www.hindustantimes.com/': 'rss',
#     'https://www.business-standard.com/': 'rss-feeds/listing/'
# }
#
# print(news_web_rss.keys())
#
# link = 'https://www.ndtv.com/'
#
# if link in news_web_rss.keys():
#     print("Present, ", end =" ")
#     print("value =", news_web_rss[link])
# else:
#     print("Not present")


# ------------------------------  2.  Import the file with class and call the methods inside it  ---------------------
# import test7 as f
#
# # access method inside class
# study_room = f.Room()
# # assign values to all the properties
# study_room.length = 42.5
# study_room.breadth = 30.8
#
# area = study_room.calculate_area()
# print("Area = ", area)
#
# # creating object of the class with no arguments.
# obj = f.NewGeeks                    # No parameters
#
# # calling the instance method using the object obj with argument
# obj.print_str("I am here")
#
# # creating object of the class with initial arguments.
# obj = f.GeekforGeeks("Hello Deepali")                               # pass the parameters while creating object only
#
# # calling the instance method using the object obj with argument
# obj.print_Geek("How are you?")
#
# url = f.FetchUrl("https://timesofindia.indiatimes.com/")
# url.fetch_url()


# -----------------------  3. Import Process1 class and call the read_main() method from it -----------------------
import process1 as p

obj = p.GetRssFeed()
print("............Reading main file")
obj.read_main()
print("reading done...........")



    
