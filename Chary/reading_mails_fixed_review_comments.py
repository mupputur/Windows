import win32com.client as client

outlook = client.Dispatch("Outlook.Application").GetNameSpace("MAPI")


class ReadMail:

    def inbox_mail(self, folder):
        inbox_message = folder.Items.GetLast()
        inbox_latest_megs = self.common(inbox_message)
        return f"Inbox latest mail is:{inbox_latest_megs}"

    def sent_mail(self, folder):
        sentbox_message = folder.Items.GetLast()
        return f"Sentbox latest mail is: {self.common(sentbox_message)}"

    def drafts_mail(self, folder):
        drafts_message = folder.Items.GetLast()
        return f"Draftbox latest mail is: {self.common(drafts_message)}"

    def deleted_mail(self, folder):
        deleted_message = folder.Items.GetLast()
        return f"Deleated Box latest mail is: {self.common(deleted_message)}"

    def outbox_mail(self, folder):
        outbox_message = folder.Items.GetLast()
        return f"Outbox latest mail is: {self.common(outbox_message)}"

    def common(self, attribute):
        mail_address = self.message_mail_address(attribute)
        time = f"The mail received at: {self.message_time(attribute)}"
        sender = f"Sender name is: {self.message_sendger(attribute)}"
        subject = f"subject in mail is: {self.message_subject(attribute)}"
        body = f"Body of the Mail is: {self.message_body(attribute)}"
        attchments = self.mail_attachments(attribute)
        latest_message = [mail_address, time, sender, subject, body, attchments]
        return latest_message

    def message_mail_address(self, folder):
        mail_ids1 = []
        recipients = folder.Recipients
        mail_ids = (folder.SenderEmailAddress, folder.CC, folder.BCC)
        try:
            for i in recipients:
                mail_ids1.append(str(i))
                mail_ids = (folder.SenderEmailAddress, folder.CC, folder.BCC)
                return f'mail recipients are : {mail_ids1},sender mail ids are: "{mail_ids}"'
        except:
            return mail_ids

    def mail_attachments(self, folder):
        subFolderItemAttachments = folder.Attachments
        no_of_attchments = subFolderItemAttachments.Count
        if no_of_attchments:

            attchments_list = [str(subFolderItemAttachments.item(x)) for x in range(1, (no_of_attchments+1)) ]
            """attchments_list = []
            for x in range(1, (no_of_attchments + 1)):
                attch = subFolderItemAttachments.item(x)
                attchments_list.append(str(attch))"""
            return f" mail having the attachments {attchments_list}"
        else:
            return " No attachments in the mail"



    def message_sendger(self, folder):
        return folder.SenderName

    def message_subject(self, folder):
        return folder.Subject

    def message_body(self, folder):
        return folder.Body

    def message_time(self, folder):

        return folder.ReceivedTime


# Class object creation......
outlook_obj = ReadMail()


def folder_acces(name):
    folder = str(name)
    count = name.Items.Count
    if count == 0:
        return f"No mails in {name}"
    if folder == "Inbox":
        inbox_result = outlook_obj.inbox_mail(name)
        return inbox_result
    elif folder == 'Sent Items':
        sent_box_result = outlook_obj.sent_mail(name)
        return sent_box_result
    elif folder == 'Drafts':
        drafts_result = outlook_obj.drafts_mail(name)
        return drafts_result
    elif folder == 'Deleted Items':
        deleted_result = outlook_obj.deleted_mail(name)
        return deleted_result
    elif folder == 'outbox':
        outbox_result = outlook_obj.outbox_mail(name)
        return outbox_result


if __name__ == "__main__":
    inbox_folder = outlook.GetDefaultFolder(6)
    print(folder_acces(inbox_folder))
    sentbox_folder = outlook.GetDefaultFolder(5)
    print(folder_acces(sentbox_folder))
    drafts_folder = outlook.GetDefaultFolder(16)
    print(folder_acces(drafts_folder))
    deleted = outlook.GetDefaultFolder(3)
    print(folder_acces(deleted))
    outbox = outlook.GetDefaultFolder(4)
    print(folder_acces(outbox))
