from deep_translator import googletranslator
translate_id='سلام'
translate =googletranslator(sourse='fa',target='en').translate(translate_id)
print(translate)
