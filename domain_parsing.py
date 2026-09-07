# s1 = "https://www.example.com/path/to/page?query=string#fragment"
# print("Protocol:", s1.split("://")[0])
# print("Domain:", s1.split("://")[1].split("/")[0])
# print("Path:", s1.split("://")[1].split("/")[1])
# print("Query:", s1.split("://")[1].split("?")[1].split("#")[0])
# print("Fragment:", s1.split("://")[1].split("?")[1].split("#")[1])
# print("Subdomain:", s1.split("://")[1].split(".")[0])

url = 'https://www.kaggle.com/datasets'
# TODO: Find the position of the colon (:) to extract protocol
# protocol = ???
print("protocol",url.split("://")[0])

# TODO: Find the positions of the dots (.) to locate the start/end of the domain
# dot1 = ???
# dot2 = ???
print("the domain name",url.split("://")[1].split(".")[1])

# TODO: Use slicing to get the protocol (before :) and the domain (between dots)
# protocol = ???
# domain = ???
print("page",url.split("://")[1].split("/")[1])

# TODO: Find the slash after the domain and slice to get the page part
# page = ???