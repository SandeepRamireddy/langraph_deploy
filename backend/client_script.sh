curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"messages": [{"role":"user", "content": "Multiply 56 with 909?"}]}' \
  http://localhost:8000/agent/calculator
