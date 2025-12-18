servers = [
    {"id": "i-123", "tag": "Production", "cost": 0.50},
    {"id": "i-456", "tag": "Dev", "cost": 0.20},
    {"id": "i-789", "tag": "Dev", "cost": 0.15},
    {"id": "i-101", "tag": "Production", "cost": 0.80}
]

total_savings = 0
count = 0
kept_servers = []

for server in servers:
    if server["tag"] == "Dev":
        count += 1
        total_savings += server["cost"]
    else:
        kept_servers.append(server)
            
servers = kept_servers

print(f"Terminated {count} servers. Total savings: ${total_savings:.2f}")
print(f"Remaining servers: {kept_servers}")


#Output:

#Terminated 2 servers. Total savings: $0.35
#Remaining servers: [{'id': 'i-123', 'tag': 'Production', 'cost': 0.5}, {'id': 'i-101', 'tag': 'Production', 'cost': 0.8}]

