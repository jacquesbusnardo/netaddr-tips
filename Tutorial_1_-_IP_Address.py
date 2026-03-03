from netaddr import IPAddress

"""
Módulo para demonstrar validação e manipulação de endereços IP usando a biblioteca netaddr.
Este módulo mostra:

Validação de endereços IPv4 e IPv6 a partir de uma lista

Tratamento de formatos de endereço inválidos com gerenciamento de exceções

Extração de propriedades de endereços IP (versão, DNS reverso, representação compactada, bits binários)

Exemplo:
O módulo demonstra como:

Criar objetos IPAddress a partir de representações em string

Capturar e tratar AddrFormatError para endereços inválidos

Acessar propriedades do endereço como versão, reverse_dns, packed e bits()

Trabalhar com endereços IPv4 e IPv6

Exemplos de endereços válidos: '10.1.0.30', '192.0.2.15', 'fd12:3456:789a:2::1'
Exemplos de endereços inválidos: '192.168.1000.0' (octeto > 255), 'fd12:3456:789a:1::INVALID' (hex inválido)

Atributos:
addr_list (list): Contém strings de endereços IP válidos e inválidos para teste
addr_obj_list (list): Armazena objetos IPAddress validados com sucesso
addr_obj (IPAddress): Objeto IPAddress único para inspeção detalhada de propriedades

Propriedades do Objeto Endereço IP:

version: Retorna 4 para IPv4 ou 6 para IPv6

reverse_dns: Retorna a representação de DNS reverso (in-addr.arpa para IPv4, ip6.arpa para IPv6)

packed: Retorna a representação binária compactada como bytes

bits(): Retorna a representação binária como uma string pontuada (ex: 11001011.00000000.01110001.01001011)
"""


addr_list = [
    '10.1.0.30',
    '172.20.0.1',
    '192.168.1000.0', #Invalido 
    '192.0.2.15',
    'fd12:3456:789a:2::1',
    'fd12:3456:789a:1::INVALID', #Invalido 
]

addr_obj_list = []

for addr in addr_list:
    try:
        addr_obj_list.append(IPAddress(addr)) 
    except Exception as e:
        print(f"Endereço inválido: {addr} - {type(e).__name__}: {e}")
    else:
        print(f"Endereço válido: {addr}")

print("---")
for addr_obj in addr_obj_list:
    print(f"IP Address: {addr_obj}")
    print(f"Version: {addr_obj.version}")
    print(f"ReverseDNS: {addr_obj.reverse_dns}")
    print("---")


print("\n---")
addr_obj = IPAddress('203.0.113.75')

print(f"IP Address: {addr_obj}")
print(f"Version: {addr_obj.version}")
print(f"ReverseDNS: {addr_obj.reverse_dns}")
print(f"Packed: {addr_obj.packed}")
print(f"bits: {addr_obj.bits()}")

# IP Address: 203.0.113.75
# Version: 4
# Reversw DNS: 75.113.0.203.in-addr.arpa.
# Packed: b'\xcb\x00qK'
# bits: 11001011.00000000.01110001.01001011