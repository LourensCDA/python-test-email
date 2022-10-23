import pydig
from telnetlib import Telnet

check_site = input("Enter the site to check: ")
print("Checking site: " + check_site)
print("MX records are:" + str(pydig.query(check_site, "MX")))

telnet_server = input("Enter the telnet server: ")
mail_from = input("Enter the mail from: ")
rcpt_to = input("Enter the rcpt to: ")

cmds = [
    "HELO gmail.com",
    f"MAIL FROM: <{mail_from}>",
    f"RCPT TO: <{rcpt_to}>",
    "close",
]

with Telnet(telnet_server, 25) as tn:
    for cmd in cmds:
        print(f"Command: {cmd}")
        tn.write(bytes(f"{cmd}\n", "utf-8"))
        line = tn.read_until(b"\n")  # Read one line
        print(f"Response: {line}\n")
