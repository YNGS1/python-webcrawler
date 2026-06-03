from bs4 import BeautifulSoup

def extract_links (html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = []

    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.append(href)
    return links


def fetch_page(url):
    import requests 

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error: Received status code{response.status_code}")
            return None
        
    except Exception as e:
        print (f"An error occured: {e}")
        return None
    
def check_security_vulnerabilities(html_content, url):
    vulnerabilities = []

    if 'admin' in html_content.lower() or 'login' in html_content.lower():
        vulnerabilities.append("possivle admin/login detected")

    if '.env' in html_content or 'config.php' in html_content or 'web.config' in html_content:
        vulnerabilities.append("possible configuration file exposure")

    if 'error' in html_content.lower() and ('mysql' in html_content.lower() or 'sql' in html_content.lower()):
        vulnerabilities.append("possible sensitive information in HTML comments")
    
    if '<script>' in html_content.lower() and 'user' in html_content.lower():
        vulnerabilities.append("Possible XSS vulnerability - user input in scripts")
    
    if 'action="http://' in html_content.lower():
        vulnerabilities.append("form submitting over HTTP (not HTTPS)")
    
    if 'jquery-1.' in html_content.lower() or 'jquery-2.' in html_content.lower():
        vulnerabilities.append("outdated jquery version")
    
    if 'index of /' in html_content.lower() and 'directory' in html_content.lower():
        vulnerabilities.append("possible directory listing enabled")

    if '/api' in html_content.lower() or '/rest' in html_content.lower():
        vulnerabilities.append("possible API endpoint exposure")

    if '<form' in html_content.lower() and 'crsf' not in html_content.lower():
        vulnerabilities.append("form without csrf protection")
    
    if '<!--'
    return vulnerabilities

test_url = "https://example.com"
html_content = fetch_page(test_url)

if html_content:
    print("successfully fetched the page!")
    print("first 100 characters:")
    print(html_content[:100])
else:
    print("Failed to fetch the page")

if html_content:
    links = extract_links(html_content)
    print(f"Found{len(links)} links on the page:")
    for link in links[:5]:
        print(link)
    
if html_content:
    links = extract_links(html_content)
    vulnerabilities = check_security_vulnerabilities(html_content, test_url)

    print(f"Found {len(links)} links on the page:")
    for link in links:
        print(f" {link}")

    print(f"\nSecurity check results:")
    if vulnerabilities:
        for vuln in vulnerabilities:
            print(f" [!] {vuln}")

    else: 
        print (" [+] No obvious vulnerabilities detected")