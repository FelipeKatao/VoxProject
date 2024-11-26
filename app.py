from VOX import projectVox

Vox_variable = projectVox.VoxConsole()
#Insira aqui o codigo a ser tratado
def Codigo():
    return "hello world"+str(10)
# Fim do codigo que será tratado

#executando Vox Tests
print(Vox_variable.VoxValidate(Codigo))


