def check_contracts(contracts_hash_table):
    contracts_list = []

    for ea, dates in contracts_hash_table.items():
        for contract_dates, contracts in dates.items():
            if contracts[3] == "Ajuste Direto" and contracts[2] > 10000.00:
                if contracts not in contracts_list:
                    contracts_list.append(contracts)

    return contracts_list
