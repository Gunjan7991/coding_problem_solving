def maximumWealth(accounts: list[list[int]]) -> int:
    richest = 0
    for account in accounts:
        richest = max(richest, sum(account))
    return richest
