# Multilingual-AI-Assistant-System
MultiLingual AI Assistant system using Generative AI


# How to run?
### STEPS:

- Clone the repository

```bash
git clone https://github.com/sudhanshusinghaiml/Multilingual-AI-Assistant-System.git
```

- Create a conda environment after opening the repository

```bash
conda create -n llmapp python=3.8 -y
```

```bash
conda activate llmapp
```


- Install the requirements
```bash
pip install -r requirements.txt
```

- Create a `.env` file in the root directory and add your GOOGLE_API_KEY credentials as follows:

```ini
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# Finally run the following command
streamlit run app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:
- Python
- Google API
- Streamlit
- PaLM2
- s2t
- t2s



# How to Deploy Streamlit app on EC2 instance

- 1. Login with your AWS console and launch an EC2 instance

- 2. Run the following commands

`Note: Streamlit by default runs on 8501, map the application port to - 8501`

```bash
sudo apt update
```

```bash
sudo apt-get update
```

```bash
sudo apt upgrade -y
```

```bash
sudo apt install git curl unzip tar make sudo vim wget -y
```


```bash
git clone "Your-repository"
```

```bash
sudo apt install python3-pip
```

```bash
pip3 install -r requirements.txt
```

```bash
### Temporary running
python3 -m streamlit run app.py
```

```bash
### Permanent running
nohup python3 -m streamlit run app.py
```
