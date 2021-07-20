'''
Faça um programa que mostre na tela uma contagem egressiva para
o estouro de fogos de artifício, indo de 10 até 0, com uma pausa
de 1 segundo entre eles.
'''
'''
Faça um programa que mostre na tela uma contagem regressiva para
o estouro de fogos de artifício, indo de 10 até 0, com uma pausa
de 1 segundo entre eles.
'''


from time import sleep

print('-='*13)
print('FESTEJOS DE FOGOS DE ARTIFÍCIOS')
print('-='*13)
print('\nCONTAGEM REGRESSIVA')
for contagem in range(10, -1, -1):
    sleep(1)
    print(contagem)
print('''
* * * * * * * * * * * * * * * * * * * *
 * * * * * * * * * * * * * * * * * * *
  * * * BUMMM! * * * * * * * *  * * *
   * * * * * * * * * * * * * * * * *
    * * * * * * * * * * * * * * * *
     * * * * * * BUMMM!* * * * * *
      * * * * * * * * * * * * * *
       * * * * * * * * * * * * *
        * * * * * * * * * * * *
         * * POOOW!! * * * * *
          * * * * * * * * * *
           * * * * * * * * *
            * * * * * * * * 
             * * * * * * *
              * * * * * *
               * * * * *
                * * * *
                 * * *
                  * *
                   *
''')
