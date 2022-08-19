from data import story

print(f"total chars in the story: {len(story)}")

#counting substring in the larg strin 
a_count = story.count('a')
print(f'a occurs{a_count} time.')
the_count = story.lower().count('the')
print(f'the occurs {the_count} time')

# replace
ustory = story.replace('of','on')
print(ustory)

# removing data
ustory = story.replace('of', '')
print(ustory)

# removing allvowels
no_vowel_story = story.replace('a','').replce('e','').replace('i','').re
print(no_vowel_story)

# retainig all vowels
only_vowel_story = ''
for char in story:
    if char in 'aeiouAEIOU ':
        only_vowel_story +=char
print(only_vowel_story)