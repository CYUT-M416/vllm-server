# A Script to use vLLM server at M-416 from anywhere
## Server
### Installation
**Use Conda:**

```bash
conda create -n myenv python=3.12 -y
conda activate myenv
pip install --upgrade uv
uv pip install vllm --torch-backend=auto
```

### Usage

**Serve the Model in the Server**
```bash
# With 1 GPU:
vllm serve <model_name>

# With 2 GPUs and so on:
vllm serve <model_name> --tensor-parallel-size 2
```
## Client 
### Installation
**Use Conda:**

```bash
conda create -n vllm-client python=3.12
conda activate vllm-client
pip install -r requirements.txt
```

**Run the script:**

```bash
# Create the .env file first.
# Change the model to the one that you're serveing in the server.
python LLM.py
```

### Note

Please set up your development environment and execute all code on your local machine. The Large Language Model (LLM) will be the only component running on the server.