from pygame import mixer
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play()
print('Caso queira parar basta apertar qualquer tecla! :)')
input( ) #É como se servisse para começar outro comando, porém esse comando está em "branco"


