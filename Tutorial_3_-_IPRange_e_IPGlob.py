"""
Exemplo rápido com IPRange e IPGlob
Demonstra como trabalhar com intervalos de IPs e padrões glob
"""

from netaddr import IPRange, IPGlob

print("=" * 60)
print("1. IPRange - Intervalo de Endereços")
print("=" * 60)

# Criar um intervalo de IPs
intervalo = IPRange('192.168.1.1', '192.168.1.10')
print(f"Intervalo: {intervalo}")
print(f"Tamanho: {len(intervalo)} IPs")
print()

# Listar os IPs no intervalo
print("IPs no intervalo:")
for ip in intervalo:
    print(f"  - {ip}")
print()

# Verificar se um IP está no intervalo
teste_ip = '192.168.1.5'
print(f"O IP {teste_ip} está no intervalo? {teste_ip in intervalo}")
print()

# IPRange com IPv6
intervalo_ipv6 = IPRange('::1', '::10')
print(f"Intervalo IPv6: {intervalo_ipv6}")
print(f"Tamanho: {len(intervalo_ipv6)} IPs")
print("Primeiros 5 IPs IPv6:")
for ip in list(intervalo_ipv6)[:5]:
    print(f"  - {ip}")
print()

print("=" * 60)
print("2. IPGlob - Padrões Glob para IPs")
print("=" * 60)

# Padrão simples com wildcard
glob1 = IPGlob('192.168.1.*')
print(f"Padrão: 192.168.1.*")
print(f"Tamanho: {len(glob1)} IPs")
print("Primeiros 5 IPs:")
for ip in list(glob1)[:5]:
    print(f"  - {ip}")
print()

# Padrão com múltiplos wildcards
glob2 = IPGlob('10.0.0-255.*')
print(f"Padrão: 10.0.0-255.*")
print(f"Tamanho: {len(glob2)} IPs")
print("Primeiros 5 IPs:")
for ip in list(glob2)[:5]:
    print(f"  - {ip}")
print()

# Padrão com intervalo específico
glob3 = IPGlob('172.16.0.0-50')
print(f"Padrão: 172.16.0.0-50")
print(f"Tamanho: {len(glob3)} IPs")
print("Todos os IPs:")
for ip in glob3:
    print(f"  - {ip}")
print()

# Padrão com intervalo no terceiro octeto
glob4 = IPGlob('10.0.0-2.*')
print(f"Padrão: 10.0.0-2.* (3º octeto: 0-2)")
print(f"Tamanho: {len(glob4)} IPs")
print("Primeiros 10 IPs:")
for ip in list(glob4)[:10]:
    print(f"  - {ip}")
print()

print("=" * 60)
print("3. Exemplo Prático - Descoberta de Rede")
print("=" * 60)

# Simular descoberta de hosts em uma faixa (pequena para demonstração)
faixa_descoberta = IPRange('192.168.1.1', '192.168.1.20')
hosts_ativos = ['192.168.1.1', '192.168.1.5', '192.168.1.10', '192.168.1.15', '192.168.1.20']

print(f"Descobrindo hosts na faixa: {faixa_descoberta}")
print(f"Hosts ativos encontrados:")
for ip_str in hosts_ativos:
    ip = int(ip_str.split('.')[-1])
    if ip_str in faixa_descoberta:
        print(f"  ✓ {ip_str}")
print()

print("=" * 60)
print("4. Comparação: IPRange vs IPGlob")
print("=" * 60)

# IPRange: definido explicitamente
range_ips = IPRange('10.0.0.1', '10.0.0.5')
print(f"IPRange('10.0.0.1', '10.0.0.5'): {list(range_ips)}")

# IPGlob: padrão com wildcard
glob_ips = list(IPGlob('10.0.0.1-5'))
print(f"IPGlob('10.0.0.1-5'): {glob_ips[:5]}")
print()

print("📌 Resumo:")
print("  • IPRange: para intervalos contíguos (início até fim)")
print("  • IPGlob: para padrões com wildcards e intervalos em cada octeto")
