class Solution1:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email_set = set()
        for email in emails:
            unique_email = ""
            for char in email:
                if char == "@" or char == "+":
                    break
                if char == ".":
                    continue
                unique_email += char
            index_atmark = email.find("@")
            unique_email += email[index_atmark:]
            unique_email_set.add(unique_email)
        return len(unique_email_set)

class Solution2:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email_set = set()
        for email in emails:
            local, domain = email.split("@")
            local_before_plus = local.split("+")[0]
            dot_removed_local = local_before_plus.replace(".", "")
            unique_email_set.add(dot_removed_local + "@" + domain)
        return len(unique_email_set)

class Solution3:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local, domain = email.split("@")
            local_before_plus = re.sub(r"\+.*", "", local)
            dot_removed_local = re.sub(r"\.", "", local_before_plus)
            unique_emails.add(f"{dot_removed_local}@{domain}")
        return len(unique_emails)
