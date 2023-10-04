import math

class RSA:
    def __init__(self, p, q, e):
        self.e=e
        self.modulus=p*q #n
        self.totient=(p-1)*(q-1) #phi_n
        self.e_coprime=self.find_coprime(self.totient*10,self.totient)
        self.modular_multi_inverse=self.mod_inverse(self.e,self.totient)

    def find_coprime(self, bound, a):
        for b in range(a+1, bound + 1):
            if self.are_coprime(a, b):
                return b
        return -1 

    def are_coprime(self, a, b):
        gcd = math.gcd(a, b)
        return gcd == 1
    
    def extended_gcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = self.extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    def mod_inverse(self, e, phi_n):
        gcd, x, _ = self.extended_gcd(e, phi_n)
        if gcd != 1:
            raise ValueError("The modular inverse does not exist.")
        else:
            return x % phi_n

    def encrypt(self, m):
        return pow(m,self.e,self.modulus)
    
    def decrypt(self, c):
        return pow(c,self.modular_multi_inverse,self.modulus)


rsa = RSA(61, 53, 17)
print(rsa.encrypt(65), "2790")
print(rsa.decrypt(2790), "65")