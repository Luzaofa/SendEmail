__author__ = 'Luzaofa'
__date__ = '2018/9/20 8:35'

import EmailHelper
import Email_config


class Email(object):

    def __init__(self):
        self.EmailHelper = EmailHelper.EmailHelper()

    def write_email(self):

        count_error = 0

        email_type = Email_config.mass_type
        if email_type == '' or email_type is None:
            print('用户配置信息缺少邮件类型')
        elif email_type == 'massage':
            self.EmailHelper.massage(subject=Email_config.subject, mass=Email_config.mass)
        elif email_type == 'html_massage':
            self.EmailHelper.html_massage(subject=Email_config.subject, mass=Email_config.mass)
        elif email_type == 'html_pic_massage':
            self.EmailHelper.html_pic_massage(subject=Email_config.subject, mass=Email_config.mass,
                                              pic_path=Email_config.mass_pic_path, cid=Email_config.cid)
        else:
            print('无效邮件类型')
            count_error += 1

        att_type = Email_config.att_type
        if att_type:
            for type_ in att_type:
                if type_ == 'xlsx_att':
                    self.EmailHelper.xlsx_att(xls_path=Email_config.xls_path)
                elif type_ == 'docx_att':
                    self.EmailHelper.docx_att(doc_path=Email_config.doc_path)
                elif type_ == 'jpg_att':
                    self.EmailHelper.jpg_att(pic_path=Email_config.pic_path)
                else:
                    print('无效附件类型')
                    count_error += 1
        return email_type, count_error

    def sand_mail(self):
        email_type, count_error = self.write_email()
        if email_type != '' and count_error == 0:
            if Email_config.receiver != '':
                self.EmailHelper.sendemail(receiver=Email_config.receiver)
            else:
                print('缺失发送用户邮件地址！')


if __name__ == '__main__':

    Email = Email()
    Email.sand_mail()


