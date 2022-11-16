import os

# read in urls.txt
def readLines(filename):
    with open(filename) as f:
        for line in f:
            yield line

def get_redirect_url(url):
    # remove last element
    url.pop()
    url_string = array_to_string(url)
    url_string = url_string[1:]
    return url_string

def get_original_url(url):
    url.pop(0)
    url.pop(1)
    url_string = array_to_string(url)
    url_string = url_string[1:]
    # remove new lines and carriage returns
    url_string = url_string.replace("\n", "")
    url_string = url_string.replace("\r", "")
    return url_string

def get_name(url):
    name = url[-1]
    name = name.replace("\n", "")
    name = name.replace("\r", "")
    return name

def get_numbered_name(count):
    return f"rule{count + 104}"

def array_to_string(array):
    url = "/".join(array)
    return url

def format_url_as_redirect(redirect_route, original_route, name):
    redirect = f"""
   <rule name="{name}" stopProcessing="true">
  <match url="^{original_route}(\/)*$" />
  <action type="Redirect" url="{redirect_route}" appendQueryString="false" />
    </rule>"""
    # remove any newlines or carriage returns 
    return redirect

def main():
    
    if os.path.exists("redirect.txt"):
        os.remove("redirect.txt")
   
    count = 0
    for full_url in readLines('urls.txt'):
        count = count + 1
        full_url = full_url.split("/")
        name = get_name(full_url)
        original_route = get_original_url(full_url)
        redirect_route = get_redirect_url(full_url)
 
        with open("redirect.txt", "a") as f:
            f.write(format_url_as_redirect(redirect_route, original_route, get_numbered_name(count)))
            f.write("\n")  

    print(f"{count} redirects created")
 
if __name__ == "__main__":
    main()  
