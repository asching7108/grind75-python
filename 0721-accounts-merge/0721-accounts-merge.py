class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adjacent = {}
        visited = {}
        merged_accounts = []

        def dfs(email, merged_account):
            visited[email] = True
            merged_account.append(email)
            for neighbor in adjacent[email]:
                if not visited[neighbor]:
                    dfs(neighbor, merged_account)

        # Build adjacent list
        for account in accounts:
            emails = account[1:]
            first_email = emails[0]
            for email in emails:
                # Add undirected edges b/w first email and other emails
                adjacent.setdefault(email, set()).add(first_email)
                adjacent.setdefault(first_email, set()).add(email)
                visited[email] = False

        # Traverse over all accounts to store components (merged accounts)
        for account in accounts:
            account_name = account[0]
            first_email = account[1]
            if not visited[first_email]:
                merged_account = []
                dfs(first_email, merged_account)
                merged_accounts.append([account_name] + sorted(merged_account))

        return merged_accounts

# N is number of accounts
# K is number of maximum number of emails of an account
# Time complexity: O(NKlogNK), in the worst case all emails belong to an account
# Space complexity: O(NK)