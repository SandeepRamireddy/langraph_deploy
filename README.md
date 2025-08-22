
<!-- uv init
uv add -r requirements.txt
uv venv
source .venv/bin/activate 
uv pip install -e .
uv build
uv run invoke_agent.py  
uv add uvicorn
uv run uvicorn app.main:app --reload

chmod +x client_script.sh
./client_script.sh


docker build -t langgraph-backend .
docker run -d -p 8000:8000 --name langgraph-app langgraph-backend
docker stop langgraph-app
docker rm langgraph-app
docker run -d -p 8000:8000   --env-file /mnt/c/langgraph_deployment/backend/app/.env   --name langgraph-app4 langgraph-backend



 sudo snap install google-cloud-cli --classic
gcloud auth login
docker build -t langgraph-backend .
gcloud auth configure-docker us-central1-docker.pkg.dev
docker tag langgraph-backend   us-central1-docker.pkg.dev/agentspace-pa/langgraph-deploy/langgraph-backend:latest
 docker push us-central1-docker.pkg.dev/agentspace-pa/langgraph-deploy/langgraph-backend:latest
-->
