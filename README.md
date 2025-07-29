🕷️ Web Application Vulnerability Scanner using Python

This project is developed as part of the Elevate Labs Internship Program. It is a lightweight Python-based tool designed to scan web applications for common security vulnerabilities like Cross-Site Scripting (XSS) and SQL Injection (SQLi). The scanner includes a simple Flask-based GUI for ease of use.

📌 Project Objective

To build an intuitive tool that helps identify common vulnerabilities in websites by analyzing HTML forms and testing input fields using crafted payloads.

The scanner aims to improve security awareness and can be used for educational and penetration testing purposes on test environments.

🔍 Features

✅ Detects common web vulnerabilities:

	Cross-Site Scripting (XSS)

	SQL Injection (SQLi)

✅ Scans and parses HTML forms from a given URL

✅ Command-line and GUI support via Flask

✅ Clean and user-friendly interface

✅ Extensible and beginner-friendly codebase

🛠️ Tools \& Technologies Used

- Python 3
- [Flask](https://flask.palletsprojects.com/) – Web framework for GUI
- [requests](https://docs.python-requests.org/) – For making HTTP requests
- [BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/) – For HTML parsing
- [re (regex)](https://docs.python.org/3/library/re.html) – For pattern matching

📁 Project Structure


web-vulnerability-scanner/

-app.py               # Flask web interface

-vuln\_scanner.py      # Core vulnerability scanning logic

-templates/
  - index.html       # UI template for entering URLs

- requirements.txt     # Python dependencies

- project\_report.pdf   # Final internship project report

- README.md            # Project documentation

🚀 How to Run

🔧 Step 1: Clone the Repository

git clone https://github.com/appsecpen/web-vulnerability-scanner.git

cd web-vulnerability-scanner


🔧 Step 2: Install Dependencies

pip install -r requirements.txt


🚀 Step 3: Run the Application

python app.py

Open your browser and visit:

http://127.0.0.1:5000


🧪 Sample Tested URLs

http://testphp.vulnweb.com

http://zero.webappsecurity.com

https://xss-game.appspot.com


⚠️ This tool is for educational use only. Do not scan real or production websites without proper authorization.


📊 Sample Output (Console)

\[+] Found 2 forms on http://testphp.vulnweb.com

\[\*] Testing form with action: /search.php

\[XSS] Vulnerable input field detected!

\[SQLi] SQL Injection attempt returned suspicious response!


👩‍💻 Developer

Yawanikha (@appsecpen)

Cybersecurity Intern, Elevate Labs

🔗 GitHub Profile


📄 License

This project is licensed under the MIT License.

See the LICENSE file for details.


🙏 Acknowledgements

OWASP Top 10

Elevate Labs – for the opportunity and guidance

The Python and Flask communities





