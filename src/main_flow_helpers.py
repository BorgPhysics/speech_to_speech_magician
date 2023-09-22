import pygame
import sounddevice as sd
from scipy.io.wavfile import write

exit_option = "You can finish the game at any time. \n" \
              "Write 'new' to start a new game, write 'exit' to finish"


def start():
    print("\n\n"
          "Hello! Welcome to the speech-to-speech wizard! Good to see you here =)\n"
          f"{exit_option}")


def record_audio(duration: int = 5, file_name: str = "recording"):
    sampling_frequency = 44100
    print("starting to record")
    recording = sd.rec(int(duration * sampling_frequency), samplerate=sampling_frequency, channels=2)
    sd.wait()

    print("finished recording")
    write(f"{file_name}.wav", sampling_frequency, recording)
    return f"{file_name}.wav"


def get_audio_sample():
    return "this is an audio sample"


def choose_figure():
    print("\n\nChoose a figure from the list:")

    figure_options = ["Figure 1", "Figure 2", "Figure 3"]
    for idx, option in enumerate(figure_options, start=1):
        print(f"{idx}. {option}")

    while True:
        choice = input("\nEnter the number of your chosen figure: ")
        try:
            if choice.lower() == "exit":
                return "exit"
            elif choice.lower() == "new":
                return "new"

            choice = int(choice)
            if 1 <= choice <= len(figure_options):
                chosen_figure = figure_options[choice - 1]
                print(f"You have chosen: {chosen_figure}")
                return chosen_figure
            else:
                print("Invalid choice. Please select a valid figure.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_transcription(audio_file_path: str) -> str:
    print(f"path for transcription is: {audio_file_path}")
    return "this is a sample transcription"


def get_gpt_answer(transcription: str, figure: str) -> str:
    # call get_gpt_response
    # not calling it now due to cost per call
    return "this is an answer from chat gpt"


def play_audio(file_name: str = "recording.wav"):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.delay(100)

    pygame.quit()


def play_audio_response(transcript: str):
    play_audio("audio_response.wav")
    return "playing response"


def play_round(user_choice: str):
    input("\nPress any key to start recording")
    user_question_path = record_audio(file_name="user_question")
    transcription = get_transcription(audio_file_path=user_question_path)
    gpt_answer = get_gpt_answer(transcription=transcription, figure=user_choice)
    print(gpt_answer)
    play_audio_response(gpt_answer)


def is_another_round() -> str:
    choice = input("\nDo you want to play another round? \n"
                   f"Type 'yes' or 'no'. {exit_option}")

    while True:
        try:
            if choice.lower() in ["exit", "new", "yes", "no"]:
                return choice.lower()
            else:
                print("No valid option was chosen. Please try again")
                choice = input("Do you want to play another round? \n"
                               "Type 'yes' or 'no'")
        except Exception as e:
            print(e)


def finish():
    print("Finishing the current session.")