
search = {}
search["sitename"] = "facebook"
search["siteurl"] = "facebook.com"
search["email"] = "pranav17502@gmail.com"
search["username"] = "pranav17502@gmail.com"

query = "SELECT * FROM pm.entries WHERE "
for i in search:
    query+=f"{i} = '{search[i]}' AND "
query = query[:-5]

print(query)