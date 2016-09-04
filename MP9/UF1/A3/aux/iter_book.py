# encoding: utf-8

# Exemples d'iteradors en el llibre de visites

import book

# 1. Simple bucle
def print_records(username):
    for k in  book.keys():
        record = book.record(k)
        if record['NAME'] == username:
            print record['TEXT']

# 2. Acumulador en llista
def list_records(username):
    result = []
    for k in  book.keys():
        record = book.record(k)
        if record['NAME'] == username:
            result.append(record)
    return result

# 3. Comprehensió de llistes
def comprehensio_1_records(username):
    return [record for record in
            [book.record(k) for k in book.keys()]
        if record['NAME'] == username]

# 4. Expressió generadora
def comprehensio_2_records(username):
    return (record for record in
            (book.record(k) for k in book.keys())
        if record['NAME'] == username)

# 5. Corutina
def generator_records(username):
    for k in book.keys():
        record = book.record(k)
        if record['NAME'] == username:
            yield record

if __name__ == "__main__":
    USER = 'Joan'
    book.open()
    print_records(USER)
    for f in (
            list_records,
            comprehensio_1_records,
            comprehensio_2_records,
            generator_records
        ):
        for record in f(USER):
            print record['TEXT']

# vim:ts=4:sw=4:ai:et
