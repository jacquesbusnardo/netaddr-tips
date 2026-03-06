"""
Exemplo de Criação de Zona Reversa com netaddr
Demonstra como trabalhar com zones de DNS reverso (reverse DNS)
Exemplo: 192.0.2.0/24
"""

from netaddr import IPNetwork, IPAddress

print("=" * 60)
print("Criando Zona Reversa para 192.0.2.0/24")
print("=" * 60)
print()

# Definir a rede
rede = IPNetwork('192.0.2.0/24')
print(f"Rede: {rede}")
print(f"Primero IP: {rede[0]}")
print(f"Último IP: {rede[-1]}")
print()

print("=" * 60)
print("1. Reverse DNS da Rede")
print("=" * 60)

# Obter o domínio reverso usando o primeiro IP da rede
primeiro_ip = rede[0]
zona_reversa = primeiro_ip.reverse_dns

# Extrair a zona reversa (últimas três partes)
# Para 192.0.2.0 → reverse é 2.0.192.in-addr.arpa
print(f"Zona Reversa: 2.0.192.in-addr.arpa")
print(f"Reverse DNS do primeiro IP ({primeiro_ip}): {zona_reversa}")
print()

# Explicação do formato
print("Explicação:")
print("  • A rede 192.0.2.0/24 cobre de 192.0.2.0 até 192.0.2.255")
print("  • Invertemos os 3 primeiros octetos: 2.0.192.in-addr.arpa")
print("  • Esta é a zona reversa para essa rede")
print()

print("=" * 60)
print("2. Reverse DNS de IPs Individuais")
print("=" * 60)

# Alguns IPs da rede com seus reversos
ips_exemplo = [
    '192.0.2.1',
    '192.0.2.50',
    '192.0.2.100',
    '192.0.2.200',
    '192.0.2.254',
]

print(f"Reverse DNS de IPs em {rede}:")
for ip_str in ips_exemplo:
    ip = IPAddress(ip_str)
    reverso = ip.reverse_dns
    print(f"  {ip_str:15} → {reverso}")
print()

print("=" * 60)
print("3. Arquivo de Zona Reversa (Bind Format)")
print("=" * 60)

# Simular um arquivo de zona reversa padrão do BIND
print("; Zona reversa para 192.0.2.0/24")
print("$ORIGIN 2.0.192.in-addr.arpa.")
print()
print("@  IN  SOA  ns1.example.com. admin.example.com. (")
print("             2024030501  ; Serial")
print("             3600        ; Refresh")
print("             1800        ; Retry")
print("             604800      ; Expire")
print("             86400 )     ; Minimum TTL")
print()
print("@  IN  NS   ns1.example.com.")
print("@  IN  NS   ns2.example.com.")
print()

# Criar registros PTR para alguns IPs
print("; PTR Records")
ips_com_hostname = {
    '192.0.2.1': 'gateway.example.com',
    '192.0.2.2': 'dns.example.com',
    '192.0.2.10': 'www.example.com',
    '192.0.2.20': 'mail.example.com',
    '192.0.2.30': 'db.example.com',
}

for ip_str, hostname in ips_com_hostname.items():
    ip = IPAddress(ip_str)
    # Extrair apenas o último octeto para o registro PTR
    ultimo_octeto = ip_str.split('.')[-1]
    print(f"{ultimo_octeto:3}  IN  PTR  {hostname}.")
print()

print("=" * 60)
print("4. Gerando Zona Reversa Automaticamente")
print("=" * 60)

# Função para gerar arquivo de zona reversa
def gerar_zona_reversa(rede_cidr, ns_primario, ns_secundario, admin_email, hosts_dict):
    """
    Gera um arquivo de zona reversa no formato BIND
    
    Args:
        rede_cidr: Rede em formato CIDR (ex: 192.0.2.0/24)
        ns_primario: Servidor NS primário
        ns_secundario: Servidor NS secundário
        admin_email: Email do administrador
        hosts_dict: Dicionário com IP → hostname
    """
    rede = IPNetwork(rede_cidr)
    # Obter reverse DNS do primeiro IP
    primeiro_ip = rede[0]
    zona_reversa = primeiro_ip.reverse_dns
    
    linhas = []
    linhas.append(f"; Zona reversa para {rede_cidr}")
    linhas.append(f"$ORIGIN {zona_reversa}")
    linhas.append("")
    linhas.append(f"@  IN  SOA  {ns_primario} {admin_email.replace('@', '.')}. (")
    linhas.append("             2024030501  ; Serial")
    linhas.append("             3600        ; Refresh")
    linhas.append("             1800        ; Retry")
    linhas.append("             604800      ; Expire")
    linhas.append("             86400 )     ; Minimum TTL")
    linhas.append("")
    linhas.append(f"@  IN  NS   {ns_primario}.")
    linhas.append(f"@  IN  NS   {ns_secundario}.")
    linhas.append("")
    linhas.append("; PTR Records")
    
    for ip_str, hostname in sorted(hosts_dict.items()):
        ip = IPAddress(ip_str)
        # Verificar se IP está na rede
        if ip in rede:
            ultimo_octeto = ip_str.split('.')[-1]
            linhas.append(f"{ultimo_octeto:3}  IN  PTR  {hostname}.")
    
    return "\n".join(linhas)

# Gerar zona reversa
hosts = {
    '192.0.2.1': 'gateway.example.com',
    '192.0.2.2': 'ns1.example.com',
    '192.0.2.3': 'ns2.example.com',
    '192.0.2.10': 'www.example.com',
    '192.0.2.20': 'mail.example.com',
    '192.0.2.30': 'db.example.com',
    '192.0.2.50': 'app.example.com',
}

zona = gerar_zona_reversa(
    '192.0.2.0/24',
    'ns1.example.com',
    'ns2.example.com',
    'admin@example.com',
    hosts
)

print(zona)
print()

print("=" * 60)
print("5. Validação de IPs na Zona Reversa")
print("=" * 60)

rede = IPNetwork('192.0.2.0/24')
ips_testar = [
    '192.0.2.1',      # Na rede
    '192.0.2.255',    # Na rede (broadcast)
    '192.0.1.1',      # Fora da rede
    '192.0.3.1',      # Fora da rede
    '10.0.0.1',       # Completamente diferente
]

print(f"Validando IPs para zona {rede}:")
for ip_str in ips_testar:
    ip = IPAddress(ip_str)
    if ip in rede:
        print(f"  ✓ {ip_str:15} está na zona")
    else:
        print(f"  ✗ {ip_str:15} não está na zona")
print()

print("=" * 60)
print("6. Resumo de Propriedades da Zona Reversa")
print("=" * 60)

rede = IPNetwork('192.0.2.0/24')
primeiro_ip = rede[0]
ultimo_ip = rede[-1]

print(f"Rede (CIDR):           {rede}")
print(f"Zona Reversa:          {primeiro_ip.reverse_dns}")
print(f"Primeira IP:           {primeiro_ip} ({primeiro_ip.reverse_dns})")
print(f"Última IP:             {ultimo_ip} ({ultimo_ip.reverse_dns})")
print(f"Total de IPs:          {rede.size}")
print(f"Hosts utilizáveis:     {rede.size - 2} (excluindo network e broadcast)")
print()

print("📌 Padrão de zona reversa:")
print(f"  • Para 192.0.2.0/24 → 2.0.192.in-addr.arpa")
print(f"  • Para 10.0.0.0/8 → 0.in-addr.arpa")
print(f"  • Para 172.16.0.0/16 → 16.172.in-addr.arpa")
