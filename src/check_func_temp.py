import asyncio

from src.handle_audio import get_transcript_async


# def check_transcript():
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(get_transcript_async("audio_response.wav"))

# check_transcript()


from src.handle_audio import record_audio

record_audio("recording_test")

