#!/bin/bash

# List all pods
pods=$(/snap/bin/microk8s.kubectl -n lazark get pods)

# Define the substring to match
substring="$1"

# Initialize variables
sum=0
count=0

# Loop through each pod
for pod in $pods; do
    # Check if the pod name contains the specified substring
    if [[ $pod == *"$substring"* ]]; then
        # Get logs of the pod
        number=$(/snap/bin/microk8s.kubectl -n lazark logs "$pod")
        
        sum=$(echo "$sum + $number" | bc)
        
        # Increment the count
        count=$((count + 1))
        
    fi
done
# Calculate average
if [ $count -gt 0 ]; then
    average=$(echo "scale=2; $sum / $count" | bc)
    echo $average
else
    echo "No pods containing the specified substring found."
fi