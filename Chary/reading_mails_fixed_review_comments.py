import win32com.client as client

outlook = client.Dispatch("Outlook.Application").GetNameSpace("MAPI")


class ReadMail:

    def inbox_mail(self,folder):
        self.inbox_message = folder.Items.GetLast()
        mail_address = f"In Inbox : {self.message_mail_address(self.inbox_message)}"
        time = f"The mail received at: {self.message_time(self.inbox_message)}"
        sender = f"Sender name is: {self.message_sendger(self.inbox_message)}"
        subject = f"subject in mail is: {self.message_subject(self.inbox_message)}"
        body = f"Body of the Mail is: {self.message_body(self.inbox_message)}"
        inbox_latest_message = [mail_address, time, sender, subject, body]
        print(inbox_latest_message)
        return inbox_latest_message

    def sent_mail(self):
        sentbox_message = sentbox_folder.Items.GetLast()
        mail_address = f"In sent box : {self.message_mail_address(sentbox_message)}"
        time = f"time_stamp is : {self.message_time(sentbox_message)}"
        sender = f"Sender Name is: {self.message_sendger(sentbox_message)}"
        subject = f"subject is: {self.message_subject(sentbox_message)}"
        body = f"Body of the sent Mail is: {self.message_body(sentbox_message)}"
        sentbox_latest_message = [f"{mail_address}", time, sender, subject, body]
        print(sentbox_latest_message)
        return sentbox_latest_message

    def drafts_mail(self):
        drafts_message = drafts_folder.Items.GetLast()
        mail_address = f"In draftbox : {self.message_mail_address(drafts_message)}"
        time = f"time_stamp is : {self.message_time(drafts_message)}"
        subject = f"subject is: {self.message_subject(drafts_message)}"
        body = f"Body of the draft Mail is: {self.message_body(drafts_message)}"
        draftbox_latest_message = [mail_address, time, subject, body]
        print(draftbox_latest_message)
        return draftbox_latest_message

    def deleted_mail(self):
        deleted_message = deleted.Items.GetLast()
        mail_address = f"In deleted box : {self.message_mail_address(deleted_message)}"
        time = f" time stamp is : {self.message_time(deleted_message)}"
        subject = f" Subject is : {self.message_subject(deleted_message)}"
        body = f" Body of the deleted mail is : {self.message_body(deleted_message)}"
        deleted_latest_message = [mail_address, time, subject, body]
        print(deleted_latest_message)
        return deleted_latest_message

    def outbox_mail(self):
        outbox_message = outbox.Items.GetLast()
        mail_address = f" In outbox : {self.message_mail_address(outbox_message)}"
        time = f"time stamp is: {self.message_time(outbox_message)}"
        subject = f"subject is : {self.message_subject(outbox_message)}"
        body = f" Body of the outbox mail is : {self.message_body(outbox_message)}"
        outbox_latest_message = [mail_address, time, subject, body]
        print(outbox_latest_message)
        return outbox_latest_message

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
    try:
        folder = str(name)
        count = name.Items.Count
        if count == 0:
            print(f"No mails in {name}")
        if folder == "Inbox":
            inbox_result = outlook_obj.inbox_mail(name)
            return inbox_result
        elif folder == 'Sent Items':
            sent_box_result = outlook_obj.sent_mail()
            return sent_box_result
        elif folder == 'Drafts':
            drafts_result = outlook_obj.drafts_mail()
            return drafts_result
        elif folder == 'Deleted Items':
            deleted_result = outlook_obj.deleted_mail()
            return deleted_result
        elif folder == 'outbox':
            outbox_result = outlook_obj.outbox_mail()
            return outbox_result
    except:
        return False

if __name__ == "__main__":
    inbox_folder = outlook.GetDefaultFolder(6)
    folder_acces(inbox_folder)
    sentbox_folder = outlook.GetDefaultFolder(5)
    folder_acces(sentbox_folder)
    drafts_folder = outlook.GetDefaultFolder(16)
    folder_acces(drafts_folder)
    deleted = outlook.GetDefaultFolder(3)
    folder_acces(deleted)
    outbox = outlook.GetDefaultFolder(4)
    folder_acces(outbox)
