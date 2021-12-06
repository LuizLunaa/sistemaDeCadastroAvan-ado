from PyQt5 import  uic,QtWidgets

app=QtWidgets.QApplication([])
cadastro_avan=uic.loadUi("cadastro_avan.ui")

def incluir():
   print("\nINCLUIR")
   
def modificar() :
   print("\nMODIFICAR")
def excluir() :
   print("\nEXCLUIR")
def consultar() :
   print("\nCONSULTAR")
def relatorio() :
   cpgto = cadastro_avan.cod_cnd_pgto.text()
   cpdes = cadastro_avan.des_cnd_pgto.text()
   cpdia = cadastro_avan.qtd_dias.text()
   print("RELATÓRIO") 
   print("\n-------------------------------")
   print("Código : ",cpgto)
   print("Descricao : ",cpdes)
   print("Preço : ",cpdia)
   print("-------------------------------\n ")

cadastro_avan.incluir.clicked.connect(incluir)
cadastro_avan.modificar.clicked.connect(modificar)
cadastro_avan.excluir.clicked.connect(excluir)
cadastro_avan.consultar.clicked.connect(consultar)
cadastro_avan.relatorio.clicked.connect(relatorio)


cadastro_avan.show()
app.exec()