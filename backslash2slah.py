#converting slash in backslah for every full path
#First, example:


full_path = "C:\Users\nfrau\Music\Esperanza Spalding - Radio music society 2012\yadayada.mp3"


full_path = full_path.replace('\\', '/')
print full_path