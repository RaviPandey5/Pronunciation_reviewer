
from dotenv import load_dotenv
import streamlit as st
import os
import speech_recognition as sr
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit CSS styles
css = """
<style>
.title {
    font-size: 36px;
    color: #00FFFF;
    text-align: left;
}
.txt {
    font-size: 18px;
    color: #4F8BF9;
    text-align: left;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)


# Function to get the pronunciation analysis response from Google Gemini
def get_gemini_response(prompt, user_input, correct_input):
    # Creating the input for Google Gemini
    model = genai.GenerativeModel('gemini-pro')
    full_prompt = f"{prompt}\nUser said: '{user_input}'\nExpected: '{correct_input}'. Provide detailed feedback on the pronunciation accuracy."

    # Send the request to the Gemini model
    response = model.generate_content([full_prompt])
    return response.text


# Function to capture speech using the microphone and update the text dynamically
def recognize_speech_dynamic():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Listening... Please speak now.")
        recognizer.adjust_for_ambient_noise(source)

        # Placeholder for dynamically updating recognized text
        recognized_text_placeholder = st.empty()

        audio = recognizer.listen(source)

        try:
            # Update the UI with dynamically recognized text
            recognized_text = recognizer.recognize_google(audio)
            recognized_text_placeholder.text(f"Recognized: {recognized_text}")
            return recognized_text
        except sr.UnknownValueError:
            recognized_text_placeholder.text("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            recognized_text_placeholder.text(f"Could not request results; {e}")
        return None


# Initialize session state variables for retrying speech recognition
if 'retry' not in st.session_state:
    st.session_state.retry = False
if 'user_pronunciation' not in st.session_state:
    st.session_state.user_pronunciation = None

# Streamlit UI for Pronunciation Assessment
st.markdown('<h1 class="title">Pronunciation Assessment System Using Google Gemini</h1>', unsafe_allow_html=True)
st.markdown('<h1 class="txt">Enter a sentence and speak it aloud for pronunciation assessment.</h1>',
            unsafe_allow_html=True)

# Input field for the correct sentence
correct_sentence = st.text_input("Enter the correct sentence for pronunciation:")

# Button to start speaking
if st.button("Start Speaking") or st.session_state.retry:
    if correct_sentence:
        # Reset retry state when speaking again
        st.session_state.retry = False

        # Capture the user's spoken text and update UI dynamically
        st.session_state.user_pronunciation = recognize_speech_dynamic()

        if st.session_state.user_pronunciation:
            # Use Google Gemini to analyze pronunciation
            prompt = """
            You are an expert in phonetics, pronunciation, and language assessment, specializing in multiple languages. Your task is to analyze the user's spoken sentence and compare it with the expected sentence. Provide detailed feedback on pronunciation, indicating which words or sounds are incorrect, how they can be improved, and a correctness score on a scale of 1 to 10.

            The assessment should be able to handle and analyze the pronunciation in any language. 
            
            ### Response Structure:
            1. **Language Detected**: Indicate the language in which the spoken sentence was detected.
            2. **Correctness Score**: Provide an overall correctness score on a scale of 1 to 10 (where 10 is perfect pronunciation and 1 is entirely incorrect).
            3. **Detailed Feedback**: Provide detailed feedback in the following format:
                - **Mispronounced Words**: List each word that was mispronounced.
                - **Sound/Syllable Issues**: For each mispronounced word, specify the exact sound(s) or syllable(s) that were incorrect.
                - **Suggested Improvements**: Provide a specific recommendation for improving the pronunciation for each word or sound.
            4. **Phonetic Transcription**: Include the phonetic transcription of the expected and actual pronunciation using IPA (International Phonetic Alphabet) for comparison.
            5. **Confidence Level**: Indicate the confidence level of the speech recognition or pronunciation analysis for each word (Low, Medium, High).
            6. **Additional Comments**: (Optional) Any other relevant feedback or suggestions to help the user improve their pronunciation.
            
            ### Example Output:
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
            
            Ensure that the response is clear, concise, and properly formatted for easy reading and improvement.

            """
            response = get_gemini_response(prompt, st.session_state.user_pronunciation, correct_sentence)
            st.subheader("Pronunciation Feedback from Google Gemini:")
            st.write(response)
        else:
            st.warning("There was an error in recognizing your speech. Please try again.")
    else:
        st.error("Please enter the correct sentence first.")

# Display a "Try Again" button if the user has already spoken or if there's an error
if st.session_state.user_pronunciation is not None:
    if st.button("Try Again"):
        # Set the retry flag to True to allow the user to try again
        st.session_state.retry = True
        st.session_state.user_pronunciation = None
