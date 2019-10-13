#! /bin/bash

mongoimport --db Trivias --collection Trivia11 --drop --file "./trivias11.json" --jsonArray
mongoimport --db Trivias --collection Categorias --drop --file "./categoria.json" --jsonArray

mongoimport --db Trivias --collection Trivia11 --drop --file "/home/heider/Desktop/ATI-2019-1/fase4-jugar/imple/categoria.json"