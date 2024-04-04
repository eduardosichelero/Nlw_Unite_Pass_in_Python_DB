class AlgumaCoisa:
    def __enter__(self):
      print("Estou entrando")

    def __exit__(self, exc_type, exc_val, exc_tp):
      print("Estou saindo")
       
with AlgumaCoisa() as ola:
    print("Estou no meio")

