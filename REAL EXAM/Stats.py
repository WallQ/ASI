def total_contracts(contracts_hash_table):
    contracts_done = 0
    ea_contracts_done = {}

    for ea, dates in contracts_hash_table.items():
        ea_contracts_done[ea] = len(dates.items())

    return ea_contracts_done


def total_contracts_value(contracts_hash_table):
    ea_contracts_total_value = {}

    for ea, dates in contracts_hash_table.items():
        contracts_value = 0.0
        for contract_dates, contracts in dates.items():
            contracts_value += contracts[2]

        ea_contracts_total_value[ea] = contracts_value

    return ea_contracts_total_value
