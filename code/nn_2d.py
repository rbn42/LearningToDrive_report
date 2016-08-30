input_layer = DataLayeaar()
# normalize input data
input_layer = Layer(input_layer, filter=lambda x: (x - T.mean(x)) / T.std(x))

layer1 = DenseLayer(input_layer=input_layer, n_in=84,
                    n_out=32, std=.005, bias=0)
layer1 = ReLU(layer1)

layer2 = DenseLayer(input_layer=layer1, n_in=32, n_out=32, std=.005, bias=0)
layer2 = ReLU(layer2)

output_layer = DenseLayer(input_layer=layer2, n_in=32,
                          n_out=n_actions, std=.005, bias=0)
