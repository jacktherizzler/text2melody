# MusicGen Integration

Welcome to the MusicGen Integration repository! This repository provides the necessary files and instructions to use MusicGen, Meta AI's advanced model for controllable music generation.

Website is Live @ `https://text2melody.onrender.com`

## About MusicGen

MusicGen is a cutting-edge AI model for text-to-music and melody-guided music generation. Developed by the FAIR team at Meta AI, it combines EnCodec for audio tokenization and a transformer-based language model for seamless music modeling.

Key features include:
- Support for text-to-music and melody-guided generation.
- Models available in various sizes: 300M, 1.5B, and 3.3B parameters.
- Focused on research and AI-driven music generation.

## Installation

1. Clone this repository:
  ```bash
  git clone https://github.com/jacktherizzler/text-to-music-gen.git
  ```
2.	Navigate to the project directory:
  ```bash
  cd text-to-music-gen
  ```
3.	Install the required dependencies:
  ```bash
  pip install flask requests flask-cors 
  ```
## Usage

To generate music using MusicGen:

1. Download the pre-trained model weights from the [official Meta AI repository](https://github.com/facebookresearch/audiocraft).  
   - Ensure you download the appropriate weights based on your use case:  
     - `facebook/musicgen-small`  
     - `facebook/musicgen-medium`  
     - `facebook/musicgen-large`  
     - `facebook/musicgen-melody`  

2. Place the downloaded weights in the `models/` directory in the project folder.

3. Run the backend server:
  ```bash
  python app.py
  ```
Before running the command, paste your huggingface API key in the place of xxxxxxxxxxxxx.

This starts the Flask server to handle API requests.
4.	Open the index.html file in a browser. Alternatively, use any live server option from your text editor to view the frontend interface.
5.	Enter a textual description of the music you want to generate (e.g., “uplifting piano melody with soft strings”) and submit it. The generated audio file will be saved and available for download.
 
## API Usage

If you want to test the backend API directly using a tool like curl:
- Example API call:
  
   ```bash
   curl -X POST http://127.0.0.1:5000/generate-audio \
   -H "Content-Type: application/json" \
   -d '{"prompt": "liquid drum and bass, atmospheric synths, airy sounds"}'
  ```
The generated audio file will be saved on the server and can be retrieved.

## File Structure

-	models/: Directory for storing pre-trained model weights.
-	app.py: Flask backend application.
-	index.html: Frontend interface for user interaction.
-	generate_music.py: Core script for processing inputs and generating audio files.
-	requirements.txt: List of Python dependencies for the project.

## Citation

```bibtex
@misc{copet2023simple,
  title={Simple and Controllable Music Generation}, 
  author={Jade Copet and Felix Kreuk and Itai Gat and Tal Remez and David Kant and Gabriel Synnaeve and Yossi Adi and Alexandre Défossez},
  year={2023},
  eprint={2306.05284},
  archivePrefix={arXiv},
  primaryClass={cs.SD}
}
```


