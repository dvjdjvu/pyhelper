#!/usr/bin/env python3
# encoding: UTF-8

import os
import ssl
import base64
import random

from collections import namedtuple
from OpenSSL import crypto

Cs = ['RU', 'CH', 'FR', 'US', 'JP', 'GE', 'NL', 'AU', 'GB', 'TL']
STs = ['MSK', 'DTR', 'BRL', 'TKO', 'PRS', 'NY', 'LND', 'BNK']
Ls = ['Center', 'Main', 'Global owner', 'Infrastructure', 'Global LTd']
Os = ['Google', 'AWS', 'Yandex', 'AliBaBa', 'Hetzner', 'CloudFlare', 'ANB']
OUs = ['Google', 'AWS', 'Yandex', 'AliBaBa', 'Hetzner', 'CloudFlare', 'ANB']
CNs = ['localhost', 'main', 'stage', 'test', 'production', 'prod']

pem_name = namedtuple('Pem', 'C ST L O OU CN')
pem_names = [
    pem_name(random.choice(Cs),
             random.choice(STs),
             random.choice(Ls),
             random.choice(Os),
             random.choice(OUs),
             random.choice(CNs))
    for _ in range(10)
]


def generate_pem0():
    pk = crypto.PKey()
    pk.generate_key(crypto.TYPE_RSA, 2048)
    pk.check()

    c = crypto.X509()

    names = random.choice(pem_names)
    c.get_subject().C = names.C
    c.get_subject().ST = names.ST
    c.get_subject().L = names.L
    c.get_subject().O = names.O
    c.get_subject().OU = names.OU
    c.get_subject().CN = names.CN
    c.set_serial_number(random.randint(0, 1024))

    before, after = (0, 60 * 60 * 24)
    c.gmtime_adj_notBefore(before)
    c.gmtime_adj_notAfter(after)
    c.set_issuer(c.get_subject())
    c.set_pubkey(pk)
    c.sign(pk, 'sha256')
    c_b = crypto.dump_certificate(crypto.FILETYPE_PEM, c)
    pk_b = crypto.dump_privatekey(crypto.FILETYPE_PEM, pk)
    return c_b.decode(), pk_b.decode()


def write_certs(key: str, cert: str, pk_gen=generate_pem0):
    """
    Генерация и записать ssl сертификатов в файлы key & cert.
    """

    c_str_b64 = os.environ.get('INTERCOM_HTTPS_CERT')
    pk_str_b64 = os.environ.get('INTERCOM_HTTPS_PK')

    if c_str_b64 and pk_str_b64:
        c_b, pk_b = base64.b64decode(c_str_b64.encode()).decode(), base64.b64decode(pk_str_b64.encode()).decode()
    else:
        c_b, pk_b = pk_gen()

    with open(cert, 'w') as f:
        f.write(c_b)

    with open(key, 'w') as f:
        f.write(pk_b)


def gen_ssl_key_cert() -> (str, str):
    """
    Возвращает пути файлов сгенерированных ssl сертификатов.
    """

    if not os.path.exists('/tmp/certificate/'):
        os.makedirs('/tmp/certificate/')

    fn_key, fn_cert = '/tmp/certificate/server.key', '/tmp/certificate/server.crt'
    write_certs(key=fn_key, cert=fn_cert)

    return fn_key, fn_cert


def get_ssl_context() -> ssl.SSLContext:
    """
    Сгенерировать ssl сертификаты для flask.
    """
    if os.environ.get('SERVICE') == 'https':
        fn_key, fn_cert = gen_ssl_key_cert()
        ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        ssl_context.load_cert_chain(fn_cert, fn_key)
    else:
        ssl_context = None

    return ssl_context


def get_digit(number, n) -> int:
    """
    Взять n-ю цифру из N-значного числа.

    Args:
        s:       (Int) Число.
        amount:  (Int) n-ая цифра.

    Returns:
        (Int).
    """

    return number // 10 ** n % 10
