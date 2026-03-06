"""
Exemplo rápido com MAC Address
Demonstra como trabalhar com endereços MAC
"""

from netaddr import EUI, mac_bare, mac_unix, mac_cisco

print("=" * 60)
print("1. Criando Endereços MAC")
print("=" * 60)

# Criar um endereço MAC a partir de string
mac1 = EUI('00:11:22:33:44:55')
print(f"MAC: {mac1}")
print(f"Tipo de objeto: {type(mac1)}")
print()

# Diferentes formatos aceitos
formatos = [
    '00:11:22:33:44:55',      # Formato padrão (separado por :)
    '00-11-22-33-44-55',      # Formato com hífen
    '0011:2233:4455',         # Formato cisco
    '001122334455',           # Sem separadores
    '00-1122-334455',         # Formato alternativo
]

print("Diferentes formatos de entrada:")
for fmt in formatos:
    try:
        mac = EUI(fmt)
        print(f"  {fmt:20} → {mac}")
    except Exception as e:
        print(f"  {fmt:20} → Erro: {e}")
print()

print("=" * 60)
print("2. Diferentes Representações de MAC")
print("=" * 60)

mac = EUI('00:11:22:33:44:55')

# Diferentes formatos de saída
print(f"Padrão (IEEE):      {mac}")
print(f"Formato BARE:       {mac.format(mac_bare)}")
print(f"Formato UNIX:       {mac.format(mac_unix)}")
print(f"Formato CISCO:      {mac.format(mac_cisco)}")
print()

# Representação binária e inteira
print(f"Binária:            {bin(int(mac))}")
print(f"Hexadecimal:        {hex(int(mac))}")
print(f"Inteira:            {int(mac)}")
print()

print("=" * 60)
print("3. Propriedades de MAC")
print("=" * 60)

mac = EUI('00:11:22:33:44:55')

print(f"MAC: {mac}")
print(f"MAC Inteiro: {int(mac)}")
print()


print("=" * 60)
print("4. Manipulação de MAC")
print("=" * 60)

mac = EUI('00:11:22:33:44:55')

# Acessar octetos individuais
print(f"MAC: {mac}")
print(f"Octetos individuais: {list(mac)}")
print(f"Primeiro octeto: {mac[0]:02x}")
print(f"Último octeto: {mac[5]:02x}")
print()

# OUI (Organization Unique Identifier) - primeiros 3 octetos
print(f"OUI (primeiros 3 octetos): {mac.oui}")
print()

print("=" * 60)
print("5. Validação e Comparação de MAC")
print("=" * 60)

mac1 = EUI('00:11:22:33:44:55')
mac2 = EUI('00:11:22:33:44:55')
mac3 = EUI('AA:BB:CC:DD:EE:FF')

print(f"MAC 1: {mac1}")
print(f"MAC 2: {mac2}")
print(f"MAC 3: {mac3}")
print()

print(f"MAC 1 == MAC 2? {mac1 == mac2}")
print(f"MAC 1 == MAC 3? {mac1 == mac3}")
print(f"MAC 1 != MAC 3? {mac1 != mac3}")
print()

print("=" * 60)
print("6. Exemplo Prático - Gerenciador de MACs")
print("=" * 60)

# Função para validar MAC
def validar_mac(mac_str):
    try:
        mac = EUI(mac_str)
        return True, mac
    except Exception as e:
        return False, str(e)

print("Validação de MACs:")
macs_testar = [
    '00:11:22:33:44:55',
    '00:11:22:33:44',        # Incompleto
    'GG:HH:II:JJ:KK:LL',     # Caracteres inválidos
    'FF:FF:FF:FF:FF:FF',     # Broadcast
]

for mac_str in macs_testar:
    valido, resultado = validar_mac(mac_str)
    if valido:
        print(f"  ✓ {mac_str:20} → Válido ({resultado.format(mac_cisco)})")
    else:
        print(f"  ✗ {mac_str:20} → Inválido ({resultado})")
print()

print("=" * 60)
print("7. Broadcast e Special MACs")
print("=" * 60)

# Endereço broadcast
mac_broadcast = EUI('FF:FF:FF:FF:FF:FF')
print(f"Broadcast MAC: {mac_broadcast}")
print(f"  • É broadcast? {all(octeto == 0xFF for octeto in mac_broadcast)}")
print()

# Endereço all zeros
mac_all_zeros = EUI('00:00:00:00:00:00')
print(f"All Zeros MAC: {mac_all_zeros}")
print()