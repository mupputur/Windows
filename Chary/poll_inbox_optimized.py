from reading_mails_fixed_review_comments import ReadMail, outlook
import pyttsx3
import time


class PollInbox(ReadMail):

    def poll_mail(self, inbox_folder):
        outlook_obj = ReadMail()
        inbox_count = inbox_folder.Items.Count
        if inbox_count:
            print(outlook_obj.inbox_mail(inbox_folder))
            count =0
            while(True):
                count = count + 1
                time.sleep(5)
                if inbox_count < inbox_folder.Items.Count:
                    engine = pyttsx3.init()
                    engine.say("you received a new mail")
                    engine.runAndWait()
                    outlook_obj.inbox_mail(inbox_folder)
                    inbox_count = inbox_folder.Items.Count
                if count == 20:
                    break
        else:
            print("No mails in Inbox")

if __name__ == "__main__":
    poll_obj = PollInbox()
    inbox_folder = outlook.GetDefaultFolder(6)
    poll_obj.poll_mail(inbox_folder)
