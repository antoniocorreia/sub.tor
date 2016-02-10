import goslate

translateTo = "pt-br"

os.chdir(dir_formatado)
for file in glob.glob("*.c"):

vtt_file = open("subtitles.vtt","r")
vtt_text = vtt_file.read()
vtt_file.close()


gs = goslate.Goslate()
gs.translate(stringOriginalLanguage,translateTo)