__author__ = 'Luzaofa'
__date__ = '2018/9/20 8:35'

import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


class EmailHelper(object):

    sender = 'XXXXX@126.com'        # 发送账户
    smtpserver = 'smtp.126.com'     # 邮箱服务器
    username = 'XXXXX@126.com'      # 用户名
    password = 'XXXXXXXXXXXXXXX'    # 授权码

    def __init__(self):

        try:
            self.msg = MIMEMultipart()
            self.msg['From'] = self.sender
            self.smtp = smtplib.SMTP()
            self.smtp.connect(self.smtpserver)
            self.smtp.login(self.username, self.password)
        except Exception as e:
            print('邮箱初始化错误：', e)

    def massage(self, subject=None, mass=None):
        """
        发送纯文本内容
        :param subject: 邮件主题
        :param mass: 纯文本信息          eg：文本内容
        :return:
        """
        self.msg['Subject'] = subject
        message = MIMEText(mass)
        self.msg.attach(message)

    def html_massage(self, subject, mass):
        """
        发送html文本
        :param subject: 邮件主题
        :param mass: html格式      eg: <p>{mass}</p>  <p><a href="http://www.luzaofa.com">爱情链接!</a></p>
        :return:
        """
        self.msg['Subject'] = subject
        mail_msg = mass
        message = MIMEText(mail_msg, 'html', 'utf-8')
        self.msg.attach(message)

    def html_pic_massage(self, subject, mass, pic_path, cid):
        """
        发送夹带cid图片信息的html文本
        :param subject: 邮件主题
        :param mass: 夹带cid图片信息的html文本   eg：<p>文本信息</p>  <img src="cid:imageid">  imageid：图片ID
        :param pic_path: 图片地址
        :cid：图片Content-ID                    eg：['cid1', 'cid2', 'cid3'
        :return:
        """
        self.msg['Subject'] = subject
        mail_msg = mass
        message = MIMEText(mail_msg, 'html', 'utf-8')
        self.msg.attach(message)
        i = 0
        for id in cid:
            mass_pic_ = open(pic_path[0], "rb")
            img = MIMEImage(mass_pic_.read())
            mass_pic_.close()
            img.add_header('Content-ID', id)
            self.msg.attach(img)
            i += 1

    def xlsx_att(self, xls_path):
        """
        发送Excel类型附件
        :param xls_path: Excel文件地址
        :return:
        """
        try:
            for file in xls_path:
                xlsxpart = MIMEApplication(open(file, 'rb').read())
                xlsxpart.add_header('Content-Disposition', 'attachment', filename=str(file).split('/')[-1])
                self.msg.attach(xlsxpart)
        except Exception as e:
            print('获取Excel文件错误：{0}'.format(e))
            pass

    def docx_att(self, doc_path):
        """word类型附件"""
        try:
            for file in doc_path:
                xlsxpart = MIMEApplication(open(doc_path, 'rb').read())
                xlsxpart.add_header('Content-Disposition', 'attachment', filename=str(file).split('/')[-1])
                self.msg.attach(xlsxpart)
        except Exception as e:
            print('获取Word文件错误：{0}'.format(e))
            pass

    def jpg_att(self, pic_path):
        """图片类型附件"""
        try:
            for file in pic_path:
                jpgpart = MIMEApplication(open(pic_path, 'rb').read())
                jpgpart.add_header('Content-Disposition', 'attachment', filename=str(file).split('/')[-1])
                self.msg.attach(jpgpart)
        except Exception as e:
            print('获取图片文件错误：{0}'.format(e))
            pass

    def mp3_att(self, mp3_path):
        """mp3类型附件"""
        try:
            for file in mp3_path:
                mp3part = MIMEApplication(open(mp3_path, 'rb').read())
                mp3part.add_header('Content-Disposition', 'attachment', filename=str(file).split('/')[-1])
                self.msg.attach(mp3part)
        except Exception as e:
            print('获取mp3文件错误：{0}'.format(e))
            pass

    def sendemail(self, receiver):
        """
        发送邮件
        :param receiver: 接受用户邮件地址   eg：['luzaofa@126.com', '15202122003@126.com']
        :return:
        """
        try:
            self.msg['To'] = ",".join(receiver)
            self.smtp.sendmail(self.sender, receiver, self.msg.as_string())
            self.smtp.quit()
            print('已经成功向:{0}发送邮件！'.format(receiver))
        except Exception as e:
            print('邮件发送失败：{0},请重新发送'.format(e))
            pass


