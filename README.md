## A Script to use vLLM server at M-416 from anywhere

### Installation

**Install Requirements:**

```bash
pip install -r requirements.txt
```

**If you use Conda:**

```bash
conda create -n vllm-client python=3.12
conda activate vllm-client
pip install -r requirements.txt
```

### Usage

**Serve the Model in the Server**
```bash
# With 1 GPU
vllm serve <model_name>

# With 2 GPUs and so on.
vllm serve <model_name> --tensor-parallel-size 2
```

**Run the script:**

```bash
# Change the model to the one that you're serveing in the server
python LLM.py
```

### Note

Please set up your development environment and execute all code on your local machine. The Large Language Model (LLM) will be the only component running on the server.