
source .venv/scripts/activate

uvicorn api:app --reload

curl http://localhost:8000/openapi.json > openapi_schema.json

> /c/Users/aftab.jalal/AppData/Roaming/Python/Python310/Scripts/openapi-generator.exe
generate -i openapi-schema.json -g mj_generator --additional-properties=mockData=true