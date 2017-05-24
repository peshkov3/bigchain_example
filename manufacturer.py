import uuid
from bigchaindb_driver import (
    BigchainDB,
)
from bigchaindb_driver.crypto import generate_keypair
from constants.application_constants import BDB_SERVER_URL

# see simple_transaction.py untill next comment
bdb = BigchainDB(BDB_SERVER_URL)
print(bdb.info())

kgd = generate_keypair()

print('Private key KGD {}'.format(kgd.private_key))
print('Public key KGD {}'.format(kgd.public_key))

for i in enumerate(range(0, 100)):

    tx_create_kgd_simple = bdb.transactions.prepare(
        operation='CREATE',
        signers=kgd.public_key,
        asset={'data':
                   {
                       'item': {
                            'name': 'alcohol item № ' + str(i),
                            'serial_number': str(uuid.uuid4())
                        }
                   }
               },
        metadata={'address': 'Kazakhstan Astana'}
    )
    tx_create_kgd_simple_signed = bdb.transactions.fulfill(
        tx_create_kgd_simple, private_keys=kgd.private_key)

    print('Posting signed transaction{}'.format(tx_create_kgd_simple_signed))
    bdb.transactions.send(tx_create_kgd_simple_signed)
