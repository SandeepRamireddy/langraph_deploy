curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"messages": [{"role":"user", "content": "What is the product of 567 and 345?"}]}' \
  http://localhost:8000/agent/stream/calculator
