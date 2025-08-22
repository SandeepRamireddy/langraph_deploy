curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"messages": [{"role":"user", "content": "Hi, I am John and my age is 40."}], "session_id":1}' \
  http://localhost:8000/agent/calculator

echo "--------------------------------------------------------------------------------------------------------------"

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"messages": [{"role":"user", "content": "Multiply my age with 100?"}], "session_id":1}' \
  http://localhost:8000/agent/calculator
