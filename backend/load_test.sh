hey -H "Content-Type: application/json" \
  -m POST \
  -d '{"messages": [{"role":"user", "content": "What is the product of 34 and 789?"}]}' \
  -n 10 \
  -c 2 \
  http://localhost:8000/agent/calculator
