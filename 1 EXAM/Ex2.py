from ReadContractFile import read
from Stats import total_contracts, total_contracts_value

contracts_hash_table = read("contratos.txt")

for ea, dates in contracts_hash_table.items():
    print(f"EA: {ea}")
    for contract_dates, contracts in dates.items():
        print(f"\tContract Date: {contract_dates}")
        print(f"\t\tEAJ: {contracts[0]} - CPV: {contracts[1]} - Price: {contracts[2]}- Product Type: {contracts[3]}")
    print("-" * 64)

total = total_contracts(contracts_hash_table)

for ea, contracts in total.items():
    print(f"EA: {ea} did {contracts} contracts.")

print("-" * 64)

value = total_contracts_value(contracts_hash_table)

for ea, contracts in value.items():
    print(f"EA: {ea} contracts cost {contracts} in total.")
