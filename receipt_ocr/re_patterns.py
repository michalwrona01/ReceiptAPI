import re
from difflib import SequenceMatcher


def get_shop_name(text):
    return text[0]


def get_address(text):
    pattern = re.compile("ul\.(.*[a-zA-Z])+", re.IGNORECASE)
    addres = pattern.findall(text)

    return addres[0] if addres else None


def get_nip_number(text):
    pattern = re.compile("NIP(.*([+-]?(?=\\.\\d|\\d)(?:\\d+)?(?:\\.?\\d*))(?:[eE]([+-]?\\d+))?)", re.IGNORECASE)
    finds_nips = pattern.findall(text)
    if finds_nips:
        nip_number_text = finds_nips[0][0]
        if nip_number_text.startswith(':') or nip_number_text.startswith(': '):
            splitted = nip_number_text.split(':')[1]
            return ''.join(splitted.split('-'))

        elif '-' in nip_number_text:
            return ''.join(nip_number_text.split('-'))

        else:
            return nip_number_text


def matcher_endline_products(row):
    if (SequenceMatcher(None, 'SPRZEDAZ OPODATK.', row).ratio() >= 0.7) or (SequenceMatcher(None, 'SP.OP A:',
                                                                                            row).ratio() >= 0.3):
        return True


def get_products(text):
    is_find = False
    products = list()

    for row in text:
        if matcher_endline_products(row) and is_find:
            break

        if is_find:
            products.append(row)

        if SequenceMatcher(None, 'PARAGON FISKALNY', row).ratio() >= 0.8 and not is_find:
            is_find = True

    return products


def get_date(text):
    pattern = re.compile("([0-9]{4}-[0-9]{2}-[0-9]{2})", re.IGNORECASE)
    return pattern.findall(text)
