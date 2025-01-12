import hashlib
import base58

def hash160_to_address(hash160):
    # Add version byte (0x00 for P2PKH)
    prefix = b'\x00'
    payload = prefix + bytes.fromhex(hash160)
    
    # Calculate checksum
    checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    
    # Append checksum to payload
    address_bytes = payload + checksum
    
    # Encode in Base58
    return base58.b58encode(address_bytes).decode()

hash160 = "739437bb3dd6d1983e66629c5f08c70e52769371"
bitcoin_address = hash160_to_address(hash160)
print(f"Bitcoin Address: {bitcoin_address}")
