import requests
 
def doWebsitesExist(file_name):
    with open(file_name, "r", encoding="UTF-8") as file:
        websites = file.read()
        websites = tuple(websites.replace("\n", " ").split(" "))
        for website in websites:
            try:
                response = requests.get(website)
                status = response.status_code
                if status == 200:
                    with open("workingSites.txt", "a", encoding="UTF-8") as file1:
                        file1.write(website + "\n")
                elif status != 200:
                    with open("deadSites.txt", "a", encoding="UTF-8") as file2:
                        file2.write(website + "\n")
            finally:
                continue
 
doWebsitesExist("webs_to_check.txt")
