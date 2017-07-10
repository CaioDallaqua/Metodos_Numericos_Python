def newton_raphson(f, f_linha, x_i, tol = 0.001, n = 1000):
    '''
        Descrição: 
                    Método Newton-Raphson para encontrar raízes.
        Entrada: 
                    f - função simbólica
                    f_linha - derivada simbólica de f
                    x_i - chute inicial
                    tol - tolerância
                    n - número máximo de iterações
        Saída:
                    Uma raiz da função ou False
        Tempo: O(n)
        Memória: O(1)
    '''
    while n > 0:
        #calcula próximo x
        x_f = x_i - f(x_i)/f_linha(x_i)
        #erro tolerável?
        if abs(x_f - x_i) <= tol:
            #encontrou raiz
            return x_f
        x_i = x_f
        n -= 1
    #não encontrou raiz
    return False
