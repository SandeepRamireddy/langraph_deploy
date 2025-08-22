curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"messages": [{"role":"user", "content": "Multiply 56 with 909?"}]}' \
  https://langgraph-deployment-1010458825042.us-central1.run.app/agent/calculator

