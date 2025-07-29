import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import datetime

def log_vulnerability(vuln_type, url, form_num, evidence, severity="Medium"):
    log_entry = (f"[{datetime.datetime.now()}] {vuln_type} found on {url} "
                 f"in form #{form_num} | Severity: {severity}\nEvidence: {evidence}\n\n")
    with open('results/scan_log.txt', 'a') as f:
        f.write(log_entry)

def test_xss(url, form, inputs, form_num):
    xss_payload = "<script>alert('XSS')</script>"
    data = {}
    for input_tag in inputs:
        name = input_tag.get('name')
        if name:
            data[name] = xss_payload

    try:
        method = form.get('method', 'get').lower()
        action = form.get('action')
        target_url = urljoin(url, action) if action else url

        if method == 'post':
            response = requests.post(target_url, data=data)
        else:
            response = requests.get(target_url, params=data)

        if xss_payload in response.text:
            log_vulnerability("XSS", target_url, form_num, xss_payload, "High")
            return True
        return False
    except Exception:
        return False


def test_sqli(url, form, inputs, form_num):
    sqli_payload = "' OR '1'='1"
    data = {}
    for input_tag in inputs:
        name = input_tag.get('name')
        if name:
            data[name] = sqli_payload

    try:
        method = form.get('method', 'get').lower()
        action = form.get('action')
        target_url = urljoin(url, action) if action else url

        if method == 'post':
            response = requests.post(target_url, data=data)
        else:
            response = requests.get(target_url, params=data)

        error_signatures = ["SQL syntax", "mysql_fetch", "You have an error in your SQL syntax",
                            "Warning: mysql", "Unclosed quotation mark", "quoted string not properly terminated"]

        for sig in error_signatures:
            if sig.lower() in response.text.lower():
                log_vulnerability("SQL Injection", target_url, form_num, sqli_payload, "High")
                return True
        return False
    except Exception:
        return False


def find_input_fields(url):
    output = ""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        forms = soup.find_all('form')
        output += f"Found {len(forms)} forms on {url}\n"

        for i, form in enumerate(forms, 1):
            output += f"\nForm #{i}\n"
            inputs = form.find_all('input')
            for input_tag in inputs:
                input_name = input_tag.get('name')
                input_type = input_tag.get('type', 'text')
                output += f"Input field - Name: {input_name}, Type: {input_type}\n"

            # Test XSS and add results
            xss_found = test_xss(url, form, inputs, i)
            if xss_found:
                output += "⚠️ Potential XSS vulnerability detected!\n"
            else:
                output += "No XSS vulnerability detected.\n"

            # Test SQLi and add results
            sqli_found = test_sqli(url, form, inputs, i)
            if sqli_found:
                output += "⚠️ Potential SQL Injection vulnerability detected!\n"
            else:
                output += "No SQL Injection vulnerability detected.\n"

    except Exception as e:
        output += f"Error fetching or parsing {url}: {e}\n"

    return output

if __name__ == "__main__":
    test_url = input("Enter URL to scan: ")
    find_input_fields(test_url)
