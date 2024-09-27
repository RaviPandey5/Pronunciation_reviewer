Here's a `README.md` file for your project. It includes instructions on how to set up and run the application, along with a brief explanation of what the project does and how to use it.

---

# Pronunciation Assessment System Using Google Gemini

This project is a **Pronunciation Assessment System** built with **Streamlit**, **Google Gemini**, and **Python's SpeechRecognition**. It allows users to input a sentence, speak it aloud, and receive detailed feedback on their pronunciation, including suggestions for improvement. The feedback is generated using **Google Gemini's AI** for pronunciation analysis.

## Features

- **Speech-to-Text Recognition**: Captures the user's spoken sentence using a microphone and transcribes it into text.
- **Google Gemini Integration**: Analyzes the pronunciation accuracy of the spoken sentence and provides detailed feedback, including mispronounced words, sound/syllable issues, phonetic transcription, and improvement suggestions.
- **Real-Time UI Updates**: Dynamically displays the recognized text as the user speaks.
- **Retry Option**: Users can retry speaking if an error occurs or if they want to improve their pronunciation further.

## Prerequisites

1. Python 3.7 or later.
2. A Google Gemini API key.
3. A working microphone for capturing speech.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pronunciation-assessment-gemini.git
cd pronunciation-assessment-gemini
```

### 2. Install dependencies

Install the necessary Python libraries using `pip`:

```bash
pip install -r requirements.txt
```

Your `requirements.txt` should contain:

```text
streamlit
python-dotenv
speechrecognition
google-generativeai
```

### 3. Setup environment variables

Create a `.env` file in the root directory of your project and add your **Google Gemini API key**:

```bash
GOOGLE_API_KEY=your_google_gemini_api_key
```

### 4. Run the application

Start the Streamlit app using the following command:

```bash
streamlit run app.py
```

This will launch the app in your browser at `http://localhost:8501`.

## Usage

1. Enter the sentence you'd like to pronounce in the input field.
2. Click on the **Start Speaking** button and speak the sentence into your microphone.
3. The app will display the transcribed text dynamically in the UI.
4. Once you've spoken, the system will use Google Gemini to analyze your pronunciation.
5. You'll receive feedback that includes:
   - Mispronounced words
   - Issues with specific sounds or syllables
   - Suggestions for improvement
   - Phonetic transcription of both your spoken and expected pronunciations
   - A correctness score out of 10
6. If you wish to try again, click the **Try Again** button to repeat the process.

## Example Response from Google Gemini

Here's an example of the feedback provided by Google Gemini:

```plaintext
1. **Language Detected**: English
2. **Correctness Score**: 7/10
3. **Detailed Feedback**:
    - **Mispronounced Words**:
      - *Example* (word spoken: "example", expected: "example"):
        - **Sound/Syllable Issues**: The initial "ex-" sound was pronounced as "ig-", which is incorrect.
        - **Suggested Improvements**: Try to emphasize the "e" sound as in "egg" rather than "i".
      - *Pronunciation* (word spoken: "pronounciation", expected: "pronunciation"):
        - **Sound/Syllable Issues**: The second syllable "nounce" was pronounced with a weak "ou" sound, making it unclear.
        - **Suggested Improvements**: Focus on making the "ou" sound clearer, similar to "ounce."
    - **Phonetic Transcription**:
      - Expected: /prəˌnʌn.siˈeɪ.ʃən/
      - Spoken: /prəˌnaʊn.siˈeɪ.ʃən/
    - **Confidence Level**: High
4. **Additional Comments**: Try to practice the syllable breakdown and slow down the pace for tricky words like "pronunciation."
```

## Troubleshooting

1. **Audio Recognition Issues**: If the app cannot recognize your speech, ensure that your microphone is working and properly configured. You can also adjust the ambient noise threshold by speaking louder or clearer.
   
2. **Google API Errors**: Make sure that your Google Gemini API key is valid and correctly set in the `.env` file.

3. **Missing Dependencies**: If the app fails to start, ensure all dependencies in `requirements.txt` are installed.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

This `README.md` file provides a clear setup and usage guide for your project, making it easy for others to understand how to install, run, and use the Pronunciation Assessment System.
