listN = ['X509 Certificate Deatails', '01 ','Issuer - Bigfishcert ','43224','2021-2027','RSA','N Mahove']
def certificate():
    return {  
            'Version Number':listN[1] , 
            'Signature Algorithm ID':listN[3], 
            ' Subject Name': listN[6],			
            'Validity period': listN[4],  
            'Subject Public Key Info':listN[5] ,  
            'Issuer Name':listN[2]
			
			
            }
print (certificate())
