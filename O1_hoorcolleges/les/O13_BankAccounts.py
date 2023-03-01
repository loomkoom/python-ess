# Example set to experiment with.
# [0] = rekening , [1] = storting
transfers = [(1, 100), (3, 500), (1, 200), (6, 600), (1, 200), (1, 400)]

# STEP 1: Compute the set of all bank account numbers
#     involved in the given set of transfers.
# - Map each transfer upon the bank account number involved.

accounts_involved = \
    set(map(lambda transfer: transfer[0], transfers))
print(accounts_involved)

# STEP 2: Compute the total amount of money deposited to
#     the bank account with number 1.
#     [ This is an intermediate step. Once we know how to
#       do that for 1 account, we will do it for all of them]
# - Filter out all transfers involving bank accounts with
#   a number different from 1
# - Map each transfer in the filtered set on the amount involved.
# - Compute the sum of all amounts deposited to bank account number 1.

total_deposited_to_1 = \
    sum(map(lambda transfer: transfer[1],
            filter(lambda transfer: transfer[0] == 1, transfers)))
print(total_deposited_to_1)

# STEP 3: Compute the total amount of money deposited to
#     all bank accounts.
# - Map each bank account number on a tuple consisting of
#   the number itself and the total of amount deposited on
#   that account.
# - Use the above formula to compute that total.

total_deposited_per_account = \
    set(map(lambda acc:
            (acc,
             sum(map(lambda transfer: transfer[1],
                     filter(lambda transfer: transfer[0] == acc, transfers))))
            , accounts_involved))
print(total_deposited_per_account)

# STEP 4: Compute the collection of all bank accounts for which
#     the total deposited amount is not below a threshold
#     to be read from the input stream.
# - Read the threshold from the standard input stream.
# - Filter all tuples from total_deposited_per_account for
#   which the total is below the threshold.
# - Map each remaining tuple on the number of bank account.
# - Remember that an iterator can only be used once.

threshold = int(input("Enter the threshold: "))
suspicious_accounts = \
    set(filter(lambda total: total[1] > threshold, total_deposited_per_account))
print(set(suspicious_accounts))
