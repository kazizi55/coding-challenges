# 通らない
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = []
        for email in emails:
            split_email = email.split("+")[1].split("@")[0]
            if split_email in unique_emails:
                continue
            unique_emails.append(email)
        return len(unique_emails)
