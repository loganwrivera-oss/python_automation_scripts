services = {
    "auth-service": "running",
    "payment-gateway": "stopped",
    "image-processor": "running",
    "email-sender": "stopped",
    "database": "running"
}

for state in services.items():
    if state[1] == "stopped":
        print(f"Restarting {state[0]}")
        services[state[0]] = "running"


print("All systems go:")
print(services)

#Output:
#Restarting payment-gateway
#Restarting email-sender
#All systems go:
#{'auth-service': 'running', 'payment-gateway': 'running', 'image-processor': 'running', 'email-sender': 'running', 'database': 'running'}


#** Process exited - Return Code: 0 **
