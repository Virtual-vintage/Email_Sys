#! usr/bin/env python
# coding:utf-8
"""
Email 监测模块
==============
author @ wud
date   @ 2018.8.17
ver 0.1
"""

from email.mime.text import MIMEText
import smtplib

sender = "x"
sender_pass = "x"
receiver = ["x", "x"]
smtp_server = "x"



class SendEmail:
    """send email"""
    def __init__(self):
        self.sender = sender
        self.sender_pass = sender_pass
        self.receiver = receiver
        self.smtp_server = smtp_server
        try:
            self.server = smtplib.SMTP(self.smtp_server, 25)
        except Exception as e:
            print "Smtp server connect failed ->" + str(e)

    def send(self, server_list):
        _send_text = "WHOIS SERVICE API VER 0.1\n\n"
        _send_text += "Author - Wangjunx@WUD\n"
        _send_text += "Harbin Institute Of Technology At Weihai\n\n"
        _send_text += "Network and Information Security Research Center\n"
        _send_text += "Domain Name System Security Technology Research laboratory\n"
        _send_text += "----------------------------------------\n"
        error_api_num = len(server_list)
        for api_server in server_list:
            print api_server
            _send_text += '*  ' + str(api_server) + '\n'
        _send_text += "----------------------------------------\n"
        msg = MIMEText(_send_text, "plain", "utf-8")
        msg['From'] = 'WUD_API_SERVICE <' + self.sender + '>'
        msg['To'] = 'Wangjunx <' + "Dns Laboratory Manager" + '>'
        msg['Subject'] = '[API_CLIENT]__' + str(error_api_num) + '__API_ERROR'
        self.server.set_debuglevel(1)
        self.server.login(self.sender, self.sender_pass)
        self.server.sendmail(self.sender, self.receiver, msg.as_string())
        self.server.quit()


if __name__ == '__main__':
    S = SendEmail()
    S.send("this is a test email")
    print "send success"
