#
# About me page content
#

def me():
   description = '''I'm Jon! I'm a software engineer, mathematician, saberist, beer snob, traveler, etc. I like to do a lot of things. I love learning new things and seeing new cultures. Currently, I work at Northrop Grumman as a Software Engineer. I've done web design and development, algorithm development for signal processing, embedded systems architecture and development, system integration, and enterprise initiatives. I like to work on hard problems, including scalability, real-time and parallel processing, multi-system communication, system of system development, and many more. In my free time, I like objective baseball research (sabermetrics), drinking new beer, and working on cool side projects. I'm a Georgia Tech graduate living in Baltimore, MD right on the water.'''

   stats = [
         ('Kirk or Picard?', 'Picard'),
         ('Favorite time travel method?', 'Tie between the Flux Capacitor and slingshotting around the sun.'),
         ('What drives me?', 'Problems need to be solved.'),
         ('Preferred text editor?', 'Vim'),
         ('Best recent technological innovation?', 'IBM Watson'),
         ('Favorite Sport?', 'Baseball'),
         ('Favorite Beer?', 'American Pale Ale')
      ]

   links = {
         'Fangraphs': 'http://fangraphs.com',
         'Hacker News': 'http://news.ycombinator.com',
      }

   me = {
      'description': description,
      'stats': [{'question':x,'answer':y} for x,y in stats]
   }
   return me
