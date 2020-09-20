import hashlib as hl
import json


def hash_string_256(string):
    return hl.sha256(string).hexdigest()


def hash_block(block):
    """Hashes a block and returns a string representation of it.

    sort_keys=True serve per fare in modo che le chiavi siano sempre nello stesso ordine
    (ricorda che i dictionary non sono ordinati e quindi non abbiamo la garanzia che tutte le coppie key->value siano
    sempre nello stesso ordine)
    Arguments:
        :block: The block that should be hashed.
    """
    return hash_string_256(json.dumps(block, sort_keys=True).encode())
