"""
Exemplo rápido com IPNetwork e IPSet
Demonstra como trabalhar com redes e conjuntos de endereços IP
"""

from netaddr import IPNetwork, IPSet

print("=" * 60)
print("1. IPNetwork - Trabalhando com Redes")
print("=" * 60)

# Criar uma rede
rede = IPNetwork('192.168.1.0/24')
print(f"Rede: {rede}")
print(f"Rede (CIDR): {rede.cidr}")
print(f"Network: {rede.network}")
print(f"Broadcast: {rede.broadcast}")
print(f"Netmask: {rede.netmask}")
print(f"Hostmask: {rede.hostmask}")
print(f"Tamanho: {rede.size} endereços")
print()

# Iterar sobre alguns hosts
print("Primeiros 5 hosts:")
for ip in list(rede)[1:6]:  # Pula o network, começa do primeiro host
    print(f"  - {ip}")
print()

# Verificar se um IP está em uma rede
teste_ip = '192.168.1.50'
print(f"O IP {teste_ip} está em {rede}? {teste_ip in rede}")
print()

# Dividir uma rede em sub-redes
print("Dividindo rede /24 em /26:")
for sub_rede in rede.subnet(26):
    print(f"  - {sub_rede} ({sub_rede.size} hosts)")
print()

print("=" * 60)
print("2. IPSet - Conjuntos de Endereços")
print("=" * 60)

# Criar um IPSet a partir de redes
conjunto1 = IPSet(IPNetwork('10.0.0.0/24'))
print(f"Conjunto 1: {conjunto1}")
print(f"Tamanho: {len(conjunto1)} IPs")
print()

# Adicionar endereços/redes
conjunto2 = IPSet()
conjunto2.add(IPNetwork('192.168.0.0/25'))
conjunto2.add('172.16.0.50')
conjunto2.add('172.16.0.51')
print(f"Conjunto 2: {conjunto2}")
print()

# Operações com conjuntos
print("Operações com Conjuntos:")
uniao = conjunto1 | conjunto2
diferenca = conjunto1 - conjunto2
interseccao = conjunto1 & conjunto2

print(f"  União: {len(uniao)} IPs")
print(f"  Diferença: {len(diferenca)} IPs")
print(f"  Interseção: {len(interseccao)} IPs")
print()

# Verificar se um IP está no conjunto
teste_ip = '10.0.0.100'
print(f"O IP {teste_ip} está em conjunto1? {teste_ip in conjunto1}")
print()

# Exemplo prático: gerenciar blocos de IPs autorizados
print("=" * 60)
print("3. Exemplo Prático - Validação de IPs")
print("=" * 60)

ips_autorizados = IPSet()
ips_autorizados.add(IPNetwork('10.0.0.0/8'))      # Rede interna
ips_autorizados.add(IPNetwork('172.16.0.0/12'))   # Rede privada
ips_autorizados.add(IPNetwork('192.168.0.0/16'))  # Rede privada

ips_para_testar = ['10.50.100.1', '8.8.8.8', '172.20.1.1', '192.168.100.1']

print(f"IPs autorizados: {len(ips_autorizados)} endereços totais\n")
for ip in ips_para_testar:
    autorizado = ip in ips_autorizados
    status = "✓ Autorizado" if autorizado else "✗ Não autorizado"
    print(f"  {ip}: {status}")
